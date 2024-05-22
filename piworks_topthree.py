import csv
import statistics

#file path to imputed dataset version
input_file_path = r'C:\Users\Eren\Downloads\country_vaccination_stats_2.csv'

with open(input_file_path, mode='r', newline='', encoding='utf-8') as file:
    input_reader = csv.DictReader(file)
    data = [row for row in input_reader]

# Dictionary to store daily vaccinations per country as country:[values]
vacc_per_country = {}

for row in data:
    country = row['country']
    daily_vaccinations = int(row['daily_vaccinations'])
    if country not in vacc_per_country:
        vacc_per_country[country]=[] #If it is the first time, empty list will be created
    vacc_per_country[country].append(daily_vaccinations)


# Calculate median for each country
median_per_country = {}
for country, value_list in vacc_per_country.items():
    median_per_country[country] = statistics.median(value_list)

# Sort countries by median and get the top 3
top_3_countries = sorted(median_per_country.items(), key=lambda item: item[1], reverse=True)[:3]


for country, median in top_3_countries:
    print(f"{country}: {median}")
