class Node:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.next = None

class EmailList:
    def __init__(self):
        self.head = None

    def add_contact(self, name, email):
        new_node = Node(name, email)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_contacts(self):
        current = self.head
        while current:
            print(f"이름: {current.name}, 이메일: {current.email}")
            current = current.next

# 이메일 리스트 생성
email_list = EmailList()

while True:
    name = input("이름을 입력하세요 (종료하려면 enter 키를 누르세요): ").strip()
    if not name:
        break
    email = input("이메일을 입력하세요: ").strip()
    email_list.add_contact(name, email)

print("\n이메일 리스트:")
email_list.print_contacts()
