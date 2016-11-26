import json
import os
import unicodedata
import sys
import shutil
import pyqrcode
import qrcode
from PIL import Image

def move(src,dest):
    shutil.move(src,dest)

class Item(object):
    def __init__(self,j):
        self.__dict__ = json.loads(j)

os.chdir('/home/vima/Python/Python/')
file = open('trial.txt')
content = file.read()

tolls=Item(content)
name = raw_input("Username:")
carno = input("Car Number:")

def GenerateTag(number):
    tag = (number * 2)*3
    return tag

text_file2 = open("cars.txt","w")

text_file2.write(str(carno))

text_file2.close()
tag = GenerateTag(carno)

print("Routes:")
for i in range(len(tolls.lists)):
    print i+1,".",tolls.lists[i]['Name']
print('\n')
choice = input("Enter choice:")
choice = choice - 1
print("Tolls Encountered:")

print('\n')


for i in range(len(tolls.lists[choice]['Tolls_Name'])):
    tolls.lists[choice]['Tolls_Name'][i] = unicodedata.normalize('NFKD',tolls.lists[choice]['Tolls_Name'][i]).encode('ascii','ignore')
    tolls.lists[choice]['Cost'][i] = int(tolls.lists[choice]['Cost'][i])
    print tolls.lists[choice]['Tolls_Name'][i],":",tolls.lists[choice]['Cost'][i]

tc = sum(tolls.lists[choice]['Cost'])
print('\n')

print "Total Cost:",tc

pay = input("Do you wish to pay? (0 or 1): ")

if pay == 1:
    #Simulate the payment gateway
    img_src = pyqrcode.create(tag)
    img_src.png('tag.png',scale=6)
    img_src.show()
else:
    exit(0)












