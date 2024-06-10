from flask import Flask
from flask_cors import CORS
from flask import Blueprint, jsonify,request
import pymysql
## Funcion para conectarnos a la base de datos de mysql
avistador_blueprint = Blueprint('avistador',__name__)
def conectar(vhost,vuser,vpass,vdb):
     conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb,)
     return conn 

@avistador_blueprint.route("/registrar_avistador",methods=['POST'])
def registrar_avistador():
    try:
        conn=conectar('localhost','root','','rasc')
        cur = conn.cursor()
        x=cur.execute(""" insert into avistador (ficha,nombre,correo) values \
            ('{0}','{1}','{2}')""".format(request.json['ficha'],\
            request.json['nombre'],request.json['correo']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
    

#consulta_general
avistador_blueprint.route("/avistador_general",)
def consulta_general():
    try:
        conn=conectar ('localhost','root','','rasc')
        cur = conn.cursor()
        cur.execute("""SELECT * FROM avistador """)
        datos=cur.fetchall()
        data=[]
        for row in datos:
            dato={'ficha':row[0],'nombre':row[1],'correo':row[2]}
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify({'baul':data,'mensaje':'Usuarios registrados'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'error'})
    
    
##eliminar avistador
avistador_blueprint.route("/actualizar_avistador/<id>",methods=['PUT'])
def actualizar(id):
    try:
        conn=conectar('localhost','root','','rasc')
        cur = conn.cursor()
        x=cur.execute("""update avistador set ficha='{0}',nombre='{1}',correo='{2}' where\ 
                id={3}""".format(request.json['ficha'],request.json['nombre'],\
                        request.json['correo'],id))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'registro actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'error'})

