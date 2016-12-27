'''
Created on 26/11/2016

@author: WorldWide Geomatics
'''

import os.path

def read_file(file_name):
    """It receives the name of a file and return its content in a string
    This function doesn't have error control"""
    if os.path.isfile(file_name):
        file_open=open(file_name, 'r') #Path from the main program
        content=file_open.read()
        file_open.close()
    else:
        content="The file doesn't exist"
    return content


def replace_text(chain_string, dictionary):
    """
    This function receives a string and a dictionary.
    It returns a string where it has replaced the keys of a dictionary
    that were on the string with the values of those keys stored on the
    dictionary.
    
    chain_string: "The song is: {{title}}. The author is: {{author}}"
    
    dictionary:
    di=dict()
    di["{{title}}"]="The number of the beast"
    di["{{author}}"]="Iron Maiden"
    
    Example of use: replace(chain_string, dictionary)
    
    Returns: The song is: The number of the beast. The author is: Iron Maiden
    """
    
    a=chain_string #makes a copy of the string in order to not modify the original
    
    for key in dictionary.keys():
        key2='{{'+key+'}}'
        a=a.replace(key2, dictionary[key])
    return a


from urlparse import parse_qs #Standard python library

def return_dict_get(environ):
    """
    This function returns a dictionary with the values of a request using
    method get
    """
    qs = environ['QUERY_STRING']
    d=parse_qs(qs, True) #The true parameter keeps blanc values, the key
                        #will stay but the value will be ""
    
    return d


def return_dict_post(environ):
    """
    Returns a dictionary key:value with the data of the formular.
    The keys are strings and the values are lists of values.
    IMPORTANT, once the post content has been read, it will not be read again,
    it will be bloqued in the computer.
    This function can only be called once per formular.
    """
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)
    return d