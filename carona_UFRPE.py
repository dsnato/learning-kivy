from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

# Simulando um banco de dados
users = {"teste": "1234"}
caronas = []

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.username = TextInput(hint_text='Matrícula')
        self.password = TextInput(hint_text='Senha', password=True)
        self.message = Label(text='')

        login_button = Button(text='Entrar')
        login_button.bind(on_press=self.verify_credentials)

        register_button = Button(text='Criar Conta')
        register_button.bind(on_press=self.create_account)

        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.message)
        layout.add_widget(login_button)
        layout.add_widget(register_button)
        self.add_widget(layout)

    def verify_credentials(self, instance):
        if self.username.text in users and users[self.username.text] == self.password.text:
            self.manager.current = 'choose_carona'
        else:
            self.message.text = 'Usuário ou senha inválidos!'

    def create_account(self, instance):
        self.manager.current = 'register'

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.username = TextInput(hint_text='Matrícula')
        self.password = TextInput(hint_text='Senha', password=True)
        self.message = Label(text='')

        register_button = Button(text='Registrar')
        register_button.bind(on_press=self.register_user)

        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.message)
        layout.add_widget(register_button)
        self.add_widget(layout)

    def register_user(self, instance):
        if self.username.text and self.password.text:
            users[self.username.text] = self.password.text
            self.message.text = 'Cadastro realizado com sucesso!'
            self.manager.current = 'login'
        else:
            self.message.text = 'Preencha todos os campos!'

class ChooseCaronaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.carona_list = ScrollView()
        self.update_carona_list()

        create_button = Button(text='Criar Carona')
        create_button.bind(on_press=self.create_carona)

        layout.add_widget(self.carona_list)
        layout.add_widget(create_button)
        self.add_widget(layout)

    def update_carona_list(self):
        carona_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        carona_layout.bind(minimum_height=carona_layout.setter('height'))

        for carona in caronas:
            btn = Button(text=f"{carona['origem']} -> {carona['destino']} ({carona['data']} {carona['horario']})\nR$ {carona['valor']} por pessoa", size_hint_y=None, height=40)
            btn.bind(on_press=lambda instance, c=carona: self.open_whatsapp(c))
            carona_layout.add_widget(btn)

        self.carona_list.clear_widgets()
        self.carona_list.add_widget(carona_layout)

    def open_whatsapp(self, carona):
        print(f"Abrindo WhatsApp para {carona['contato']}")

    def create_carona(self, instance):
        self.manager.current = 'create_carona'

class CreateCaronaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.origem = TextInput(hint_text='Origem')
        self.destino = TextInput(hint_text='Destino')
        self.data = TextInput(hint_text='Data (DD/MM/AAAA)')
        self.horario = TextInput(hint_text='Horário (HH:MM)')
        self.valor = TextInput(hint_text='Valor por pessoa')
        self.observacao = TextInput(hint_text='Observações')

        submit_button = Button(text='Criar Carona')
        submit_button.bind(on_press=self.add_carona)

        layout.add_widget(self.origem)
        layout.add_widget(self.destino)
        layout.add_widget(self.data)
        layout.add_widget(self.horario)
        layout.add_widget(self.valor)
        layout.add_widget(self.observacao)
        layout.add_widget(submit_button)
        self.add_widget(layout)

    def add_carona(self, instance):
        caronas.append({
            'origem': self.origem.text,
            'destino': self.destino.text,
            'data': self.data.text,
            'horario': self.horario.text,
            'valor': self.valor.text,
            'observacao': self.observacao.text,
            'contato': 'whatsapp_link'
        })
        self.manager.get_screen('choose_carona').update_carona_list()
        self.manager.current = 'choose_carona'

class CaronaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(ChooseCaronaScreen(name='choose_carona'))
        sm.add_widget(CreateCaronaScreen(name='create_carona'))
        return sm

if __name__ == '__main__':
    CaronaApp().run()
