import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.popup import Popup

class Main(Screen):
    pass
class Subjects(Screen):
    pass

class Monday(Screen):
    pass

class Tuesday(Screen):
    pass

class Wednesday(Screen):
    pass

class Thursday(Screen):
    pass

class Friday(Screen):
    pass

class Saturday(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv= Builder.load_file('window.kv')

class TIMETABLE(App):
    def close_(self):
        App.get_running_app().stop()
        Window.close()
    def build(self):
        return kv
TIMETABLE().run()
