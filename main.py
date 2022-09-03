from json import detect_encoding
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera
class ScannerApp(App):
    def build(self):
        self.cam = Camera()
        self.cam.resolution = (800, 800)
        self.cam.play = True
        layout = BoxLayout()
        layout.add_widget(self.cam)
        self.make_button(layout, "take picture", self.take_pic)
        self.make_button(layout, "Should I Eat It", self.detect_labels)
        return layout

    def take_pic(self, *args):
        self.cam.export_to_png("./scan.png")

    def detect_labels(self, *args):
        print("detecting labels")

        #Should I Eat It Button
    def make_button(self, layout, text, fun):
        button = Button(text=text)
        button.size_hint = (.5,.2)
        button.pos_hint = {'x': .30, 'y': .30}
        button.bind(on_press=fun)
        layout.add_widget(button)

ScannerApp().run()