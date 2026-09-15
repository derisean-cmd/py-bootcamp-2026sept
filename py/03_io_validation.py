# data input
username = str(input("Your username: "))
exam_cat = input("""JLPT candidate? (true/false):""").lower().strip()

if exam_cat == "true":
        while True:
                JLPT = int(input("Enter your JLPT Level: n"))
                if JLPT >=1 and JLPT <=5:
                        break
        print(f"Hello {username}, welcome to the JLPT Calculator")
        
else: 
        print(f"""Hi {username}, This calculator is only meant for JLPT.""") 
        print("Please use other calculator if you are not doing JLPT")



# Exercise1
print("This is the N1 calculator, please insert your score accordingly")
sess1 = int(input("session1 - language knowledge (?/60): "))
if sess1 >= 19 and sess1 <= 60:
        print("Great, enter your reading score")
elif sess1 < 19:
        print("Failed JLPT, see you next time")      
elif sess1 > 60:
        print("Seriously? insert score properly onegaishimasu")

sess2 = int(input("session2 - reading (?/60): "))
sess3 = int (input("session3 - listening (?/60): "))








