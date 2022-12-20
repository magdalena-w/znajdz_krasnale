from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from krasnalmarker import SingleKrasnal, KrasnalMarker

class HomeMapView(MapView):
    getting_krasnals_timer = None
    krasnal_names = []
    krasnals = []

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
        pathname =  (krasnal[2]).replace(" ", "_")
        newKrasnal = SingleKrasnal(krasnal[0], krasnal[1], krasnal[2], pathname)
        marker = KrasnalMarker()
        marker.lat = krasnal[0]
        marker.lon = krasnal[1]
        marker.assignedKrasnal = newKrasnal
        ##DEBUG:
        #print(marker.path)
        #Add the marker to the map
        self.add_marker(marker)

        #Keep track of the marker's name
        self.krasnal_names.append(krasnal[2])
        self.krasnals.append(newKrasnal)
        
        #print(self.get_krasnal_by_name(krasnal[2]))
        
        pass
    
    def get_krasnal_by_name(self, name):
        for krasnal in self.krasnals:
            if krasnal.name == name:
                return krasnal
        return None
