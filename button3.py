from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        btn1 = Button(text="1", size_hint=(1, 0.2))  # 20% da altura
        btn2 = Button(text="2", size_hint=(1, 0.3))  # 30% da altura
        btn3 = Button(text="3", size_hint=(1, 0.5))  # 50% da altura

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout

MeuApp().run()
