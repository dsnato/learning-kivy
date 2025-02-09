from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal', spacing=10, padding=20)
        btn1 = Button(text='Botão 1', size_hint=(1, 0.2))
        btn2 = Button(text='Botão 2', size_hint=(1,0.8))
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        return layout

MeuApp().run()
