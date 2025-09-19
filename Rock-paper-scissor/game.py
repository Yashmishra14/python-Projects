"""
Workflow of project:
1-input from user(Rock,paper,scissor)
2-computer choice(computer will choose redomly not conditionally)
3-result print 


A-Rock
Rock-Rock=tie
Rock-paper=paper win
Rock-scissor=Rock win

B-paper
paper-paper=tie
paper-rock=paper win
paper-scissor=scissor win

c-scissor
scissor-scissor=tie
scissor-paper=scissor win
scissor-Rock=Rock win

"""
import random

item_list=["Rock","paper","scissor"]
user_choice=input("Enter Your Move=Rock,paper,scissor=")
com_choice=random.choice(item_list)

print(f"User choice ={user_choice},Computer choice={com_choice}")

if user_choice==com_choice:
    print("match tie better luck")

elif user_choice=="Rock":
    if com_choice=="paper":
        print("paper wins:Computer")
    else:
        print("You win")

elif user_choice=="paper":
    if com_choice=="scissor":
        print("Computer Win")
    else:
        print("You win")

elif user_choice=="scissor":
    if com_choice=="paper":
        print("scissor cute paer,you win")
    else:
        print("computer win")


