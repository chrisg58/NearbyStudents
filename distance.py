import math, requests, json, urllib, codecs
from apiclient.discovery import build

earthRad = 3959

def distance(lat1, lng1, lat2, lng2):
	latr1 = math.radians(lat1)
	latr2 = math.radians(lat2)
	dlat = math.radians(lat2-lat1)
	dlong = math.radians(lng2 - lng1)
	a = math.sin(dlat/2) * math.sin(dlat/2) + (math.cos(latr1) * math.cos(latr2) * math.sin(dlong/2) * math.sin(dlong/2))
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	return earthRad * c
	
def main():
	print(str(distance(40.9175789, -74.1481710, 40.8586979, -74.0683850)) + " miles")

if __name__ == '__main__':
	main()
#cd d:documents/school/Bergen\ Academies/programming/Data\ Structures\ -\ OS
#http://maps.googleapis.com/maps/api/directions/[xml or json]?origin=[]&destination=[]
#https://developers.google.com/api-client-library/python/start/get_started