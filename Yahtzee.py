# Author: Maryam Taj
# Name of Program: Yahtzee
# Description of Program: This program simulates a game of Yahtzee, wherin the user tries to gain the highest number of points through various combinations
# of their dice.

def Yahtzee():
    import random,sys
    # Import pre-built libraries of code
    print("Welcome to the ever-reliable cure for boredom, Yahtzee!")
    # Introduction

    pL = {}
    # Create empty dictionary 

    for x in range(16,1,-1):
    # Beginning at x = 16, and decreasing by 1 until x = 2, the following code repeats a total of 15 times. Thus, the player can finalize answers for all 15 combinations. 
        print("Let's roll the dice.")

        dice = []
        print("-"*10)
        for i in range(1,6):
            x = random.randint(1,6)
            dice.append(x)
            print("Dice",i,":",dice[i-1])
        print("-"*10)
    # Computer prints green statement. Creates empty list. Prints '----------'. Beginning at i = 1, until i = 5, it repeats the following code for each die. First, it
    # randomly generates a number between 1 and 6. It appends each number to the dice list. Then, it alerts the user of what they rolled for each die. Finally, it
    # print '----------'.

        for i in range(3,1,-1):
            Userchoice = input("Which dice would you like to roll again? Type [x y], in which x and y represent the dice that you would like to change. Type [0] to change\
                               nothing.").split()
    # Beginning at i = 3 and decreasing by 1 until i = 2, it repeats the following code a total of 2 times. First, it asks the user about re-rolls. It splits the user's
    # response into individual string statements within a list. For instance, '0 1 2' becomes ('0','1','2'). This is convenient because user can ask to re-roll mutliple
    # dice simultaneously. 

            if '0' in Userchoice: break
    # If user responds 0, implying no re-rolls, the computer ignores the indented code below until 'frequency = [0] * 7
            
            for i in range(5,0,-1):
                if str(i) in Userchoice:
                    dice[i-1] = random.randint(1,6)
                    print("You rolled",dice[i-1],"for Dice",i)
    # Beginning at i = 5 and decreasing by 1 until i = 1, the following code repeats a total of 5 times. Computer checks whether the user responded the integer i. If yes,
    # it randomly generates a new number for that die and alters the value in the original list.

            print("-"*10)
            for i in range(1,6): print("Dice",i,":",dice[i-1])
            print("-"*10)
    # Print '----------'. Beginning at i = 1 until i = 5, the computer notifies the user of their final rolls for each die.

        frequency = [0]*7
        for i in dice: frequency[i] += 1
    # Create a list titled, frequency, with 7 0's. For each value in the dice list, increase frequency's value by 1 for the corresponding position. For instance, if
    # Dice 1 rolled 2, then the frequency of 2 = 0 + 1 = 1.

        def mode(dice):
            One = frequency[1]
            Two = 2 * frequency[2]
            Three = 3 * frequency[3]
            Four = 4 * frequency[4]
            Five = 5 * frequency[5]
            Six = 6 * frequency[6]
            return One,Two,Three,Four,Five,Six
        a,b,c,d,e,f= mode(dice)
    # Using the frequency list, this function evaluates the frequency of each dice value and returns its sum. For example, if the user has rolled 5 2's. Then,
    # their total sum for 2's is 10.

        def smode(dice):
            if all( x not in pL for x in ['1','2','3','4','5','6']):
                Sum,Bonus = 0,0
            else:
                Sum = sum(mode(dice))
                if Sum>=63:
                    Bonus = 35
                else:
                    Bonus = 0
            return Sum,Bonus
        g,h = smode(dice)
    # This function returns the sum and bonus values. If 1,2,3,4,5 and 6 are not in the original dictionary, pL, then computer cannot calculate the sum or bonus. The
    # six values must be finalized first. If they are in pL, adding their values provides the sum. If the sum exceeds 63 points, they gain a bonus 35 points. Otherwise,
    # bonus = 0.
                
        def fmode(dice):
            if max(frequency) == 3:
                kind3 = sum(dice) 
                kind4,y = 0,0
            elif max(frequency) == 4:
                kind3,kind4 = sum(dice),sum(dice) 
                y = 0
            elif max(frequency) == 5:
                kind3,kind4 = sum(dice),sum(dice)
                y = 50
            else:
                kind3,kind4,y = 0,0,0
            return (kind3,kind4,y)
        i,j,k = fmode(dice)
    # Using the freqency list, this function detects three of a kind, four of a kind, or yahtzee and returns their scores. If a dice value has a frequency of 3, the
    # three of a kind score is the sum of the dice. Four of a kind and yahtzee scores are 0. If a dice value has a frequency of 4, then the three of a kind and four
    # of a kind scores are the sum of the dice. Yahtzee score is 0. If a dice value has a frequency of 5, then three of a kind and four of a kind scores are the sum
    # of the dice, and yahtzee score is 50 points.
            
        def fhmode(dice):
            if 2 in frequency and 3 in frequency: return 25
            else: return 0
    # Using the frequency list, this function detects full house and returns its score. If the same dice value rolled twice and another, thrice, the full house score
    # is the sum of all the dice values. If this didn't occur, the full house score is 0.

        def ssmode(dice):
            if 1 in dice and 2 in dice and 3 in dice and 4 in dice: return 30
            elif 2 in dice and 3 in dice and 4 in dice and 5 in dice: return 30
            elif 3 in dice and 4 in dice and 5 in dice and 6 in dice: return 30
            else: return 0
    # This function detects small straight and returns its score. If user rolled 1,2,3, and 4, then their small straight score is 30. Likewise, if they rolled any
    # other four consecutive numbers, their small straight score is 30. Else, the score is 0.

        def lsmode(dice):
            if 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice: return 40
            elif 2 in dice and 3 in dice and 4 in dice and 5 in dice and 6 in dice: return 40
            else: return 0
    # This function detects large straight and returns its score. If user rolls any five consecutive numbers, their large straight score is 40. Else, it is 0.

        def cmode(dice): return sum(dice)
    # This function returns the sum of all the dice. 
       
        tL = {'1':a,'2':b,'3':c,'4':d,'5':e,'6':f,'Sm':g,'Bn':h,'3k':i,'4k':j,'Y':k,'Fh':fhmode(dice),'Ss':ssmode(dice),'Ls':lsmode(dice),'Ch':cmode(dice)}
        print("Temporary Scoreboard:")
        print(tL)
    # tL is a list which provides the user an overview of their potential scores. For instance, if user rolled 5 3's, they could choose to gain 50 points (yahtzee) or
    # 15 points (3's). The scoreboard conveys this to them.

        while True:
            User = input("What combination would you like to lock in? Type a right side value (#1,#2,Ls,Ss...) to indicate your preference. Remember, once locked, you \
                    cannot change your score for that combination. Choose wisely.")
    # Computers asks user to lock in a value of their choice. 

            if User not in pL:
                if User == 'Sm' or User == 'Bn':
                    if all( x not in pL for x in ['1','2','3','4','5','6']):print("Lock in your 1,2,3,4,5 and 6's first.")
                    else:
                        pL[User] = tL[User]
                        break
                else:
                    pL[User] = tL[User]
                    break
            else:
                print("You already locked in the score for this value. Try again.")
    # If user responds with a value that is not in the original dictionary, pL, and therefore, has not been locked in, computer adds the value to the dictionary. However,
    # if the value was 'Sm' - Sum - or 'Bn' - Bonus - then they cannot be locked in before finalizing the ones,twos,threes,fours,fives and sixes. Furthermore, if the
    # value is already in pL, the user cannot lock it again.
       
        print("Permanent Scoreboard",end = ":")
        print(pL)
        TotalScore = sum(pL.values())
        print("TotalScore",TotalScore,sep = ":")
    # Computer shows the official scoreboard and provides the total sum of all the points.
    return

