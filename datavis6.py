#line chart
import pandas as pd
import matplotlib.pyplot as plt

years=['2012','2013','2014','2015','2016','2017']
profits=[19,10,10.5,8.8,10.9,9.75]

#create the line graph
plt.plot(years,profits,'blue')

plt.xlabel('years')
plt.ylabel('profits in ml rs')
plt.title('XYZ comp')

plt.show()
