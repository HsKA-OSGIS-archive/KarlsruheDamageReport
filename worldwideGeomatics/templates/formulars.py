# -*- coding: utf-8 -*-

'''
Created on 26/11/2016

@author: Worldwide Geomatics
'''

import worldwide.wwfunctions
import os

dir_base=os.path.dirname(__file__) #path to current file

def create_search():
    """
    Function to create the search formular
    """
    file_name=dir_base+"/html_formulars/search.html"
    search=worldwide.wwfunctions.read_file(file_name)
    
    return search

def create_create():
    """
    Function to create the create formular
    """
    file_name=dir_base+"/html_formulars/create.html"
    create=worldwide.wwfunctions.read_file(file_name)
    
    return create

def create_edit():
    """
    Function to create the edit formular
    """
    file_name=dir_base+"/html_formulars/edit.html"
    edit=worldwide.wwfunctions.read_file(file_name)
    
    return edit

def create_login():
    """
    Function to create the login formular
    """
    file_name=dir_base+"/html_formulars/login.html"
    login=worldwide.wwfunctions.read_file(file_name)
    
    return login

def create_register():
    """
    Function to create the register formular
    """
    file_name=dir_base+"/html_formulars/register.html"
    register=worldwide.wwfunctions.read_file(file_name)
    
    return register