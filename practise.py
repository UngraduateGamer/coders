import random
print('''Computer's Turn ---
      Choose snake (s), water (w) and gun (g)
      ''')
user=input('''User's Turn ---
      Choose snake (s), water (w) and gun (g)
      ''')
randomnumber=random.randint(1,3)
if randomnumber==1:
    computer='s'
elif randomnumber==2:
    computer='w'
elif randomnumber==3:
    computer='g'

def gamewin():
    if computer==user:
        return None
    
    elif computer=="s":
        if user=='w':
            return 0
        elif user=='g':
            return 1
        
            
    elif computer=="w":
        if user=='s':
            return 1
        elif user=='g':
            return 0
        
            
    elif computer=="g":
        if user=='s':
            return 1
        elif user=='g':
            return 0
        
print("Computer Choose: ",computer)
print("User Choose:" ,user)
result=gamewin()
if result==None:
    print("MAtch was Tie")
elif result:
    print("User Won this Match")
else:
    print("computers win")
    

        