class Wheel(object):
	def __init__(self,name,weight,cost):
		self.name = name 
		self.weight = weight
		self.cost = cost

class Frame(object):
	def __init__(self,name,material,weight,cost):
		self.name = name
		self.material = material
		self.weight	= weight
		self.cost	= cost

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
	
	def pop_factory_inv(self,model): # Takes passed in Manufacturer and pops model from list
		self.model = model
	 	factory_index = self.factory_inv.index(model)
	 	self.factory_inv.pop(factory_index)

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

class BikeShop(object):                     # Make Bicycle Shop
	def __init__(self,name,markup):
		self.name = name
		self.markup = markup # Markup Rate from wholesale price
		self.shop_inv = []
		self.running_profit = 0 # Used for caculating profit when bike is sold initalize at 0

	def s_buy_bike(self,model): # BikeShop buys a bike from Factory, costs are calculated and inventory moved
		self.model = model
		self.model.wholesale_cost = model.manu_cost*self.markup
		self.model.retail_cost = self.model.wholesale_cost*self.markup
		schwinn.pop_factory_inv(model.model_name) # Remove from factory inventory
		self.shop_inv.append(model.model_name)
	
	def t_buy_bike(self,model): # BikeShop buys a bike from Factory, costs are calculated and inventory moved
		self.model = model
		self.model.wholesale_cost = model.manu_cost*self.markup
		self.model.retail_cost = self.model.wholesale_cost*self.markup
		trek.pop_factory_inv(model.model_name) # Remove from factory inventory
		self.shop_inv.append(model.model_name)

	def pop_shop_inv(self,model): # Takes passed in Manufacturer and pops model from list
		self.model = model
		shop_index = self.shop_inv.index(model)
		self.shop_inv.pop(shop_index)

	def sell_bike(self,model,customer): # BikeShop sells bike removes from shop_inv list
		self.model = model
		self.customer = customer
		self.pop_shop_inv(model.model_name) # Remove from shop inventory
		self.sale_profit = model.retail_cost-model.wholesale_cost #- self.model.wholesale_cost
		self.running_profit = self.running_profit+self.sale_profit
		print ''
		print 'You just sold a ' + str(model.model_name) + ' to :' + str(self.customer.name) + '!'
		print 'You just made : $'+ str(self.sale_profit) + ' on this sale!'
		print 'So far you have profited $' + str(self.running_profit) + "."
		print ''

class Customer(object):
	
	def __init__(self,name,budget):
		self.name = name
		self.budget = budget

		# schwinn.pop_shop_inv(model.model_name) # Remove from factory inventory
		# self.cust_inv.append(model.model_name)

# Make some wheels ** name,weight,cost
wheel_1 = Wheel('SlowBurner',2.6,45)
wheel_2 = Wheel('FreeBurner',2.3,65)
wheel_3 = Wheel('FastBurner',2.1,95)

# Make some frames ** name,material,weight,cost
frame_1 = Frame('low_frame','steel',12,65)
frame_2 = Frame('med_frame','aluminum',9,95)
frame_3 = Frame('high_frame','carbon',6,125)

# Build the Factory instances ** name, markup
schwinn = Factory('Schwinn',1.25)   # Build two factories
trek    = Factory('Trek',1.45)

# Create the bike models ** model_name,factory,Wheel,Frame
schwinn_a = DesignModel('Schwinn A-2100',schwinn,wheel_1, frame_1)
schwinn_b = DesignModel('Schwinn B',schwinn,wheel_2, frame_1)
schwinn_c = DesignModel('Schwinn C',schwinn,wheel_2, frame_3)
trek_a =    DesignModel('Trek A',trek,wheel_3, frame_3)
trek_b =    DesignModel('Trek B',trek,wheel_1, frame_3)
trek_c =    DesignModel('Trek C',trek,wheel_2, frame_3)

# Build the bikes at Factory using the bike models we created above ** 
schwinn_a.S_build_bike()
schwinn_b.S_build_bike()
schwinn_c.S_build_bike()
trek_a.T_build_bike()
trek_b.T_build_bike()
trek_c.T_build_bike()

# Build a BikeShop ** name,markup
summitcity = BikeShop('Summit City',1.2) 

billy = Customer('Billy',1000) # Make Customer ** Name, Budget
ray = Customer('Ray',500) # Make Customer ** Name, Budget
wanda = Customer('Wanda',200) # Make Customer ** Name, Budget
# Buy particular bike models at BikeShop takes inventory from Factory
summitcity.s_buy_bike(schwinn_a)
summitcity.s_buy_bike(schwinn_c)
summitcity.s_buy_bike(schwinn_b)
summitcity.t_buy_bike(trek_a)
summitcity.t_buy_bike(trek_c)
summitcity.t_buy_bike(trek_b)

# print summitcity.shop_inv


summitcity.sell_bike(schwinn_b,billy)
print schwinn.factory_inv
print summitcity.shop_inv
summitcity.sell_bike(schwinn_a,ray)
print schwinn.factory_inv
print summitcity.shop_inv
summitcity.sell_bike(schwinn_c,wanda)
print schwinn.factory_inv
print summitcity.shop_inv
# summitcity.sell_bike(schwinn_a)
# summitcity.sell_bike(trek_a)
# print summitcity.shop_inv


