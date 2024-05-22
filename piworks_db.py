import pymysql
import statistics

# Database connection details
connection = pymysql.connect(
    user='your_user',
    password='your_password',
    host='your_host',
    database='your_database'
)
query = "SELECT country, date, daily_vaccinations, vaccines FROM country_vaccination_table"
cursor = connection.cursor()
cursor.execute(query)
rows = cursor.fetchall()

# Process the daily vacc data for every country into a dictionary
data = {}
for row in rows:
    country, date, daily_vaccinations, vaccines = row
    try:
        daily_vaccinations = int(daily_vaccinations)
        if country not in data:
            data[country] = []
        data[country].append(daily_vaccinations)
    except TypeError:
        continue

#To store median values of all countries
median_per_country = {}
for country, value_list in data.items():
    median_per_country[country] = statistics.median(value_list)


#query for updating the missing value field which means daily_vacc will be null
update_query =  """
UPDATE country_vaccination_table
SET daily_vaccinations = %s
WHERE country = %s AND date = %s AND daily_vaccinations IS NULL
""" 

for row in rows:
    country, date, daily_vaccinations, vaccines = row
    try:
        daily_vaccinations = int(daily_vaccinations)
    except TypeError: #If the field is null then we get typeerror so we can understand that the field should be updated
        if country in median_per_country:
            cursor.execute(update_query, (median_per_country[country], country, date))
        else: #default value if country didnt have any previous vacc values
            cursor.execute(update_query, (0, country, date))
        continue

connection.commit()
cursor.close()
connection.close()
