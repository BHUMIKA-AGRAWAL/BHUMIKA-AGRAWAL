# importing libraries
from PyQt5.QtWidgets import
*from PyQt5.QtGui import 
*from PyQt5.QtCore import 
*import random
import sys 
import pyttsx3
speaker=pyttsx3.init() 
class Window(QMainWindow): 	
  def _init(self):		
    super().init_() 		
    # setting window title		
    self.setWindowTitle("Python ")	
    self.setGeometry(100, 100, 320, 350) 		
    # calling method		self.UiComponents() 	
    # showing all the widgets		self.show() 	
    # defining random words		self.words = ['accessible','attentive','azure','beneficial','chum','compassionate','fascinated','generous','jittery','jovial',		 'keen','onomatopoeia','optimistic','pragmatic','quiescent','receptive','tactful','whizbang','zeitgeist'] 		
    # default current word		self.current_text = "" 
    # method for components of GUI	def UiComponents(self): 
    # creating head label		
    head = QLabel("Scramble Words", self)		
    head.setGeometry(20, 10, 280, 60) 
    font = QFont('Times', 15)	
    font.setBold(True)		
    font.setItalic(True)	
    font.setUnderline(True)	
    head.setFont(font) 	
    head.setAlignment(Qt.AlignCenter) 	
    color = QGraphicsColorizeEffect(self)	
    color.setColor(Qt.red)	
    head.setGraphicsEffect(color)			
    # creating label to show the scramble word	
    
    self.j_word = QLabel(self)	
    self.j_word.setGeometry(30, 80, 260, 50)	
    self.j_word.setStyleSheet("border : 2px solid black; background : white;")		
    self.j_word.setFont(QFont('Times', 12))	
    self.j_word.setAlignment(Qt.AlignCenter) 
    # creating a line edit widget for input text	
    self.input = QLineEdit(self)
    self.input.setGeometry(20, 150, 200, 40)
    self.input.setAlignment(Qt.AlignCenter) 	
    # creating push button to check the input	
    self.check = QPushButton("Check", self)		
    self.check.setGeometry(230, 155, 80, 30)	
    # adding action to the check button	
    self.check.clicked.connect(self.check_action) 
    # result label		self.result = QLabel(self)		
    self.result.setGeometry(40, 210, 240, 50)	
    self.result.setFont(QFont('Times', 13))	
    self.result.setAlignment(Qt.AlignCenter)	
    self.result.setStyleSheet("border : 2px solid black; background : blue;")
    
    
  #creating pygt5 gui app 
  App = QApplicatiin(sys.argv)
  #creating the instance of our window
  window = window()
  
  #starting the app
  sys.exit(App.exec())
