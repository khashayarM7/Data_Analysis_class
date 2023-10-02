import pandas as pd
import matplotlib.pyplot as plt

# open file
file = pd.read_csv('HW1week1 .csv')
# we should change population from str to int bc of ( , ) for example : 321,213,211
file['Population'] = file['Population'].str.replace(',', '').astype(int)
# scatter plot we choose color x,y and dot also with alpha we can provide better overview
plt.scatter(file['Longitude'], file['Latitude'], color="navy", s=file['Population']/100000, alpha=0.7)
# title name
plt.title("the ten most population cities of iran")
# x label name
plt.xlabel("Latitude")
# y label name
plt.ylabel("Longitude")
# we should put name of cities in each dot
for i, row in file.iterrows():
    plt.annotate(row['City'], (row['Longitude'], row['Latitude']), fontsize=10, alpha=0.9, ha='left', color="pink")
# show plot
plt.show()
