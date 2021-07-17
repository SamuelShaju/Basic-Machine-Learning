#1) Which are the movies with the third-lowest and third-highest budget?
#2) What is the average number of words in movie titles between the years 2000-2005?
#3) What is the most common Genre for Vin Diesel & Emma Watson movies?
#4) Which are the movies with the most and least earned revenue?
#5) What is the average runtime of movies in the year 2006?

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv=pd.read_csv(r'C:\Users\Samuel\Desktop\Sam\Verzeo\VerzeoMinorProject\tmdb-movies.csv')
df=pd.DataFrame(csv)

#Q1]
df1=df.sort_values('budget')                                                               #Sorted the dataframe wrt budget

df1=df1[df['budget']>1000]                                                                 #For cleaning I have removed any movi with budget less then 1000$
bdgt=df1.iloc[2,3]
print(df1[df1['budget']==bdgt])                                                            #Printing the third cheapest movies
bdgt=df1.iloc[-3,3]
print(df1[df1['budget']==bdgt])                                                            #Printing the third costliest movies



#Q2]
df2=df.sort_values('release_year')                                                         #copying database to df2 sorted by year(unnecessary to sort,done for cleaner dataset)
df2=df2[df2['release_year']>=2000]
df2=df2[df2['release_year']<=2005]                                                         #Filtering to movies with release date between 2000 and 2005(both inclusive)

df2=df2['original_title'].str.split(' ').str.len()                                         #Converting all values in original_title to series and replacing with number of words
sum=df2.sum()                                                                              #sum of number of words
print(sum/df2.size)                                                                        #printing average (1687=len of series)




#Q3]




#Q4]
df4=df.sort_values('revenue')
df4=df4[df4['revenue']>1000]                                                               #removing revenues less than 1000$ to clean unnecessary data
print(df4[0:1])                                                                            #printing lowest revenue
print(df4[-1:])                                                                            #printing highest revenue



#Q5]
df5=df[df['release_year']==2006]                                                           #Making dataframe with 2006 movies
total_runtime=df5['runtime'].sum()                                                         #Calculating total runtime
len=df5['runtime'].size                                                                    #Calculating number of movies
print(total_runtime/len)                                                                   #printing average runtime