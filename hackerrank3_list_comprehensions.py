#Let's learn about list comprehensions! You are given three integers X,Y and Z  representing the dimensions of a cuboid along with an integer N .
#You have to print a list of all possible coordinates given by (i,j,z) on a 3D grid where the sum of i+j+k is not equal to N .
#Here, 0<=i<=X;0<=j<=Y; 0<=k<=Z
#Input Format

#Four integers X,Y,Z and N each on four separate lines, respectively.

#Constraints

#Print the list in lexicographic increasing order.

x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())
print [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)if ((i+j+k) != n)]

# ar = []
# p = 0
# for i in range ( x + 1 ) :
#     for j in range( y + 1):
#         if i+j != n:
#             ar.append([])
#             ar[p] = [ i , j ]
#             p+=1
# print ar

# x = int ( raw_input())
# y = int ( raw_input())
# n = int ( raw_input())
# print [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]


#------

for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print reduce(lambda acc, n: acc * 10 + n, range(1, i+1) + range(i -1, 0, -1))


#-------
#python 3
a = int(input())
b= int(input())
print (a//b)
print (a%b)
print (divmod(a,b))

#------
#Power - Mod Power
a = int(raw_input())
b= int(raw_input())
m = int(raw_input())
print pow(a,b)
print pow(a,b,m)
