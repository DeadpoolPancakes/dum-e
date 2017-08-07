file = open("testfile.txt","r")
 
print ("booya")

v = 0
for i in file.readlines():
    v = v + 1
    print(v)
    print (i)
  