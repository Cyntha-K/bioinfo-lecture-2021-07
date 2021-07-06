
import sys

#with open("noname.txt", 'r') as fr:
#    read = fr.readlines()

#    print(read)

try:
    with open("noname.txt", 'r') as fr:
        read = fr.readlines()
    print(read)

except FileNotFoundError as err:
    print(err)
    #noname.txt를 생성하는 과정을 해도 됨
    sys.exit()