def CootieCatcher():
    import time,sys
    # Bring in libraries of pre-built code
    while True:
        Introduction=print('Double, double toil and trouble. Fire burn and caldron bubble. Welcome, my friend, to the world of mysticism. Let us discover your fortune.')                                                                                                    
        while True:
            Userchoice=input('Choose a colour. "RED", "BLUE", "GREEN", or "YELLOW".')
            # User chooses one of the four given colours
            Colours=['RED','BLUE','GREEN','YELLOW']
            # I created a list that stores all the colours, so instead of writing "if userchoice!= 'Red' and userchoice!='Blue' and userchoice!='Green' and userchoice
            # !='Yellow'", I can just write if userchoice not in Colours
            def IncorrectResponse(x):
                    print('Tsk,tsk. You are making me impatient. Remember, respond in uppercase letters and choose from the given options.')
            # I created a function, IncorrectResponse, that prints 'Tsk,tsk....'. This way, I do not have to write the same sentence repeatedly, but I can simply call the
            # function again
            if Userchoice not in Colours:
               IncorrectResponse(Userchoice)
            # if the user types something other than the four options in the Colours list, the 'Tsk,tsk...' statement appears, and they must choose from the four colours
            # again
            else:
                print('You have selected',Userchoice+'.')
            # if the user types one of the four uppercase options, the green statement appears
                Confirmation=input('Print [Y] to confirm your choice, or [N] to change.')
                if Confirmation=='Y':
                    print('Excellent!I foresee greatness in your future.')
                    for i in range(0,len(Userchoice)):
                        time.sleep(0.5)
                        print(Userchoice[i])   
                    break
            # if user confirms their choice and types 'Y', their chosen colour pops up letter by letter, after 0.5 second intervals
                elif Confirmation=='N': 
                    print('Try again, but know that this change of heart was preordained.')
            # if user wants to change their choice, the green statement appears and they must choose from the four colours above again
                else:
                    print(IncorrectResponse(Userchoice))
            # if user types anything other than 'Y' or 'N', the 'Tsk,tsk..." pops up and they must choose from the four colours above again        

        Length=len(Userchoice)
            # the variable, Length, is equal to the user's colour's length (number of letters)
        def YResponse(x):
            print("Lovely. Let's proceed.")
            for i in range(1, x+1):
                time.sleep(0.5)
                print(i)
            # the function, YResponse, is the new procedure everytime the user confirms their choice. The 'Lovely..' statement appears and the computer counts up to the
            # user's chosen number with 0.5 second intervals
        def NResponse(x):
            print('If you must change, do so, but time is ticking, my friend.')
            # the function, NResponse, is the new procedure everytime the user wants to change their choice. The green statement appears
        def EResponse(x):
            print('No time for mistakes. Try again, quickly!')
            # the function, EResponse, is the new procedure everytime the user types in anything other than 'Y' or 'N'. The green statement appears
        while True:    
            if Length%2==0:
                Userchoice=int(input('Choose a number between 1,2,5 and 6.'))
            # if the user's colour had an even number of letters, they must choose from the following numbers
                ENumbers=[1,2,5,6]
                if Userchoice not in ENumbers:
                   IncorrectResponse(Userchoice)
            # if the user types anything outside the ENumbers list, the IncorrectResponse function happens. The 'Tsk,tsk..' statement appears and they must choose from the
            # four numbers again
                else:
                    print('You have selected',str(Userchoice)+'.')
            # if the user types in 1,2,5 or 6, the computer repeats their answer to them
                    Confirmation=input('Print [Y] to confirm your choice, [N] to change.')
                    if Confirmation=='Y':
                        YResponse(Userchoice)
                        break
            # if the user confirms their answer, the YResponse function happens, with the 'Lovely...' statement, and the counting up to the number
                    elif Confirmation=='N':
                        NResponse(Userchoice)
            # if the user wants to change their choice, the NResponse function happens, with the 'If you must...' statement, and the user must choose from the four
            # numbers again
                    else:
                        EResponse(Userchoice)
            # if the user types anything other than 'Y' or 'N', the EResponse function happens, with the 'No time..' statement, and the user must choose from the four
            # numbers again
            else:
                Userchoice=int(input('Now,choose a number between 3,4,7 and 8.'))
            # if the user's colours had an odd number of letters, the user must choose from the four numbers above
                ONumbers=[3,4,7,8]
                if Userchoice not in ONumbers:
                    IncorrectResponse(Userchoice)
            # if the user types anything outside the ONumbers list, the IncorrectResponse function happens. The 'Tsk,tsk..' statement appears and they must choose from the
            # four numbers again 
                else:
                    print('You have selected',str(Userchoice)+'.')
            # if the user types in 3,4,7 or 8, the computer repeats their answer to them
                    Confirmation=input('Print [Y] to confirm your choice, [N] to change.')
                    if Confirmation=='Y':
                        YResponse(Userchoice)
                        break
            # if the user confirms their choice, the YResponse function happens, with the 'Lovely..' statement, and the counting up to the number
                    elif Confirmation=='N':
                        NResponse(Userchoice)
            # if the user wants to change their choice, the NResponse function happens, with the 'If you must...' statement, and the user must choose from the four
            # numbers again
                    else:
                        EResponse(Userchoice)
            # if the user types in anything other than 'Y' or 'N', the EResponse function happens, with the 'No time..' statement, and the user must choose from the four
            # numbers again

        if int(Userchoice)%2==0:
            Userchoice=int(input('Last step before you discover your fate. Pick another number between 1,2,5 and 6.'))
            EFortunes={1:'when the ground turns liquid, the false leader shall bring an age of anarchy and the rise of mankind.',2:'once the mark of the one becomes \
                    the mark of many, a secret meeting shall bring new aggressions.',5:'when the day is longest, your young one shall cause a reunion of friends.',6:\
                    'once the dark one returns, children of darkness shall bring an aeon of fortune.'}
            # If the user's chosen number was even, they choose from 1,2,5 and 6. Each number has a corresponding fortune
            print('Your fortune reads,', EFortunes[Userchoice])
            # the computer reads the number's corresponding fortune to the user
        else:
            Userchoice=int(input("We're almost there. Pick another number between 3,4,7, and 8."))
            OFortunes={3:'upon the day lightning strikes twice, a proposition shall bring forth an era of sorrow.',4:'upon the day when the shrouded is revealed,\
                    a woman of grey shall cause a strengthening of bonds and an age of failing crops.',7:'when air turns to fire, the foreign one shall bring a country\
                    doom.',8:'when the brother becomes the father, a man clad in green shall mark an age of justice and an era of favorable crop yields.'}
            # if the user's chosen number was odd, they choose from 3,4,7 and 8. Each number has a corresponding fortune
            print('Your fortune reads,',OFortunes[Userchoice])
            # the computer reads the number's corresponding fortune to the user

        while True:
            Replay=input('Would you like to read your fortune again? Type [Y] to begin the process again, or [N] to leave.')
            if Replay=='Y':
                print('Very well.')
                break
            # if the user types 'Y' to play the game again, the game restarts from the beginning
            elif Replay=='N':
                print('Farewell, then, and heed my words. Those who ignore, repent.')
                sys.exit()
            # if the user types 'N' to end the game, the game ends
            else:
                print('Speak louder, my friend.')
            # if the user types anything other than 'Y' or 'N', the 'Speak...' statement appears and the user must answer the 'Would you like...' question again
            return

