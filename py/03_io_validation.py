# data input
username = str(input("Your username: "))
exam_cat = input("""JLPT candidate? (true/false):""").lower().strip()

if exam_cat == "true":
        JLPT = int(input("Enter your JLPT Level: n"))
        JLPT >=1 and JLPT <=5;
        print(f"Hello {username}, welcome to the JLPT Calculator")
        
else: 
        print(f"""Hi {username}, This calculator is only meant for JLPT.""") 
        print("Please use other calculator if you are not doing JLPT")
        break

# Exercise1
print("This is the N1 calculator, please insert your score accordingly")
sess1 = int(input("session1 - language knowledge (?/60): "))
sess2 = int(input("session2 - reading (?/60): "))
sess3 = int (input("session3 - listening (?/60): "))








