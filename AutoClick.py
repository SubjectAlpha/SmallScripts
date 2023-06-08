import pyautogui, time, keyboard, random


click_box = []
y_upper_limit = 15
y_lower_limit = 0
x_upper_limit = 30
x_lower_limit = 5

def get_position():
    return pyautogui.position()

def click():
    pyautogui.click(get_position().x, get_position().y)

def midpoint(p1, p2):
    return pyautogui.Point(x = (p1.x+p2.x)/2, y = (p1.y+p2.y)/2)

def run():
    for _ in range(0,4):
        print("wait")
        time.sleep(3)
        print("got it")
        click_box.append(get_position())
    
    itr = 0

    while(True):
        if keyboard.is_pressed('q'):
            quit()

        top_l_pos = click_box[0]
        bot_l_pos = click_box[1]
        bot_r_pos = click_box[2]
        top_r_pos = click_box[3]

        l_mid = midpoint(top_l_pos, bot_l_pos)
        r_mid = midpoint(top_r_pos, bot_r_pos)

        #need to know if on left or right
        

        if(itr % 2):
            x = random.randrange(int(l_mid.x) + x_upper_limit, int(l_mid.x))
            y = random.randrange(int(l_mid.y) + y_upper_limit, int(l_mid.y))
            pyautogui.moveTo(x, y, duration = random.random())
        else:
            x = random.randrange(int(r_mid.x) + x_upper_limit, int(r_mid.x))
            y = random.randrange(int(r_mid.y) + y_upper_limit, int(r_mid.y))
            pyautogui.moveTo(x, y, duration = random.random())
        click()
        time.sleep(2)

        itr += 1

if __name__ == "__main__":
    run()