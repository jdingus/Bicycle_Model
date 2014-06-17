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
		self.weight = Wheel.weight + Frame.weight

schwinn_a = Bike_Model('Schwinn A-2100','Schwinn',wheel_1, frame_1)
schwinn_b = Bike_Model('Schwinn B','Schwinn',wheel_2, frame_1)
schwinn_c = Bike_Model('Schwinn C','Schwinn',wheel_2, frame_3)
trek_a = Bike_Model('Trek A','Trek',wheel_3, frame_3)
trek_b = Bike_Model('Trek B','Trek',wheel_1, frame_3)
trek_c = Bike_Model('Trek C','Trek',wheel_1, frame_3)

class Manufacturer(object):
	def __init__(self,name,margin):
		self.name = name
		self.factory_inv = []
		self.margin = margin

	def build_bike(self,model):   
		self.factory_inv.append(model)

schwinn = Manufacturer('Schwinn',1.2)   # Create 2 manufacturers
trek = Manufacturer('Trek',1.4)

schwinn.build_bike(schwinn_a)  # Add 3 bike models for schwinn
schwinn.build_bike(schwinn_c)
schwinn.build_bike(schwinn_b)

trek.build_bike(trek_a)  # Add 3 bike models for trek
trek.build_bike(trek_c)
trek.build_bike(trek_b)

# for i in range(0,len(schwinn.factory_inv)):
# 	print schwinn.factory_inv[i].name

# print schwinn.factory_inv
# print trek.factory_inv

class BikeShop(object):                     # Make Bicycle Shop
	def __init__(self,name,markup):
		self.name = name
		self.markup = markup # Markup Rate from wholesale price
		self.bike_inv = []

	def buy_bike(self,model):
		self.bike_inv.append(model)

summitcity = BikeShop('Summit City',1.2) # BikeShop created

summitcity.buy_bike(schwinn_a)
summitcity.buy_bike(schwinn_b)
summitcity.buy_bike(schwinn_c)

model_to_buy = schwinn_b
factory_index = schwinn.factory_inv.index(model_to_buy)
print factory_index
print schwinn.factory_inv[factory_index].name


# print summitcity.bike_inv[inv_index].weight
# summitcity.bike_inv.pop(inv_index)
# print summitcity.bike_inv[0].name

# for i in range(0,len(summitcity.bike_inv)):
# 	print summitcity.bike_inv[i].name

