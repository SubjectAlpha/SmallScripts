import time

def example_function(a, b):
    return a + b

def basic_recursion(a, b):
    print(a)
    if a == b:
        return True
    return basic_recursion(a + 1, b)

if __name__ == "__main__":
    print(example_function(1, 2))
    time.sleep(5)

    try:
        create_file = open("test.txt", "w")
        create_file.write("Hello World")
        create_file.close()

        read_file = open("test.txt", "r")
        print(read_file.read())
        read_file.close()
    except Exception as e:
        print(e)
    time.sleep(5)

    print(basic_recursion(1, 5))
    time.sleep(5)