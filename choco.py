from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
 
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
 
from kivy.config import Config
 
Config.set('graphics', 'resizable', '0');
Config.set('graphics', 'width', '640');
Config.set('graphics', 'height', '480');
 
 
Builder.load_string("""
<LoginScreen>:
    AnchorLayout:
        BoxLayout:
            orientation: 'vertical'
            size_hint: [0.5, 0.5]
            GridLayout:
                rows: 2
                cols: 2
                padding: [0, 20, 0, 0]
                spacing: [25]
                Label:
                    text: 'Email'
                    size_hint_x: None
                    width: 100
                    font_size: 16
                TextInput:
                    text: ''
                    font_size: 20
                    multiline: False
                    padding: [6, 6, 0, 6]
                Label:
                    text: 'Password'
                    size_hint_x: None
                    width: 100
                    font_size: 16
                TextInput:
                    text: ''
                    font_size: 20
                    multiline: False
                    padding: [6, 6, 0, 6]
            GridLayout:
                cols: 3
                padding: [0, 20, 0, 70]
                CheckBox:
                Widget:
                Button:
                    text: 'Log in'
                    background_color: [.97, .55, .12, 1]
                    background_normal: ''
                    on_press:
                        ConfigChange
                        root.manager.transition.direction = 'left'
                        root.manager.current = 'Main'
 
                    
<MainScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'Login'
""")
 
 
class LoginScreen(Screen):
    pass
    # def ConfigChange(self, instance):
 #      Config.set('graphics', 'resizable', '0')
 #      Config.set('graphics', 'width', '720')
 #      Config.set('graphics', 'height', '640')
 
class MainScreen(Screen):
    pass
 
sm = ScreenManager(transition=NoTransition())
sm.add_widget(LoginScreen(name='Login'))
sm.add_widget(MainScreen(name='Main'))
 
class TestApp(App):
 
    def build(self):
        self.title = "Email"
        return sm
 
if __name__ == '__main__':
    TestApp().run()
