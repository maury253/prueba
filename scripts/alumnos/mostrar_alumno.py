from PyQt6.QtWidgets import QApplication, QTableWidgetItem,QDialog
import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import Qt
from PyQt6 import uic
import pandas as pd
from scripts.recursos import misc
from scripts.alumnos.editar_alumno import editarAlumno

class mostrarAlumno(QDialog):
   

    ventana_mostrar_alumno = ""
    

    def __init__(self, parent = None):
        super(mostrarAlumno,self).__init__()
        uic.loadUi(misc.rutaMostrarAlumno, self)
        self.parent = parent
       
        self.tablaDatos.itemDoubleClicked.connect(self.obtenerDatos)

        self.mostrarInformacion()

    def mostrarInformacion(self):
        frame = pd.read_csv(misc.ruta)
        self.tablaDatos.setRowCount(len(frame))
        self.tablaDatos.setColumnCount(len(frame.columns))
        
        self.tablaDatos.setHorizontalHeaderLabels(frame.columns.to_list())
        self.tablaDatos.setColumnHidden(0,True) #ocultar columna

        for renglon_indice, renglon in enumerate(frame.itertuples(index=False)):
           
            for columna_indice, valor in enumerate(renglon):
                item = QTableWidgetItem(str(valor))
                self.tablaDatos.setItem(renglon_indice, columna_indice, item)
  

    def obtenerDatos(self, item):
        row = self.tablaDatos.currentRow()
                
        id = self.tablaDatos.item(row, 0).text()

       
        if not self.parent.ventana_editar_alumno:
            gui = editarAlumno(id, self)
            self.ventana_editar_alumno = self.parent.mdiArea.addSubWindow(gui)
            self.ventana_editar_alumno.setWindowFlags(Qt.WindowType.FramelessWindowHint)
            gui.showMaximized()
        else:
            for win in self.parent.mdiArea.subWindowList():
                if win == self.ventana_editar_alumno:
                    self.parent.mdiArea.setActiveSubWindow(win)


        
    
    def closeEvent(self, event):
        self.parent.ventana_mostrar_alumno = ""
        event.accept()

if __name__ == "__main__":
    myApp = QApplication(sys.argv)
    mostrar = mostrarAlumno()
    mostrar.show()
    sys.exit(myApp.exec())
 