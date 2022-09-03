from json import detect_encoding
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from example_output import example_aws_output
import boto3
import random

class ScannerApp(App):
    def build(self):
        self.cam = Camera()
        self.cam.resolution = (800, 800)
        self.cam.play = True
        layout = BoxLayout()
        layout.add_widget(self.cam)
        side_layout = BoxLayout()
        side_layout.orientation = "vertical"
        layout.add_widget(side_layout)
        self.make_widget(side_layout, Button, "take picture", fun=self.take_pic)
        self.make_widget(side_layout, Button, "Should I Eat It", fun=self.detect_labels)
        self.results = self.make_widget(side_layout, Label, "results")
        self.results.text_size = [self.results.width, None] 
        return layout

    def take_pic(self, *args):
        self.cam.export_to_png("./scan.png")

    def parse_responses(self, responses):
        responses = [i["Name"] for i in example_aws_output]
        possible_responses = ["Probably don't eat it", "You might glow after", "It might not kill you?"]
        # for res in responses:
        #     for key in joke_dictionary:
        #         if(res in joke_dictionary[key]):
        #             possible_responses += [key]
        r = random.randint(0, len(possible_responses)-1)
        return possible_responses[ r ]

    def detect_labels(self, *args):
        print("detecting labels")
        if not example_aws_output:
            client=boto3.client('rekognition')
            with open("./scan.png", 'rb') as image:
                response = client.detect_labels(Image={'Bytes': image.read()})
            print(response["Labels"])
            response = self.parse_responses(response["Labels"])      
            self.results.text =  response
        else:
            response = self.parse_responses(example_aws_output)      
            self.results.text =  response

    def make_widget(self, layout, Widget, text, fun=None):
        widget = Widget(text=text)
        widget.size_hint = (.5,.2)
        widget.pos_hint = {'x': .30, 'y': .30}
        if fun: widget.bind(on_press=fun)
        layout.add_widget(widget)
        return widget

ScannerApp().run()