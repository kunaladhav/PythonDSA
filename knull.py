

# def recurringFirstItem(input):
#     result = set()
#     for i in input:
#         if i in result:
#             return i
#         result.add(i)
#     return None

# print(recurringFirstItem([1,5,5,1,3,4,6]))


# def kunal(item):
#     for i in item:
#         return i


# print(kunal([1, 5, 5, 1, 3, 4, 6]))


# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList():
#     def __init__(self):

#         self.head = None

#     def insertItem(self, data):

#         newNode = Node(data)

#         if self.head is None:
#             self.head = newNode
#         else:
#             tempNode = self.head
#             while tempNode.next:
#                 tempNode = tempNode.next
#             tempNode.next = newNode

#     # ---------------------------------------------------------------------------------------------------

#     '''
#     the tempNode here will only be true till the last node in the list (the Door and Kid example)
#     Time when the tempNode will be False when the last node's next is pointing no None
#     so None is False, so it will exit the loop

#     Now we are at the last node we can insert our new node
#     So that's why

#     tempNode.next = newNode

#     which means the last node is pointing at the newNode which is to be inserted

#     '''
#     # ----------------------------------------------------------------------------------------------------

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         #print("None")


# llist = LinkedList()        # Creating an Instance of a class to call its methods

# llist.insertItem(3)
# llist.insertItem(4)
# llist.insertItem(5)
# llist.insertItem(6)

# llist.display()


# Sliding Window

# def slidingwindow(arr, k):

#     size_arr = len(arr)


# t = int(input());


# for _ in range(t):
#     x = list(map(int, input().split()));
#     print(type(x));
#     sum = 0;

#     for i in range(len(x)-1):
#         if x[i] < x[i+1]:
#             sum += x[i];

#     print(sum);


# -----------------------------------------------------------------------------------------------------------------------------

# --- Neetcode Array 2 ---

# s = "rat"
# t = "cat"

# results = set(s)
# resultt = set(t)

# if results == resultt:
#     print(True)
# else:
#     print(False)

# -----------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

#                      Python DSA Course Practice Rough Sheet

# -------------------------------------------------------------------------------------
