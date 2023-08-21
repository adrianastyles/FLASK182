from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="DB_Fruteria"
app.secret_key='mysecretkey'
mysql= MySQL(app)


@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        VFruta = request.form['txtFruta']
        VTemporada = request.form['txtTemporada']
        VPrecio = request.form['txtPrecio']
        VStock = request.form['txtStock']
        
        CS= mysql.connection.cursor()
        CS.execute('insert into tbFrutas (fruta, temporada, precio, stock) values (%s, %s, %s, %s)', (VFruta, VTemporada, VPrecio, VStock))
        mysql.connection.commit()
        
        flash('Fruta agregada de manera correcta')
        
    return redirect(url_for('index'))

@app.route('/vista')
def vista():
    CS = mysql.connection.cursor()
    CS.execute('SELECT * FROM tbFrutas')
    data = CS.fetchall()
    CS.close()
    return render_template('vista.html', frutas=data)


@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    if request.method == 'POST':
        busqueda = request.form['busqueda']
        CS = mysql.connection.cursor()
        CS.execute('SELECT * FROM tbFrutas WHERE id = %s OR fruta = %s', (busqueda, busqueda))
        data = CS.fetchall()
        CS.close()
        return render_template('consulta.html', frutas=data)
    return render_template('consulta.html')


@app.route('/editar/<id>')
def editar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('SELECT * FROM tbFrutas WHERE id=%s', (id,))
    consulId = curEditar.fetchone()
    curEditar.close()
    
    return render_template('editar.html', fruta=consulId)



@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        VFruta = request.form['txtFruta']
        VTemporada = request.form['txtTemporada']
        VPrecio = request.form['txtPrecio']
        VStock = request.form['txtStock']
        
        curAct = mysql.connection.cursor()
        curAct.execute('UPDATE tbFrutas SET fruta=%s, temporada=%s, precio=%s, stock=%s WHERE id=%s', (VFruta, VTemporada, VPrecio, VStock, id))
        mysql.connection.commit()
        
        flash('Album actualizado correctamente')
        return redirect(url_for('index'))


@app.route('/eliminar/<id>')
def eliminar(id):
    curEliminar = mysql.connection.cursor()
    curEliminar.execute('DELETE FROM tbFrutas WHERE id=%s', (id,))
    mysql.connection.commit()
    
    flash('Fruta eliminada correctamente')
    return redirect(url_for('vista'))


if __name__ == '__main__':
    app.run(debug=True, port=8000)