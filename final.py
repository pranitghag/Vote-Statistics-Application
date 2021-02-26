f=open("dataset.txt","r")
data=f.read()
f.close()
votes={"1":[],
        "2":[]}
data=data.split("\n")

for i in range(len(data)):
    line=data[i].split(" ")
    # print(line)
    if line[0]=="1":
        votes["1"].append(line[1:])
    elif line[0]=="2":
        votes["2"].append(line[1:])

votes1 = len(votes["1"])
votes2 = len(votes["2"])
count1=0
count2=0
for v in votes["1"]:
    if v[0]=="M":
        count1+=1
    elif v[0]=="F":
        count2+=1

per1 = count1/votes1
per1 = per1*100
print(count1)
print(count2)
print(votes1)
print(votes2)
print(votes1-votes2)
print("Percentage of male voters for candidate 1 : "+str(per1))
