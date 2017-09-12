filename = "testfile.txt"
file = open(filename,"r")

for line in reversed(list(open(filename))):
    
    if line.rstrip('\n ') == "forward":
        print("going forward")
    else:
        print(line.rstrip())
    
