import pandas as pd
import numpy as np

movies = pd.read_csv("pandas\movies.csv")
directors =pd.read_csv("pandas\directors.csv")

movies = movies.drop(columns=['Unnamed: 0'])
directors = directors.drop(columns=['Unnamed: 0'])

# print(movies.head())
# print(directors.head())

df =pd.merge(movies,directors,left_on='director_id',right_on='id')
# print(df.head())

# group  by directors name  and calculate the avg rating  : 

director_rating = df.groupby('director_name')['vote_average'].mean().reset_index()
# print(director_rating)

# sort by avg rating  :

top_5 = director_rating.sort_values(by='vote_average',ascending=False).head(5)
print(top_5)

# task  : 2 movies count  ==> top 5 bottom  5 
"""
director_name  movie_count 
Christopher Nolan  20

"""

