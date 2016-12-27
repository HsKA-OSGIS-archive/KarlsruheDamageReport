# -*- coding: utf-8 -*-

'''
Created on 26/11/2016

@author: Worldwide Geomatics
'''
from worldwide import wwfunctions
from templates import templates
from templates import formulars
from templates.templates import start_general_section, create_map, create_section_table, close_general_section
from py import conexion

def process_menu_option(environ, oConnexion):
    """
    This function studies the option of the menu that has been chosen and
    generates the appropriate page.
    The first time returns the complete page but the rest it only changes
    the section that should be inserted in the document using Ajax
    """
    
    d=wwfunctions.return_dict_get(environ)
    application=d.get('application',[''])[0] #Returns [''] if there's no key
    #that means is the first time that it's executed
    
    if application=="":
        """
        Returns the complete page
        """
        html=templates.create_complete_page(True, True)
        
    elif application=="home":
        """
        Returns the home page
        """
        start_general=start_general_section()
        search=formulars.create_search()
        tables="""
            <section id='tables' class='tables' style="display:none;"></section>
            """
        close_general=close_general_section()
        html=start_general+search+tables+close_general
        
    elif application=="create":
        """
        Returns the create page
        """
        
        if oConnexion.conn==True:
            start_general=start_general_section()
            create=formulars.create_create()
            tables="""
            <section id='tables' class='tables' style="display:none;"></section>
            """
            close_general=close_general_section()
            html=start_general+create+tables+close_general
        elif oConnexion.conn==False:
            tit="<h1>You have to be logged to access this section</h1>"
            start_general=start_general_section()
            login=formulars.create_login()
            close_general=close_general_section()
            html=start_general+tit+login+close_general
        else:
            html='<section id="general_section"><h1>You have to be logged to access this section</h1></section>'
        
        
    elif application=="editing":
        """
        Returns the edit page
        """
        if oConnexion.user_type=="Administrator":
            start_general=start_general_section()
            edit=formulars.create_edit()
            tables="""
            <section id='tables' class='tables' style="display:none;"></section>
            """
            close_general=close_general_section()
            html=start_general+edit+tables+close_general
            
        elif oConnexion.conn==False:
            tit="<h1>You have to be logged as Administrator to access this section</h1>"
            start_general=start_general_section()
            login=formulars.create_login()
            close_general=close_general_section()
            html=start_general+tit+login+close_general 
            
        else:
            html='<section id="general_section"><h1>You have to be logged as Administrator to access this section</h1></section>'
        
    elif application=="login":
        """
        Returns the login page
        """
        start_general=start_general_section()
        login=formulars.create_login()
        close_general=close_general_section()
        html=start_general+login+close_general
        
    elif application=="logout":
        """
        Your session is disconnected
        """
        html='<section id="general_section"><h1>Your session is disconnected</h1></section>'
        
    elif application=="register":
        """
        Returns the register page
        """
        start_general=start_general_section()
        register=formulars.create_register()
        close_general=close_general_section()
        html=start_general+register+close_general
        
    else:
        start_general=start_general_section()
        content="<h1>Incorrect Option</h1>"
        close_general=close_general_section()
        html=start_general+content+close_general
        
    return html