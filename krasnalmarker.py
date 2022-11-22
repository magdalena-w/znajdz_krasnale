from kivy_garden.mapview import MapMarkerPopup
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage


def show_popup(self):
    image_path = self.path if self.path != "" else "resources/images/empty.jpg"
    if not self.dialog:
            self.dialog = MDDialog(
                title=self.name,
                type="custom",
                content_cls=
                MDBoxLayout(
                    FitImage(
                        source=image_path,
                        #allow_stretch=True,
                        height = 400,
                        size_hint_y = None,
                    ),
                    MDLabel(
                        text="Koordynaty:",
                    ),
                    MDLabel(
                        text="X = "+str(self.lat),
                    ),
                    MDLabel(
                        text="Y = "+str(self.lon),
                    ),
                    orientation="vertical",
                    adaptive_height = True,
                    padding = (-15,-15,-15,25),
                    spacing = 35,
                )
            )
    self.dialog.open()
    
class KrasnalMarker(MapMarkerPopup):
    dialog = None
    name = ""
    path = "resources/images/krasnals/"
    
    def on_release(self):
        show_popup(self)
        pass
    
