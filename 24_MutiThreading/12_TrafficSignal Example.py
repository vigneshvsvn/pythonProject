import time
from time import sleep
from threading import *



def trafficPolice():
	while True:
		sleep(10)
		print("Giving Green Signal")
		e.set()
		sleep(20)
		print("Giving Red Signal")
		e.clear()


def vehicles():
	num=0
	while True:
		print("Vehicles are waiting for Green Signal")
		e.wait()
		print("Traffic Signal is Green. Vehicle can Move")
		while e.is_set():
			num=num+1
			print(f"VehicleNo: {num}, crossing the Signale")
			time.sleep(2)
		print("Traffic Signal is Red, Vehicles has to Wait")

e=Event()

t1=Thread(target=trafficPolice)
t2=Thread(target=vehicles)

t1.start()
t2.start()
