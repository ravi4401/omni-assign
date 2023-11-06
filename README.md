print("rock...")
print("scissors...")
print("paper...")

p1=input("enter your play: ")
p2=input("enter your play: ")

if p1=="rock" and p2=="paper":
    print("p2 wins! game")
elif p1=="paper" and p2=="scissors":
    print("p2 wins! game")
elif p1=="rock" and p2=="scissors":
    print("p1 wins game!")
elif p1=="paper" and p2=="rock":
    print("p1 wins game!")
elif p1=="scissor" and p2=="paper":
    print("p1 wins game")
elif p1=="scissor" and p2=="rock":
    print("p2 wins game")
else:
    print("draw")