def Magic8Ball():
    import random
    #Import random module which will randomly output a number from 1 to 20, with 1 and 20 included
    print('Welcome to the 21st century Magic 8-Ball.')
    #Introduction

    while True:
        Userchoice = input('What is your question today?')
        #Computer asks user to type their question                                                                                                                                                 
                                                                                                                                                           
                                                                                                                                                           
        print("I see.. Well, you must realize that given our advances in technology, the future is entirely calculable, \
        as inevitable as mathematics. An advanced grasp of probability mapped onto a thorough apprehension of human \
        psychology and the known dispositions of any given individual can reduce the number of variables that influence \
        life's outcomes considerably. But, to answer your question..")
        #Computer discusses technology and mathematics in predicting the future
        #Backslashes are equivalent to an 'Enter' and move code to a new line, so it fits on one screen. Remove them before
        #running the code because they add unnecessary space to the code
                                                                                                                                                   
                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                   
        Dictionary = {1: 'You may rely on it.', 2: 'It is certain.', 3: 'It is decidedly so.', 4: 'Yes', 5: 'Without a doubt.', \
                      11: 'My sources say no.', 12: "Don't count on it.", 13: 'Very doubtful.', 14: 'Outlook not so good.', \
                      15: 'My reply is no.', 6: 'As I see it, yes.', 7: 'Most likely.', 8: 'Yes, definitely.', 9: 'Outlook good.', \
                      10: 'Signs point to yes.', 16: 'Ask again later.', 17: 'Better not tell you now.', 18: 'Concentrate and ask again.', \
                      19: 'Cannot predict now.', 20: 'Reply hazy, ask again.'}
        #Computer's possible answers (string values) coincide with keys (integers). Dictionaries are more helpful to store strings as integers than lists
        #because lists rely on position. print(List[20]) prints the string in position 20. However, in dictionaries, it prints the string next to integer 20.
        #This gives the coder more flexibility as they can refer to strings based on their keys (integer), rather than counting their position every time.

                                                                                                                                          
        x = random.randint(1,20)
        print(Dictionary[x])
        #Assign x the value of the random integer output. For future reference, use random.choice[Dictionary], which randomly chooses a string from the dictionary.
        #This skips the x=random.randint(1,20) step and print(Dictionary[x]) step. 
        #Computer answers the user's question. It print the value assigned to x in the dictionary 

        Replay = str(input('Would you like to play again?'))
        #Computer asks the user if they would like to play again?

        if Replay == 'Yes':                                                                                                                                
            print("I see that you are beginning to understand the world's predictability. As they say, the universe is rarely so lazy so as to \
            indulge in coincidences. There is a pattern to everything. Find the pattern, and you have the world at your fingertips. But I digress...")
        #If user replies 'Yes', the code underneath the while True statement begins again

        if Replay == 'No':                                                                                                                                 
            print('Very well.')
            break
        #If user replies 'No', the computer responds and breaks out of the while True loop, concluding the code
        #All quotations originate from Sir Arthur Canon Doyle's work, Sherlock Holmes
            return

