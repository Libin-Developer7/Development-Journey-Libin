fr_path="file-works\\toyota-process\\toyota.csv"
fr=open(fr_path,"r")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
# print first five rows
print(data[:5])
# print total no. of rows
print(len(data))
# all unique models
all_models=[vehicle.get("model") for vehicle in data]
unq_models=set(all_models)
print(unq_models)
# model count
count={v:all_models.count(v) for v in all_models}
print(count)
# most common model
most_cmmn=[k for k,v in count.items() if v==max(count.values())]
print(most_cmmn)
# most expensive model
most_exp=sorted(data, key=lambda x:int(x.get("price")),reverse=True)[:1]
print(most_exp)
# model with highest mileage
most_exp=sorted(data, key=lambda x:int(x.get("mileage")),reverse=True)[:1]
print(most_exp)
# most popular model in 2016
all_v_2016=[vehicle.get("model") for vehicle in data if vehicle.get("year")=="2016"]
count_2016={v:all_v_2016.count(v) for v in all_v_2016}
most_2016=[k for k,v in count_2016.items() if v==max(count_2016.values())]
print(most_2016)
# most popular transmission
all_transmissions=[vehicle.get("transmission") for vehicle in data]
count_t={t:all_transmissions.count(t) for t in all_transmissions}
most_pop_t=[k for k,v in count_t.items() if v==max(count_t.values())]
print(most_pop_t)
# most popular fuel type
all_fuels=[vehicle.get("fuelType") for vehicle in data]
count_f={f:all_fuels.count(f) for f in all_fuels}
most_pop_f=[k for k,v in count_f.items() if v==max(count_f.values())]
print(most_pop_f)