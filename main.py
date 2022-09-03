from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera

class ScannerApp(App):
    def build(self):
        self.cam = Camera()
        self.cam.resolution = (800, 800)
        self.cam.play = True
        button = Button(text="take picture")
        button.size_hint = (.5,.2)
        button.pos_hint = {'x': .25, 'y': .25}
        button.bind(on_press=self.take_pic)
        layout = BoxLayout()
        layout.add_widget(self.cam)
        layout.add_widget(button)
        return layout

    def take_pic(self, *args):
        self.cam.export_to_png("./scan.png")
    
ScannerApp().run()