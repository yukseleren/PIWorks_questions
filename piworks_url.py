import pymysql

connection = pymysql.connect(
    user='your_user',
    password='your_password',
    host='your_host',
    database='your_database'
)
input = input("For which device do you need url? \n-->")
# Read the data from the database
query = """SELECT 
    Device_Type,
    REPLACE(REPLACE(REPLACE(REPLACE(Stats_Access_Link, '<url>', ''), '</url>', ''), 'http://', ''), 'https://', '') AS Pure_URL
FROM 
    device_stats
    WHERE Device_Type = %s;"""
cursor = connection.cursor()
cursor.execute(query,input)
row = cursor.fetchall()
print("Device_Type = {}\nPure Url = {}".format(input, row[0][1]))



# Close the database connection
cursor.close()
connection.close()
