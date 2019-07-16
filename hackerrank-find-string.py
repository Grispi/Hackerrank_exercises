def count_substring(string,sub_string):
    count = 0
    for i in range(0,(len(string)-len(sub_string)+1)):
        if string[i] == sub_string[0]:
            flag = 1
            print ("i es igual s ", i)
            for j in range(0, len(sub_string)):
                if string[i+j]!= sub_string[j]:
                    print (i, j)
                    flag=0
                    break
            if flag ==1:
                print ("i y j",i, j)
                count +=1
    return count

def count_substring2(string,sub_string):
    count = 0
    for i in range(0,(len(string)-len(sub_string)+1)):
        if string[i:i+len(sub_string)] == sub_string:
            count +=1
    return count


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print count
    print count_substring2(string, sub_string)


# Sample Input
#
# ABCDCDC
# CDC
# Sample Output
#
# 2

# string, substring = (input().strip(), input().strip())
# print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))
