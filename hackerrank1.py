import numpy

first_line = raw_input().split(" ")
n= int(first_line[0])
m = int(first_line[1])

list =[]
for i in range(0,n):
    line = raw_input().split(" ")
    list_2 = []
    list.append(list_2)
    for j in line:
        list_2.append(int(j))

my_array = numpy.array(list)


numpy.set_printoptions(legacy='1.13')
print numpy.mean(my_array, axis = 1)
print numpy.var(my_array, axis = 0)
print numpy.std(my_array, axis = None)   
