from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer

Config.set('graphics', 'resizable', '0');
Config.set('graphics', 'width', '300');
Config.set('graphics', 'height', '350');

class MyApp(App):
    def build(self):

        fl = FloatLayout(size = (200, 200))
        fl.add_widget(Button(text = "кнопка1",
        font_size=15,
        on_press=self.btn_press,
        background_color=[1,0,0,1],
        background_normal='',
        size_hint = (.5, .25),
        pos = (200, 350)))
        fl.add_widget(Button(text = "кнопка2",
        font_size=15,
        on_press=self.btn_press,
        background_color=[0,1,0,1],
        background_normal='',
        size_hint = (.5, .25),
        pos = (200, 120)))
        return fl

    def btn_press(self, instance):
        print("Button is pressed")
        instance.text = "Я нажата"

if __name__ == "__main__":
    MyApp().run()


    
