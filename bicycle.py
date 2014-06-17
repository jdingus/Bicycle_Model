class Wheel(object):
	def __init__(self,name,weight,cost):
		self.name = name 
		self.weight = weight
		self.cost = cost

wheel_1 = Wheel('SlowBurner',2.6,45)
wheel_2 = Wheel('FreeBurner',2.3,65)
wheel_3 = Wheel('FastBurner',2.1,95)

class Frame(object):
	def __init__(self,name,material,weight,cost):
		self.name = name
		self.material = material
		self.weight	= weight
		self.cost	= cost

frame_1 = Frame('low_frame','steel',12,65)
frame_2 = Frame('med_frame','aluminum',9,95)
frame_3 = Frame('high_frame','carbon',6,125)

class Bike_Model(object):
	def __init__(self,name,manufacturer,Wheel,Frame):
		self.name = name
		self.manufacturer = manufacturer
		self.wheel = Wheel
		self.frame = Frame
		self.cost = 2 * Wheel.cost + Frame.cost	

bike_1 = Bike_Model('Schwinn A','Schwinn',wheel_1, frame_1)
bike_2 = Bike_Model('Trek A','Trek',wheel_3, frame_3)
bike_3 = Bike_Model('Schwinn B','Schwinn',wheel_2, frame_1)
bike_4 = Bike_Model('Trek B','Trek',wheel_1, frame_3)
bike_5 = Bike_Model('Schwinn C','Schwinn',wheel_2, frame_3)
bike_6 = Bike_Model('Trek C','Trek',wheel_1, frame_3)

class Manufacturer(object):
	def __init__(self,name,margin):
		self.name = name
		self.models = []
		self.margin = margin

	def add_model(self,model):
		self.models.append(model)

schwinn = Manufacturer('Schwinn',1.2)   # Create 2 manufacturers required
trek = Manufacturer('Trek',1.4)

schwinn.add_model(bike_1)  # Add 3 bike models for schwinn
schwinn.add_model(bike_2) 
schwinn.add_model(bike_3)

trek.add_model(bike_4)  # Add 3 bike models for trek
trek.add_model(bike_5) 
trek.add_model(bike_6)

# Make Bicycle Shop
class BikeShop(object):
	def __init__(self,name,markup):
		self.name = name
		self.markup = markup # Markup Rate from wholesale price
		self.models = []

	def add_bike(self,model):
		self.models.append(model)

summitcity = BikeShop('Summit City',1.2)
summitcity.add_bike(bike_1)
summitcity.add_bike(bike_2)
summitcity.add_bike(bike_3)
summitcity.add_bike(bike_4)
summitcity.add_bike(bike_5)
summitcity.add_bike(bike_6)

for model in summitcity.models:
	print "Model: " + str(model.name) + " *** " + "Cost: " + str(model.cost)
# 	def calc_retail(self,)


# for models in schwinn.models:
# 	i=models.cost
# 	i+=models.cost
# print "Sum of all the models is $" + str(i)
# print "With tax that would be: $" + str(i*1.070)
