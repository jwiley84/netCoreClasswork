import random

#coin = random.randint(0,1);


def coinToss(end):
    tails = 0;
    heads = 0;
    face = "heads"
    #toss coin. Heads are 0, tails are 1.
    for toss in range(0,end):
        coin=random.randint(0,1);
        if (coin == 0):
            heads += 1;
            face = "heads"
        else:
            tails += 1;
            face = "tails"
        print("Attempt #" + str(toss + 1) + ": Throwing a coin ... It's " + face + " ... You've got " + str(heads) + " heads and " + str(tails) + " tails so far")
    print("Ending the program, thank you!")

coinToss(5000)