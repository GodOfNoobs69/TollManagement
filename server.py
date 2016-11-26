import os
import sys
import pyqrcode
import qrtools

os.chdir('/home/vima/Python/Python/')

qr = qrtools.QR()
qr.decode("tag.png")
tag = qr.data
tag = int(tag)
tag = ((tag/3)/2)

tf1 = open("cars.txt","r")

carno = tf1.readline()
carno = int(carno)
if(tag == carno):
    print("Toll Accepted")

else:
    print("Toll Not Paid")
    
