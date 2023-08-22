from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="DB_Papeleria"
app.secret_key='mysecretkey'
mysql= MySQL(app)


@app.route('/')
def index():
    return render_template('utiles.html')

@app.route('/utiles')
def utiless():
    return render_template('utiles.html')

@app.route('/empleados')
def empleados():
    return render_template('empleados.html')

@app.route('/Cempleados')
def Cempleados():
    return render_template('consultarEmpleados.html')

@app.route('/Cutiles')
def Cutiles():
    return render_template('consultarUtiles.html')

@app.route('/CApellido')
def CApellido():
    return render_template('consultarApellido.html')


@app.route('/guardarUtiles', methods=['POST'])
def guardarUtiles():
    if request.method == 'POST':
        VarNombre = request.form['txtNU']
        VarClasi = request.form['txtCU']
        VarCant = request.form['txtCantidad']
        VarPrecio = request.form['txtPrecio']
        
        CS= mysql.connection.cursor()
        CS.execute('insert into TB_Utiles (nombre, clasificacion, cantidad, precio_compra) values (%s, %s, %s, %s)', (VarNombre, VarClasi, VarCant, VarPrecio))
        mysql.connection.commit()
        
        flash('Se agregó el útil correctamente')
        
    return redirect(url_for('index'))

@app.route('/guardarEmpleados', methods=['POST'])
def guardarEmpleados():
    if request.method == 'POST':
        VarNombre = request.form['txtNE']
        VarAP = request.form['txtAP']
        VarAM = request.form['txtAM']
        VarPuesto = request.form['txtPuesto']
        VarContraseña = request.form['txtCont']
        
        CS= mysql.connection.cursor()
        CS.execute('insert into TB_Empleados (nombre, apellidoP, apellidoM, puesto, contraseña) values (%s, %s, %s, %s, %s)', (VarNombre, VarAP, VarAM, VarPuesto, VarContraseña))
        mysql.connection.commit()
        
        flash('Se agregó el empleado correctamente')
        
    return redirect(url_for('empleados'))


@app.route('/consultarUtiles')
def consultarUtiles():
    CS = mysql.connection.cursor()
    CS.execute('SELECT * FROM TB_Utiles')
    data = CS.fetchall()
    CS.close()
    return render_template('consultarUtiles.html', utiles=data)

@app.route('/consultarEmpleados')
def consultarEmpleados():
    CS = mysql.connection.cursor()
    CS.execute('SELECT * FROM TB_Empleados')
    data = CS.fetchall()
    CS.close()
    return render_template('consultarEmpleados.html', empleados=data)

@app.route('/eliminar/<id>')
def eliminar(id):
    curEliminar = mysql.connection.cursor()
    curEliminar.execute('DELETE FROM TB_Empleados WHERE id_empleados=%s', (id,))
    mysql.connection.commit()
    
    flash('Empleado eliminado correctamente')
    return redirect(url_for('consultarEmpleados'))

@app.route('/consultarApellido', methods=['GET', 'POST'])
def consultarApellido():
    if request.method == 'POST':
        busqueda = request.form['busqueda']
        CS = mysql.connection.cursor()
        CS.execute('SELECT * FROM TB_Empleados WHERE id_empleados = %s OR apellidoP = %s', (busqueda, busqueda))
        data = CS.fetchall()
        CS.close()
        return render_template('consultarApellido.html', empleados=data)
    return render_template('consultarApellido.html')

@app.route('/editar/<id>')
def editar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('SELECT * FROM TB_Utiles WHERE id_utiles=%s', (id,))
    consulId = curEditar.fetchone()
    curEditar.close()
    
    return render_template('editar.html', util=consulId)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        VN = request.form['txtNU']
        VC = request.form['txtCU']
        VCA = request.form['txtCantidad']
        VP = request.form['txtPrecio']
        
        curAct = mysql.connection.cursor()
        curAct.execute('UPDATE TB_Utiles SET nombre=%s, clasificacion=%s, cantidad=%s, precio_compra=%s WHERE id_utiles=%s', (VN, VC, VCA, VP, id))
        mysql.connection.commit()
        
        flash('Util actualizado correctamente')
        return redirect(url_for('consultarUtiles'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)