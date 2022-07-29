from node import Node

class SingleLinkedList():
    def __init__(self) -> None:
        self.tail = None
        self.size = 0

    def append(self,data):
        node = Node(data)

        if self.tail == None:
            self.tail = node
        else:
            current = self.tail

            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def size(self):
        return self.size
    
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val
    
    def delete(self,data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                self.size -= 1

            
            previous = current
            current = current.next 
    
    def search(self,data):
        for node in self.iter():
            if node == data:
                print(f"Data {data} found!")
                return
        print(f"Data {data} not found!")

    def clear(self):
        self.tail = None
        self.sieze = 0
    
    def print(self):
        for item in self.iter():
            print(item, end=" ")
        print()

if __name__ == "__main__":
    words = SingleLinkedList()
    words.append("pan")
    words.append("carne")
    words.append("queso")
    words.append("tomate")
    print(words.size)

    for word in words.iter():
        print(word)

    words.search("queso")
    words.print()
    words.delete("tomate")
    words.search("tomate")
    words.print()
    words.clear()
    words.print()
