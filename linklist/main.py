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

  # insert at end
  def inser_at_end(self,node):
    current = self
    while current.next:
      current = current.next
    current.next = Node(node)
  
  # insert at beginning
  def insert_at_beginning(self,node):
    new_node = Node(node)
    new_node.next = self
    return new_node

  # delete by value:
  def delete_by_value(self,val):
    # check if val == self.data
    # if true delete and return
    # else current = self:
    if val == self.data: #val == 1
      # [1, 2, 3, 4, 5]
      self.data = self.next.data
      self.next = self.next.next
      return
    else:
      current = self.next
      while current:
        if val == current.data:
          current.data = current.next.data
          current.next = current.next.next
          return
        current = current.next
      print("Value not found")

# recursive print
def recursive_print( node):
  if node is None:
    print(None)
    return
  print(node.data, end=" -> ")
  recursive_print(node.next)

a = Node(1)
a.inser_at_end(2)
a.inser_at_end(3)
a.inser_at_end(4)
a.inser_at_end(5)

a.traverse_print()
a.delete_by_value(21)
a.traverse_print()
