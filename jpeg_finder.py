import sys
import os

if len(sys.argv) is 1:
    print('Useage : <dir>')
    exit(1)


for (path, dir, files) in os.walk(sys.argv[1]):
    print(dir)
    print(path)
    for filename in files:
        offset = 0
        IN = open(path + "\\" + filename, 'rb')
        data = IN.read(11)
        if data[:4] == b'\xff\xd8\xff\xe0' and data[6:] == b'JFIF\x00': 
            print(path + "\\" + filename + " is jpeg")
        else:
            print(path + "\\" + filename + " is not jpeg")


            
        