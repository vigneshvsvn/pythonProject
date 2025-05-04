"""
Binary Data: Bytes and bytearray suitable for Binary data.

usually in real time pillow library will be used. Not like this.

"""

f1=open('Briyani.jpg','rb')
data=f1.read()
print('Type of data:',type(data))

f2=open("Chicken_Briyani.jpg",'wb')
f2.write(data)

f1.close()
f2.close()
print("New Image File Created.")
