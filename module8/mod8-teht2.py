import mysql.connector

connection = mysql.connector.connect(
    host= '127.0.0.1',
    port = 3306,
    user= "root",
    password = 'mehdizaidane1',
    database = 'flight_game',
    autocommit = True
)

maakoodi = input("Syötä maakoodi: ")

closed = []
small_airport = []
medium_airport = []
large_airport = []
heliport = []


cursor = connection.cursor()
sql = f"SELECT airport.type FROM airport WHERE airport.iso_country = '{maakoodi}'"
cursor.execute(sql)
response = cursor.fetchall()

for row in response:
    if row[0] == "closed":
        closed.append(row[0])
    elif row[0] == "small_airport":
        small_airport.append(row[0])
    elif row[0] == "medium_airport":
        medium_airport.append(row[0])
    elif row[0] == "large_airport":
        large_airport.append(row[0])
    elif row[0] == "heliport":
        heliport.append(row[0])


print(f"There are {len(small_airport)} small airports, {len(medium_airport)} medium airports, {len(large_airport)} large airports, {len(heliport)} heliports and {len(closed)} closed airports")