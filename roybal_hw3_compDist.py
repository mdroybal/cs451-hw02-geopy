#Monte Roybal
#Dr. Richard Medina
#9-16-18
#Simple Python Utility: Compute Distance Between Two Locations

from geopy.distance import geodesic
from geopy.geocoders import Nominatim

#Compute Location Class
class Compute_Loc():
	def __init__(self,address="",location=""):
		"""Class Attributes"""
		self.address = address
		self.location = location

	def __str__(self):
		return "{}".format(self.location.address)

	def get_addr(self):#Function to Get address from user input
		self.address = raw_input("")
		self.get_loc()

	def get_loc(self):#Function to Get location with call to geopy function
		self.location = geolocator.geocode(self.address)

class Coordinates():
	def __init__(self,coordinates=""):
		self.coordinates = coordinates

	def __str__(self):
		return "Coordinates are {}".format(self.coordinates)

	def get_coors(self,loc):
		self.coordinates = (loc.latitude,loc.longitude)

class Compute_Dist():    
    def __init__(self,distance=0):
    	self.distance = distance
    
    def __str__(self):
    	return "Distance is:{}".format(get_dist())

    def get_dist(self,locA,locB):
    	return (geodesic(locA,locB).miles)


if __name__ == "__main__":
	geolocator = Nominatim()
	locationA = Compute_Loc()
	coordinatesA = Coordinates()
	locationB = Compute_Loc()
	coordinatesB = Coordinates()
	distance = Compute_Dist()
	
	print "Please enter a starting address:"
	locationA.get_addr()
	print "\nPlease enter an ending address:"
	locationB.get_addr()
	coordinatesA.get_coors(locationA.location)
	coordinatesB.get_coors(locationB.location)

	print "\nDistance between {} and {} is {} miles.".format(locationA,locationB,distance.get_dist(coordinatesA.coordinates,coordinatesB.coordinates))
