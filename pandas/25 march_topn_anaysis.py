import pandas as pd
import numpy as np

movies = pd.read_csv("pandas\movies.csv")
directors =pd.read_csv("pandas\directors.csv")

movies = movies.drop(columns=['Unnamed: 0'])
directors = directors.drop(columns=['Unnamed: 0'])

# print(movies.head())
# print(directors.head())

# df =pd.merge(movies,directors,left_on='director_id',right_on='id')
# print(df.head())

# group  by directors name  and calculate the avg rating  : 

# director_rating = df.groupby('director_name')['vote_average'].mean().reset_index()
# print(director_rating)

# sort by avg rating  :

# top_5 = director_rating.sort_values(by='vote_average',ascending=False).head(5)
# print(top_5)

# task  : 2 movies count  ==> top 5 bottom  5 
"""
director_name  movie_count 
Christopher Nolan  20

# """
# top_5 =df.groupby("director_name")['title'].count()
# # print(top_5)

# direcotor_count =df.groupby("director_name")['title'].count().sort_values(ascending=False).head(5)
# print(direcotor_count)

"""
Consider the following data:
data = {
    "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
    "B": [50, 40, 40, 30, 50],
    "C": [True, False, False, False, True]
}
Convert this to a Pandas DataFrame and remove duplicate rows from it. Reset index values.
"""
"""
data = {
    "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
    "B": [50, 40, 40, 30, 50],
    "C": [True, False, False, False, True]
}

df = pd.DataFrame(data)
# print(df)

# x=df.drop_duplicates(keep=False,ignore_index=True)
# print(x)

df.drop_duplicates(inplace=True,ignore_index=True)
# print(df.reset_index())
print(df)"""


# import pandas as pd
# import plotly.express as px
# import plotly.io as pio

# pio.renderers.default = "notebook"

# # Dataset
# df = pd.DataFrame({
#     "Department":["IT","HR","Finance","Marketing"],
#     "Budget":[50000,30000,40000,20000]
# })

# # 🔥 Find highest budget index
# max_index = df['Budget'].idxmax()

# # Create pull list (explode effect)
# pull = [0]*len(df)
# pull[max_index] = 0.2   # pull highest outward

# # Create pie chart
# fig = px.pie(
#     df,
#     names='Department',
#     values='Budget',
#     title='Department Budget Allocation'
# )

# # Update layout for required features
# fig.update_traces(
#     pull=pull,                      # pull highest slice
#     textinfo='percent+label',       # show % + label
#     textposition='inside'           # text inside pie
# )

# fig.show()

import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()