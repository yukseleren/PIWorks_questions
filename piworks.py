import csv

# File paths should be changed for any different pc
input_file_path = r'C:\Users\Eren\Downloads\country_vaccination_stats.csv'
output_file_path = r'C:\Users\Eren\Downloads\country_vaccination_stats_2.csv'



with open(input_file_path, mode='r', newline='', encoding='utf-8') as file:
    input_reader = csv.DictReader(file)
    input_data = [row for row in input_reader]

#To store min vacc values of all countries
min_vacc_dict = {}

# First for loop to add the minimum value to dictionary
for row in input_data:
    country = row['country']
    #We use try except block to be able to handle missing values easily
    try:
        daily_vaccinations = int(row['daily_vaccinations'])
        if country not in min_vacc_dict or daily_vaccinations < min_vacc_dict[country]:
            min_vacc_dict[country] = daily_vaccinations
    except ValueError:
        continue

# Second for loop to fill the missing data
for row in input_data:
    if row['daily_vaccinations'] == '':
        country = row['country']
        row['daily_vaccinations'] = "{}".format(min_vacc_dict.get(country, 0)) 
    #For any country that doesnt have any data previously will be initiated with default value 0

#Function to create the output file 
def write_csv(file_path, data, fieldnames):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

write_csv(output_file_path, input_data, fieldnames=input_data[0].keys())

