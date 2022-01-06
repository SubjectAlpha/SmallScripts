import time

#CHARLIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;':,./<>?"
CHARLIST = "abcdefghijklmnopqrstuvwxyz"
START_TIME = time.time()

def main(password, current_guess="", count=0):
    print(f"[{round(time.time() - START_TIME, 3)}] {current_guess}")
    if len(password) == len(current_guess):
        count += 1
        if current_guess == password:
            return True, count
        return False, count
    else:
        for char in CHARLIST:
            found, count = main(password, current_guess + char, count)
            if found:
                return True, count
        return False, count

if __name__ == "__main__":
    password = input("Enter password: ")
    result, count = main(password)
    print(f'Took {round(time.time() - START_TIME, 3)} seconds and {count} tries')