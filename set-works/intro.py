boys_height={175,180,180,182,169}
print(boys_height)

bharath_foods={"tea","coffee","battora","fruit meals","gheeroast","masala dosa"}
pathans_foods={"tea","coffee","boost","fried rice"}
all_foods=bharath_foods.union(pathans_foods)
print(all_foods)

common_foods=bharath_foods.intersection(pathans_foods)
print(common_foods)
unique_foods=bharath_foods.difference(pathans_foods)
print(unique_foods)

set_a={100,200,300,400}
set_b={10,20}
set_c={100,200,20}
print(set_a.issuperset(set_b))
print(set_b.issubset(set_a))
print(set_a.issuperset(set_c))
print(set_c.issubset(set_a))
print(set_a.symmetric_difference(set_b))
set_a.add(500)
print(set_a)
set_a.update(set_b)
print(set_a)

"""
subset
superset
symmetric difference

"""