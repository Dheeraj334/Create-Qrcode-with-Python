import pyqrcode
import string
import random as random
y=3
a=[]
n=int(input("Enter the value which you want to make the qrcode"))
for i in range(n):
   value=input("Enter the String ")
   a.append(value)
print("Your list is:-",a)
res=''.join(random.choices(string.ascii_uppercase + string.digits, k = y)) 
for j in range(n):
    for b in range(n):
        qr= pyqrcode.create(a[j])
        qr.png(res+'.png',scale=8)

