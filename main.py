from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtUiTools import *
import math

class Calc(QMainWindow):
    def __init__(self):
        super().__init__()


        loader = QUiLoader()
        self.ui = loader.load("design.ui")
        self.ui.show()
        self.ui.btn_add.clicked.connect(self.add)
        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_pow.clicked.connect(self.pow)
        self.ui.btn_root.clicked.connect(self.root)
        self.ui.btn_mod.clicked.connect(self.mod)
        self.ui.btn_sin.clicked.connect(self.sin)
        self.ui.btn_cos.clicked.connect(self.cos)
    
    def sub(self):
        self.op = "sub"
        self.num1 = int(self.ui.tb.text())
        self.ui.tb.setText("")
  
    def add(self) :
        self.op = "add"
        self.num1 = int(self.ui.tb.text())
        self.ui.tb.setText("")

    def mul(self) :
        self.op = "mul"
        self.num1 = int(self.ui.tb.text())
        self.ui.tb.setText("")
    
    def div(self) :
        self.op = "div"
        self.num1 = int(self.ui.tb.text())
        self.ui.tb.setText("")
        
    def pow(self) :
        self.op = "pow"
        self.num1 = int(self.ui.tb.text())
        self.ui.tb.setText("")

    def mod(self) :
        self.op = "mod"
        self.num1 = int(self.ui.tb.text())
        self.ui.tb.setText("")

    def sin(self) :
        self.op = "sin"
        self.num1 = int(self.ui.tb.text())
        self.ui.tb.setText("")

    def cos(self) :
        self.op = "cos"
        self.num1 = int(self.ui.tb.text())
        self.ui.tb.setText("")

    def root(self) :
        self.op = "root"
        self.num1 = int(self.ui.tb.text())
        self.ui.tb.setText("")


    def equal(self):
        if self.op == "sin" :
            self.result = math.sinh(self.num1)   
        elif self.op == "cos" :
            self.result = math.cosh(self.num1)
        elif self.op == "root" :
            self.result = self.num1 ** 0.5
        else : 
            self.num2 = int(self.ui.tb.text())
            if self.op == "add" :
                self.result = self.num1 + self.num2
            elif self.op == "sub" :
                self.result = self.num1 - self.num2
            elif self.op == "mul" :
                self.result = self.num1 * self.num2
            elif self.op == "div" :
                self.result = self.num1 / self.num2
            elif self.op == "pow" :
                self.result = self.num1 ** self.num2
            elif self.op == "mod" :
                self.result = self.num1 % self.num2
        self.ui.tb.setText(str(self.result))


my_app = QApplication()
main_window = Calc()
my_app.exec()