def RockPaperScissors():
    while True:
        import random,sys
        print("Welcome to the Virtual Rock-Paper-Scissors game! This is the perfect addition for quarantine-bound folks!")
        #Introduction
        while True:
            userchoice=int(input("Please select [1] for 'Rock', [2] for 'Paper' or [3] for 'Scissors' ."))
            #Program asks user to select 1 for 'Rock', 2 for 'Paper' or 3 for 'Scissors'
            if userchoice == 1:
                print("You selected 'Rock'.")
                #If user selects 1 for 'Rock', the green statement informs them of their choice and exits the loop
                break
            elif userchoice == 2:
                print("You selected 'Paper'.")
                #If user selects 2 for 'Paper', the green statement informs them of their choice and exits the loop
                break
            elif userchoice == 3:
                #If user selects 3 for 'Scissors', the green statement informs them of the choice and exits the loop
                print("You selected 'Scissors'.")                                                            
                break                                                                                                          
            else:
                print("Invalid answer. Try again.")
                #If user types any integer other than 1,2, or 3 the green statements appears and restarts the loop, asking them to select either 1 or 2 

        while True:
            confirmation = input("Type [Y] to confirm or [N] to change your choice.")
            #Program asks user to confirm their choice. Type 'Y' for confirmation or 'N' for refutation
            if confirmation == "Y":
                print("Excellent!")
                #If user types 'Y', the program outputs 'Excellent!' and exits the loop   
                break
            elif confirmation == "N":                                                                       
                if userchoice == 1:
                    userchoice=int(input("Choose between [2] for 'Paper' or [3] for 'Scissors'."))
                    #If user types 'N' and their initial choice was 1 for 'Rock', the program asks them to choose between remaining options; 2 for 'Paper' or 3
                    #for 'Scissors'
                    if userchoice == 2:
                        userchoice = 2
                        print( "You selected 'Paper'.")
                        #If user selects 2 for 'Paper', the green statement appears and the program exits the loop 
                        break
                    if userchoice == 3:
                        userchoice = 3
                        print("You selected 'Scissors'.")
                        #If user selects 3 for 'Scissors', the green statement appears and the program exits the loop
                        break
                if userchoice == 2:
                    userchoice=int(input("Choose between [1] for 'Rock' or [3] for 'Scissors'."))
                    #If user's initial choice was 2 for 'Paper', the program asks them to choose between 1 for 'Rock' and 3 for 'Scissors'
                    if userchoice == 1:
                        userchoice = 1
                        print("You selected 'Rock'.")
                        #If user selects 1 for 'Rock', the green statement appears and the program exits the loop
                        break
                    if userchoice == 3:
                        userchoice = 3
                        print("You selected 'Scissors'.")
                        #If user selects 3 for 'Scissors', the green statement appears and the program exits the loop
                        break
                if userchoice == 3:
                    userchoice=int(input("Choose between [1] for 'Rock' or [2] for 'Paper'."))
                    #If user's initial choice was 3 for 'Scissors', the program asks them to choose between 1 for 'Rock' and 2 for 'Paper'
                    if userchoice == 1:
                        userchoice = 1
                        print("You selected 'Rock'.")
                        #If user selects 1 for 'Rock', the green statement appears and the program exits the loop
                        break
                    if userchoice == 2:
                        userchoice = 2
                        print("You selected 'Paper'.")
                        #If user selects 2 for 'Scissors', the green statement appears and the program exits the loop
                        break
            else:
                #If user types any letter other than 'Y' or 'N', the program prints the green statement and restarts the loop, asking them to confirm their choice
                print("Error. Please try again.")
        
        Computer = random.randint(1,3)
        if Computer == 1:
            print("The computer generated 'Rock'.")
            #If computer generates 1, the green statement appears
            if Computer == userchoice:
                print("It's a tie.")
                #If computer and user both selected 1, the green statement appears and alerts the user of the tie
            if Computer != userchoice:
                print("Oops. You lost. Better luck next time!")
                #If computer selected 1 and user selected 2 or 3, the green statement appears and the user loses
        elif Computer == 2:
            print("The computer generated 'Paper'.")
            #If computer generates 2, the green statement appears
            if Computer == userchoice:
                print("It's a tie.")
                #If computer and user selected 2, the green statement appears and informs the user of the tie
            if Computer != userchoice:
                print("Congratulations! You won!")
                #If computer selected 2 and user selected 1 or 3, the green statement appears and the user wins 
        else:
            print("The computer generated 'Scissors.")
            #If computer generates anything other than 1 or 2 - in other words, when it generates 3 - the green statement appears
            if userchoice == 1:
                print("Congratulations!You won!")
                #If computer generates 3 and the user selects 1, the user wins
            if userchoice == 2:
                print("Oops. You lost. Better luck next time!")
                #If computer generates 3 and the user selects 2, the user loses
            if userchoice == 3:
                print("It's a tie.")
                #If computer and user selected 3, it is a tie
                
        while True:
            replay = input("Would you like to play again? Type [Y] for 'Yes' or [N] for 'No'.")
            #The program asks the user if they would like to play again, accepting 'Y' or 'N' for an answer
            if replay == "Y":
                print("Loading....")
                #If user types 'Y', the green statement appears. The program exits the loop so it doesn't repeat the replay question and after waiting 1 second, the
                # game restarts again
                import time
                time.sleep(1)
                break
            elif replay == "N":
                print("Thanks for playing!")
                #If user types 'N', the green statement concludes the game and exits the inner loop, preventing the replay question from reappearing. It then exits the
                # outer loop, preventing the game from restarting
                sys.exit()
            else:
                print("Invalid answer. Please try again.")
                #If user types any other piece of string besides Y or N, the green statement appears and the replay loop begins again
                return

