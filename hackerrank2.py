import numpy
n = int(raw_input())
a = [map(int,raw_input().split()) for _ in range(n)]
b = []
for i in range(n):
    line = raw_input().split()
    list_2 = []
    b.append(list_2)
    for j in line:
        list_2.append(int(j))

print numpy.dot(a, b)

#--------------------------


import numpy
a = map(int,raw_input().split())
b = map(int,raw_input().split())

print numpy.inner(a, b)
print numpy.outer(a, b)

#-------------
    n = int(raw_input())
    arr = list(map(int, raw_input().split()))
    maximum = max(arr)
    i = 0
    while i<n:
        if max(arr) == maximum:
            arr.remove(max(arr))
        i+=1
    print (max(arr))
#-----------------------

n = int(raw_input())
student_list = []
score_list = []
dict_list = {}
for _ in range(n):
    a =raw_input()
    score = float(raw_input())
    if score in dict_list:
        dict_list[score].append(a)
    else:
        dict_list[score] = [a]

    student_list.append([a,score])
    score_list.append(score)
# print dict_list
#transformo el dictionario en lista
new_list= []
for i in dict_list:
    new_list.append([i, dict_list[i]])
new_list.sort()
result = new_list[1][1]
# print new_list
result.sort()
for x in range(len(result)):
    print result[x]

#---------------
score_list = {}
for _ in range(input()):
    name = raw_input()
    score = float(raw_input())
    if score in score_list:
        score_list[score].append(name)
    else:
        score_list[score] = [name]
new_list = []
for i in score_list:
    new_list.append([i, score_list[i]])
new_list.sort()
result = new_list[1][1]
result.sort()
print (*result, sep = "\n")


#---------------------
if __name__ == '__main__':
    def average(lista):
        total_product = 0
        for x in lista:
            total_product = total_product + x

            aver = total_product / len(lista)

        return aver
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()



# print student_marks
lista = student_marks.get(query_name)
# print lista
result =  average(lista)
print "{0:.2f}".format(result)

#---------------
#input1: 5
#input2: 12 4 5 -1 9
#You are given a space separated list of integers. If all the integers are positive,
#then you need to check if any integer is a palindromic integer.
n = int(raw_input())
value=raw_input().split()
# print value
result_a = all([int(j)>=0 for j in value])
# print result_a
result_b = any([i==i[::-1] for i in value])
print (result_a and result_b)

#---------------
# Enter your code here. Read input from STDIN. Print output to STDOUT

new_list = list(raw_input())
# print new_list
sort_list= (sorted(new_list))
lower_list=""
upper_list=[]
odd_list=[]
even_list=[]
for letter in sort_list:
    if letter.islower():
        lower_list+=letter
        # lower_list.append(letter)
    elif letter.isupper():
        upper_list.append(letter)
    elif  letter.isdigit():
        number = int(letter)
        if number%2 == 0:
            even_list.append(letter)
        else:
            odd_list.append(letter)
    else:
        print "algo anda mal"

separator = ''
# print (separator.join(lower_list))
print lower_list+(separator.join(upper_list))+(separator.join(odd_list))+(separator.join(even_list))
