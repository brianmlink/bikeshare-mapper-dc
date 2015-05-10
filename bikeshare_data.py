import requests
import xml.etree.ElementTree as ET
import csv

bs_response = requests.get('https://www.capitalbikeshare.com/data/stations/bikeStations.xml')

bs_xml = bs_response.content

root = ET.fromstring(bs_xml)

with open('bs_stations.csv', 'wb') as csvfile:
    linewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for station in root:
        name = station.find('name').text 
        lat = station.find('lat').text
        lon = station.find('long').text
        linewriter.writerow([name, lat, lon])
