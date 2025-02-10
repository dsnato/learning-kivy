from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.button import Button

class MeuApp(App):
    def abrir_popup(self, instance):
        pop = Popup(title="Meu Popup", content=Button(text="Fechar", on_press=lambda x: pop.dismiss()), size_hint=(0.5, 0.5))
        pop.open()

    def build(self):
        return Button(text="Abrir Popup", on_press=self.abrir_popup)

MeuApp().run()
