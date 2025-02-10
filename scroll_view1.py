from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        scroll = ScrollView()

        layout = BoxLayout(orientation="vertical", size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))

        # Adicionando vários botões para testar a rolagem
        for i in range(30):
            btn = Button(text=f"Botão {i + 1}", size_hint_y=None, height=50)
            layout.add_widget(btn)

        scroll.add_widget(layout)
        return scroll

MeuApp().run()