def HeadsorTails():
    while True:
        import random
        print("Welcome to the Magnificent Coin Toss Simulator!")
        #Introduction
        while True:
            userchoice=int(input("Please select [1] for 'Heads', or [2] for 'Tails'."))
            #Program asks user to select 1 for 'Heads or 2 for 'Tails'
            if userchoice == 1:
                print("You have selected 'Heads'.")
                #If user selects 1 for 'Heads', the green statement informs them of their choice and exits the loop
                break
            elif userchoice == 2:
                print("You have selected 'Tails'.")
                #If user selects 2 for 'Tails', the green statement informs them of their choice and exits the loop
                break
            else:
                print("Invalid answer. Try again.")
                #If user types any integer other than 1 or 2, the green statements appears and restarts the loop, asking them to select either 1 or 2 

        while True:
            confirmation = input("Type [Y] to confirm or [N] to change your choice.")
            #Program asks user to confirm their choice. Type 'Y' for confirmation or 'N' for refutation
            if confirmation == "Y":
                print("Excellent!")
                #If the user types 'Y', the program outputs 'Excellent!' and exits the loop   
                break
            elif confirmation == "N":                                                                       
                if userchoice == 1:
                    #If user types 'N' and their initial choice was 1 for 'Heads', the program changes their choice to 2 for 'Tails', prints the green statement and
                    # exits the loop
                    userchoice = 2
                    print("Correction. You selected 'Tails'.")
                    break
                if userchoice == 2:
                    #If user types 'N' and their initial choice was 2 for 'Tails', the program changes their choice to 1 for 'Heads', prints the green statement and
                    # exits the loop
                    userchoice = 1
                    print("Correction. You selected 'Heads'.")
                    break
            else:
                #If user types any letter other than 'Y' or 'N', the program prints the green statement and restarts the loop, asking them to confirm their choice
                print("Error. Please try again.")
                
        print("Now, the Magnificent Coin Toss Simulator flips the coin...ba-dum, ba-dum,ba-daaaa!!!")
        #The program prints the green statement
        Coin=random.randint(1,2)
        #The random coin flip simulator generates either 1 or 2, where 1 represents 'Heads' and 2 represents 'Tails' 
        if Coin == 1:
            print("The Magnificent Coin Toss Simulator generated 'Heads'.")
            #If the random coin flip simulator generates 1, the green statement appears
            if Coin == userchoice:
                print("Congratulations!You won!")
                #If the random coin flip simulator generates 1 and the user also selected 1 as their final choice, the green statement appears and the user wins
            if Coin != userchoice:
                print("Oops. You lost. Better luck next time!")
                #If the random coin flip simulator generates 1 and the user selected 2 as their final choice, the green statement informs them that they lost
        if Coin == 2:
            print("The Magnificent Coin Toss Simulator generated 'Tails'.")
            #If the random coin flip simulator generates 2, the green statement appears 
            if Coin == userchoice:
                print("Congratulations!You won!")
                #If the random coin flip simulator generates 2, and the user's final choice was also 2, the green statements informs them that they won
            if Coin != userchoice:
                print("Oops. You lost. Better luck next time!")
                #If the random coin flip simulator generates 2, and the user's final choice was 1, the green statement informs them that they lost

        replay = input("Would you like to play again? Type [Y] for 'Yes' or [N] for 'No'.")
        #The program asks the user if they would like to play again, accepting 'Y' or 'N' for an answer
        if replay == "N":
            print("Thanks for playing!")
            #If user types 'N', the green statement concludes the game and exits the loop, preventing the game from restarting
            break
        if replay == "Y":
            print("Loading....")
            #If user types 'Y', the green statement appears and after waiting 1 second, the game restarts again
            import time
            time.sleep(1)
            return

