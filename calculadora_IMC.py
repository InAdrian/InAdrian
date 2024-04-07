from PySide6.QtWidgets import (QApplication,
                               QWidget,
                               QLabel,
                               QPushButton,
                               QLineEdit)
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtCore import Qt
import sys
import os
basedir = os.path.dirname(__file__)
print(f"ruta base:{basedir}")
print(f"Directorio actual: {os.getcwd}")


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_main()

    def setup_main(self):
        self.setWindowTitle("CALCULADORA IMC")
        self.resize(280,180)
    
        x=10
        y=-10

        self.imclb=QLabel('IMC=>',self)
        self.imclb.move(x,y+30)
        self.imcln = QLineEdit(self)  
        self.imcln.setGeometry(x+50,y+28,148,25)
        self.imcln.setPlaceholderText("Nº calculado")
        self.imcln.setReadOnly(True)  

        self.generolb=QLabel("Género:",self)
        self.generolb.move(x,y+60)
        self.generoln = QLineEdit(self)
        self.generoln.setGeometry(x+50,y+58,148,25)
        self.generoln.setPlaceholderText("M/F")

        self.alturalb=QLabel("Altura:",self)
        self.alturalb.move(x,y+90)
        self.alturaln = QLineEdit(self)
        self.alturaln.setGeometry(x+50,y+88,148,25)
        self.alturaln.setPlaceholderText("metros")

        self.pesolb=QLabel("Peso:",self)
        self.pesolb.move(x,y+120)
        self.pesoln = QLineEdit(self)
        self.pesoln.setGeometry(x+50,y+118,148,25)
        self.pesoln.setPlaceholderText("kilogramos")

        button_calcular = QPushButton("Calcular", self)      
        button_calcular.setGeometry(x,y+150,200,25)
        button_calcular.clicked.connect(self.realizar_calculo)




    def realizar_calculo(self):
        peso = self.pesoln.text()
        altura = self.alturaln.text()
        genero = self.generoln.text().lower()

        try:
            altura = float(altura)
            peso = float(peso)
        except ValueError:
            self.imcln.setText("Ingresar valores numéricos válidos.")
            return
        if altura <= 0 or peso <= 0:
            self.imcln.setText("Altura y peso deben ser mayores a 0.")
            return
        imc = peso / (altura ** 2)
        categoria = self.categorizar_imc(imc, genero)  
        self.imcln.setText(f"{imc:.2f} - {categoria}")



        
    def categorizar_imc(self,imc,genero):
        genero = genero.lower()
        if genero == 'm':
            if imc<20:
                return ('desnutricion')
            elif imc>20 and imc<24.9:
                return ('normalidad')
            elif imc>25 and imc<29.9:
                return ('sobrepeso')
            elif imc>30 and imc<40:
                return ('obesidad')
            else:
                return ('obesidad grave')
        
        elif genero == 'f':
            if imc<19:
                return ('desnutricion')
            elif imc>19 and imc<23.9:
                return ('normalidad')
            elif imc>24 and imc<27.9:
                return ('sobrepeso')
            elif imc>28 and imc<32:
                return ('obesidad')
            else:
                return ('obesidad grave')
        else:
            return ('N/D')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

      

