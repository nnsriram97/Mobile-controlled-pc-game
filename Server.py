import socket         #Socket for Wireless communication
import win32api       
import win32con
import time         
s=socket.socket()
host='192.168.xx.xx'      #Host ip address
port=5003
s.bind((host,port))       #bind to the host ip
print 'hello'             #just to know that it binded correctly
s.listen(5)               #listen
c,addr=s.accept()         #accept connection if available
print 'Got connected',addr
def pressAndHold(args):               #Press and Hold a Key
    win32api.keybd_event(args, 0,0,0)
    time.sleep(.05)
def release(args):                    #Release a pressed key
    win32api.keybd_event(args,0 ,win32con.KEYEVENTF_KEYUP ,0)
def press(args):                      #tapping a key
    win32api.keybd_event(args, 0,0,0)
    time.sleep(.05)
    win32api.keybd_event(args,0 ,win32con.KEYEVENTF_KEYUP ,0) 
uparr=0x57			#Hex decimal code for W
leftarr=0x41		#Hex decimal code for A
rightarr=0x44		#Hex decimal code for D
downarr=0x53		#Hex decimal code for S
w=0					#flag to know key press
a=0					#flag to know key press
d=0 				#flag to know key press
x=0         #flag to know key press
while True:                                   #The main Loop
	try:
		val=c.recv(50003)         #receive a line 
		arr=val.split()           #Separate them into different strings. A lot of values get received in single line but we 
		#print arr[0],arr[1],arr[2],arr[3],arr[4][0]      # use only the values received frist
		if arr[4][0]=='1':        #Press spacebar
			press(0x20)
		if float(arr[0])<-6.0:    #according to the values i have called key press events
			if w==1:
				release(uparr)
				w=0
			pressAndHold(downarr)
			x=1
			if float(arr[1])>-2.5 and float(arr[1])<2.5:
				if a==1:
					release(leftarr)
					a=0
				if d==1:
					release(rightarr)
					d=0
			elif -(float(arr[1]))>5.0:
				if d==1:
					release(rightarr)
					d=0
				pressAndHold(leftarr)
				a=1
			elif float(arr[1])>5.0:
				if a==1:
					release(leftarr)
					a=0
				pressAndHold(rightarr)
				d=1
			elif -(float(arr[1]))>2.50:
				if d==1:
					release(rightarr)
					d=0
				pressAndHold(leftarr)
				a=1
			elif float(arr[1])>2.50:
				if a==1:
					release(leftarr)
					a=0
				pressAndHold(rightarr)
				d=1
		elif float(arr[0])>-6.0:
			if x==1:
				release(downarr)
				x=0
			pressAndHold(uparr)
			w=1
			if float(arr[1])>-2.5 and float(arr[1])<2.5:
				if a==1:
					release(leftarr)
					a=0
				if d==1:
					release(rightarr)
					d=0
			elif -(float(arr[1]))>5.0:
				if d==1:
					release(rightarr)
					d=0
				pressAndHold(leftarr)
				a=1
			elif float(arr[1])>5.0:
				if a==1:
					release(leftarr)
					a=0
				pressAndHold(rightarr)
				d=1
			elif -(float(arr[1]))>2.50:
				if d==1:
					release(rightarr)
					d=0
				pressAndHold(leftarr)
				a=1
			elif float(arr[1])>2.50:
				if a==1:
					release(leftarr)
					a=0
				pressAndHold(rightarr)
				d=1	
	except:
		print "Game Over"
		if x==1:
			release(downarr)
			x=0
		if w==1:
			release(uparr)
			w=0
		if a==1:
			release(leftarr)
			a=0
		if d==1:
			release(rightarr)
			d=0
		break
