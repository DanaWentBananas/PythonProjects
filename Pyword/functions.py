import random
import json

def play():

    name = input("Enter your player name: ").title()

    f = open("words.txt","r")
    words = [word.strip() for word in f]
    rounds=3
    turns=6
    points=0

    for round in range(rounds):

        print("Round "+str(round+1)+":")
        #word = words[random.randint(0,len(words)-1)]
        word = "hello"
        markedword = "XXXXX"
        alph = "abcdefghijklmnopqrstuvwxyz"
        markedalph = " "*len(alph)
        turnsleft=6
        guesses=[]

        for turn in range(turns):

            while True:
                guess = input(str(turn+1)+"? ").strip().lower()
                if not guess.isalpha():
                    print("Invalid guess. Please only enter letters.")
                elif len(guess)!=5:
                    print("Invalid guess. Please enter exactly 5 characters.")
                else:
                    break

            markedword = list(markedword)
            markedalph = list(markedalph)
            for i in range(5):
                if guess[i] not in word:
                    markedword[i]="X"
                    loc = alph.find(guess[i])
                    markedalph[loc]="X"
                elif guess[i] in word and guess[i]==word[i]:
                    markedword[i]="!"
                    loc = alph.find(guess[i])
                    markedalph[loc]="!"
                elif guess[i] in word:
                    markedword[i]="?"
                    loc = alph.find(guess[i])
                    markedalph[loc]="?"

            markedword = "".join(markedword)
            markedalph = "".join(markedalph)
            guesses.append(markedword)
            print(markedword+"     "+markedalph)
            print(guess+"     "+alph)

            turnsleft-=1

            if guess==word:
                if turnsleft==6:
                    print("Impossible! You earned 64 points this round")
                    points+=64
                if turnsleft==5:
                    print("Genius! You earned 32 points this round")
                    points+=32
                if turnsleft==4:
                    print("Magnificent! You earned 16 points this round")
                    points+=16
                if turnsleft==3:
                    print("Impressive! You earned 8 points this round")
                    points+=8
                if turnsleft==2:
                    print("Splendid! You earned 4 points this round")
                    points+=4
                if turnsleft==1:
                    print("Great! You earned 2 points this round")
                    points+=2
                if turnsleft==0:
                    print("Phew! You earned 1 points this round")
                    points+=1
                break
            if turnsleft==0:
                print("You ran out of tries")
                print("The word was "+word+".")

        print("Round "+str(round+1)+" summary")
        for x in guesses:
            print("   "+x)

    f = open("halloffame.json","r")
    halloffame = json.load(f)
    if len(halloffame)<6 and str(points) not in halloffame:
        print("Way to go "+name+"!")
        print("You earned a total of "+str(points)+" points and made it into the Hall of Fame!")
        halloffame[points]=name
        halloffame = sort(halloffame)
        f = open("halloffame.json","w")
        json.dump(halloffame,f)
        f.close()
        show()
        return
    for score in halloffame:
        if points>int(score) and str(points) not in halloffame:
                print("Way to go "+name+"!")
                print("You earned a total of "+str(points)+" points and made it into the Hall of Fame!")
                halloffame[points]=name
                halloffame = sort(halloffame)
                f = open("halloffame.json","w")
                json.dump(halloffame,f)
                f.close()
                show()
                return
    print("You earned a total of "+str(points)+" points.")
                        



def show():
    f = open("halloffame.json","r")
    halloffame = json.load(f)
    if not halloffame:
        print("Play a new game to be the first!")
        return
    print("## : Score : Player")
    for count,(key,val) in enumerate(halloffame.items(),start=1):
        print(" "+str(count)+" : "+str(key).rjust(5)+" : "+val)

def sort(halloffame):
    halloffame = {int(k):v for k,v in halloffame.items()}
    halloffame = dict(sorted(halloffame.items()))
    halloffame = {k:v for k,v in halloffame.items()}
    return halloffame
