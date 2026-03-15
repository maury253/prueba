import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6 import uic
from PyQt6.QtCore import Qt
from scripts.alumnos.crear_alumno import nuevoAlumno
from scripts.alumnos.mostrar_alumno import mostrarAlumno
from scripts.alumnos.editar_alumno import editarAlumno

from scripts.recursos import misc
class pantalla_principal(QMainWindow):


    ventana_registrar_alumno = ""
    ventana_mostrar_alumno = ""
    ventana_editar_alumno = ""

    def __init__(self, parent = None):
        super(pantalla_principal,self).__init__()
        uic.loadUi(misc.rutaMenu, self)

        self.mdiArea.viewport().setStyleSheet("background-image: url(menu.jpeg);" 
        "background-position: center;" 
        "background-repeat: no-repeat;")

        self.botonCrearAlumno.triggered.connect(self.registrar_alumno)
        self.botonMostrarAlumno.triggered.connect(self.mostrar_alumno)

    def registrar_alumno(self):
        guiRegistrarAlumno = nuevoAlumno(self)

        if not self.ventana_registrar_alumno:
            self.ventana_registrar_alumno = self.mdiArea.addSubWindow(guiRegistrarAlumno)
            guiRegistrarAlumno.showMaximized()
        else:
            for win in self.mdiArea.subWindowList():
                if win == self.ventana_registrar_alumno:
                    self.mdiArea.setActiveSubWindow(win)

    def mostrar_alumno(self):
        gui = mostrarAlumno(self)

        if not self.ventana_mostrar_alumno:
            self.ventana_mostrar_alumno = self.mdiArea.addSubWindow(gui)
            self.ventana_mostrar_alumno.setWindowFlags(Qt.WindowType.FramelessWindowHint)
            gui.showMaximized()
        else:
            for win in self.mdiArea.subWindowList():
                if win == self.ventana_mostrar_alumno:
                    self.mdiArea.setActiveSubWindow(win)
   
      

        

        

    


myWindow = QApplication(sys.argv)
myclase = pantalla_principal()
myclase.show()
sys.exit(myWindow.exec())

