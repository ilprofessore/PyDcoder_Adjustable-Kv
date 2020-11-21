# setting python_var: kivy_var doesnt work some times
# but
# setting var: var works all the time, so use that.

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from encode import encode_module  # my custom made module.
from decode import decode_module  # my custom made module.
from kivy.lang import Builder

Builder.load_file("design.kv")


class ScreenOne(Screen):
    pass


class ScreenTwo(Screen):
    encrypt_input = ObjectProperty(None)

    @property
    def encrypt_submit(self):
        global encrypt
        encrypt = self.encrypt_input.text
        encrypt = encode_module(encrypt)

    @property
    def clear(self):
        self.encrypt_input.text = ""


class ScreenThree(Screen):
    decrypt_input = ObjectProperty(None)

    @property
    def decrypt_submit(self):
        global decrypt
        decrypt = self.decrypt_input.text
        decrypt = decode_module(decrypt)

    @property
    def clear(self):
        self.decrypt_input.text = ""


class ScreenFour(Screen):
    encrypt_output = ObjectProperty(None)

    @property
    def encrypt_set(self):
        self.encrypt_output.text = encrypt


class ScreenFive(Screen):
    decrypt_output = ObjectProperty(None)

    @property
    def decrypt_set(self):
        self.decrypt_output.text = decrypt


class Manager(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)
    screen_four = ObjectProperty(None)
    screen_five = ObjectProperty(None)


class MainApp(App):
    def build(self):
        return Manager()


if __name__ == '__main__':
    MainApp().run()
