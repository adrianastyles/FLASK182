from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app= Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='DB_Floreria'
app.secret_key='mysecretkey'

mysql = MySQL(app)

@app.route('/')

def index():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from tbFlores')
    consulta = curSelect.fetchall()
    
    return render_template('index.html', listFlores=consulta)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        nombre = request.form['txtNombre']
        cantidad = request.form['txtCantidad']
        precio = request.form['txtPrecio']
        
        CS = mysql.connection.cursor()
        CS.execute('insert into tbFlores(nombre,cantidad,precio) values(%s,%s,%s)',(nombre, cantidad, precio))
        mysql.connection.commit()
    
    flash('Flor agregada correctamente')
    return redirect(url_for('index'))

@app.route('/editar/<id>')
def editar(id):
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from tbFlores where id = %s ', (id,))
    consulID = curEditar.fetchone()
    
    return render_template('editar.html', flor=consulID)


@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        
        nombre = request.form['txtNombre']
        cantidad = request.form['txtCantidad']
        precio = request.form['txtPrecio']
        
        curAct = mysql.connection.cursor()
        curAct.execute('update tbFlores set nombre=%s,cantidad=%s,precio=%s where id=%s',(nombre, cantidad, precio, id))
        mysql.connection.commit()
        
        flash('Flor actualizada correctamente')
        return redirect(url_for('index'))
    
    
@app.route('/busq/<nom>' ,methods=['POST'] )
def busqR(nom):
    
    if request.method == 'POST':
        
        nom = request.form['txtNombre']
        
        curAct = mysql.connection.cursor()
        curAct.execute('select * from requisicion where nombre=%s', (nom,))
        mysql.connection.commit()
        
        return redirect(url_for('index'))

if __name__ =='__main__':
    app.run(port= 5000, debug=True)