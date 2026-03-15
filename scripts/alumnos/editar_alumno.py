from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
import sys
from PyQt6 import uic
import pandas as pd
from scripts.recursos import misc

class editarAlumno(QDialog):
    def __init__(self, id , parent = None):
        super(editarAlumno,self).__init__()
        uic.loadUi(misc.rutaEditarAlumno,self)

        self.id = id
        self.Boton_Registro.clicked.connect(self.guardarCambios)
        df = pd.read_csv(misc.ruta)
        busqueda_id = df[df["Id"]== int(id)].iloc[0].to_dict()

        nombre = busqueda_id["Nombre"]
        apellidoPaterno = busqueda_id["Apellido paterno"]
        apellidoMaterno = busqueda_id["Apellido materno"]
        edad = busqueda_id["Edad"]
        genero = busqueda_id["Genero"]
        carrera = busqueda_id["Carrera"]
        semestre = busqueda_id["Semestre"]

        self.Nombre.setText(nombre)
        self.ApellidoPaterno.setText(apellidoPaterno)
        self.ApellidoMaterno.setText(apellidoMaterno)
        self.Edad.setText(str(edad))
        self.Genero.setText(genero)
        self.Carrera.setText(carrera)
        self.Semestre.setText(str(semestre))

        
    
    def guardarCambios(self):
        nombre = self.Nombre.text()
        apellidoPaterno = self.ApellidoPaterno.text()
        apellidoMaterno = self.ApellidoMaterno.text()
        edad = self.Edad.text()
        genero = self.Genero.text()
        carrera = self.Carrera.text()
        semestre = self.Semestre.text()

        apellidoMaternoSi = True
        if not apellidoMaterno:
            apellidoMaternoSi = False
        
        if not nombre or not apellidoPaterno or not edad or not carrera or not genero or not semestre:
            QMessageBox.warning(self, "App", "Por favor ingrese todos los datos")
            return
        if not apellidoMaternoSi:
            apellidoMaterno = " "
        df = pd.read_csv(misc.ruta)
        df.loc[df["Id"]== int(self.id), "Nombre"] = nombre
        df.loc[df["Id"]== int(self.id), "Apellido paterno"] = apellidoPaterno
        df.loc[df["Id"]== int(self.id), "Apellido materno"] = apellidoMaterno
        df.loc[df["Id"]== int(self.id), "Edad"] = edad
        df.loc[df["Id"]== int(self.id), "Genero"] = genero
        df.loc[df["Id"]== int(self.id), "Carrera"] = carrera
        df.loc[df["Id"]== int(self.id), "Semestre"] = semestre


        df.to_csv("datos.csv", index=False)

        
    
    def closeEvent(self, event):
        self.parent.ventana_editar_alumno = ""
        event.accept()






if __name__ == "__main__":

    myApp = QApplication(sys.argv)
    frmEditarAlumno = editarAlumno()
    frmEditarAlumno.show()
    sys.exit(myApp.exec())