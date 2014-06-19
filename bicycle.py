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

class Factory(object):
	def __init__(self,factory_name,markup):
		self.factory_inv = []
		self.factory_name = factory_name
		self.markup = markup

	def print_factory_inv(self):                
		print 'Current ' + self.factory_name + ' inventory:'
	 	for i in range(0,len(self.factory_inv)):
 	 		print self.factory_inv[i]  #.self.factory_name
		# print '*******************************'	

schwinn = Factory('Schwinn',1.25)   # Build two factories
trek    = Factory('Trek',1.45)

class DesignModel(object):
	def __init__(self,model_name,factory,Wheel,Frame):
		self.factory_name = factory.factory_name
		self.model_name = model_name
		self.markup = factory.markup	
		self.wheel = Wheel
		self.frame = Frame
		self.manu_cost = 2 * Wheel.cost + Frame.cost	
		self.weight = Wheel.weight + Frame.weight

	def S_build_bike(self):
		schwinn.factory_inv.append(str(self.model_name))
	
	def T_build_bike(self): 
		trek.factory_inv.append(str(self.model_name))

schwinn_a = DesignModel('Schwinn A-2100',schwinn,wheel_1, frame_1)
schwinn_b = DesignModel('Schwinn B',schwinn,wheel_2, frame_1)
schwinn_c = DesignModel('Schwinn C',schwinn,wheel_2, frame_3)
trek_a =    DesignModel('Trek A',trek,wheel_3, frame_3)
trek_b =    DesignModel('Trek B',trek,wheel_1, frame_3)
trek_c =    DesignModel('Trek C',trek,wheel_2, frame_3)

schwinn_a.S_build_bike()
schwinn_b.S_build_bike()
schwinn_c.S_build_bike()

# print schwinn.factory_inv

trek_a.T_build_bike()
trek_b.T_build_bike()
trek_c.T_build_bike()

# print trek.factory_inv

schwinn.print_factory_inv()

raise SystemExit


# 	def print_factory_inv(self):                # Example of call: schwinn.print_factory_inv()
# 		print 'Current ' + self.name + ' inventory:'
# 		for i in range(0,len(self.factory_inv)):
#  			print self.factory_inv[i].name
# 		print '*******************************'		

# 	def pop_factory_inv(self,model): # Takes passed in Manufacturer and pops model from list
# 		# self.model = model
# 	 	factory_index = self.factory_inv.index(model)
# 	 	self.factory_inv.pop(factory_index)

# 	def calc_wholesale_cost(self,model): # Calculates wholesale price
# 		wholesale_cost = model.manu_cost*self.markup
# 		print wholesale_cost

# schwinn = Manufacturer('Schwinn',1.2)   # Create 2 manufacturers
# trek = Manufacturer('Trek',1.4)

# schwinn.build_bike(schwinn_a)  # Add 3 bike models for schwinn
# schwinn.build_bike(schwinn_c)
# schwinn.build_bike(schwinn_b)

# trek.build_bike(trek_a)  # Add 3 bike models for trek
# trek.build_bike(trek_c)
# trek.build_bike(trek_b)

# class BikeShop(object):                     # Make Bicycle Shop
# 	def __init__(self,name,markup):
# 		self.name = name
# 		self.markup = markup # Markup Rate from wholesale price
# 		self.shop_inv = []

# 	def buy_bike(self,model):
# 		self.shop_inv.append(model)
# 		# self.pop_factory_inv(model)

# 	def print_shop_inv(self):               
# 		print 'Current ' + self.name + ' inventory:'
# 		for i in range(0,len(self.shop_inv)):
#  			print self.shop_inv[i].name
# 		print '*******************************'	
	
# 	def pop_shop_inv(self,model): # Takes passed in BikeShop and pops model from list
# 		shop_index = self.shop_inv.index(model)
# 	 	self.shop_inv.pop(shop_index)	

# 	def calc_retail_cost(self,model): # Calculates retail price
# 		# import Manufacturer calc_wholesale_cost
# 		retail_cost = Manufacturer.calc_wholesale_cost.wholesale_cost.model*self.markup
# 		print retail_cost

# summitcity = BikeShop('Summit City',1.2) # BikeShop created

# summitcity.buy_bike(schwinn_a)
# summitcity.buy_bike(schwinn_b)
# summitcity.buy_bike(schwinn_c)

# summitcity.calc_retail_cost(schwinn_a)
# summitcity.calc_retail_cost(schwinn_b)
# summitcity.calc_retail_cost(schwinn_c)

# raise SystemExit


# schwinn.print_factory_inv()
# schwinn.pop_factory_inv(schwinn_a)
# schwinn.print_factory_inv()

# print '$$$$$$$$$$$$$'

# summitcity.print_shop_inv()
# summitcity.pop_shop_inv(schwinn_a)
# summitcity.print_shop_inv()

