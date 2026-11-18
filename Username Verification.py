counter = 0
while True:
        user_input = input("Enter username: ").strip().upper()
        if user_input=="SKD":
            print(f"Welcome {user_input}")
            break

        else:
                counter = counter+1
                print(f"INCORRECT USERNAME. Attempt {counter} of 3")
                if counter == 1:
                        print(f"You have 2 attempts remaining out of 3")
                if counter == 2:
                        print(f"You have 1 attempts remaining out of 3")
                if counter == 3:
                        print("LOCKED OUT. Too many attempts")
                        break
