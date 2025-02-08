from kivy.app import App
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        btn = Button(text="Clique aqui")
        btn.bind(on_press=self.botao_clicado)  # Associa o evento de clique à função
        return btn

    def botao_clicado(self, instancia):
        print("Botão foi clicado!")

MeuApp().run()
