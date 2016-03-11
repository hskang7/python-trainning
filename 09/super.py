class A:
    def __init__(self):
        print("A.__init__()")
        self.message = "Hello"
        
class B(A):
    def __init__(self):
        print("B.__init__()")
        
        super().__init__()
        print("self.message is " + self.message)
        
if __name__ == "__main__":
        b = B()