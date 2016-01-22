import random

def print_board(map):
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""

turnp1 = ""
turnai= ""
human = ""
ai = ""
winner = ""
cornermove = ""

done = False
moved = False

# Function to decide what sign human wants to play in the game
def decideSign():
    turnp1 = raw_input("What will you play? 'X' or 'O' ")
  
    while turnp1 not in ('x','o','X','O'):
        print "Wrong Choice!"
        turnp1 = raw_input("What will you play? 'X' or 'O' ")
    if turnp1 == 'x' or turnp1 == 'X':
        print "Ok, You are X.. \n"
        turnai = 'o'
    else:
        print "Ok, You are O.. \n"
        turnai = 'x'
    return turnp1.upper(), turnai.upper()

def check_done(human, ai, map):
    winner=""
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " ":
            winner=map[i][0]
            if winner==human:
                print human," won..!!\n"
                return True
            else:
                print ai," won..!!\n"
                return True
                 
        if map[0][i] == map[1][i] == map[2][i] != " ":
            winner=map[0][i]
            if winner==human:
                print human," won..!!\n"
                return True
            else:
                print ai," won..!!\n"
                return True
             
    if map[0][0] == map[1][1] == map[2][2] != " ":
         winner=map[0][0]
         if winner==human:
          print human," won..!!\n"
          return True
         else:
          print ai," won..!!\n"
          return True
         
    if map[0][2] == map[1][1] == map[2][0] != " ":
         winner=map[0][2]
         if winner==human:
          print human," won..!!\n"
          return True
         else:
          print ai," won..!!\n"
          return True
    
    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        winner="Draw"
        print "Hahaha....It is a Draw\n"
        return True
        








# Move generator's turn

def ai_move(human, ai, map):
 print "My Move.....!!"
 moved = False
 
 # Winning move check.
 for i in range(0,3):
        if map[i][0] == map[i][1] == ai != " ":
            if map[i][2] ==" ":
              map[i][2]=ai
              moved = True
              
              return   
        elif map[i][0] == map[i][2] == ai != " ":
            if map[i][1] ==" ":
              map[i][1]=ai
              moved = True
              
              return             
        elif map[i][1] == map[i][2] == ai != " ":
            if map[i][0] ==" ":
              map[i][0]=ai
              moved = True
              
              return            
 for i in range(0,3):
        if map[0][i] == map[1][i] == ai != " ":
            if map[2][i] ==" ":
              map[2][i]=ai
              moved = True
              
              return   
        elif map[0][i] == map[2][i] == ai != " ":
            if map[1][i] ==" ":
              map[1][i]=ai
              moved = True
              
              return             
        elif map[1][i] == map[2][i] == ai != " ":
            if map[0][i] ==" ":
              map[0][i]=ai
              moved = True
              
              return

 if map[0][0] == map[1][1] == ai != " ":
            if map[2][2] ==" ":
              map[2][2]=ai
              moved = True
              
              return   
 elif map[0][0] == map[2][2] == ai != " ":
            if map[1][1] ==" ":
              map[1][1]=ai
              moved = True
              
              return             
 elif map[1][1] == map[2][2] == ai != " ":
            if map[0][0] ==" ":
              map[0][0]=ai
              moved = True
              
              return             
         
 if map[0][2] == map[1][1] == ai != " ":
            if map[2][0] ==" ":
              map[2][0]=ai
              moved = True
              
              return   
 elif map[0][2] == map[2][0] == ai != " ":
            if map[1][1] ==" ":
              map[1][1]=ai
              moved = True
              
              return             
 elif map[1][1] == map[2][0] == ai != " ":
            if map[0][2] ==" ":
              map[0][2]=ai
              moved = True
              
              return
            
 # Blocking move check.
 
 for i in range(0,3):
        if map[i][0] == map[i][1] == human != " ":
            if map[i][2] ==" ":
              map[i][2]=ai
              moved = True
              
              return   
        elif map[i][0] == map[i][2] == human != " ":
            if map[i][1] ==" ":
              map[i][1]=ai
              moved = True
              
              return             
        elif map[i][1] == map[i][2] == human != " ":
            if map[i][0] ==" ":
              map[i][0]=ai
              moved = True
              
              return            
 for i in range(0,3):
        if map[0][i] == map[1][i] == human != " ":
            if map[2][i] ==" ":
              map[2][i]=ai
              moved = True
              
              return   
        elif map[0][i] == map[2][i] == human != " ":
            if map[1][i] ==" ":
              map[1][i]=ai
              moved = True
              
              return             
        elif map[1][i] == map[2][i] == human != " ":
            if map[0][i] ==" ":
              map[0][i]=ai
              moved = True
              
              return

 if map[0][0] == map[1][1] == human != " ":
            if map[2][2] ==" ":
              map[2][2]=ai
              moved = True
              
              return   
 elif map[0][0] == map[2][2] == human != " ":
            if map[1][1] ==" ":
              map[1][1]=ai
              moved = True
              
              return             
 elif map[1][1] == map[2][2] == human != " ":
            if map[0][0] ==" ":
              map[0][0]=ai
              moved = True
              
              return             
         
 if map[0][2] == map[1][1] == human != " ":
            if map[2][0] ==" ":
              map[2][0]=ai
              moved = True
              
              return   
 elif map[0][2] == map[2][0] == human != " ":
            if map[1][1] ==" ":
              map[1][1]=ai
              moved = True
              
              return             
 elif map[1][1] == map[2][0] == human != " ":
            if map[0][2] ==" ":
              map[0][2]=ai
              moved = True
              
              return

