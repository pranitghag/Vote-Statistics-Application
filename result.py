# Author : Pranit Ghag
# This file has the child class for inheritence

# Importing the file with the parent class
import election
# Importing the custom library
import myLib

# Child class Result that inherits from parent class Election
class Result(election.Election):
    def __init__(self):
        # Initializing the variables
        election.Election.__init__(self)
        self.votes={"1":[],
                "2":[]}
        self.male_percentage=0
        self.female_percentage=0
        self.candidate1_percentage=0
        self.candidate2_percentage=0
        self.votes_candidate1 = 0
        self.votes_candidate2 = 0

    # Function to get the votes using the read_votes() function from the parent class
    def get_votes(self):
        self.votes = self.read_votes()

    # Function to store the votes for candidate 1 and candidate 2 using the count_votes_total() function from the parent class
    def total_votes(self):
        # count_votes_total returns a tuple
        res = self.count_votes_total()
        self.votes_candidate1 = res[0]
        self.votes_candidate2 = res[1]

    # Function to project the winner fo the election
    def winner(self):
        # Using if loop to determine the winner of the elction
        if self.votes_candidate1>self.votes_candidate2:
            print("The projected winner is Candidate 1 with "+str(self.votes_candidate1)+" votes from a total "+str(myLib.TOTAL_VOTES)+" votes")
        elif self.votes_candidate1<self.votes_candidate2:
            print("The projected winner is Candidate 2 with "+str(self.votes_candidate2)+" votes from a total "+str(myLib.TOTAL_VOTES)+" votes")
        else:
            print("This is an unlikely tie. Prepare for a recount and runoffs.")

    # Function to calculate the percentage of voters for a candidate based on gender
    def calc_percentage_gender(self,candidate):
        res = self.count_votes_gender(candidate)
        if candidate == 1:
            votes = self.votes_candidate1
        elif candidate == 2:
            votes = self.votes_candidate2
        male = res[0]
        female = res[1]
        self.male_percentage = (male/votes)*100
        self.female_percentage = (female/votes)*100
        # Function returns a tuple for percentages
        return self.male_percentage,self.female_percentage

    # Function to calculate the percentage of voters voting for candidate 1 and candidate 2
    # This function uses a constant from the custom library
    def calc_percentage_total(self):
        self.candidate1_percentage = (self.votes_candidate1/myLib.TOTAL_VOTES)*100
        self.candidate2_percentage = (self.votes_candidate2/myLib.TOTAL_VOTES)*100
        # Returns percentages as a tuple
        return self.candidate1_percentage,self.candidate2_percentage


# Opening a text file to store the results
f=open('results.txt','w')
# Creating an instance for class Result
r = Result()
# Calling function get_votes() to read from a text file to a data structure
r.get_votes()
# Calling function to count the votes
r.total_votes()
# Calling function to project a winner
r.winner()
# Calling funcrion to count votes for a candidate between two ages
r.count_votes_age(25,35,2)

result = []
# Calling function to calculate the percentage of votes for candidate 1 and 2
res = r.calc_percentage_total()
# Writing the results in a text file
f.write("The percentage of voters voting for candidate 1 is "+str(res[0])+"\n")
f.write("The percentage of voters voting for candidate 2 is "+str(res[1])+'\n')
result.append(res[0])
result.append(res[1])
# Calling function to calculate the percentage of votes for candidate 1 based on gender
res = r.calc_percentage_gender(1)
# Writing the results in a text file
f.write("The percentage of voters voting for candidate 1 that are male is "+str(res[0])+'\n')
f.write("The percentage of voters voting for candidate 1 that are female is "+str(res[1])+'\n')
result.append(res[0])
result.append(res[1])
# Calling function to calculate the percentage of votes for candidate 2 based on gender
res = r.calc_percentage_gender(2)
# Writing the results in a text file
f.write("The percentage of voters voting for candidate 2 that are male is "+str(res[0])+'\n')
f.write("The percentage of voters voting for candidate 2 that are female is "+str(res[1])+'\n')
result.append(res[0])
result.append(res[1])

# List of issues faced by the voters
n = ['Percentage_for_C1','Percentage_for_C2','Percentage_of_male_for_C1','Percentage_of_female_for_C1',
    'Percentage_of_male_for_C2','Percentage_of_female_for_C2']

# Using the custom library to plot the values
myLib.plot([1,20,40,60,80,100],result,'Result','Range','Votes',n)

# Fucntion called to count the votes for candidate 1 based on race
race_1 = r.count_votes_race(1)
# Fucntion called to count the votes for candidate 2 based on race
race_2 = r.count_votes_race(2)
res2=[]
n2=[]
# Using for loop to create lists to plot a graph
for i in race_1:
    n2.append(i)
    res2.append(race_1[i])

# Writing the results in a text file
f.write("\n")
f.write("The number of votes for candidate 1 based on race are: \n")
f.write(str(race_1)+'\n')
f.write("The number of votes for candidate 2 based on race are: \n")
f.write(str(race_2)+'\n')
# Using the custom library to plot the values
myLib.plot([0,int(res[0]/4),int(3*res[0]/4),res[0]],res2,'Result for Candidate 1','X-axis','Votes based on race',n2)
res2=[]
n2=[]
# Using for loop to create lists to plot a graph
for i in race_2:
    n2.append(i)
    res2.append(race_2[i])

# Using the custom library to plot the values
myLib.plot([0,int(res[1]/4),int(3*res[1]/4),res[1]],res2,'Result for Candidate 2','X-axis','Votes based on race',n2)

res2=[]
n2=[]
# Calling function to count the votes based on issues faced by the voters
sentiment = r.count_votes_sentiment()
# Writing the results in a text file
f.write("The number of votes casted based on different issues is : \n")
f.write(str(sentiment)+"\n")
# Closing the output file
f.close()

# Using for loop to create lists to plot a graph
for i in sentiment:
    n2.append(i)
    res2.append(sentiment[i])


s=[]
for i in range(0,max(res2),int(max(res2)/15)):
    s.append(i)
# Using the custom library to plot the values
myLib.plot(s,res2,'Result for Candidates','X-axis','Votes based on issues',n2)
