# -*- coding: utf-8 -*-

'''
Created on 26/11/2016

@author: Worldwide Geomatics
'''

import sys
import os


sys.path.append("D:/LiClipse/plugins/org.python.pydev_3.9.2.201502042042/pysrc" )


dir_base=os.path.dirname(__file__)
sys.path.append(dir_base)

from worldwide import wwfunctions
import templates.templates
from py import process_menu_option
from py import process_form
from py import conexion

#import pydevd

def application(environ, start_response):
    #pydevd.settrace()
    
    d=wwfunctions.return_dict_get(environ)
    selection=d.get('application',[''])[0] #Returns [''] if there's no key
    #that means is the first time that it's executed
    
    if selection=="logout":
        oSession=environ["beaker.session"]
        oConnexion=conexion.logout(oSession)

    
    else:
        oSession=environ["beaker.session"]
        oConnexion=conexion.check_session(oSession)
    
    if environ['REQUEST_METHOD']=='POST':
        opf=process_form.process_forms(environ)
        html=opf.process_form()
    else:
        html=process_menu_option.process_menu_option(environ, oConnexion)
    #Envío al servidor. Siempre igual
    status='200 OK'
    response_headers = [('Content-Type', 'text/html'),('Content-Length', str(len(html)))]
    start_response(status, response_headers)
    return [str(html)]

from beaker.middleware import SessionMiddleware
application=SessionMiddleware(application)