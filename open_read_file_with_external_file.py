f=open ("test.txt", "r")        #read file
print (f.read(3))        #read first 3bytes as a header string
print (f.read())		#read whole file
print (f.readlines ())   #read lines until whole file

f.close()

