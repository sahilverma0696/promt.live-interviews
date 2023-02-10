"""
Create Linkedlist (int)
populate data and print
"""
class Node():
    def __init__(self,value = None):
        self.next = None
        self.val = value 

class LinkedList():

    def __init__(self):
        self.head = Node()
        self.tail = self.head
    
    def addNode(self,value) :
        self.tail.next = Node(value)
        self.tail = self.tail.next
    
    def getAllNodesValues(self) :
        ans = []
        curr = self.head.next
        while curr is not None :
            ans.append(curr.val)
            curr = curr.next
        
        return ans

    def reverseLL(self):
        """
        head -> 1-> 2-> 3 -> 4
        head   1  2-> 3 -> 4
        1 2-> 3 -> 4
        1<- 2 3->4    cuurHead = 3  reamin = 4 temp = 
        1<- 2<-3 4
        1<-2<-3<-4 
        """
        #head -> 1-> 2-> 3 -> 4
        currhead = self.head.next   #1
        self.head.next = None  # head   1-> 2-> 3 -> 4
        prev = None
        if not currhead : return 
        remain = None
        while currhead :
            remain = currhead.next  # None
            currhead.next = prev    #  None<-1 <-2<- 3 <-4
            prev = currhead         #  3
            currhead = remain       #  4
        self.head.next = prev

    """
    1-> 2-> 3 -> 4  k = 2
    2 -> 1 -> 4 -> 3  5-> 6
     2 -> 1  -> 4->3 -> 6->5  _
    """ 

    def reverseKLL(self,k):
        """
        head -> 1-> 2-> 3 -> 4
        """
        #head -> 1-> 2-> 3 -> 4 
        """
        tail = None
         None 1<-2  
            3  
        """
        currhead = self.head.next   
        self.head.next = None  
        prev = None
        if not currhead : return 
        remain = None
        cnt  = 1
        tail = currhead
        while currhead :
            if cnt  == k :
                self.head.next = currhead 
                tail.next = self.reverseKLL(k)
                cnt  = 1
            remain = currhead.next  
            currhead.next = prev    
            prev = currhead         
            currhead = remain 
            cnt += 1     
        self.head.next = prev
    










ll = LinkedList()
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.addNode(4)
print(ll.getAllNodesValues())
ll.reverseLL()
print(ll.getAllNodesValues())



