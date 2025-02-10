from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")  # Criando o layout

        btn1 = Button(text="Botão 1")
        btn2 = Button(text="Botão 2")

        layout.add_widget(btn1)  # Adiciona o primeiro botão
        layout.add_widget(btn2)  # Adiciona o segundo botão

        return layout

MeuApp().run()
