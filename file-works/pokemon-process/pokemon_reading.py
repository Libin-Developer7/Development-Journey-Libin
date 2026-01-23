fr_path="file-works\\pokemon-process\\pokemon_stats_2025.csv"
fr=open(fr_path,"r")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
# all columns
print(reader.fieldnames)
# first five rows
print(data[:5])
# all pokemons
names=[p.get("name") for p in data]
print(names)
# all grass types
grass_types=[p.get("name") for p in data if p.get("type_1")=="grass"]
print(grass_types)
# max weight for grass type
grass_type_weights=[int(p.get("weight")) for p in data if p.get("type_1")=="grass"]
print(max(grass_type_weights))
max_weighed_grass_type= [p.get("name") for p in data if (p.get("type_1")=="grass") and int(p.get("weight"))==max(grass_type_weights)]
print(max_weighed_grass_type)
# max count in type1
all_type_1=[p.get("type_1") for p in data]
count_dict={t:all_type_1.count(t) for t in all_type_1}
print(count_dict)
max_type_1=[k for k,v in count_dict.items() if v==max(count_dict.values())]
print(max_type_1)
# max count in type2
all_type_2=[p.get("type_2") for p in data]
type2_count_dict={t:all_type_2.count(t) for t in all_type_2}
print(type2_count_dict)
# sorted by hp
pokemon_hp = {p.get("name"):int(p.get("hp")) for p in data}
sorted_hp = sorted(pokemon_hp,key=pokemon_hp.get, reverse=True)
print(sorted_hp[:5])
sorted_by_hp=sorted(data,key=lambda x:int(x.get("hp")),reverse=True)
srt=[p.get("name") for p in sorted_by_hp]
print(srt[:5])
# grass type pokemon in new csv
fw_path="file-works\\pokemon-process\\grass_type.csv"
fw=open(fw_path,"w")
