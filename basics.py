import time

BASIC_INT = 1024
BASIC_FLOAT = 3.14
BASIC_STR = "Hello World"

if __name__ == "__main__":
    print(BASIC_INT)
    print(BASIC_FLOAT)
    print(BASIC_STR)
    time.sleep(5)

    if True:
        print("True")
    time.sleep(5)

    print(BASIC_INT * 2)
    time.sleep(5)

    for x in range(0, 10):
        print(x)
    time.sleep(5)

    count = 0
    while True:
        if count == 5:
            break
        print(count)
        count += 1
    time.sleep(5)
    
    try:
        print(BASIC_INT / 0)
    except ZeroDivisionError as e:
        print(e)
    time.sleep(5)