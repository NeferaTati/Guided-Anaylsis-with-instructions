years = [(row["YEAR"]) for row in state_data.txt]
print(years)

def percent_change(List_data, year1, year2, column):
    old_val = 0
    new_val = 0
    for row in List_data:
        #at year1, assign the val of my column into old_val
        if row["YEAR"] == year1:
            old_val = float(row[column])
# at year 2, get the value of my column
        if row["YEAR"] == year2:
            new_val = float(row[column])

            
perc_change = (old_val - new_val) / old_val * 100
return perc_change


for i in range(len(years)):
    if i + 1 >= len(years):
        break
    y1 = years[i]
    y2 = years[i + 1]

    change = percent_change(state_data.txt, y1, y2,"AVG_MATH_4_SCORE")





























#import csv

#