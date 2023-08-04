#importacion del framework
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL


#inicializacion del APP o servidor
app= Flask(__name__)
#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
app.secret_key='mysecretkey'
mysql=MySQL(app)


#declaracion de ruta  http://localhost:5000 
@app.route('/')
def index():
    CC=mysql.connection.cursor()
    CC.execute('select * from albums1')
    conAlbums=CC.fetchall()
    #print(conAlbums)
    return render_template('index.html', listAlbums=conAlbums)

#ruta http:localhost:5000/guaradr tipo POST para Insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method =='POST':
        #pasamos a variables el contenido de los inputs
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
        #Conectar y ejecutar  el insert
        CS=mysql.connection.cursor()
        CS.execute('insert into albums1(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo, Vartista, Vanio))
        mysql.connection.commit()
        #print(titulo,artista,anio)
    
    flash('El album fue agregado correctamente')
    return redirect(url_for('index'))    

@app.route('/editar/<id>')
def editar(id):
    cursoID=mysql.connection.cursor()
    cursoID.execute('select * from albums1 where id_album=%s',(id))
    constID=cursoID.fetchone()
    return render_template('editaralbum.html',album=constID)

@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method =='POST':
        Vartitulo=request.form['txtTitulo']
        Varartista=request.form['txtArtista']
        Varanio=request.form['txtAnio']
        
        curAct=mysql.connection.cursor()
        curAct.execute('update albums1 set titulo= %s,artista= %s,anio= %s where id_album= %s',(Vartitulo,Varartista,Varanio,id))
        mysql.connection.commit()
    
    flash('Se actualizo el Album '+ Vartitulo)
    return redirect(url_for('index'))

@app.route('/borrar/<id>')
def borrar(id):
    cursorID=mysql.connection.cursor()
    cursorID.execute('select * from albums1 where id_album=%s',(id))
    albumELi=cursorID.fetchone()
    return render_template('eliminaralbum.html',albumEli=albumELi)

@app.route('/eliminar/<id>',methods=['POST'])
def eliminar(id):
    if request.method =='POST':
        curEli=mysql.connection.cursor()
        curEli.execute('delete from albums1 where id_album= %s',(id))
        mysql.connection.commit()
        
    flash('Se Elimino el Album ')
    return redirect(url_for('index'))

#ejecucion del Servidor en el Puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)