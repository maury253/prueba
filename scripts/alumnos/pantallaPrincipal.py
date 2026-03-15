import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

from scripts.alumnos.crear_alumno import nuevoAlumno
from scripts.alumnos.mostrar_alumno import mostrarAlumno
from scripts.alumnos.borrar_alumno import mostrarAlumnoEliminar

class pantalla_principal(QMainWindow):
    def __init__(self, parent = None):
        super(pantalla_principal,self).__init__()
        uic.loadUi("UI/alumno/pantallaPrincipal.ui", self)

       

        self.botonRegistro.clicked.connect(self.llamarCrearAlumno)
        self.botonMostrar.clicked.connect(self.llamarMostrarAlumno)
        self.botonEliminar.clicked.connect(self.llamarBorrarAlumno)


    def llamarCrearAlumno(self):
        self.ventanaCrear = nuevoAlumno()
        self.ventanaCrear.exec()
    
    def llamarMostrarAlumno(self):
        self.ventanaMostrar = mostrarAlumno()
        self.ventanaMostrar.exec()

    def llamarBorrarAlumno(self):
        self.ventanaEliminar = mostrarAlumnoEliminar()
        self.ventanaEliminar.exec()
       
            

myWindow = QApplication(sys.argv)
myclase = pantalla_principal()

myclase.show()
sys.exit(myWindow.exec())