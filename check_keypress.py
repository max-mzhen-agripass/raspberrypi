import keyboard


while True:
    if keyboard.is_pressed("g"):
        print("You pressed 'g'.")
        break
    else: print("not g")