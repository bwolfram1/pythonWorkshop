import random
import time

print("Welcome to the...")
time.sleep(1)
print("""

 ______     ______     ______      ______     _____     __   __   ______     __   __     ______   __  __     ______     ______    
/\  ___\   /\  ___\   /\  == \    /\  __ \   /\  __-.  /\ \ / /  /\  ___\   /\ "-.\ \   /\__  _\ /\ \/\ \   /\  == \   /\  ___\   
\ \___  \  \ \ \____  \ \  _-/    \ \  __ \  \ \ \/\ \ \ \ \'/   \ \  __\   \ \ \-.  \  \/_/\ \/ \ \ \_\ \  \ \  __<   \ \  __\   
 \/\_____\  \ \_____\  \ \_\       \ \_\ \_\  \ \____-  \ \__|    \ \_____\  \ \_\\"\_\    \ \_\  \ \_____\  \ \_\ \_\  \ \_____\ 
  \/_____/   \/_____/   \/_/        \/_/\/_/   \/____/   \/_/      \/_____/   \/_/ \/_/     \/_/   \/_____/   \/_/ /_/   \/_____/ 
                                                                                                                                  
""")

time.sleep(3)

print("You walk into a hackathon and see a table with google swag.")
spc1 = str(input("Do you take it? [y/n]: "))

if spc1 == "y":
    print("You have taken the swag!")
    time.sleep(3)
    swag = 1
else:
    print("You didn't take the swag")
    swag = 0
print("As time goes hacking begins. You have an idea to ise a GCP API")
spc2 = str(input("Do you use API? [y/n]: "))
if spc2 == "y":
    print("You have used the API!")
    time.sleep(2)
    print("You begin to program the function in python.")
    time.sleep(2)
    print("You run into some runtime errors.")
    time.sleep(2)
    spc3 = str(input("Do you try to fix this error? [y/n]: "))
    if spc3 == "y":
        if swag == 1:
            print("You have some google swag. Maybe you can summon a Google Engineer to help!")
            time.sleep(1)
            print("You quickly arrange the swag into a G and say Google backwards. 'ELGOOG'")
            time.sleep(2)
            print("==============================================================")
            print("                         SUMMONING                            ")
            print("==============================================================")
            print("You must get a 5 or higher to successfully summon the engineer")
            print("If the program power level is bigger than yours you will fail ")
            s = int(random.randint(3,10))
            f = int(random.randint(1,5))
            print("Your power level is ", s)
            print("The program's power level is ", f)
            time.sleep(1)
            
            if f > s:
                print("The program's power level was too high. You couldn't solve the runtime error in time.")
                fixed = 0
            else:
                print("Your power level was higher than the program and you were able to fix the error in time.")
                fixed = 1
        else:
            print("You have to go through loads of documention to find out how to fix the error.")
            wait.sleep(1)
            print("It's taking hours to find the error you are having. You quickly look at Stack Exchange to search for the error.")
            time.sleep(1)
            print("==============================================================")
            print("                           FIXING                             ")
            print("==============================================================")
            print("You must get a 5 or higher to successfully fix the program    ")
            print("If the program power level is bigger than yours you will fail ")
            x = int(random.randint(1,8))
            y = int(random.randint(1,5))
            time.sleep(1)

            if y > x:
                print("The program's power level was too high. You were not able to fix the error.")
                fixed = 0
            else:
                print("Stack Exchange was able to pull through another time! The problem is fixed.")
                fixed = 1
    if fixed == 0:
        print("""

 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                          
""")
        wait.sleep(2)
        print("You were not able to solve the problem. You didn't finish your hack. Better luck next time!")
    else:
        print("""
        
__/\\\________/\\\_________________________________________________________________________________/\\\____        
 _\///\\\____/\\\/________________________________________________________________________________/\\\\\\\__       
  ___\///\\\/\\\/_____________________________________________________________/\\\________________/\\\\\\\\\_      
   _____\///\\\/__________/\\\\\_____/\\\____/\\\____________/\\____/\\___/\\_\///___/\\/\\\\\\___\//\\\\\\\__     
    _______\/\\\_________/\\\///\\\__\/\\\___\/\\\___________\/\\\__/\\\\_/\\\__/\\\_\/\\\////\\\___\//\\\\\___    
     _______\/\\\________/\\\__\//\\\_\/\\\___\/\\\___________\//\\\/\\\\\/\\\__\/\\\_\/\\\__\//\\\___\//\\\____   
      _______\/\\\_______\//\\\__/\\\__\/\\\___\/\\\____________\//\\\\\/\\\\\___\/\\\_\/\\\___\/\\\____\///_____  
       _______\/\\\________\///\\\\\/___\//\\\\\\\\\______________\//\\\\//\\\____\/\\\_\/\\\___\/\\\_____/\\\____ 
        _______\///___________\/////______\/////////________________\///__\///_____\///__\///____\///_____\///_____
 

        """)
        time.sleep(1)
        print("You were able to fix the problem and you won the hackathon!")

else:
    print("You don't use the API and you don't impress the judges. You don't win the hackathon.")
    time.sleep(1)
    print("""
    
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                          
    """)

