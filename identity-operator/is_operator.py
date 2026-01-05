# is operator checks whether variable is pointing to the same object
person_from_chavakkad = "adhnan"
person_from_kakkanad = "adhnan"

print(person_from_chavakkad == person_from_kakkanad) 
#True

print(person_from_chavakkad is person_from_kakkanad)
#True- only in the case of string, since no new object is created

person_list_from_chavakkad = ["adhnan"]
person_list_from_kakkanad = ["adhnan"]

print(person_list_from_chavakkad == person_list_from_kakkanad) # True
print(person_from_chavakkad is person_from_kakkanad) 
#False- since different object is created for each string