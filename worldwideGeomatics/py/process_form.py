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
from cgitb import html
from beaker.session import Session, _session_id
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
import json
import os
import sys
import the_porn_fighter
sys.path.append(r"D:\LiClipse\plugins\org.python.pydev_3.9.2.201502042042\pysrc")
#import pydevd

current_path=os.path.dirname(os.path.abspath(__file__))

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
            
        elif self.name_form=="create_form":
            self.connection()
            html=self.process_form_create()
            
        elif self.name_form=="edit_form":
            self.connection()
            html=self.process_form_edit()
            
        elif self.name_form=="click_table":
            self.connection()
            html=self.process_click_table()
        
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
        self.type=self.dpost["type-form"][0]  #First, it knows the option selected, this will be used for apply different processes
        
        ##PROCESS FOR GEOMETRY**************************************************
        """
        In this part, when the field geom is changed, it makes zoom to the objects as well as sends a json file with the selection "geometry" (javascript will manage it)
        """
        if self.type=="geometry":
            
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
                        
                    #With this sentence, it finds the incident types according to the geometry type
                    sql_geom="SELECT incident from public.incidents_type WHERE geometry='"+self.geom+"' ORDER BY incident"
                    self.cursor.execute(sql_geom)
                    result_type=self.cursor.fetchall()
                    #Here it creates a json file in order to send all the values needed by javascript, in this case, it indicates that geometry has been selected and the extension                
                    json_resp=json.dumps({"selection":"geometry", "extension":extension, "geom_type":result_type}) 
                    html=json_resp                    
                else:
                    self.geom="empty" 
                    json_resp=json.dumps({"selection":"geometry", "extension":'null', "geom_type":'null'}) 
                    html=json_resp    
            else:
                self.geom="empty"
        
        ##PROCESS FOR TYPE
            """
            In this part, when the field incident_type is changed, it makes zoom to the objects as well as sends a json file with the selection "incident_type" (javascript will manage it)
            """
        elif self.type=="incident_type":
            #pydevd.settrace()
            where="WHERE "
            if "incident_type" in self.dpost.keys():
                if self.dpost["incident_type"][0]!='none':
                    self.incident_type=self.dpost["incident_type"][0]
                    #Here it creates the WHERE part of the sql sentence depending on the incident_type chosen
                    where+=" type = '"+ str(self.incident_type)+"' "
                    
                    if self.dpost["geom"][0]=="POINT":
                        self.type_table='public.reportspoints'
                    elif self.dpost["geom"][0]=="LINE":
                        self.type_table='public.reportslines'
                    elif self.dpost["geom"][0]=="POLYGON":
                        self.type_table='public.reportspolygons'
                        
                    #With this sentence, it returns the extension of the selection
                    sql= 'SELECT ST_AsGeoJSON(ST_Extent(geometry)) FROM '+self.type_table+' '+where+";"
                    self.cursor.execute(sql)
                    result=self.cursor.fetchall()
                    if (result==[(None,)] or result==[]):
                        extension='null'
                    else:
                        extension=result[0][0]
                    #Here it creates a json file in order to send all the values needed by javascript, in this case, it indicates that geometry has been selected and the extension                       
                    json_resp=json.dumps({"selection":"incident_type", "extension": extension})
                    html=json_resp                                
                else:
                    self.incident_type="empty"
                    json_resp=json.dumps({"selection":"incident_type", "extension": 'null'})
                    html=json_resp
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
                    sql="SELECT reportid FROM "+self.type_table+" "+where+" ORDER BY reportid ASC;"
                else:
                    sql="SELECT reportid FROM public.reportspoints "+where+" UNION DISTINCT SELECT reportid FROM public.reportslines "+where+" UNION DISTINCT SELECT reportid FROM public.reportspolygons "+where+" ORDER BY reportid ASC;"
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
                    sql_points="SELECT "+ variables +" FROM public.reportspoints "+where+" ORDER BY reportid ASC;"
                    self.cursor.execute(sql_points)
                    list_points=self.cursor.fetchall()
                    table_points=templates.create_table(list_points, 'tab_points')
                    table_lines=None
                    table_polygons=None
                elif self.geom=="LINE":
                    sql_lines="SELECT "+ variables +" FROM public.reportslines "+where+" ORDER BY reportid ASC;"
                    self.cursor.execute(sql_lines)
                    list_lines=self.cursor.fetchall()
                    table_points=None
                    table_lines=templates.create_table(list_lines, 'tab_lines')
                    table_polygons=None
                elif self.geom=="POLYGON":
                    sql_polygons="SELECT "+ variables +" FROM public.reportspolygons "+where+" ORDER BY reportid ASC;"
                    self.cursor.execute(sql_polygons)
                    list_polygons=self.cursor.fetchall()
                    table_points=None
                    table_lines=None      
                    table_polygons=templates.create_table(list_polygons, 'tab_polygons')
                else:
                    sql_points="SELECT "+ variables +" FROM public.reportspoints "+where+" ORDER BY reportid ASC;"
                    self.cursor.execute(sql_points)
                    list_points=self.cursor.fetchall()
                    table_points=templates.create_table(list_points, 'tab_points')
                    sql_lines="SELECT "+ variables +" FROM public.reportslines "+where+" ORDER BY reportid ASC;"
                    self.cursor.execute(sql_lines)
                    list_lines=self.cursor.fetchall()
                    table_lines=templates.create_table(list_lines, 'tab_lines')
                    sql_polygons="SELECT "+ variables +" FROM public.reportspolygons "+where+" ORDER BY reportid ASC;"
                    self.cursor.execute(sql_polygons)
                    list_polygons=self.cursor.fetchall()
                    table_polygons=templates.create_table(list_polygons, 'tab_polygons')
                
                html_section=templates.create_section_table(table_points, table_lines, table_polygons)
       
                json_resp=json.dumps({"selection":"#tables", "html": html_section, "extension": "null"})
                html=json_resp
                
        return html     
       
                    
    def process_form_register(self):
        """
        This function processes the data introduced on the form search and inserts the data into the DB, creating the appropiate sql sentence
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
        values+="'"+self.email.lower()+"', "
            
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
        where_email="WHERE email='"+self.email.lower()+"';"
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
    
    
    def process_form_create(self):
        """
        This function processes the data introduced on the form create and inserts the data into the DB, creating the appropiate sql sentence
        Depending on which options has been chosen in the form
        """
        variables="type, description, solved, geometry, userid, image, emergency"
        values=""
        
        #pydevd.settrace()
        self.type=self.dpost["type-form"][0]  #First, it knows the type of form, this will be used for apply different processes
        
        #Global checking variables
        check_type=False
        inserted=False
        #pydevd.settrace()
        #******************************* GEOMETRY *******************************************#
        #First, it takes the geometry type and generates the list of incidents
        if self.type=="point":
            self.geom="POINT"
            self.type_table='public.reportspoints'
            
            #With this sentence, it finds the incident types according to the geometry type
            sql_geom="SELECT incident from public.incidents_type WHERE geometry='"+self.geom+"' ORDER BY incident"
            self.cursor.execute(sql_geom)
            result_type=self.cursor.fetchall()
            
            #******************************** ID **********************************#
            #Here it finds the last ID of the corresponding table and indicates the next id on the ID field
            sql_id="SELECT reportid FROM "+self.type_table+" ORDER BY reportid DESC LIMIT 1"
            self.cursor.execute(sql_id)
            result_id=self.cursor.fetchall()
            if result_id!=[]:
                last_id=result_id[0][0]
            else:
                last_id='null'
        
        if self.type=="line":
            self.geom="LINE"
            self.type_table='public.reportslines'
            
            #With this sentence, it finds the incident types according to the geometry type
            sql_geom="SELECT incident from public.incidents_type WHERE geometry='"+self.geom+"' ORDER BY incident"
            self.cursor.execute(sql_geom)
            result_type=self.cursor.fetchall()
            
            #******************************** ID **********************************#
            #Here it finds the last ID of the corresponding table and indicates the next id on the ID field
            sql_id="SELECT reportid FROM "+self.type_table+" ORDER BY reportid DESC LIMIT 1"
            self.cursor.execute(sql_id)
            result_id=self.cursor.fetchall()
            if result_id!=[]:
                last_id=result_id[0][0]
            else:
                last_id='null'
        
        if self.type=="polygon":
            self.geom="POLYGON"
            self.type_table='public.reportspolygons'
            
            #With this sentence, it finds the incident types according to the geometry type
            sql_geom="SELECT incident from public.incidents_type WHERE geometry='"+self.geom+"' ORDER BY incident"
            self.cursor.execute(sql_geom)
            result_type=self.cursor.fetchall()
            
            #******************************** ID **********************************#
            #Here it finds the last ID of the corresponding table and indicates the next id on the ID field
            sql_id="SELECT reportid FROM "+self.type_table+" ORDER BY reportid DESC LIMIT 1"
            self.cursor.execute(sql_id)
            result_id=self.cursor.fetchall()
            if result_id!=[]:
                last_id=result_id[0][0]
            else:
                last_id='null'
            
        
            
        #************************* TYPE OF INCIDENT ***************************#
        if 'incident_type' in self.dpost.keys():
            self.incident_type=self.dpost["incident_type"][0]
            #**************************** INCIDENT TYPE ***************************#
            #creates the SQL sentence for insert the new user on the DB
            
            sql_check_type="SELECT incident from public.incidents_type WHERE geometry='"+self.geom+"' ORDER BY incident"
            self.cursor.execute(sql_check_type)
            result_type=self.cursor.fetchall()
            for incident in result_type:
                type_db=str(incident[0])
                if self.incident_type==type_db:
                    check_type=True
                    inserted=True
                    break
                    
            if check_type==True:
                hack_alert='null'
            else:
                hack_alert="Not bad, but you will have to do it better :)"

        else:
            self.incident_type="empty"
        values+="'"+self.incident_type+"', "

        #**************************** DESCRIPTION *****************************#
        if 'desc' in self.dpost.keys():
            #************************ SPAM CONTROL ****************************#
            file_name=os.path.join(current_path, 'list_porn.txt')
            porn_list=open(file_name,'r')
            list_vector=[]
            for word in porn_list:
                list_vector.append(word.rstrip())
            porn_filter = the_porn_fighter.PornFighter(list_vector, replacements="$@%-?!")
            porn_filter.inside_words=True
            porn_filter.complete=True
            spam_desc=porn_filter.clean(str(self.dpost["desc"][0]))
            self.desc=spam_desc
        else:
            self.desc="empty"
        values+="'"+self.desc+"', "

        
        #******************************* SOLVED *******************************#
        self.solved='False'
        values+="'"+self.solved+"', "
        
        #****************************** GEOMETRY ******************************#
        #pydevd.settrace()
        if 'type-geometry' in self.dpost.keys():
            if self.dpost["type-geometry"][0]!="":
                if self.geom=="POINT":
                    coord=self.dpost["type-geometry"][0].split(",")
                    self.geometry="ST_GeomFromText('POINT("+coord[0]+" "+coord[1]+")',4326)"

                if self.geom=="LINE":
                    coord=self.dpost["type-geometry"][0].split(",")
                    coord_string="LINESTRING("
                    for i in range(0, len(coord), 2):
                        coord_string+=coord[i]+" "+coord[i+1]+","
                    coord_fin=coord_string[:-1]+")"
                    self.geometry="ST_GeomFromText('"+coord_fin+"',4326)"
                    
                if self.geom=="POLYGON":
                    coord=self.dpost["type-geometry"][0].split(",")
                    coord_string="POLYGON(("
                    for i in range(0, len(coord), 2):
                        coord_string+=coord[i]+" "+coord[i+1]+","
                    coord_fin=coord_string[:-1]+"))"
                    self.geometry="ST_GeomFromText('"+coord_fin+"',4326)"
                    
                values+=self.geometry+", "
                inserted=True
                missing='null'
        else:
            inserted=False
            missing="Please, digitalize a feature for creating an incident"
        
        
        #****************************** USER ID ********************************
        
        user=str(self.environ['beaker.session']._sess['user'])
        sql_userid="SELECT userid from public.users WHERE username='"+user+"'"
        self.cursor.execute(sql_userid)
        result_userid=self.cursor.fetchall()
        
        if result_userid!=[]:
            self.userid=result_userid[0][0]
            values+="'"+str(self.userid)+"', "
        
        
        #******************************* IMAGE ********************************#
        if 'img' in self.dpost.keys():
            self.img=self.dpost["img"][0]
        else:
            self.img="empty"
        values+="'"+self.img+"', "
        
        #***************************** EMERGENCY ******************************#
        self.emergency='False'
        values+="'"+self.solved+"'"
             
        
        
        #************* CHECK IF THE USER HAS DIGITALIZED BEFOR INSERT *********#
        if inserted==True and check_type==True:
            #pydevd.settrace()
            sql="INSERT INTO "+self.type_table+" ("+variables+") VALUES ("+values+");"
            self.cursor.execute(sql)
            self.conn.commit()
            json_resp=json.dumps({"selection":"geometry", "geom_type":result_type, "last_id":last_id, "hack":hack_alert, "geometry":missing, "created":self.geom+" created!"})   
        else: 
            json_resp=json.dumps({"selection":"geometry", "geom_type":result_type, "last_id":last_id})   

        html=json_resp
        
        return html
    
    def process_form_edit(self):
        """
        This function processes the data introduced on the form create and inserts the data into the DB, creating the appropiate sql sentence
        Depending on which options has been chosen in the form
        """
        
        self.option=self.dpost["option"][0]  #First, it knows the type of form, this will be used for apply different processes
        
        variables="(type, description, solved, emergency)"
        values=""
        #pydevd.settrace()
        #ID of the selected feature
        if 'admin_id' in self.dpost.keys():
            self.admin_id=self.dpost["admin_id"][0]
            selected=True
        else:
            selected=False
            self.admin_id="empty"
        
        #Type of incident of the selected feature
        if 'old_type_admin' in self.dpost.keys():
            self.old_type_admin=self.dpost["old_type_admin"][0]
        else:
            self.old_type_admin="empty"
        
        #************************* TYPE OF INCIDENT ***************************#       
        if 'type_admin' in self.dpost.keys():
            table=self.dpost["table_selected"][0]
            if table=="public.reportspoints":
                geometry_type="POINT"
            if table=="public.reportslines":
                geometry_type="LINE"
            if table=="public.reportspolygons":
                geometry_type="POLYGON"
            self.type_admin=self.dpost["type_admin"][0]
            #**************************** INCIDENT TYPE ***************************#
            #creates the SQL sentence for insert the new user on the DB
            
            sql_check_type="SELECT incident from public.incidents_type WHERE geometry='"+geometry_type+"' ORDER BY incident"
            self.cursor.execute(sql_check_type)
            result_type=self.cursor.fetchall()
            for incident in result_type:
                type_db=str(incident[0])
                if self.type_admin==type_db:
                    check_type=True
                    inserted=True
                    break
                else:
                    check_type=False 
                    
            if check_type==True:
                hack_alert='null'
                values+="'"+self.type_admin+"', "
            else:
                values+="'"+self.old_type_admin+"', "
                hack_alert="Not bad, but you will have to do it better :)"  
        else:
            self.type_admin="empty"
            values+="'"+self.old_type_admin+"', "
        
        #Description of incident of the selected feature
        if 'old_desc_admin' in self.dpost.keys():
            self.old_desc_admin=self.dpost["old_desc_admin"][0]
        else:
            self.old_desc_admin="empty"
        
        #************************ DESCRIPTION UPDATED *************************#
        if 'desc_admin' in self.dpost.keys():
            #************************ SPAM CONTROL ****************************#
            file_name=os.path.join(current_path, 'list_porn.txt')
            porn_list=open(file_name,'r')
            list_vector=[]
            for word in porn_list:
                list_vector.append(word.rstrip())
            porn_filter = the_porn_fighter.PornFighter(list_vector, replacements="$@%-?!")
            porn_filter.inside_words=True
            porn_filter.complete=True
            spam_desc=porn_filter.clean(str(self.dpost["desc_admin"][0]))
            self.desc_admin=spam_desc
            values+="'"+self.desc_admin+"', "
        else:
            self.desc_admin="empty"
            values+="'"+self.old_desc_admin+"', "
        
        #Incident solved or not
        if 'solved' in self.dpost.keys():
            self.solved='TRUE'
        else:
            self.solved="FALSE"
        values+="'"+self.solved+"', "
            
        #Incident is an emergency or not
        if 'emergency' in self.dpost.keys():
            self.emergency='TRUE'
        else:
            self.emergency="FALSE"
        values+="'"+self.emergency+"'"
            
        if selected==True:
            if self.option=='update':
                #pydevd.settrace()
                sql_update="UPDATE "+table+" SET "+variables+" = ("+values+") WHERE reportid = "+self.admin_id
                self.cursor.execute(sql_update)
                self.conn.commit()
                message="null"
                updated="Feature updated!"
                deleted="null"
            if self.option=='delete':
                sql_delete="DELETE FROM "+table+" WHERE  reportid = "+self.admin_id
                self.cursor.execute(sql_delete)
                self.conn.commit()
                message="null"
                updated="null"
                deleted="Feature deleted!"
        else:
            message="Select a feature to update or delete"
            updated="null"
            deleted="null"
        
        json_resp=json.dumps({"message":message, "updated": updated, "deleted": deleted})
        html=json_resp
        
        return html
            
    
    def process_click_table(self):
        id_feature=self.dpost["result"][0]
        table=self.dpost["type_table"][0]
        menu_option=self.dpost["menu_option"][0]
        if table=="tab_points":
            table_selected="public.reportspoints"
            geometry_type="POINT"
        if table=="tab_lines":
            table_selected="public.reportslines"
            geometry_type="LINE"
        if table=="tab_polygons":
            table_selected="public.reportspolygons"
            geometry_type="POLYGON"
        where="WHERE reportid = '"+ str(id_feature)+"'"
        sql= 'SELECT ST_AsGeoJSON(ST_Extent(geometry)) FROM '+table_selected+' '+where+";"                    
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        if (result==[(None,)] or result==[]):
            extension='null'
        else:
            extension=result[0][0]
        
        if menu_option=="editing_li":
            #pydevd.settrace()
            sql_values='SELECT * FROM '+table_selected+' '+where+";"
            self.cursor.execute(sql_values)
            result_values=self.cursor.fetchall()
            if (result_values==[(None,)] or result_values==[]):
                values='null'
            else:
                values=result_values[0]
            
            #With this sentence, it finds the incident types according to the geometry type
            sql_geom="SELECT incident from public.incidents_type WHERE geometry='"+geometry_type+"' ORDER BY incident"
            self.cursor.execute(sql_geom)
            result_type=self.cursor.fetchall()
        else:
            result_type='null'
            values='null'
                             
        json_resp=json.dumps({"section":"click_table", "extension": extension, "values":values, "menu_option": menu_option, "table_selected": table_selected, "incident_type": result_type})
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