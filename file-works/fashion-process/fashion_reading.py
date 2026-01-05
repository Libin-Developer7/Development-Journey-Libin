fr_path="file-works\\fashion-process\\Winter_Fashion_Trends_Dataset.csv"
fr=open(fr_path,"r")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
# print first five rows
print(data[:5])
# print total no. of rows
print(len(data))
# all unique categories
all_categories=set()
categories=[all_categories.add(fashion.get("Category")) for fashion in data]
print(all_categories)
# most popular item in winter
winter_category=[fashion.get("Category") for fashion in data if fashion.get("Season").startswith("Winter")]
item_count_winter={w:winter_category.count(w) for w in winter_category}
max_count_item=[k for k,v in item_count_winter.items() if v==max(item_count_winter.values())]
print(max_count_item)
# trending brands
trending_brands=[fashion.get("Brand") for fashion in data if fashion.get("Trend_Status")=="Trending"]
print(set(trending_brands))
# most trending brand
trending_brands=[fashion.get("Brand") for fashion in data if fashion.get("Trend_Status")=="Trending"]
tb_count={b:trending_brands.count(b) for b in trending_brands}
max_trending=[k for k,v in tb_count.items() if v==max(tb_count.values())]
print(max_trending)
# item with highest popularity
popularity=[float(fashion.get("Popularity_Score")) for fashion in data]
most_popular=[fashion for fashion in data if float(fashion.get("Popularity_Score"))==max(popularity)]
print(most_popular)
# item with highest customer rating
customer_rating=[float(fashion.get("Customer_Rating")) for fashion in data]
most_rated=[fashion for fashion in data if float(fashion.get("Customer_Rating"))==max(customer_rating)]
print(most_rated)
# top 5 expensive items
sorted_data=sorted(data, key=lambda x:float(x.get("Price(USD)")),reverse=True)[:5]
print(sorted_data)
# favourite brand of male customers
male_chosen_brands=[fashion.get("Brand") for fashion in data if fashion.get("Gender")=="Men"]
brand_count={b:male_chosen_brands.count(b) for b in male_chosen_brands}
m_popular_brand=[k for k,v in brand_count.items() if v==max(brand_count.values())]
print(m_popular_brand)


