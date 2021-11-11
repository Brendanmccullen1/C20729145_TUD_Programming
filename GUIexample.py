# OOP 2021-22
# B. Schoen-Phelan
# October 2021
# code adapted from kivy tutorial by Python Simplified:
# https://www.youtube.com/watch?v=YDp73WjNISc

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}


        #add widgets to window
        self.im = Image(source="dog.png")
        self.window.add_widget(self.im)

        self.greeting = Label(
                        text="What's your name?",
                        font_size = 38,
                        color = "#00FFCE")
        self.window.add_widget(self.greeting)

        self.user = TextInput(
                    multiline = False,
                    padding_y = (20,20),
                    size_hint = (1,0.3))
        self.window.add_widget(self.user)

        self.button = Button(
                      text="Click me",
                      size_hint = (1, 0.3),
                      bold = True,
                      background_color = "#00FFCE")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, event):
        self.greeting.text = "Hello " + self.user.text + "!"
        self.im.source = "horses.jpg"

if __name__ == "__main__":
    SayHello().run()


