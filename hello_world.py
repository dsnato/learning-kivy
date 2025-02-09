import kivy
kivy.require('2.3.1')

from kivy.app import App
from kivy.uix.label import Label


class hello_world(App):

    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
    hello_world().run()
