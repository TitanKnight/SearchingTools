import os
from os.path import join

my_path = input('Enter the path to search. Do not forget to add "/" at the end. >>> ')
my_ing = input("Enter the file extension. >>> ")
my_ing = my_ing.lower()
my_ing = my_ing[1:len(my_ing)]
file_list = []
all_list = []
number_of = 0
all_file = open("Result.txt", 'w')

for root, dirs, files in os.walk(my_path):
    dl = len(files)
    for x in range(0, dl):
        y = files[x]
        z = y.split('.')
        v = len(z)-1
        if z[v] == my_ing:
            file_list.append(y)
            print(y, "   ", join(root, y))
            file_text = y + "   " + join(root, y)
            all_list.append(file_text)
            number_of += 1
            all_file.write("""
""")
            all_file.write(file_text)
        else:
            pass
print('')
print('There are no more files with the extension', my_ing.upper(), 'in the path given. ')
all_string = str(all_list)
all_file.close()
input()
