fr_path="file-works\\mental-health-process\\mental_health_social_media_dataset.csv"
fr=open(fr_path,"r")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
# print first five rows
print(data[:5])
# print total no. of rows
print(len(data))
# total male and female social media users
males=[person for person in data if person.get("gender")=="Male"]
females=[person for person in data if person.get("gender")=="Female"]
print(len(males))
print(len(females))
# average screen time for all users
screen_time=[int(person.get("daily_screen_time_min")) for person in data]
avg_scrn_time=sum(screen_time)/len(screen_time)
print(avg_scrn_time)
# average social media time
sm_time=[int(person.get("social_media_time_min")) for person in data]
avg_sm_time=sum(sm_time)/len(sm_time)
print(avg_sm_time)
# most used platform
all_platforms=[person.get("platform") for person in data]
count={pf:all_platforms.count(pf) for pf in all_platforms}
max_pf=[k for k,v in count.items() if v==max(count.values())]
print(max_pf)
# percentage of stressed users
all_stressed=[person for person in data if person.get("mental_state")=="Stressed"]
percent_strs_user=len(all_stressed)/len(data)*100
print(percent_strs_user)
# avg physical activity among stressed users
all_stressed_PA=[int(person.get("physical_activity_min")) for person in data if person.get("mental_state")=="Stressed"]
avg_PA_for_stressed=sum(all_stressed_PA)/len(all_stressed_PA)
print(avg_PA_for_stressed)
# avg PA among healthy users
all_healthy_PA=[int(person.get("physical_activity_min")) for person in data if person.get("mental_state")=="Healthy"]
avg_PA_for_healthy=sum(all_healthy_PA)/len(all_healthy_PA)
print(avg_PA_for_healthy)
# names of healthy users and their avg screen time
healthy_people=[person.get("person_name") for person in data if person.get("mental_state")=="Healthy"]
print(healthy_people)
healthy_screen_time=[int(person.get("daily_screen_time_min")) for person in data if person.get("mental_state")=="Healthy"]
avg_healthy_screen_time=sum(healthy_screen_time)/len(healthy_screen_time)
print(avg_healthy_screen_time)
