from crypt import methods
from importlib.resources import contents
from flask import Flask, render_template, request
import os
import NLTK_alolitm
app = Flask(__name__, template_folder='template')
temp  = os.getcwd() + "/flask/Document"
name = []

@app.route('/')
def upload_file():
    print(temp)
    return render_template('index.html')

@app.route('/show_file', methods = ['POST'])
def display_file():
    f = request.files.getlist('file[]')
    for i in f :
        comm = os.path.join(temp,i.filename)
        i.save(comm)
        name.append(comm)   
        
    return render_template('index.html',contents = name) 

@app.route('/search_word',methods = ['POST'])
def search_word():
    key = request.form['key']
    res = NLTK_alolitm.Algolitm(name,key)
    
    return render_template('index.html',res = res)

@app.route('/top5',methods = ['POST'])
def top5w():
    hower = NLTK_alolitm.BOW()
    return render_template('index.html',hower = hower)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)

