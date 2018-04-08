from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.app import StringProperty

class MilesToKilometersApp(App):
    def build(self):
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_to_kms')
        return self.root

    def handle_increment(self, number):
        try:
            increment = int(self.root.ids.input_number.text) + number
            self.root.ids.input_number.text = str(increment)
        except ValueError:
            self.root.ids.input_number.text = '0'
            increment = int(self.root.ids.input_number.text) + number
            self.root.ids.input_number.text = str(increment)

    def miles_to_kms(self):
        miles = self.root.ids.input_number.text
        try:
            kilometers = int(miles) * 1.6
            self.root.ids.output_label.text = str(kilometers)
        except ValueError:
            self.root.ids.output_label.text = '0'



MilesToKilometersApp().run()
