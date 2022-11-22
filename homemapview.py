from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from krasnalmarker import KrasnalMarker

class HomeMapView(MapView):
    getting_krasnals_timer = None
    krasnal_names = []

    def start_getting_krasnals_in_fov(self):
        #After .5 second, get the krasnals in the field of view
        try:
            #Whenever user moves map, timer is canceled and restarted
            self.getting_krasnals_timer.cancel()
        except:
            pass

        self.getting_krasnals_timer = Clock.schedule_once(self.get_krasnals_in_fov, 0.5)

    def get_krasnals_in_fov(self, *args):
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = "SELECT * FROM krasnals WHERE x > %s AND x < %s AND y > %s AND y < %s" % (min_lat, max_lat, min_lon, max_lon)
        app.cursor.execute(sql_statement)
        krasnals = app.cursor.fetchall()
        ##DEBUG:
        #print(krasnals)
        for krasnal in krasnals:
            name = krasnal[2]
            if name not in self.krasnal_names:
                self.add_krasnal(krasnal)
            else:
                pass
        

    def add_krasnal(self, krasnal):
        #Create a marker for the krasnal
        marker = KrasnalMarker(lat=krasnal[0], lon=krasnal[1])
        marker.name = krasnal[2]
        pathname =  (krasnal[2]+".jpg").replace(" ", "_")
        marker.path += pathname
        print(marker.path)
        #Add the marker to the map
        self.add_widget(marker)

        #Keep track of the marker's name
        self.krasnal_names.append(krasnal[2])
        
        pass