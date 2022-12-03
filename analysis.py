from portfolio.skeleton import AMZN
import statistics as s

list1 = AMZN



#Within `analysis.py`, iterate through each week of each company,
#iterate through each list[]

for x in list1 :
    print(s.mean(x))
    print(s.stdev(x))
    

practice = [s.mean(x)for x in list1]
print(practice)

newlist = [s.mean(item) for item in list1 ]
print(newlist)

    
    


#and calculate standard deviation of each stock.
    # use stat function with mean, medium etc 

practice2 = [s.median(x)for x in list1]
print(f"median is...{practice2} ")


#Print out these values with descriptive strings so that we could view

 #(output)   #str -"azmn mean", "azmn mode":stat.M(str), "amzn medium": stat.M(str)


#how standard deviation is behaving.
    

weeks = 1
for row in AMZN:
    print(weeks,s.stdev(row))
    weeks += 1
import  matplotlib.pyplot as plt
plt.plot(std)
weeks = 1

std = []
for row in AMZN:
    std.append(s.stdev(row))
    print(weeks,s.stdev(row))
    weeks+=1

plt.plot(std)
weeks = 1

