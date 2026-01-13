class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
  
  # traversing (visiting each node)
  def traverse_print(self):
    current = self
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print(None)

  # insert at back
  def inser_at_end(self,node):
    current = self
    while current.next:
      current = current.next
    current.next = Node(node)
  
  def insert_at_beginning(self,node):
    new_node = Node(node)
    new_node.next = self
    return new_node

# recursive print
def recursive_print( node):
  if node is None:
    print(None)
    return
  print(node.data, end=" -> ")
  recursive_print(node.next)

a = Node(10)
a.inser_at_end(12)
a.inser_at_end(11)
a.inser_at_end(0)
a.inser_at_end(12)
new_lst = a.insert_at_beginning(20)
recursive_print(a)
recursive_print(new_lst)
