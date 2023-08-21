from tkinter import messagebox
import sqlite3

class controlador:
    
    def __init__ (self):
        pass
    
    def conexionBD (self):
        try:
            conexion = sqlite3.connect ("C:/Users/mecat/OneDrive/Documentos/GitHub/FLASK182/bd_act4.db")
            print ("conectado a la BD")
            return conexion
        
        except sqlite3.OperationalError:
            print ("no se pudo conectar")
            
    def Guardar (self, nom, pre, mar, clas):
        #llamar metodo conexion
        conx = self.conexionBD()
        
        #validar vacíos
        if (nom == "" or pre == "" or mar == "" or clas == ""):
            messagebox.showwarning ("Warning", "Formulario incompleto")
            conx.close()
            
        else:
            cursor = conx.cursor()
            datos = (nom, pre, mar, clas)
            sqlInsert = "insert into almacen_bebidas(nombre, precio, marca, tipo) values (?, ?, ?, ?)"
            
            #ejecutar insert
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Registro exitoso", "Registro guardado")
    
    def Eliminar(self, id):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == ""):
            messagebox.showwarning ("Warning", "Ingresa un ID")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "DELETE FROM almacen_bebidas WHERE id = "+ id
                
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect)
                conx.commit()
                conx.close()
                
            except sqlite3.OperationalError:
                print ("Error")
            
    def consultarRegistros(self):
        #1. Realizar conexión a la base de datos
        conx = self.conexionBD()
        
        try: 
                #4. Preparar lo necesario
            cursor = conx.cursor()
            sqlSelect = "select * from almacen_bebidas"
                
                #5. Ejecutar y cerrar conexión
            cursor.execute(sqlSelect)
            RSregistro = cursor.fetchall()
            conx.close()
            return RSregistro
                
        except sqlite3.OperationalError:
            print ("Error de consulta todos los usuarios")
            
    def ActualizarNom(self, id, nom):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or nom == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y nombre")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE almacen_bebidas SET nombre = ? WHERE id = ?"
                actualizar = (nom, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                messagebox.showinfo("Actualización exitosa", "Nombre actualizado")
                
            except sqlite3.OperationalError:
                print ("Error para actualizar nombre")
    
    def ActualizarPre(self, id, precio):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or precio == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y precio")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE almacen_bebidas SET precio = ? WHERE id = ?"
                actualizar = (precio, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                messagebox.showinfo("Actualización exitosa", "Precio actualizado")
                
            except sqlite3.OperationalError:
                print ("Error para actualizar precio")
                
    def ActualizarMarca(self, id, marca):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or marca == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y marca")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE almacen_bebidas SET marca = ? WHERE id = ?"
                actualizar = (marca, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                messagebox.showinfo("Actualización exitosa", "Marca actualizada")
                
            except sqlite3.OperationalError:
                print ("Error para actualizar marca")
                
    def ActualizarTipo(self, id, tipo):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or tipo == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y clasificación")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE almacen_bebidas SET tipo = ? WHERE id = ?"
                actualizar = (tipo, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                messagebox.showinfo("Actualización exitosa", "Clasificación actualizada")
                
            except sqlite3.OperationalError:
                print ("Error para actualizar tipo")
    
    def promedio(self):
        #1. Realizar conexión a la base de datos
        conx = self.conexionBD()
        
        try: 
                #4. Preparar lo necesario
            cursor = conx.cursor()
            sqlSelect = "SELECT AVG(precio) FROM almacen_bebidas" 
                
                #5. Ejecutar y cerrar conexión
            cursor.execute(sqlSelect)
            RSregistro = cursor.fetchall()
            conx.close()
            return RSregistro
        
        except sqlite3.OperationalError:
            print ("Error de consulta promedio")
    