import pandas as pd
import matplotlib.pyplot as plt

#take the percentage of employees in 4 departments
slices=[50,20,15,15]

#take the department names
depts=['Sales','production','HR','Finance']

#take the colors for each dept
cols=['magenta','cyan','brown','gold']

#create a piechart
plt.pie(slices,labels=depts,colors=cols,startangle=90,explode=(0,0.2,0,0),shadow=True,autopct='%.1f%%')

#set company title
plt.title('Capgemini')

#show legend
plt.legend()
plt.show()
