def safe_file_operation(file, func):
    try:
        print("executing " + str(func))
        return func(file)
    finally:
        file.close()
        print("file closed.")
        
def read_some(file):
    return file.read()

file = open("test.txt")
s = safe_file_operation(file, read_some)
print(s)
