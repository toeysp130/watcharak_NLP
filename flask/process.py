from importlib.resources import contents
from flask import Flask, render_template, request
import os
app = Flask(__name__, template_folder='template')
temp  = os.getcwd() + "/flask/Document"

@app.route('/')
def upload_file():
    print(temp)
    return render_template('index.html')

@app.route('/show_file', methods = ['POST'])
def display_file():
    f = request.files.getlist('file[]')
    article = []
    for i in f :
        comm = os.path.join(temp,i.filename)
        i.save(comm)
        file = open(comm,"r")
        article.append(file.read())   
        
    return render_template('index.html',contents = article) 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)