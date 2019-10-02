from kivy.app import App
from kivy.uix.button import Label

class testApp(App):
    def build(self):
        return Label(text='Hello World')

testApp().run()
