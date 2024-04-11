from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class LenPasword(Screen):
    pass

program = ScreenManager()
program.add_widget(LenPasword(name = "lenpasword"))

class PaswordingApp(App):
    def build(self):
        boxlayout = BoxLayout(orientation = "vertical", spacing = 5, padding = [10])

        button_new_pasword = Button(text = "New Pasword",
                                    background_color = [0, 1.5, 3, 1],
                                    size_hint = [1, 0.1])

        boxlayout.add_widget(button_new_pasword)

        return boxlayout
        return program

if __name__ == "__main__":
    PaswordingApp().run()