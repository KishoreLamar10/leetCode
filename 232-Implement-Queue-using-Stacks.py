class MyQueue(object):

    def __init__(self):
        self.input = []
        self.output = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        while len(self.input) > 1:
            self.output.append(self.input.pop())
        ans = self.input.pop()
        while self.output:
            self.input.append(self.output.pop())
        
        return ans
        

    def peek(self):
        """
        :rtype: int
        """
        while len(self.input) > 1:
            self.output.append(self.input.pop())
        ans = self.input[-1]
        while self.output:
            self.input.append(self.output.pop())
        
        return ans
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.input) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()