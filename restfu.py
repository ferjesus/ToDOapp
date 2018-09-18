#! /usr/bin/env python
from flask import Flask, request,jsonify
import json
import sys
from datetime import datetime
from Clases.CTarea import *

app = Flask(__name__)

# ------------------------------------------------
# WS CONSULTA DE TAREAS PENDIENTES
# ------------------------------------------------
@app.route('/wsConsultaTareas', methods=['POST'])
def f_ConsultaTarea():
    lo = CTarea()
    lo.pcParam = request.get_data()
    llOk = lo.omConsultaTareas()
    if not llOk:
       return lo.pcError
    return lo.pcData

@app.route('/wsRegistroTareas', methods=['POST'])
def f_RegistroTarea():
    lo = CTarea()
    lo.pcParam = request.get_data()
    llOk = lo.omRegistroTarea()
    if not llOk:
       return lo.pcError
    return lo.pcData






if __name__ == '__main__':
   #app.run(host='localhost', debug=True, port=8080)
   app.run(host='0.0.0.0', debug=True, port=8082, threaded=True)
   #app.run(host='192.168.0.3', debug=True, port=8080)
