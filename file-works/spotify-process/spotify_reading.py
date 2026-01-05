fr_path="file-works\\spotify-process\\spotify_data clean.csv"
fr=open(fr_path,"r",encoding="utf-8")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
for i in range(5):
    print(data[i])
print(len(data))
artists={album.get("artist_name") for album in data}
print(artists)
exp_almbums =[album for album in data if album.get("explicit")=="TRUE"]
print("explicit albums",len(exp_almbums))
popular_album=[album.get("track_name") for album in data if int(album.get("track_popularity"))>50]
print(popular_album)
popularity=[int(album.get("track_popularity")) for album in data]
most_popular=[album.get("track_name") for album in data if int(album.get("track_popularity"))==max(popularity)]
print(most_popular)
avg_popularity=sum(popularity)/len(data)
print(avg_popularity)
all_albums=[album.get("album_name") for album in data]
track_count={alb:all_albums.count(alb) for alb in all_albums}
print(track_count)
artist=input("enter artist name ")
artist_tracks=[album.get("track_name") for album in data if artist.casefold()==album.get("artist_name").casefold()]
print(artist_tracks)
all_durations=[(float(album.get("track_duration_min"))) for album in data]
print(max(all_durations))
longest_track=[album.get("track_name") for album in data if float(album.get("track_duration_min"))==max(all_durations)]
print(longest_track)
artst_flws={album.get("artist_name"):int(album.get("artist_followers")) for album in data}
srt_flwrs=sorted(artst_flws,key=artst_flws.get,reverse=True)[:5]
print(srt_flwrs)
explicit_pop=[int(album.get("track_popularity")) for album in data if album.get("explicit")=="TRUE"]
avg_exp=sum(explicit_pop)/len(explicit_pop)
print("explicit popularity",avg_exp)
non_explicit_pop=[int(album.get("track_popularity")) for album in data if album.get("explicit")=="FALSE"]
avg_nonexp=sum(non_explicit_pop)/len(non_explicit_pop)
print("non explicit popularity",avg_nonexp)
genre=[album.get("artist_genres") for album in data]
genre_count={g:genre.count(g) for g in genre}
print(genre_count)