import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

def generate_lotto_numbers():
    lotto_numbers = random.sample(range(1, 46), 6)
    return lotto_numbers

def main():
    lotto_numbers = generate_lotto_numbers()

    linked_list = LinkedList()
    for number in lotto_numbers:
        linked_list.append(number)

    print("로또 번호:")
    current = linked_list.head
    while current:
        print(current.data)
        current = current.next

if __name__ == "__main__":
    main()




