read_path="file-works\\movies.csv"
fr=open(read_path,"r")
import csv
reader=csv.DictReader(fr)

data = [row for row in reader]
# for mov in range(5):
#     print(data[mov])
# length_data= len(data)
# print(length_data)
# headers= data[0].keys()
# print(headers)

# # year= input("enter year ")
# # mov_by_year = [ mov["Film"] for mov in data if mov["Year"]==year]
# # print(mov_by_year)

# ratings = [int(mov.get("Audience score %")) for mov in data]
# max_rating = max(ratings)
# highest_rated_mov=[ mov["Film"] for mov in data if mov["Audience score %"]==str(max_rating)]
# print(highest_rated_mov)

# genre = input("enter genre ")
# mov_by_genre = [{mov["Film"]:mov["Genre"]} for mov in data if mov["Genre"]==genre]
# print(mov_by_genre)

# fw_path="file-works\\movie_process\\top_rated.csv"
# fw=open(fw_path,"w")
# top_rated=[fw.write(mov["Film"]+"\n") for mov in data if int(mov["Audience score %"])>80]

# fw_genre_path="file-works\\movie_process\\genre_count.txt"
# fw_genre = open(fw_genre_path,"w")
# genre_count={}
# for mov in data:
#     if mov["Genre"] in genre_count:
#         genre_count[mov["Genre"]]+=1
#     else:
#         genre_count[mov["Genre"]]=1
# for k,v in genre_count.items():
#     fw_genre.write(k + " " + str(v) + "\n")

fw_srt_path = "file-works\\movie_process\\sorted_movies.csv"
fw_srt = open(fw_srt_path,"w")
sorted_by_score= sorted(data, key= lambda mov:int(mov.get("Audience score %")), reverse=True)
print(sorted_by_score)
for mov in sorted_by_score:
    fw_srt.write(mov["Film"] + "\n")

movies_missing_data = []

for movie in data:
    if any(value == "" or value is None for value in movie.values()):
        movies_missing_data.append(movie)

print("movies with missing data", movies_missing_data)

movie = input("enter a movie name ")
for mov in data:
    if movie.casefold() == mov["Film"].casefold():
        print(mov["Film"])

