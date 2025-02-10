from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")

        self.btn = Button(text="Remover-me")
        self.btn.bind(on_press=self.remover_botao)

        self.layout.add_widget(self.btn)  # Adiciona o botão

        return self.layout

    def remover_botao(self, instance):
        self.layout.remove_widget(self.btn)  # Remove o botão da interface

MeuApp().run()
