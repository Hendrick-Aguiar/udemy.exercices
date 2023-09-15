
import kivy
from kyvy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childapp(GridLayout):
    def__init__(self,**kwargs):
        super(childapp, self).__init__()
        self.cols = 2
        self.add.widget(Label(text = 'Student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)
        

self.add.widget(Label(text = 'Student Marks'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)
