#Using pandas, find the movie that is rated most often.
#For example, if a movie with ID 2 is rated 1000 times and no other movie is rated more then 1000,
# then answer should be like this: “movie id: 2 is rated most often, 1000 times.”
  
import pandas as pd


dataframe = pd.read_csv("ratings.csv",index_col = False, sep = ",", names = ["User_ID", "Movie_ID", "Rating","Timestamp"])  

new_data_frame = dataframe[["Movie_ID","Rating"]]

max_most_rated = (new_data_frame["Movie_ID"].value_counts().max())
def most_rated_movie():
    for id, movie_id in enumerate(new_data_frame['Movie_ID'].value_counts().head(1).index.tolist()):
        print('  movie id:', movie_id, "is rated most", max_most_rated, "times." )
most_rated_movie()

def Average_Rate():
    Movie_greater_10 = new_data_frame.groupby("Movie_ID").count()['Rating']

    The_list = Movie_greater_10[Movie_greater_10 > 10].mean()

    print(" The average rating for movie greater than 10 is",The_list)

Average_Rate()

def Top_five_movie():
    new_ratings1 = new_data_frame.groupby("Movie_ID").agg(Rating=('Rating','mean'),Number_Rating=('Rating','count')).reset_index()      

    Top_five  = (new_ratings1[new_ratings1.Number_Rating > 10])

    print(Top_five.sort_values(by="Rating",ascending=False).round(2).head(5).reset_index(drop=True))
Top_five_movie()