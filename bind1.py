from kivy.app import App
from kivy.uix.textinput import TextInput

class MeuApp(App):
    def build(self):
        entrada = TextInput()
        entrada.bind(text=self.texto_alterado)  # Associa a mudança de texto à função
        return entrada

    def texto_alterado(self, instancia, valor):
        print(f"Novo texto: {valor}")  # Exibe o novo valor no terminal

MeuApp().run()
