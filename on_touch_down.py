from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window

class MyWidget(Widget):

    def on_touch_down(self, touch):
        # Verifica se o toque ocorreu dentro do widget
        if self.collide_point(*touch.pos):
            print(f"Toque detectado na posição: ({touch.x}, {touch.y})")
            # Adiciona um Label na posição do toque
            label = Label(text=f"({touch.x}, {touch.y})", pos=(touch.x, touch.y))
            self.add_widget(label)
            return True  # Consome o evento
        return super(MyWidget, self).on_touch_down(touch)  # Propaga o evento

class MyApp(App):

    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()