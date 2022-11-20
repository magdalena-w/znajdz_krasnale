from kivymd.app import MDApp
from specialbuttons import LabelButton, ImageButton
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition

from kivy.core.window import Window

from homemapview import HomeMapView
from homegpshelper import HomeGpsHelper

import os

Window.size = (375, 750)


class HomeScreen(Screen):
    pass


class MainApp(MDApp):
    current_lat = 51.107883
    current_lon = 17.038538

    if os.path.isfile("resources/text/profile_source.txt"):
        with open("resources/text/profile_source.txt", "r") as f:
            some_path = f.read()
            if len(some_path) > 0:
                img_source_path = some_path
            else:
                img_source_path = "resources/images/empty.jpg"
    else:
        img_source_path = "resources/images/empty.jpg"

    def on_start(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "200"  # "500"
        self.theme_cls.theme_style = "Light"

        # Initialize GPS
        HomeGpsHelper().run()

    def change_screen(self, screen_name, direction='forward', mode=""):
        # Get the screen manager from the kv file.
        screen_manager = self.root.ids.screen_manager

        if direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)
        screen_manager.current = screen_name

        if screen_name == "home_screen":
            self.root.ids.titlename.title = "Znajdz krasnala"


MainApp().run()
