fr_path="file-works\\country-wise-process\\country_wise_latest_covid.csv"
fr=open(fr_path,"r")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
# all column names
print(reader.fieldnames)
# total no. of rows
print(len(data))
# first five rows
print(data[:5])
# all countries in data
all_countries=[country.get("Country/Region") for country in data]
print(all_countries)
# all countries starting with letter A
countries_startswith_A = [country for country in all_countries if country.startswith("A")]
print(countries_startswith_A)
# country with highest covid count
covid_count=[int(country.get("Confirmed")) for country in data]
print(max(covid_count))
max_count_country=[country.get("Country/Region") for country in data if int(country.get("Confirmed"))==max(covid_count)]
print(max_count_country)
# country with highest death count
death_count=[int(country.get("Deaths")) for country in data]
print(max(death_count))
death_count_by_country=[country.get("Country/Region") for country in data if int(country.get("Deaths"))==max(death_count)]
print(death_count_by_country)
# countries and recovered people
countries_and_recoveries={country.get("Country/Region"):int(country.get("Recovered")) for country in data}
print(countries_and_recoveries)
# sorting countries by recovery
sorted_countries=sorted(countries_and_recoveries, key=countries_and_recoveries.get,reverse=True)
print(sorted_countries)
# top five highest recovered countries
top_five_recovered=sorted_countries[:5]
print(top_five_recovered)
# countries with less than hundred new cases
low_new_cases=[country.get("Country/Region") for country in data if int(country.get("New cases"))<100]
print(low_new_cases)
# country with least number of new cases
new_cases=[int(country.get("New cases")) for country in data]
least_new_cases=[country.get("Country/Region") for country in data if int(country.get("New cases"))==min(new_cases)]
print(least_new_cases)
# country with highest number of new cases
highest_new_cases=[country.get("Country/Region") for country in data if int(country.get("New cases"))==max(new_cases)]
print(highest_new_cases)
# country with least new recoveries
new_recoveries=[int(country.get("New recovered")) for country in data]
least_new_recoveries=[country.get("Country/Region") for country in data if int(country.get("New recovered"))==min(new_recoveries)]
print(least_new_recoveries)
# country with highest new recoveries
highest_new_recoveries=[country.get("Country/Region") for country in data if int(country.get("New recovered"))==max(new_recoveries)]
print(highest_new_recoveries)