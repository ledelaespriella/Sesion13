from flask import Flask, render_template, request, flash
import os
from formularios import formEstudiante,formLogin
import sqlite3
from sqlite3 import Error
from markupsafe import escape


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=['GET', 'POST'])
def home():
    form = formEstudiante()
    
    return render_template("Estudiantes.html", form=form)

@app.route("/estudiante/save", methods=['POST'])
def guardar_estudiante():
    form = formEstudiante()
    
    if request.method =='POST':
        documento = form.documento.data
        nombre = form.nombre.data
        ciclo=form.ciclo.data
        sexo= form.sexo.data
        estado= form.estado.data
        
        try:
            with sqlite3.connect('Estudiantes.db') as con:
                cur=con.cursor() #manipula la conexion a la base de datos
                cur.execute("INSERT INTO estudiantes(documento,nombre,ciclo,sexo,estado) VALUES(?,?,?,?,?)",(documento,nombre,ciclo,sexo,estado))
                con.commit()
                return "Guardado satisfactoriamente"
            
        except Error as e:
            print(e)
    return "No se pudo guardar"
   
@app.route("/estudiante/get", methods=['POST'])
def estudiante_get():
    form = formEstudiante()
    
    if request.method =='POST':
        documento = form.documento.data 
          
        try:
            with sqlite3.connect('Estudiantes.db') as con:
                con.row_factory=sqlite3.Row #convierte la respuesta de la Bd en un diccionario
                cur=con.cursor() #manipula la conexion a la base de datos
                cur.execute("SELECT * FROM estudiantes WHERE documento=?",[documento])
                row = cur.fetchone()
                if row is None:
                    flash("Estudiante no se encuentra en la base de datos")
                return render_template("vista_estudiante.html",row=row)
                      
        except Error as e:
            print(e)
    return "Error en el metodo"

@app.route("/estudiante/list", methods=['POST'])
def estudiante_list():
    if request.method =='POST':
        try:
            with sqlite3.connect('Estudiantes.db') as con:
                con.row_factory=sqlite3.Row #convierte la respuesta de la Bd en un diccionario
                cur=con.cursor() #manipula la conexion a la base de datos
                cur.execute("SELECT * FROM estudiantes")
                row = cur.fetchall()
                if row is None:
                    flash("No existe informacion alguna en la base de datos")
                return render_template("vista_estudiante.html",row=row)
                      
        except Error as e:
            print(e)
    return "Error en el metodo"

@app.route("/estudiante/update", methods=['POST'])
def estudiante_update():
    form = formEstudiante()
    
    if request.method =='POST':
        documento = form.documento.data
        nombre = form.nombre.data
        ciclo=form.ciclo.data
        sexo= form.sexo.data
        estado= form.estado.data
        try:
            with sqlite3.connect('Estudiantes.db') as con:
                con.row_factory=sqlite3.Row #convierte la respuesta de la Bd en un diccionario
                cur=con.cursor() #manipula la conexion a la base de datos
                cur.execute("UPDATE estudiantes SET nombre=?, ciclo=?, sexo=?, estado=? WHERE documento=?",(nombre,ciclo,sexo,estado,documento))
                con.commit()
                if con.total_changes > 0:
                    mensaje = " Estudiante modificado"
                else:
                    mensaje = "Estudiante no modificado"
                
                      
        except Error as e:
            print(e)
        finally:
            return mensaje

@app.route("/estudiante/delete", methods=['POST'])
def estudiante_delete():
    form = formEstudiante()
    
    if request.method =='POST':
        documento = form.documento.data 
          
        try:
            with sqlite3.connect('Estudiantes.db') as con:
                cur=con.cursor() #manipula la conexion a la base de datos
                cur.execute("DELETE FROM estudiantes WHERE documento=?",[documento])
                if con.total_changes > 0:
                    mensaje = " Estudiante eliminado"
                else:
                    mensaje = "Estudiante no encontrado"
                      
        except Error as e:
            print(e)
        finally:
            return mensaje
    
#inyección SQL
@app.route("/login", methods=["GET", "POST"])
def login():
    form = formLogin()
    if request.method == "GET":
        return render_template("login.html", form=form)
    
    if request.method == "POST":
        user = form.usuario.data
        password = form.clave.data
        try:
            with sqlite3.connect("Estudiantes.db") as con:
                cur = con.cursor()                                      #' or 1=1 --
                #cur.execute("SELECT * FROM Usuarios WHERE usuario = '"+user+"' AND clave='"+password+"' ") 
                cur.execute("SELECT * FROM Usuarios WHERE usuario = ? AND clave=? ", [user, password]) #de esta manera se evita la inyección
                if cur.fetchone():
                    return "Usuario logueado"
                else:
                    return "Usuario no permitido"
        except Error:
            print(Error)

#inyeccion js
@app.route("/inyeccion_xss", methods=["GET", "POST"])            
def inyect():
    form=formLogin()
    if request.method == "GET":
        return render_template("xss.html", form=form)
    if request.method == "POST":
        usuario=escape(form.usuario.data)
        
        return usuario
    

    

if __name__ == '__main__':
    app.run(debug=True, port=8000)