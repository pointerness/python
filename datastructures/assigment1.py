#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data=""
    #write your logic here
    for i in range(len(list1)):
        if( list1[i] != None):
            merged_data+=list1[i]
        j=len(list2) -i-1
        if(list2[j] != None):
            merged_data+=list2[j]
        merged_data+=" "
    return merged_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)