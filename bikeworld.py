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
	
	def build_bike(self,model):
		"""on factory schwinn take model schwinn_a.name and append to factory_inv[]""" 
		self.factory_inv.append(model.model_name)

	def sell_bike(self,model):
		"""on factory schwinn take model schwinn_a.name and pop from factory_inv[]""" 
		index = self.factory_inv.index(model.model_name)
		self.factory_inv.pop(index)

	def print_factory_inv(self):                
		print 'Current ' + self.factory_name + ' inventory:'
	 	for i in range(0,len(self.factory_inv)):
 	 		print self.factory_inv[i] #.self.factory_name
		# print '*******************************'	

class BikeShop(object):
	def __init__(self,name,markup):
		self.inventory = []
		self.name = name
		self.markup = markup
	
	def shop_buy_bike(self,model):
		"""on shop summitciy take model schwinn_a.name and append to .inventory[]""" 
		self.inventory.append(model.model_name) # add model name to shop inventory[]
		index = model.factory_name.factory_inv.index(model.model_name)
		model.factory_name.factory_inv.pop(index)

	def shop_sell_bike(self,model):
		"""on shop summitciy take model schwinn_a.name and pop from .inventory[]""" 
		index = self.inventory.index(model.model_name)
		self.inventory.pop(index)
		# print self.inventory

	def print_inventory(self):                
		print 'Current ' + self.name + ' inventory:'
	 	for i in range(0,len(self.inventory)):
 	 		print self.inventory[i] 
		# print '*******************************'	

	def print_weight(self):

		for i in range(0,len(self.inventory)):
			print self.inventory[i]

class DesignModel(object):
	def __init__(self,model_name,factory,Wheel,Frame):
		self.factory_name = factory
		self.model_name = model_name
		self.markup = factory.markup	
		self.wheel = Wheel
		self.frame = Frame
		self.manu_cost = 2 * Wheel.cost + Frame.cost
		self.retail_cost = self.manu_cost*factory.markup	
		self.weight = Wheel.weight + Frame.weight

class Customer(object):
	
	def __init__(self,name,budget):
		self.name = name
		self.budget = budget

	def cust_buy_bike(self,shop,model):
		cost_bike = model.retail_cost
		self.budget = self.budget-cost_bike
		shop.shop_sell_bike(model)
		# print self.budget
		# self.budget -= shop.model.retail_cost
		# print self.budget
		

		# schwinn.pop_shop_inv(model.model_name) # Remove from factory inventory
		# self.cust_inv.append(model.model_name)


