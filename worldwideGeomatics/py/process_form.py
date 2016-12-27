# -*- coding: utf-8 -*-

'''
Created on 26/11/2016

@author: Worldwide Geomatics
'''

from templates import templates
from worldwide import wwfunctions
from py import conexion
import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
import json

import sys
sys.path.append(r"D:\LiClipse\plugins\org.python.pydev_3.9.2.201502042042\pysrc")
#import pydevd

class process_forms():
    """
    Class that process received forms
    """
    
    #Class variables
    environ=None
    name_form=None
    dpost=None
    user=None
    psw=None
    html=None
    
    def __init__(self, environ):
        """
        Constructor. Receives the parameter environ and initiallize the variables 
        of the class
        """
        #pydevd.settrace()
        self.environ=environ
        self.dpost=wwfunctions.return_dict_post(environ)
        self.name_form=self.dpost["name_form"][0]

    def process_form(self):
        """
        Studies which form has been sended and performs the necessary action
        """
        
        if self.name_form=="login_form":
            self.connection()
            html=self.process_form_login()
            
        elif self.name_form=="search_form":
            self.connection() #connection to the DB
            html=self.process_form_search()
        
        elif self.name_form=="register_form":
            self.connection()
            html=self.process_form_register()
        
        else:
            html='<section id="general_section"><h1>Nothing has been programmed yet for form {}'.format(self.name_form)+'</h1></section>'
        
        return html
    
    def process_form_login(self):
        
        """
        This function processes the data introduced on the form login and retrieves the data from the DB. After that, logs in with the username and password
        """
        
        variables= "username, password, typeofuser"
        
        #Take the variables from the form
        if "user" in self.dpost.keys():
            self.user=self.dpost["user"][0]
        if "pass" in self.dpost.keys():
            self.psw=self.dpost["pass"][0]
            
        
        where="WHERE username='"+self.user+"' AND password='"+self.psw+"'"
            
        #creates and execute SQL sentence
        sql='SELECT '+variables+' FROM public.users '+where+';'
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        
        if result!=[]:
            self.user=result[0][0]
            self.psw=result[0][1]
            self.usertype=result[0][2]
            #Make the connection with the DB
            oConexion=conexion.Conexion(self.user, self.psw, self.usertype)
            oSession=self.environ["beaker.session"]
            conexion.keep_session_variables(oSession, oConexion)
            html='<section id="general_section"><h1>Logged as %s, with %s rights'%(self.user, oConexion.user_type)+'</h1></section>'
        else:
            self.user=''
            self.psw=''
            self.usertype=''
            html='<section id="general_section"><h1>The user %s is not registered.'%(self.user)+'</h1></section>'
        
        return html
    
    def process_form_search(self):
        """
        This function processes the data introduced on the form search and retrieves the data from the DB, creating the appropiate sql sentence
        Depending on which options has been chosen in the form
        """
        #pydevd.settrace()
        self.type=self.dpost["type-form"][0]  #First, it knows the type of form, this will be used for apply different processes
        
        ##PROCESS FOR GEOMETRY**************************************************
        """
        In this part, when the field geom is changed, it makes zoom to the objects as well as sends a json file with the selection "geometry" (javascript will manage it)
        """
        if self.type=="geometry":
            #pydevd.settrace()
            if "geom" in self.dpost.keys():
                if self.dpost["geom"][0]!='none':
                    self.geom=self.dpost["geom"][0]
                    #Here it assign a diferent type_table depending on the geometry type chosen
                    if self.geom=="POINT":
                        self.type_table='public.reportspoints'
                    elif self.geom=="LINE":
                        self.type_table='public.reportslines'
                    elif self.geom=="POLYGON":
                        self.type_table='public.reportspolygons'
                    #With this sentence, it returns the extension of the selection
                    sql='SELECT ST_AsGeoJSON(ST_Extent(geometry)) FROM '+self.type_table+";"
                    self.cursor.execute(sql)
                    result=self.cursor.fetchall()
                    if (result==[(None,)] or result==[]):
                        extension='null' 
                    else:
                        extension=result[0][0]
                    #Here it creates a json file in order to send all the values needed by javascript, in this case, it indicates that geometry has been selected and the extension                
                    json_resp=json.dumps({"selection":"geometry", "extension":extension}) 
                    html=json_resp                    
                else:
                    self.geom="empty"    
            else:
                self.geom="empty"
        
        ##PROCESS FOR TYPE
            """
            In this part, when the field incident_type is changed, it makes zoom to the objects as well as sends a json file with the selection "incident_type" (javascript will manage it)
            """
        elif self.type=="incident_type":
            where="WHERE "
            if "incident_type" in self.dpost.keys():
                if self.dpost["incident_type"][0]!='none':
                    self.incident_type=self.dpost["incident_type"][0]
                    #Here it creates the WHERE part of the sql sentence depending on the incident_type chosen
                    where+=" type = '"+ str(self.incident_type)+"' "
                    #With this sentence, it returns the extension of the selection
                    sql= 'SELECT ST_AsGeoJSON(ST_Extent(geometry)) FROM public.reportspoints '+where+" UNION DISTINCT SELECT ST_AsGeoJSON(ST_Extent(geometry)) FROM public.reportslines "+where+" UNION DISTINCT SELECT ST_AsGeoJSON(ST_Extent(geometry)) FROM public.reportspolygons "+where+";"
                    self.cursor.execute(sql)
                    result=self.cursor.fetchall()
                    if (result==[(None,)] or result==[]):
                        extension='null'
                    else:
                        extension=result[0][0]
                    #Here it creates a json file in order to send all the values needed by javascript, in this case, it indicates that geometry has been selected and the extension                       
                    json_resp=json.dumps({"selection":"incident_type", "extension": "null"})
                    html=json_resp                                
                else:
                    self.incident_type="empty"
            else:
                self.incident_type="empty"
                
        ##PROCESS FOR SEND AND SEARCH*******************************************
            """
            In this part, when the button search is clicked for first time, it shows the search helper and changes the type of form to send (javascript will manage it)
            """
        elif self.type=="send" or self.type=="search":                     
            where="WHERE "
            if "geom" in self.dpost.keys():
                if self.dpost["geom"][0]!='none':
                    self.geom=self.dpost["geom"][0]
                    if self.geom=="POINT":
                        self.type_table='public.reportspoints'
                    elif self.geom=="LINE":
                        self.type_table='public.reportslines'
                    elif self.geom=="POLYGON":
                        self.type_table='public.reportspolygons'
                else:
                    self.geom="empty"    
            else:
                self.geom="empty"
                
            if "incident_type" in self.dpost.keys():
                if self.dpost["incident_type"][0]!='none':
                    self.incident_type=self.dpost["incident_type"][0]
                    if where=="WHERE ":
                        where+=" type = '"+self.incident_type+"' "
                    else:
                        where+=" AND type = '"+self.incident_type+"' "
                else:
                    self.incident_type="empty"
            else:
                self.incident_type="empty"
                
            #PROCESS FOR SEARCH*************************************************
            if self.type=="search":
                #pydevd.settrace()
                if "id" in self.dpost.keys():
                    self.id=self.dpost["id"][0]
                    if where=="WHERE ":
                        where+=" reportid = '"+self.id+"' "
                    else:
                        where+=" AND reportid = '"+self.id+"' "
                else:
                    self.id="empty"
                if where=="WHERE ":
                    where=""
                if self.geom!="empty":
                    sql="SELECT reportid FROM "+self.type_table+" "+where+";"
                else:
                    sql="SELECT reportid FROM public.reportspoints "+where+" UNION DISTINCT SELECT reportid FROM public.reportslines "+where+" UNION DISTINCT SELECT reportid FROM public.reportspolygons "+where+";"
                self.cursor.execute(sql)
                list_values=self.cursor.fetchall()
                #Here it creates the search helper depending on the SQL result
                html_section=templates.create_id(list_values)
                json_resp=json.dumps({"selection":"#final_id", "html": html_section, "extension": 'null'})
                html=json_resp
                
                
                
            #PROCESS FOR SEND***************************************************
                """
                In this part, when the button search is clicked for second time, it takes the selection from the search helper shows the results depending on the SQL generated
                """
            elif self.type=="send":
                #pydevd.settrace()
                variables= "reportid, type, description, image" 
                if self.dpost["final_id"][0]!='none':
                    self.final_id=self.dpost["final_id"][0]
                    if where=="WHERE ":
                        where+=" reportid = '"+self.final_id+"' "
                    else:
                        where+=" AND reportid = '"+self.final_id+"' "            
                else:    
                    self.final_id="empty"
                
                if where=="WHERE ":
                    where=""
                
                if self.geom=="POINT":    
                    sql_points="SELECT "+ variables +" FROM public.reportspoints "+where+";"
                    self.cursor.execute(sql_points)
                    list_points=self.cursor.fetchall()
                    table_points=templates.create_table(list_points)
                    table_lines=None
                    table_polygons=None
                elif self.geom=="LINE":
                    sql_lines="SELECT "+ variables +" FROM public.reportslines "+where+";"
                    self.cursor.execute(sql_lines)
                    list_lines=self.cursor.fetchall()
                    table_points=None
                    table_lines=templates.create_table(list_lines)
                    table_polygons=None
                elif self.geom=="POLYGON":
                    sql_polygons="SELECT "+ variables +" FROM public.reportspolygons "+where+";"
                    self.cursor.execute(sql_polygons)
                    list_polygons=self.cursor.fetchall()
                    table_points=None
                    table_lines=None      
                    table_polygons=templates.create_table(list_polygons)
                else:
                    sql_points="SELECT "+ variables +" FROM public.reportspoints "+where+";"
                    self.cursor.execute(sql_points)
                    list_points=self.cursor.fetchall()
                    table_points=templates.create_table(list_points)
                    sql_lines="SELECT "+ variables +" FROM public.reportslines "+where+";"
                    self.cursor.execute(sql_lines)
                    list_lines=self.cursor.fetchall()
                    table_lines=templates.create_table(list_lines)
                    sql_polygons="SELECT "+ variables +" FROM public.reportspolygons "+where+";"
                    self.cursor.execute(sql_polygons)
                    list_polygons=self.cursor.fetchall()
                    table_polygons=templates.create_table(list_polygons)
                
                html_section=templates.create_section_table(table_points, table_lines, table_polygons)
       
                json_resp=json.dumps({"selection":"#tables", "html": html_section, "extension": "null"})
                html=json_resp
                
        return html     
       
                    
    def process_form_register(self):
        """
        This function processes the data introduced on the form search and retrieves the data from the DB, creating the appropiate sql sentence
        Depending on which options has been chosen in the form
        """
        #pydevd.settrace()
        variables="name, surname, birthdate, countryoforigin, sex, postalcode, phonenumber, email, username, password, workingsector, typeofuser"
        values=""
        
        if 'name' in self.dpost.keys():
            self.name=self.dpost["name"][0]
        else:
            self.name="empty"
        values+="'"+self.name+"', "
            
        if 'surname' in self.dpost.keys():
            self.surname=self.dpost["surname"][0]
        else:
            self.surname="empty"
        values+="'"+self.surname+"', "
            
        if 'birth' in self.dpost.keys():
            self.birthdate=self.dpost["birth"][0]
        else:
            self.birthdate="empty"
        values+="'"+self.birthdate+"', "
            
        if 'country' in self.dpost.keys():
            self.countryoforigin=self.dpost["country"][0]
        else:
            self.countryoforigin="empty"
        values+="'"+self.countryoforigin+"', "
            
        if 'gender' in self.dpost.keys():
            self.sex=self.dpost["gender"][0]
        else:
            self.sex="empty"
        values+="'"+self.sex+"', "
            
        if 'pc' in self.dpost.keys():
            self.postalcode=self.dpost["pc"][0]
        else:
            self.postalcode="empty"
        values+="'"+self.postalcode+"', "
            
        if 'tel' in self.dpost.keys():
            self.phonenumber=self.dpost["tel"][0]
        else:
            self.phonenumber="empty"
        values+="'"+self.phonenumber+"', "
            
        if 'mail' in self.dpost.keys():
            self.email=self.dpost["mail"][0]
        else:
            self.email="empty"
        values+="'"+self.email+"', "
            
        if 'user' in self.dpost.keys():
            self.username=self.dpost["user"][0]
        else:
            self.username="empty"
        values+="'"+self.username+"', "
            
        if 'pass' in self.dpost.keys():
            self.password=self.dpost["pass"][0]
        else:
            self.password="empty"
        values+="'"+self.password+"', "
            
        if 'sector' in self.dpost.keys():
            self.workingsector=self.dpost["sector"][0]
        else:
            self.workingsector="empty"
        values+="'"+self.workingsector+"', "
            
        self.typeofuser='Editor'
        values+="'"+self.typeofuser+"'"
        
        ###********CHECK IF THE USER ALREADY EXISTS ON THE DATABASE***********##
        where_email="WHERE email='"+self.email+"';"
        where_username="WHERE username='"+self.username+"';"
        
        sql_email="SELECT email FROM public.users "+where_email
        sql_username="SELECT username FROM public.users "+where_username
        
        self.cursor.execute(sql_email)
        res_email=self.cursor.fetchall()
        self.cursor.execute(sql_username)
        res_username=self.cursor.fetchall()
        
        if res_email!=[]:
            json_resp=json.dumps({"existing":"email"})
        elif res_username!=[]:
            json_resp=json.dumps({"existing":"username"})
        else:
            #creates the SQL sentence for insert the new user on the DB
            sql="INSERT INTO public.users ("+variables+") VALUES ("+values+");"
            self.cursor.execute(sql)
            self.conn.commit()
            html_section="<section id='general_section'><h1>Hi "+self.username+" welcome to our comunity!</h1></section>"
            json_resp=json.dumps({"existing":"none", "html":html_section})
        
        html=json_resp
        
        return html

    
    def connection(self):
        """
        Function to connect with the Postgresql database
        """
        self.database='karlsruhedamagereport'
        self.user='postgres'
        self.password='postgres'
        self.host='localhost'
        self.port=5432
        self.conn=psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host, port=self.port)    
        self.cursor=self.conn.cursor()