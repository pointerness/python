#DSA-Assgn-3

def check_double(list1,list2):
    new_list=[]
    #write your logic here
    for num in list1:
        if(list2.count(2*num) != 0):
            new_list.append(num)
    return new_list

#Provide different values for the variables and test your program
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1, list2))