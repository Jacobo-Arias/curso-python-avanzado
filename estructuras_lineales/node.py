

class Node:
    def __init__(self,data,next=None) -> None:
        self.data = data
        self.prev = None
        self.next = next
        if self.next:
            self.next.prev = self
    
    def __str__(self) -> str:
        return f"{self.data}"


if __name__ == "__main__":
    n1 = Node("a")
    print(n1)
    print(n1.next)
    n2 = Node("b",n1)
    print(n2)
    print(n2.next)