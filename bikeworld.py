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
	def __init__(self,name,markup):
		self.name = name
		self.inv = []
		self.markup = markup
	
	def build_bike(self,model):
		"""on factory schwinn take model schwinn_a.name and append to factory_inv[]""" 
		self.inv.append(model)

	def sell_bike(self,model):
		"""on factory schwinn take model schwinn_a.name and pop from factory_inv[]""" 
		index = self.inv.index(model)
		self.inv.pop(index)

	def print_inv(self):                
		print 'Current ' + self.name + ' inventory:'
	 	for i in range(0,len(self.inv)):
 	 		print self.inv[i].name #.self.factory_name
		# print '*******************************'	


class DesignModel(object):
	def __init__(self,model_name,factory,wheel,frame):
		self.name = model_name
		self.factory = factory
		self.markup = factory.markup	
		self.wheel = wheel
		self.frame = frame
		self.manu_cost = 2 * wheel.cost + frame.cost
		self.retail_cost = self.manu_cost*factory.markup	
		self.weight = 2 * wheel.weight + frame.weight

class BikeShop(object):
	def __init__(self,name,markup):
		self.inv = []
		self.cust_list = []
		self.name = name
		self.markup = markup
		self.sold_count = 0
		self.profit = 0
	
	def buy_bike(self,model):
		"""on shop summitciy take model schwinn_a.name and append to .inventory[]""" 
		self.inv.append(model) # add model name to shop inventory[]
		index = model.factory.inv.index(model)
		model.factory.inv.pop(index)

	def sell_bike(self,model):
		"""on shop summitciy take model schwinn_a.name and pop from .inventory[]""" 
		index = self.inv.index(model)
		self.inv.pop(index)
		self.sold_count += 1
		profit = model.retail_cost - model.manu_cost
		self.profit += profit

	def print_name_wt(self):
		print ()
		print 'Current ' + self.name + ' Model listing with Weights:'
	 	for i in range(0,len(self.inv)):
 	 		print self.inv[i].name + ' : ' + str(self.inv[i].weight) + ' lbs'	
 	 	print ()

	def print_inv(self):                
		print 'Current ' + self.name + ' inventory:'
	 	for i in range(0,len(self.inv)):
 	 		print self.inv[i].name
		# print '*******************************'	

	def print_customer_report(self):
		""" Takes the cust_list and prints out all of the bikes they can afford """
		print self.name + ' Customer Report:'
		print ()
	 	for customer in range(0,len(self.cust_list)):
 	 		print 'Bikes recommended for : ' + self.cust_list[customer].name
 	 		print '--------------------------------------------'
 	 		for model in range(0,len(self.inv)):
 	 			if self.inv[model].retail_cost < self.cust_list[customer].budget:
 	 				print self.inv[model].name + ' : $'+str(self.inv[model].manu_cost)
 	 		print ()
 	 	print '****** CUSTOMER REPORT END ******'
 	 	print ()

class Customer(object):
	
	def __init__(self,name,budget):
		self.name = name
		self.budget = budget

	def buy_bike(self,shop,model):
		self.model = model
		cost_bike = model.retail_cost
		self.budget = self.budget-model.retail_cost
		shop.sell_bike(model)
		self.print_cust_log()

	def print_cust_log(self):
		print ()
		print self.name + ', Thank You for your purchase of the ' + self.model.name + ' : ' + '$' + str(self.model.retail_cost) + '.'
		print 'You have $' + str(self.budget) + ' left in your budget.'
		print 'Please Come Again!'
		print ()



	# def print_customers(self):
	# 	# print self.budget
	# 	# self.budget -= shop.model.retail_cost
	# 	# print self.budget

	def visit_store(self,shop):
		shop.cust_list.append(self)
		# schwinn.pop_shop_inv(model.model_name) # Remove from factory inventory
		# self.cust_inv.append(model.model_name)


