from kivy_garden.mapview import MapMarkerPopup
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage


        
class SingleKrasnal():
    def __init__(self, lat, lon, name, filepath):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.path = "resources/images/krasnals/" + filepath + ".jpg"
        pass
    
    dialog = None
    
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
    lat = 0
    lon = 0
    assignedKrasnal = (lat, lon, "", "")

    def on_release(self):
        self.assignedKrasnal.show_popup()
        pass