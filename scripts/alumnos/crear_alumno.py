
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox,QDialog
from PyQt6.QtCore import Qt
import os
from PyQt6 import uic
import pandas as pd
from scripts.recursos import misc
class nuevoAlumno(QDialog):
    def __init__(self, parent = None):
        super(nuevoAlumno,self).__init__()
        uic.loadUi(misc.rutaCrearAlumno, self)

        self.parent = parent

        self.Nombre.setPlaceholderText("campo requerido")
        self.ApellidoPaterno.setPlaceholderText("campo requerido")
        self.ApellidoMaterno.setPlaceholderText("opcional")
        self.Edad.setPlaceholderText("campo requerido")
        self.Genero.setPlaceholderText("campo requerido")
        self.Carrera.setPlaceholderText("campo requerido")
        self.Semestre.setPlaceholderText("campo requerido")

        self.Boton_Registro.clicked.connect(self.guardar)

    def guardar(self):
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
        archivo_existe = os.path.isfile(misc.ruta)
        with open(misc.ruta, mode= "a", encoding="UTF-8") as archivo:
            if not archivo_existe:
                archivo.write("Id,Nombre,Apellido paterno,Apellido materno,Edad,Genero,Carrera,Semestre\n")
                id =1
            if archivo_existe :
                df = pd.read_csv(misc.ruta)
                id = len(df)
                id += 1

            if apellidoMaternoSi:
                archivo.write(f"{id},{nombre},{apellidoPaterno},{apellidoMaterno},{edad},{genero},{carrera},{semestre}\n")
            else:
                archivo.write(f"{id},{nombre},{apellidoPaterno}, ,{edad},{genero},{carrera},{semestre}\n")


            QMessageBox.information(self, "App", "datos almacenados correctamente")

            self.Nombre.clear()
            self.ApellidoPaterno.clear()
            self.ApellidoMaterno.clear()
            self.Edad.clear()
            self.Genero.clear()
            self.Carrera.clear()
            self.Semestre.clear()

    def closeEvent(self, event):
        self.parent.ventana_registrar_alumno = ""
        event.accept()
            



if __name__ == "__main__":
    myWindow = QApplication(sys.argv)
    myclase = nuevoAlumno()

    myclase.show()
    sys.exit(myWindow.exec())