vehicles = [
    {"name": "Swift", "brand": "Maruti Suzuki", "price": 650000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Baleno", "brand": "Maruti Suzuki", "price": 820000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Creta", "brand": "Hyundai", "price": 1500000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "i20", "brand": "Hyundai", "price": 950000, "model": 2021, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Seltos", "brand": "Kia", "price": 1600000, "model": 2023, "color": "Silver", "fuel_type": "Diesel"},
    {"name": "Sonet", "brand": "Kia", "price": 1200000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Harrier", "brand": "Tata", "price": 1900000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "Nexon", "brand": "Tata", "price": 1200000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Punch", "brand": "Tata", "price": 800000, "model": 2023, "color": "Green", "fuel_type": "Petrol"},
    {"name": "XUV700", "brand": "Mahindra", "price": 2200000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Thar", "brand": "Mahindra", "price": 1700000, "model": 2022, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Scorpio N", "brand": "Mahindra", "price": 2000000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "City", "brand": "Honda", "price": 1500000, "model": 2021, "color": "Silver", "fuel_type": "Petrol"},
    {"name": "Amaze", "brand": "Honda", "price": 900000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Kiger", "brand": "Renault", "price": 800000, "model": 2021, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Duster", "brand": "Renault", "price": 1300000, "model": 2020, "color": "Brown", "fuel_type": "Diesel"},
    {"name": "EcoSport", "brand": "Ford", "price": 1100000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Endeavour", "brand": "Ford", "price": 3600000, "model": 2020, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Altroz", "brand": "Tata", "price": 950000, "model": 2022, "color": "Golden", "fuel_type": "Petrol"},
    {"name": "Venue", "brand": "Hyundai", "price": 1300000, "model": 2023, "color": "Red", "fuel_type": "Petrol"}
]

color_red=[ veh.get("name") for veh in vehicles if veh.get("color")=="Red"]
print(color_red)
model_2022=[ veh.get("name") for veh in vehicles if veh.get("model")==2022]
print(model_2022)
fuel_diesel=[ veh.get("name") for veh in vehicles if veh.get("fuel_type")=="Diesel"]
print(fuel_diesel)
veh_prices=[ {veh.get("name"):veh.get("price")} for veh in vehicles]
print(veh_prices)
price_ten_lakh=[ veh.get("name") for veh in vehicles if veh.get("price")>1000000]
print(price_ten_lakh)
tata_veh=[ veh.get("name") for veh in vehicles if veh.get("brand")=="Tata"]
print(tata_veh)
tata_2022=[ veh.get("name") for veh in vehicles if veh.get("brand")=="Tata" and veh.get("model")==2022]
print(tata_2022)
min_price=min([veh.get("price") for veh in vehicles])
veh_min_price=[ {veh["name"]:veh["price"]} for veh in vehicles if veh["price"]==min_price]
print(veh_min_price)
maruti_veh=[ veh.get("name") for veh in vehicles if veh["brand"]=="Maruti Suzuki"]
print(maruti_veh)
hyundai_five_lakh=[ veh.get("name") for veh in vehicles if veh["brand"]=="Hyundai" and veh["price"]>500000]
print(hyundai_five_lakh)
model_2022_2024= [ veh.get("name") for veh in vehicles if veh.get("model")>=2022 and veh.get("model")<=2024]
print(model_2022_2024)
brand_count={}
for veh in vehicles:
    brands=veh.get("brand")
    if brands in brand_count:
        brand_count[brands]+=1
    else:
        brand_count[brands]=1
print(brand_count)
max_count=max(brand_count.values())
print(max_count)
for k,v in brand_count.items():
    if max_count==v:
        print(k,v)
mahindra=[veh.get("price") for veh in vehicles if veh["brand"]=="Mahindra"]
print(max(mahindra))
tata=[veh.get("price") for veh in vehicles if veh["brand"]=="Tata"]
print(max(tata))
mahindra_costly=[{veh["brand"]:veh["name"]} for veh in vehicles if veh["price"]==max(mahindra)]
print(mahindra_costly)
tata_costly=[ {veh["brand"]:veh["name"]} for veh in vehicles if veh["price"]==max(tata)]
print(tata_costly)
model_count={}
for veh in vehicles:
    model=veh.get("model")
    if model in model_count:
        model_count[model]+=1
    else:
        model_count[model]=1
max_model=max(model_count.values())
for k,v in model_count.items():
    if v==max_model:
        print(k,v)



    