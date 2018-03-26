from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicKivyWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre","Owen Wilson"]

    def build(self):
        self.title = "Dynamic Kivy Widgets"
        self.root = Builder.load_file('dynamic_kivy_widgets')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)

    def clear_all(self):
        self.root.ids.entries_box.clear_widgets()


DynamicKivyWidgetsApp().run()