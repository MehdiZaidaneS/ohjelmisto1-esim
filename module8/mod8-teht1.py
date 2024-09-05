import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='mehdizaidane1',
         autocommit=True
         )



ICAO = input("Syötä ICAO koodi: ")

cursor = connection.cursor()
sql = f"SELECT airport.name, country.name FROM airport, country WHERE airport.ident = '{ICAO}' and airport.iso_country = country.iso_country"
cursor.execute(sql)

response = cursor.fetchall()

for row in response:
  print(f"The airport name with the code {ICAO} is {row[0]} with location in {row[1]}")