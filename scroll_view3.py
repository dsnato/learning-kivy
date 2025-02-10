from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        scroll = ScrollView()

        texto = "Kivy é um framework para criar aplicações multi-plataforma." * 20  # Texto longo
        label = Label(text=texto, size_hint_y=None, text_size=(400, None))
        label.bind(texture_size=label.setter("size"))  # Ajusta a altura dinamicamente

        scroll.add_widget(label)
        return scroll

MeuApp().run()
