#DSA-Exer-2

class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
    
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node
    
    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()
                                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg
    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data() == data):
                break
        return temp
    def insert(self,data,data_before):
        temp=self.__head
        new_node=Node(data)
        while(temp is not None):
            if(temp.get_data()==data_before):
                new_node.set_next(temp.get_next())
                temp.set_next(new_node)
                break
            else:
                temp = temp.get_next()
        if(temp is None):
            print("Node does not exists adding new")
            self.add(data)
            
                
        
def count_nodes(biscuit_list):
        count=0
        temp=biscuit_list.get_head()
        # Write your logic here
        while(temp is not None):
            count+=1
            temp=temp.get_next()
        return count

biscuit_list=LinkedList()
biscuit_list.add("Goodday")
biscuit_list.add("Bourbon")
biscuit_list.add("Hide&Seek")
biscuit_list.add("Nutrichoice")

print(count_nodes(biscuit_list))
list1=LinkedList()
#Add all the required element(s)\
list1.add("Sugar")
list1.add("Biscuit")
list1.add("Milk")
list1.add("Juice")
#Search for the required node
list1.display()
node=list1.find_node("Sugar")

if(node!=None):
    print("Node found")
else:
    print("Node not found") 
list1.insert("Salt","Sugar")

list1.insert("NewItem","Chocolate")
list1.display()
                                              