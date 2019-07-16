def mutate_string(string, position, character):
    new_string = string[:position] + character + string[position+1:]
    return new_string

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new

#opcion2
#>>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string
# abrackdabra

# Sample Input
# abracadabra
# 5 k
# Sample Output
# abrackdabra
