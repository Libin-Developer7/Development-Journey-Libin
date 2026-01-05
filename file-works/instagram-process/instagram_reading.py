fr_path="file-works\\instagram-process\\Instagram_Analytics.csv"
fr=open(fr_path,"r")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
# print first five rows
five_rows=data[:5]
print(five_rows)
# print category of first five rows
five_categories=[media.get("content_category") for media in data][:5]
print(five_categories)
# total rows in data
print(len(data))
# all unique categories
all_categories=set()
categories=[all_categories.add(media.get("content_category")) for media in data]
print(all_categories)
# count media in tech category
tech_category=[media.get("content_category") for media in data if media.get("content_category")=="Technology"]
print(len(tech_category))
# media type with highest likes
likes=[int(media.get("likes")) for media in data]
most_likes=[{media.get("media_type"):media.get("content_category")} for media in data if int(media.get("likes"))==max(likes)]
print(most_likes)
# highest media count
all_media=[media.get("media_type") for media in data]
media_count={m:all_media.count(m) for m in all_media}
print(media_count)
for k,v in media_count.items():
    if v==max(media_count.values()):
        print(k,v)
# most followers gained and media type
followers=[int(media.get("followers_gained")) for media in data]
max_followers={media.get("media_type"):media.get("followers_gained") for media in data if int(media.get("followers_gained"))==max(followers)}
print(max_followers)
# avg comments for all media
all_cmmnts=[int(media.get("comments")) for media in data]
avg_comments=sum(all_cmmnts)/len(all_cmmnts)
print(avg_comments)
# Most shared media
shares=[int(media.get("shares")) for media in data]
print(max(shares))
most_shared=[{media.get("media_type"):media.get("content_category")} for media in data if int(media.get("shares"))==max(shares)]
print(most_shared)
