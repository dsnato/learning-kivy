from kivy.app import App
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        return Button(
            text="Clique aqui",
            size_hint=(0.3, 0.2),  # 30% da largura, 20% da altura
            pos_hint={"center_x": 0.5, "center_y": 0.5}  # Centralizado na tela
        )

MeuApp().run()