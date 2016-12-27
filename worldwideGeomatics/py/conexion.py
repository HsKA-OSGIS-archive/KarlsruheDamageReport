# -*- coding: utf-8 -*-

'''
Created on 26/11/2016

@author: Worldwide Geomatics
'''

from templates import templates
from worldwide import wwfunctions

import sys
sys.path.append(r"D:\LiClipse\plugins\org.python.pydev_3.9.2.201502042042\pysrc")
#import pydevd

class Conexion():
    """
    Class that process the received forms
    """
    #Variables de la clase
    user=None
    password=None
    conn=None
    user_type=None
    
    def __init__(self, user, password, type):
        #Check which user is
        if user!="" and password!="" and type!="":
            self.conn=True
        else:
            self.conn=False
            
        #If it's connected, adds the values of user and password
        if self.conn:           
            self.user=user
            self.password=password
            self.user_type=type
        else:
            self.user_type= False
            self.user= False
            self.password= False
        
#This function keeps the variables in a dictionary
def keep_session_variables(oSession, oConexion):
    oSession["user"] = oConexion.user
    oSession["password"] = oConexion.password    
    oSession["user_type"] = oConexion.user_type
    oSession.save()
    
#This function checks if the dictionary has the variables and, in that case,
#it loggin with them
def check_session(oSession):
    if oSession.has_key("user") and oSession.has_key("password"):
        oConexion=Conexion(oSession["user"], oSession["password"], oSession["user_type"])
    else:
        oConexion=Conexion("", "", "")        
    return oConexion

def logout(oSession):
    oSession.delete()
    oSession.invalidate()