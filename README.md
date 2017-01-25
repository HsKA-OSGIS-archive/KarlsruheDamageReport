# KarlsruheDamageReport
Repo for Worldwide Geomatics

**************** INSTALL PROJECT **********************

1º Download and install the ms4w folder from: http://ms4w.com/
	Now, you have to have the ms4w folder into your C:/ where Apache folder is into this one.

2º Open the file "httpd.conf", located inside of C:\ms4w\Apache\conf and <IfModule dir_module> has to be like this:
	<IfModule dir_module>
    		DirectoryIndex index.html index.html.var index.php index.phtml index.php3 index.cgi index.wsgi
	</IfModule>

3º Add also this lines into "httpd.conf":
	#Handler of scripts wsgi
	AddHandler wsgi-script .wsgi

4º Add into this folder "C:\ms4w\Apache\modules" the file "mod_wsgi.so". You can find this file in our configuration_help folder located in our github

5º Continuing into the "httpd.conf" file, add these lines after the last LoadModule:
	#Load wsgi Module
	LoadModule wsgi_module modules/mod_wsgi.so

6º Create a new folder named "desweb" into "C:\ms4w\apps" and copy the project folder "worldwideGeomatics" into "C:\ms4w\apps\desweb".

7º Create a new file named "httpd_worldwideGeomatics.conf" into "C:\ms4w\httpd.d" and add next lines inside:

	WSGIScriptAlias "/worldwideGeomatics/" "C:/ms4w/apps/desweb/worldwideGeomatics/index.py"
	
	<Directory "C:/ms4w/apps/desweb/worldwideGeomatics/">
	  AllowOverride None
	  Order deny,allow
	  Allow from all
	</Directory>

8º Create a new file named "httpd_desweb.conf" into "C:\ms4w\httpd.d" and add next lines inside:

	alias "/desweb/" "C:/ms4w/apps/desweb/"

	<Directory "C:/ms4w/apps/desweb">
		Options -Indexes FollowSymLinks
		AllowOverride None
		Order deny,allow
		Allow from all
	</Directory>

9º Install psycopg2 using pip (python) in cmd. --> (pip install psycopg2)

10º Install beaker using pip (python) in cmd. --> (pip install beaker)


****************DATABASE CONFIGURATION*****************

1º Install postgresql with postGis extension in you computer (for example v.5.5)

2º Open pgAdminIII and create a new database named "karlsruhedamagereport" (IMPORTANT: name must be the same)

3º Restore de database created with "karlsruhedamagereport.backup". You can find this file in our configuration_help folder located in our github.

********************* GEOSERVER ************************ 