while True:
    Question = input("Welcome to the game arcade! What would you like to play today? Mind-boggling Yahtzee, multicolored Cootie Catcher, mystical Magic 8-Ball,\
                 aggressive Rock-Paper-Scissors or the reliable Heads or Tails? Have your pick!")
    # Computer asks user about preferred game 
    if Question == 'Yahtzee':
        Yahtzee()
    # If user types yahtzee, computer calls the yahtzee function, and starts the game
    elif Question == 'Cootie Catcher':
        CootieCatcher()
    # If user types Cootie Catcher, computer calls the CootieCatcher function, and starts the game    
    elif Question == 'Magic 8-Ball':
        Magic8Ball()
    # If user types Magic 8-Ball, computer calls the Magic8Ball function, and starts the game
    elif Question == 'Rock-Paper-Scissors':
        RockPaperScissors()
    # If user types Rock-Paper-Scissors, computer calls the RockPaperScissors function, and starts the game
    elif Question == 'Heads or Tails':
        HeadsorTails()
    # If user types Heads or Tails, computer calls the HeadsorTails function, and starts the game
    else:
        print('Please try again.')
    # If user types anything else other than the given options in the correct format, the computer prints the green statement and reposes the original question

    Question2 = input('Would you like to explore other games?')
    # Computer asks user if they would like to play another game?
    if Question2 == 'Yes':
        continue
    # If user types yes, then the code above repeats and the user can select another game.
    if Question2 == 'No':
        print('Thanks for playing. See you next time!')
        break
    # If user types no, then the computer ends the game

                                                                                                                                                           

      


