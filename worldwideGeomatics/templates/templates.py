# -*- coding: utf-8 -*-

'''
Created on 26/11/2016

@author: Worldwide Geomatics
'''

import worldwide.wwfunctions
import formulars
import os

dir_base=os.path.dirname(__file__) #path to current file

def create_head():
    """
    The document starts and creates the head
    """
    file_name=dir_base+"/html_sections/head.html"
    head=worldwide.wwfunctions.read_file(file_name)
    
    return head

def create_header():
    """
    Starts the body and creates the main menu
    """
    file_name=dir_base+"/html_sections/header.html"
    header=worldwide.wwfunctions.read_file(file_name)
    
    return header

def create_map():
    """
    Creates the map
    """
    file_name=dir_base+"/html_sections/map.html"
    map_sec=worldwide.wwfunctions.read_file(file_name)
    
    return map_sec

def create_section_points():
    """
    Creates the points section
    """
    file_name=dir_base+"/html_sections/table_points.html"
    points_sec=worldwide.wwfunctions.read_file(file_name)
    
    return points_sec

def create_section_lines():
    """
    Creates the lines section
    """
    file_name=dir_base+"/html_sections/table_lines.html"
    lines_sec=worldwide.wwfunctions.read_file(file_name)
    
    return lines_sec

def create_section_polygons():
    """
    Creates the polygons section
    """
    file_name=dir_base+"/html_sections/table_polygons.html"
    polygons_sec=worldwide.wwfunctions.read_file(file_name)
    
    return polygons_sec

def create_section_table(table_points=None, table_lines=None, table_polygons=None):
    """
    Creates the table, replacing a dictionary with the table on the html
    """
    section_tables="<section id='tables' class='tables'>"
    if table_points!=None:
        dic_points={}
        dic_points["TABLE_POINTS"]=table_points
        points=worldwide.wwfunctions.replace_text(create_section_points(), dic_points)
        section_tables+=points
        
    if table_lines!=None:
        dic_lines={}
        dic_lines["TABLE_LINES"]=table_lines
        lines=worldwide.wwfunctions.replace_text(create_section_lines(), dic_lines)
        section_tables+=lines
        
    if table_polygons!=None:
        dic_polygons={}
        dic_polygons["TABLE_POLYGONS"]=table_polygons
        polygons=worldwide.wwfunctions.replace_text(create_section_polygons(), dic_polygons)
        section_tables+=polygons
    
    section_tables+="</section>"
    
    return section_tables

def create_aside():
    """
    Creates the lateral menu
    """
    file_name=dir_base+"/html_sections/aside.html"
    aside=worldwide.wwfunctions.read_file(file_name)
    
    return aside

def create_footer():
    """
    Creates the footer and finishes the html
    """
    file_name=dir_base+"/html_sections/footer.html"
    footer=worldwide.wwfunctions.read_file(file_name)
    
    return footer

def start_general_section():
    """
    Starts general section
    """
    html='<section id="general_section">'
    
    return html

def close_general_section():
    """
    Closes general section
    """
    html='</section>'
    
    return html

def create_complete_page(draw_map=False, draw_search=False, html_ins=None):
    """
    Creates a web page with all of its parts and allows changing the content
    of the main section giving the html code and allows to visualize or not 
    the map and the table.

    Parameters:
    * draw_map: if it's true, it will creates openlayers map section
    * draw_table: if it's true, it will creates the table
    * html_ins: html code
    """
    #pydevd.settrace()

    head=create_head()
    header=create_header()
    start_general=start_general_section()
    
    if draw_map:
        map_sec=create_map()
    else:
        map_sec=""
        
    if draw_search:
        search=formulars.create_search()
    else:
        search=""
        
    tables="""
    <section id='tables' class='tables' style="display:none;"></section>
    """
        
    if html_ins <> None:
        section=html_ins
    else:
        section=""
        
    close_general=close_general_section()
    aside=create_aside()
    footer=create_footer()
    html=head+header+map_sec+start_general+section+search+tables+close_general+aside+footer 
    return html

def create_table(list_values):
    """
    This function creates a table in html from a list of values
    """
    table="<table>\n"
    table+="""
    <thead>\n
    <th>ID</th>\n
    <th>TYPE</th>\n
    <th>DESCRIPTION</th>\n
    <th>IMAGE</th>\n
    </thead>\n
    <tbody>\n
    """
    for row in list_values:
        table+='<tr>\n'
        for value in range(0, len(row)):
            table+="<td>"+str(row[value])+"</td>\n"    #for to create each value of each object/attribute (row) of the table
        table+="</tr>\n"
    table+="</tbody>\n</table>"
    
    return table


def create_id(list_values):
    """
    This function creates the aditional input field for select the id on the form search
    """
    if list_values!=[]:
        html='<select id="final_id" name="final_id" class="correct">\n<option value="none">All ID</option>\n'
        for element in list_values:
            html+='<option value="'+str(element[0])+'">'+str(element[0])+'</option>\n'
        html+="</select>\n"
    else:
        html='<select id="final_id" name="final_id" class="error" required>\n<option value="none">There are no coincidences on the DB</option>\n</select>\n'
    
    return html