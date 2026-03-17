from PyQt6.QtWidgets import QApplication, QTableWidgetItem,QDialog, QMessageBox
import sys
from PyQt6 import uic
import pandas as pd
from scripts.recursos import misc

from scripts.alumnos.editar_alumno import editarAlumno

class mostrarAlumnoEliminar(QDialog):
    def __init__(self, parent = None):
        super(mostrarAlumnoEliminar,self).__init__()
        uic.loadUi(misc.rutaMostrarAlumno, self)

        #es la linea que nos permite
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


        ventanaBorrar = eliminarAlumno( id, self)
        if ventanaBorrar.exec():
            self.mostrarInformacion()

if __name__ == "__main__":
    myApp = QApplication(sys.argv)
    mostrar = mostrarAlumnoEliminar()
    mostrar.show()
    sys.exit(myApp.exec())


class eliminarAlumno(QDialog):
    def __init__(self, id, parent=None):
        super().__init__()
        uic.loadUi(misc.rutaConfirmarEliminacionAlumno, self)

        self.id = id
        self.botonConfirmar.clicked.connect(self.eliminar)
        self.botonCancelar.clicked.connect(self.cancelar)
        self.mostrarAlumno()

    def mostrarAlumno(self):
        df = pd.read_csv(misc.ruta)

        alumno = df[df["Id"] == int(self.id)]
        alumno_dict = alumno.iloc[0].to_dict()
        # Configurar tabla
        self.tablaEliminar.setColumnCount(len(alumno_dict))
        self.tablaEliminar.setRowCount(1)
        self.tablaEliminar.setHorizontalHeaderLabels(alumno_dict.keys())
        self.tablaEliminar.setColumnHidden(0, True)  # ocultar Id 

        for columna_indice, valor in enumerate(alumno_dict.values()):
            item = QTableWidgetItem(str(valor))
            self.tablaEliminar.setItem(0, columna_indice, item)

    def eliminar(self):
        df = pd.read_csv(misc.ruta)

        df = df[df["Id"] != int(self.id)]
        df.to_csv(misc.ruta, index=False)
        QMessageBox.information(self, "App", "Alumno eliminado correctamente")
        self.accept()

    def cancelar(self):
        self.accept()

         



 