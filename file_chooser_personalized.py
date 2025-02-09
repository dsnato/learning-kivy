from kivy.app import App
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.filechooser = FileChooserListView()
        self.filechooser.bind(on_selection=self.selecionado)

        self.label = Label(text="Nenhum arquivo selecionado")

        btn = Button(text="Abrir Arquivo", size_hint=(1, 0.2))
        btn.bind(on_press=self.abrir_arquivo)

        layout.add_widget(self.filechooser)
        layout.add_widget(btn)
        layout.add_widget(self.label)

        return layout

    def selecionado(self, filechooser, selection):
        if selection:
            self.label.text = f"Selecionado: {selection[0]}"

    def abrir_arquivo(self, instance):
        if self.filechooser.selection:
            arquivo = self.filechooser.selection[0]
            print(f"Abrindo: {arquivo}")

MeuApp().run()
