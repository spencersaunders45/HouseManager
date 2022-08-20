import sys
from PyQt5.QtWidgets import *

class Widgets():
   
   def projects(w):
      label2 = QLabel(w)
      label2.setText("project")
      label2.move(200, 200)
      label2.show()
      return label2

   def average_time():
      average_time = QLabel()
      average_time.setText("3 months")
      return average_time

   def project_time():
      project_time = QLabel("18 days")

   def project_tasks():
      task = QLabel("task")

   def current_spent():
      spent = QLabel("$3.00")

   def budget_goal():
      budget_goal = QLabel("$100.00")

   def notes():
      note = QLabel("this is a note")