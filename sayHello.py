mrom kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window
        self.window.cols = 1

        self.window.add_widget(Image(source="norickroll.png"))
        self.greeting = Label(text="Do You want to get ricked rolled?")
        self.window.add_widget(self.greeting)
        self.user = TextInput(multiline=False)
        self.window.add_widget(self.user)
        self.button = Button(text="GREET")
        self.button.bind(on_press=self.event)
        self.window.add_widget(self.button)

        return self.window
        

    def event(self, instance):
        self.greeting.text = "No I dont care ... Get rick rolled anyway " + self.user.text +"!"

if __name__ == "__main__":
    SayHello().run()
