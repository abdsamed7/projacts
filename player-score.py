player1_score=0
player2_score=0
while player1_score<3 and player2_score<3:
    p1=input("player1:choose rock, paper or sciser:").lower() 
    p2=input("palyer2:choose rock , paper or sciser:").lower()
    if p1==p2:
        print("try again")
    elif (p1=='rock' and p2=='scissors') or (p1=='paper' and p2=='rock') or (p1=='scissors' and p2=='paper') :
     print("p1 win the round") 
     player1_score+=1
    elif (p2=='rock' and p1=='scissors') or (p2=='paper' and p1=='rock') or (p2=='scissors' and p1=='paper'):
     print("p2 win the round ")
     player2_score+=1
    else:
       print("ivalid input.please try again.")
print("final result:")
if player1_score==3:
   print("player1 win the game")
elif player2_score==3:
   print("player2 win the game")         

        