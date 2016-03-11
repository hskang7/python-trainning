class A:
    def __init__(self):
        print(self)
        self.message = "Hello, World."
        
    def print_message(self):
        print(self.message)
        
class B(A):
    pass

if __name__ == "__main__":
        a = A()
        a.print_message()
        
        b = B()
        b.print_message()