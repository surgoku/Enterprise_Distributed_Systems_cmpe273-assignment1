from flask import Flask
import sys
import os
import subprocess

'''
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
'''

#'''
app = Flask(__name__)

global folder_name

#whenever we start a webserver on local machine, the server hits the localhost. Local host is nothing but the default webserver running on your local machine and it can be seen by https://localhost:5000/
#In flask @app.route enforces the response for the URL pattern mentioned in app.rooute method for example here '/' . / implies localhost:port#/ 
# default homepage url after localhost
@app.route("/") #response for the default page after running the app
def hello():
    return "Hello from Dockerized Flask App!!"


#"""
#2.#app.route are runtime methods which run when user execute the url pattern in web application. Flash tries to find the requesteed url pattern in app.route defintions.
@app.route("/v1/<variable>", methods=['GET']) # v1 is a static variable and in our project the url will be changing, the user will request content/data based on different/variable filename. The <variable> will take care of it.
def render_page(variable):
	global folder_name
	command_3 = 'cat ' + folder_name + "/" + variable
	cat_out = subprocess.check_output(command_3, shell=True)
	return cat_out
#"""

#1.
def process_args_and_get_data(args):   #ARGUMENT =URL
	git_url =  args[1]
	command = 'git clone ' + git_url
	os.system(command)
	a = git_url.split('/')
	folder_name = a[-1]
	#print a[-1]
	command_2 = 'ls ' + folder_name
	#files = os.system(command_2)
	files = subprocess.check_output(command_2, shell=True)
	list_files = files.split('\n')
	yml_files = [i for i in list_files if '.yml' in i ]
	return folder_name, yml_files

	

if __name__ == "__main__":
	#objective : return or show the file in a given url to repo. since the name of the folder can change and the return type and name of files are something that can change. Therefor we need to retrieve this info from clone repo.

	#""" 
	global folder_name
	args = sys.argv
	folder_name, yml_files = process_args_and_get_data(args) #getting the name of the clone folder. This helps in retrieving the requested file dynamically from this folder. 
	#"""

	app.run(debug=True,host='0.0.0.0') #runs the flask(server) and starts the app

#'''
 