f = open("hello.txt", "w")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("hello.txt", "r")
print(f.read())
