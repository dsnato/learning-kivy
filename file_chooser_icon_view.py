from kivy.app import App
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        filechooser = FileChooserIconView()  # Modo ícones
        filechooser.bind(on_selection=self.selecionado)

        self.label = Label(text="Selecione um arquivo")

        layout.add_widget(filechooser)
        layout.add_widget(self.label)

        return layout

    def selecionado(self, filechooser, selection):
        if selection:
            self.label.text = f"Arquivo selecionado: {selection[0]}"

MeuApp().run()
