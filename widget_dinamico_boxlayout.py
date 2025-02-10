from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")

        self.btn_add = Button(text="Adicionar Label")
        self.btn_add.bind(on_press=self.adicionar_label)

        self.layout.add_widget(self.btn_add)  # Adiciona o botão à interface

        return self.layout

    def adicionar_label(self, instance):
        label = Label(text="Novo Label Adicionado!")
        self.layout.add_widget(label)  # Adiciona um novo Label ao layout

MeuApp().run()
