# Author : Pranit Ghag

# Importing random library to create an unbiased dataset
import random
# Democrat = 1 and Republican = 2
cand=["1","2"]
count1=0
count2=0
# Opening file to write data
f = open("dataset.txt","w")

# Using for loop to create data
for i in range(50000):
    # List to store vote
    vote=[]
    # Using random library to choose
    winner = random.choice(cand)
    vote.append(winner)
    f.write(winner+" ")
    gend=["M","F"]
    # Using random library to choose
    g = random.choice(gend)
    f.write(g+" ")
    vote.append(g)
    # Using if statement to choose between candidate 1 and 2
    if(winner=="1"):
        # Using random library to choose
        age = random.randint(18,61)
        r = ["B","W","H","A","B","W","H","A","B","W","H","A"]
        # Using random library to choose
        race = random.choice(r)
        reason = ["Pro-choice","Black-Lives-Matter","Against","Climate-change","Defund-the-police","Economy","Healthcare","Gun-control","Coronavirus"]
        # Using random library to choose
        reas = random.choice(reason)
        count1+=1
    else:
        # Using random library to choose
        age = random.randint(25,91)
        r = ["B","W","H","A","W","W","W","W","W"]
        # Using random library to choose
        race = random.choice(r)
        reason = ["Pro-life","Blue-Lives-Matter","Against","QAnon","Economy","Gun-policy","Immigration","Riots"]
        # Using random library to choose
        reas = random.choice(reason)
        count2+=1
    # Writing the randomly chosen values
    f.write(str(age)+" ")
    f.write(race+" ")
    f.write(reas+"\n")


# Closing the file
f.close()
print("Count 1 : "+str(count1))
print("Count 2 : "+str(count2))
