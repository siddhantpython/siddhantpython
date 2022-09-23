f=open("mydata","r") #r: is to read only
##print(f.read())#printing the read part in console

f1=open("myqualiications","w")#w:is to wirte new stuff in new or same file
for data in f:
    f1.write(data)

f1=open("myqualiications","a")#a: is to append the new stuf to same file without deleting the old stuff
f1.write(" i have done B.tech from mechanical engineering")

f1=open("myqualiications",'r')
print(f1.read())

f2=open("IMG2018.jpg",'rb') #rb:as image is in binary format,hence we use key "rb" as read binary.
f3=open("img.jpg","wb")#wb : it is write binary
for i in f2:
    f3.write(i)

