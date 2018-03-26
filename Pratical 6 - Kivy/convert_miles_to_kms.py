from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window


class MilesToKilometersApp(App):
    def build(self):
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_to_kms')
        return self.root

    def handle_increment(self, number):
        increment = int(self.root.ids.input_number.text) + number
        self.root.ids.input_number.text = str(increment)

MilesToKilometersApp().run()
