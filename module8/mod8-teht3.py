from geopy import distance
import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'mehdizaidane1',
    database = 'flight_game',
    autocommit = True
)



ekakoodi = input("Syötä ensimmäisen ICAO-koodi: ")
tokakoodi = input ("Syötä toisen ICAO-koodi: ")


cursor = connection.cursor()


sql = f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport WHERE airport.ident = '{ekakoodi}'"
sql2 = f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport WHERE airport.ident = '{tokakoodi}'"
cursor.execute(sql)
response1 = cursor.fetchall()

cursor.execute(sql2)
response2 = cursor.fetchall()


etaisyys = distance.distance(response1, response2).km

print(f"ICAO-koodilla {ekakoodi} varustetun lentokentän ja koodin {tokakoodi} lentokentän välinen etäisyys on {etaisyys:.2f}km")



