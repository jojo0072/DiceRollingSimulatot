import random
import os
def main():
    print("Dice Rolling Simulator\n")
    while True:
        num_dices=input("How many dices do you want to roll?: ")
        num_sides=input("How many sides should the dice have?: ")
        if not(num_dices.isdigit() and num_sides.isdigit()) or not(int(num_dices)>0 and int(num_sides)>3):
            print("Invalid Input!")
        else:
            break
    num_dices, num_sides=int(num_dices), int(num_sides)         
    roll_dices(num_dices, num_sides)
    play_again=input("Enter to play again: ")
    if play_again == "":
        os.system('clear')
        main()    
def roll_dices(num_dices, num_sides):
    x=0
    stats=[]
    while x < num_dices:
        x+=1
        res=random.randint(1, num_sides)
        print(f"{num_sides}-sided dice: {res}")
        stats.append(res) 
    dices_stats(stats, num_dices, num_sides)    
def dices_stats(stats, num_dices, num_sides):
    print("\nStatistics: ")
    print(f"\nYou rolled {num_dices}-times")    
    for y in range(1, num_sides+1):
        if y in stats:
            k=stats.count(y)
            res=k / len(stats)    
            print(f"Probability of {y}: {res*100:.2f}%")
    print("Average roll:", sum(stats)//len(stats), "\n")
main()    