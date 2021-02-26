# Author : Pranit Ghag
# This is a custom library
# This file has the parent class and its functions

# Parent class definition
class Election():
    def __init__(self):
        # Initializing variables
        self.votes={"1":[],
                "2":[]}
        self.votes_candidate1 = 0
        self.votes_candidate2 = 0
        self.votes_male = 0
        self.votes_female = 0
        self.votes_age = 0
        self.sentiment={}
        self.race_candidate1={}
        self.race_candidate2={}

    # Function to read the votes from a text file and storing it in a python dictionary named 'votes'
    def read_votes(self):
        # Opening the file
        f=open("dataset.txt","r")
        # Storing data in a variable
        data=f.read()
        # Closing the file
        f.close()
        # Cleaning up the data
        data=data.split("\n")
        # Using the for loop to store the data in a data structure called a dictionary
        for i in range(len(data)):
            line=data[i].split(" ")
            if line[0]=="1":
                self.votes["1"].append(line[1:])
            elif line[0]=="2":
                self.votes["2"].append(line[1:])
        # Function returns the dictionary
        return self.votes

    # Function to count the votes for the individual candidates in the form fo a tuple
    def count_votes_total(self):
        self.votes_candidate1 = len(self.votes["1"])
        self.votes_candidate2 = len(self.votes["2"])
        return self.votes_candidate1,self.votes_candidate2

    # Function to count the votes got by a candidate based on gender
    def count_votes_gender(self,candidate):
        self.votes_male=0
        self.votes_female=0
        candidate = str(candidate)
        # Using for loop to iterate over the votes for a candidate
        for v in self.votes[candidate]:
            # Using if statement to check the votes received based on gender
            if v[0]=="M":
                self.votes_male+=1
            elif v[0]=="F":
                self.votes_female+=1
        # Function returns the votes as a tuple
        return self.votes_male,self.votes_female

    # Fucntion to get the number of votes for a candidate in a age group
    def count_votes_age(self,age1,age2,candidate):
        candidate = str(candidate)
        # Using for loop to iterate over the votes for a candidate
        for v in self.votes[candidate]:
            # Using if statement to count the votes in the range of the ages requested
            if int(v[1])>age1 and int(v[1])<=age2:
                self.votes_age+=1
        # Function returns the number of votes
        print("The number of votes for candidate "+str(candidate)+" between ages "+str(age1)+" and "+str(age2)+" is "+str(self.votes_age))
        return self.votes_age

    # Function to count the number of voters voting for their respectiv issues
    def count_votes_sentiment(self):
        # Using for loop to iterate over the votes for candidate 1
        for v in self.votes["1"]:
            # Using if statement to count the votes for respective issues
            if v[3] not in self.sentiment:
                self.sentiment[v[3]] = 1
            else:
                self.sentiment[v[3]] +=1
        # Using for loop to iterate over the votes for candidate 2
        for v in self.votes["2"]:
            # Using if statement to count the votes for respective issues
            if v[3] not in self.sentiment:
                self.sentiment[v[3]] = 1
            else:
                self.sentiment[v[3]] +=1
        # Function returns a dictionary with the number of votes
        return self.sentiment

    def count_votes_race(self,candidate):
        candidate = str(candidate)
        if candidate == "1":
            for v in self.votes["1"]:
                if v[2] not in self.race_candidate1:
                    self.race_candidate1[v[2]] = 1
                else:
                    self.race_candidate1[v[2]] += 1
            # Function returns a dictionary with the number of votes
            return self.race_candidate1
        else:
            for v in self.votes["2"]:
                if v[2] not in self.race_candidate2:
                    self.race_candidate2[v[2]] = 1
                else:
                    self.race_candidate2[v[2]] += 1
            # Function returns a dictionary with the number of votes
            return self.race_candidate2
