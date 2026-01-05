fr_path="file-works\\dog-breeds-process\\dog_breeds.csv"
fr=open(fr_path,"r")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
# total no. of rows
print(len(data))
# first five rows
print(data[:5])
# all dog breeds
all_breeds=[dog.get("Breed") for dog in data]
print((set(all_breeds)))
# all countries with dog breeds
all_countries=[dog.get("Country of Origin") for dog in data]
print(set(all_countries))
# country and dog breeds
breed_count={d:all_countries.count(d) for d in all_countries}
print(breed_count)
# country with most breeds
most_dog_breeds=[k for k,v in breed_count.items() if v==max(breed_count.values())]
print(most_dog_breeds)
# all eye colors
all_eye_colors=[dog.get("Color of Eyes") for dog in data]
print(set(all_eye_colors))
# character traits
traits=[dog.get("Character Traits") for dog in data]
print(set(traits))
# all dog breeds from germany
german_dog_breeds=[dog.get("Breed") for dog in data if dog.get("Country of Origin")=="Germany"]
print(german_dog_breeds)
# all dog breeds from germany
english_dog_breeds=[dog.get("Breed") for dog in data if dog.get("Country of Origin")=="England"]
print(english_dog_breeds)



