from kivymd.app import MDApp
from specialbuttons import LabelButton, ImageButton
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition

from kivy.core.window import Window

from homemapview import HomeMapView
from homegpshelper import HomeGpsHelper

import sqlite3
import os

Window.size = (375, 750)


class HomeScreen(Screen):
    pass


class CollectedScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignUpScreen(Screen):
    pass

class FileSelectionScreen(Screen):
    
    def select(self, *args):
        try:
            file_path = args[1][0]
            filename = os.path.basename(file_path)
            self.confirm_label.text = "Powtierdź: " + filename
        except: pass
    
    def confirm(self):
        pass
         
class MainApp(MDApp):
    current_lat = 51.107883
    current_lon = 17.038538
    
    # For database connection later on
    connection = None
    cursor = None

    img_source_path = "resources/images/empty.jpg"

    def on_start(self):
        # Set theme
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "200"  # "500"
        self.theme_cls.theme_style = "Light"

        # Initialize GPS
        HomeGpsHelper().run()
        
        # Connect to database
        self.connection = sqlite3.connect("resources/data/krasnale.db")
        self.cursor = self.connection.cursor()

    def change_screen(self, screen_name="home_screen", direction="None", mode="push"):
        # Get the screen manager from the kv file.
        screen_manager = self.root.ids.screen_manager
        screen_manager.transition = CardTransition(direction=direction, mode=mode) if direction != "None" else NoTransition()
        screen_manager.current = screen_name
        
        # Changes screen title to one defined in the screen in .kv file
        # self.root.ids.titlename.title = screen_manager.get_screen(screen_name).title
            
    def change_theme(self):
        if (self.theme_cls.theme_style == "Light"):
            self.theme_cls.primary_palette = "Teal"
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_hue = "500"
            # For some reason doesn't change all text colors.
        else:
            self.theme_cls.primary_palette = "Teal"
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_hue = "500"

MainApp().run()
