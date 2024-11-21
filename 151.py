my_file = open("names.txt",'r')
names = my_file.read().splitlines()
for name in names:
    print(name)
my_file.close()

#after - using with - will close the file

with open("names.txt", "r") as my_file:
    names = my_file.read().splitlines()
    for name in names:
        print(name)