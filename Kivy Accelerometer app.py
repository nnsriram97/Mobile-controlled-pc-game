
import socket                                   #for wifi communication

from kivy.app import App                        #import app
from kivy.uix.button import Button              #Button for brake and nitro   
from kivy.uix.gridlayout import GridLayout      #The way in which the screen is organized
from kivy.uix.label import Label                #a label to show accelerometer values
from plyer import accelerometer                 #object to read the accelerometer
from kivy.clock import Clock                    #clock to schedule a method
s=socket.socket()                               #create a socket object
host='192.168.xx.xx'                            # Specify the ip address of the host
port=5003                                       #a Port for communication 
s.connect((host,port))                          #connect to the specified host
w=0                                             #
e=0                                             #Flags to notify the button press
class Accel(GridLayout):                          
    def nitof(self,*args):                      #On release of nitro button makes w=0
        global w
        w=0
    def left(self,*args):                       #On press of nitro button makes w=1
        global w
        w=1
    def righ(self,*args):                       #On press of brake Button makes e=1
        global e
        e=1
    def rel(self,*args):                        #On release of Breake makes e=0
	    global e
	    e=0
    def __init__(self,**kwargs):                #Constructor to initialize the Accel
        try:
            super(Accel,self).__init__(**kwargs)
            self.cols=3
            self.rows=1
            self.q=Button(text='Brake')         #creating a brake button
            self.q.bind(on_press=self.righ)
            self.q.bind(on_release=self.rel)
            self.a=Button(text='Nitro')         #creating Nitro button and following lines binds them 
            self.a.bind(on_press=self.left)
            self.a.bind(on_release=self.nitof)
            self.l=Label(text="Accelerometer")	#A label showing accelerometer values
            self.add_widget(self.a)             #adding all the widgets
            self.add_widget(self.l)        
            self.add_widget(self.q)
        except:
            s.send('0')
        try:
            accelerometer.enable()              #Enabling the accelerometer
        except:
            self.l.text='Failed to start accelerometer'
        Clock.schedule_interval(self.accel, 1.0/30)   #Scheduling the interval to get accelerometer values
    def accel(self,*args):
	    global e
	    global w
	    txt = ""
	    try:
		    txt = "Accelerometer:\nX = %.2f\nY = %.2f\nZ = %2.f " %(accelerometer.acceleration[0],accelerometer.acceleration[1],accelerometer.acceleration[2])
	    except:
		    txt = "Cannot read accelerometer!"                           #error
	    self.l.text = txt                         #adds the txt
	    s.send("%.2f %.2f %.2f %d %d"%(accelerometer.acceleration[0],accelerometer.acceleration[1],accelerometer.acceleration[2],w,e))      
        #The above line sends teh accelerometer values along with the button press flags
class TestApp(App):       #The app class
    def build(self):
        return Accel()    

TestApp().run()       #Run the app class
