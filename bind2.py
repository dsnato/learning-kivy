from kivy.app import App
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        btn = Button(text="Clique aqui")
        btn.bind(size=self.tamanho_mudou)  # Monitora mudanças de tamanho do botão
        return btn

    def tamanho_mudou(self, instancia, valor):
        print(f"Novo tamanho: {valor}")  # Mostra o novo tamanho do botão

MeuApp().run()
