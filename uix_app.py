from kivy.app import App
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        return Label(text="Meu primeiro app Kivy!")

    def on_start(self):
        print("O app iniciou!")

    def on_stop(self):
        print("O app foi fechado!")

    def on_pause(self):
        print("O app foi minimizado!")
        return True  # Retorna True para permitir a pausa

    def on_resume(self):
        print("O app voltou da pausa!")

MeuApp().run()
