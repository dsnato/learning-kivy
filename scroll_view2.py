from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        scroll = ScrollView(do_scroll_x=True, do_scroll_y=False)

        layout = BoxLayout(orientation="horizontal", size_hint_x=None)
        layout.bind(minimum_width=layout.setter("width"))

        for i in range(20):
            btn = Button(text=f"Item {i + 1}", size_hint_x=None, width=150)
            layout.add_widget(btn)

        scroll.add_widget(layout)
        return scroll

MeuApp().run()
