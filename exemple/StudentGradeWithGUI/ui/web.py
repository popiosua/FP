'''
Created on Nov 28, 2018

@author: Dell
'''
from flask import Flask, jsonify

class WebPagesUI:
    def __init__(self,serv):
        self.__srv = serv
        self.__app = Flask(__name__)
        self.__app.add_url_rule('/', 'index', self.index)
        self.__app.add_url_rule('/cati', 'cati', self.howManyStudents)
        self.__app.add_url_rule('/studenti', 'studenti', self.search)
        
    def startUI(self):
        self.__app.run(debug=True)
    
    def index(self):
        return "<h1>Aplicatie WEB<h1><a href='/cati'>Cati studenti?</a><br><a href='/studenti'>Studentii?</a>"
    
    def howManyStudents(self):
        return str(self.__srv.getNrStudents())
    
    def search(self):
        return jsonify([toDict(e) for e in self.__srv.search("")])

def toDict(st):
    return {"ID":st.getId(),"name":st.getName(),"adress":str(st.getAdr())}