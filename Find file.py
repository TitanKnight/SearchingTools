import os
from os.path import join

my_path = "C:/"
my_file = input("Enter the name of file what you're searching. >>> ")
find = False

print('Wait...')

for root, dirs, files in os.walk(my_path):
    if my_file in files:
        print('File found! %s' % join(root, my_file))
        find = True
        break
    else:
        find = False
if find == False:
    print('File not found.')
input()
