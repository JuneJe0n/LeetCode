class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if self.q1: # if q2 is empty
            self.q1.append(x)
        else: # if q1 is empty or both
            self.q2.append(x)

    def pop(self) -> int:
        # move elements to other until the pop
        if self.q1: # if q2 is empty
            for _ in range(len(self.q1) - 1):
                element = self.q1.popleft()
                self.q2.append(element)
                print(element)
                print(self.q2)
            return self.q1.popleft()
        else: # if q1 is empty
            for _ in range(len(self.q2) - 1):
                element = self.q2.popleft()
                self.q1.append(element)
            return self.q2.popleft()

    def top(self) -> int:
        # move elements, peek, move 
        if self.q1: # if q2 is empty
            for _ in range(len(self.q1)):
                element = self.q1.popleft()
                self.q2.append(element)
        else: # if q1 is empty
            for _ in range(len(self.q2)):
                element = self.q2.popleft()
                self.q1.append(element)
        
        return element

    def empty(self) -> bool:
        # check if both are empty
        return True if not self.q1 and not self.q2 else False




