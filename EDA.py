import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

csv=pd.read_csv(r'C:\Users\Samuel\Desktop\Sam\Verzeo\VerzeoMinorProject\tmdb-movies.csv')
df=pd.DataFrame(csv)
df=df.sort_values('release_year')

x=df['release_year']
y=df['budget']

plt.plot(x,y)
plt.show()


y=df['vote_average']
plt.scatter(x,y)
plt.show()

