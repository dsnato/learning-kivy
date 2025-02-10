from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

class Tela1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text="Ir para Tela 2", on_press=self.ir_para_tela2))

    def ir_para_tela2(self, instance):
        self.manager.current = "tela2"

class Tela2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text="Voltar para Tela 1", on_press=self.ir_para_tela1))

    def ir_para_tela1(self, instance):
        self.manager.current = "tela1"

class MeuApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Tela1(name="tela1"))
        sm.add_widget(Tela2(name="tela2"))
        return sm

MeuApp().run()
