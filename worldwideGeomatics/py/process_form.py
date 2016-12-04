# -*- coding: utf-8 -*-

'''
Created on 26/11/2016

@author: Worldwide Geomatics
'''

from templates import templates
from worldwide import wwfunctions
from py import conexion

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
        self.html=self.process_form()

    def process_form(self):
        """
        Studies which form has been sended and performs the necessary action
        """
        
        if self.name_form=="login_form":
            html=self.process_form_login()
            
        else:
            html='<section id="general_section"><h1>Nothing has been programmed yet for form {}'.format(self.name_form)+'</h1></section>'
        
        return html
    
    def process_form_login(self):
        self.user=self.dpost["user"][0]
        self.psw=self.dpost["pass"][0]
        
        oConexion=conexion.Conexion(self.user, self.psw)
        oSession=self.environ["beaker.session"]
        conexion.keep_session_variables(oSession, oConexion)
        
        if oConexion.conn:
            html='<section id="general_section"><h1>Logged as %s, with %s rights'%(self.user, oConexion.user_type)+'</h1></section>'
        else:
            html='<section id="general_section"><h1>The user %s is not registered.'%(self.user)+'</h1></section>'
        #tit="<h1>Logged as %s, with %s rights"%(self.user, self.psw)+"</h1>"
        
        return html