# Block the fork. If human selects center square, mark any random corner which is open.
            
 if map[1][1]==human:
            while moved != True:
             cornerlist=[1,3,7,9]
             
             cornermove= random.choice(cornerlist)

       
             if cornermove <=9 and cornermove >=1:
                Y = cornermove/3
                X = cornermove%3
                if X != 0:
                    X -=1
                else:
                     X = 2
                     Y -=1
                    
                if map[Y][X] == " ":
                    map[Y][X] = ai
                    moved = True
                    
                    return
                


# Mark the center square if open.
                
 if map[1][1] == " ":
    map[1][1]=ai
    moved = True
    
    return 
# Block the fork. If human picks any side's middle square, mark any one of the corners of the square which is open.

 if map[0][1]== human:
     if map[0][0]== " ":
        map[0][0]=ai
        
        moved = True
        return
     elif map[0][2]==" ":
        map[0][2]=ai
        
        moved = True
        return
 if map[1][0]== human:
     if map[0][0]== " ":
        map[0][0]=ai
        
        moved = True
        return
     elif map[2][0]==" ":
        map[2][0]=ai
        
        moved = True
        return
 if map[2][1]== human:
     if map[2][0]== " ":
        map[2][0]=ai
        
        moved = True
        return
     elif map[2][2]==" ":
        map[2][2]=ai
        
        moved = True
        return
 if map[1][2]== human:
     if map[2][2]== " ":
        map[2][2]=ai
        
        moved = True
        return
     elif map[0][2]==" ":
        map[0][2]=ai
        
        moved = True
        return   


 # Block the fork. If human selects a corner and center square is taken by the AI.

 if map[1][1] == ai and map[0][0]== human:
     if map[0][1]== " ":
        map[0][1]=ai
        
        moved = True
        return
     elif map[1][0]==" ":
        map[1][0]=ai
        
        moved = True
        return
 if map[1][1] == ai and map[2][2]== human:
     if map[2][1]== " ":
        map[2][1]=ai
        
        moved = True
        return
     elif map[1][2]==" ":
        map[1][2]=ai
        
        moved = True
        return
 if map[1][1] == ai and map[2][0]== human:
     if map[1][0]== " ":
        map[1][0]=ai
        
        moved = True
        return
     elif map[2][1]==" ":
        map[2][1]=ai
        
        moved = True
        return
 if map[1][1] == ai and map[0][2]== human:
     if map[0][1]== " ":
        map[0][1]=ai
        
        moved = True
        return
     elif map[1][2]==" ":
        map[1][2]=ai
        
        moved = True
        return    
    
    
    

                
         
# AI will pick any random legal move if no conditions above are valid.
    
 while moved != True:  
    pos= random.randrange(0,9)

       
    if pos <=9 and pos >=1:
                Y = pos/3
                X = pos%3
                if X != 0:
                    X -=1
                else:
                     X = 2
                     Y -=1
                    
                if map[Y][X] == " ":
                    map[Y][X] = ai
                    moved = True
                    
                   
                
            
# Human's move

def human_move(human, map):
    
 moved = False
 while moved != True:
        print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
        print "7|8|9"
        print "4|5|6"
        print "1|2|3 \n"
        print

        try:
            pos = input("Select: ")
            if pos <=9 and pos >=1:
                Y = pos/3
                X = pos%3
                if X != 0:
                    X -=1
                else:
                     X = 2
                     Y -=1
                    
               
                if map[Y][X] != " ":
                    print "Sorry, this position is already taken...... \n "
                if map[Y][X] == " ":
                    map[Y][X] = human
                    moved = True   
                
            
        except:
            print "You need to add a numeric value"

 # Function called if human is 'X'
 
def man_first(human, ai, map):
    done=False
    while done != True:
        print "Your move...?\n"
        human_move(human, map)
        print_board(map)
        print "\n"
        done=check_done(human, ai, map)
        
        if done == True:
            break
        else:
            pass
        ai_move(human, ai, map)
        print_board(map)
        print "\n"
        done=check_done(human, ai, map)
        
        if done == True:
            break
        else:
            pass

 # Function called if AI Move Generator is 'X'
 
def ai_first(human, ai, map):
    done=False
    while done != True:
        ai_move(human, ai, map)
        print_board(map)
        print "\n"
        done=check_done(human, ai, map)
        
        if done == True:
            break
        else:
            pass
        print "Your move...?\n"
        human_move(human, map)
        print_board(map)
        print "\n"
        done=check_done(human, ai, map)
        
        if done == True:
            break
        else:
            pass
       
  
    
        
def main_function(human, ai):
    
    map = [[" "," "," "],
           [" "," "," "],
           [" "," "," "]]
    done = False
    moved = False
    print "Welcome to Tic Tac Toe Move Generator.."
    print_board(map)
    print "\n"
    a = decideSign()
    human = a[0]
    ai = a[1]
    print "X always plays first.....!!! \n"
   
    if human == 'X':
         
         man_first(human, ai, map)
        
    elif human == 'O':
           
         ai_first(human, ai, map)



        
playagain = 'Y'
# Game play again logic

while playagain == 'Y':        
  main_function(human, ai)
  playagain  = raw_input("Play again?  'Y' or 'N' ")
  while playagain not in ('y','Y','n','N'):
        print "Wrong Choice!"
        playagain = raw_input("Play again?  'Y' or 'N' ")
  if playagain == 'y' or playagain == 'Y':
        playagain=playagain.upper()   
  elif playagain == 'n' or playagain == 'N':
        playagain=playagain.upper()
        print "---THE END---"
        

