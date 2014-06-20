from bikeworld import Wheel,Frame,Factory,DesignModel,BikeShop,Customer

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
schwinn.build_bike(schwinn_a)
schwinn.build_bike(schwinn_b)
schwinn.build_bike(schwinn_c)

trek.build_bike(trek_a)
trek.build_bike(trek_b)
trek.build_bike(trek_c)

# trek.print_factory_inv()
# schwinn.print_factory_inv()

# Build a BikeShop ** name,markup
summitcity = BikeShop('Summit City',1.2)

# Have shop buy some bike models
summitcity.shop_buy_bike(schwinn_a)
summitcity.shop_buy_bike(schwinn_b)
summitcity.shop_buy_bike(schwinn_c)

# summitcity.print_inventory()

# schwinn.print_factory_inv()

summitcity.shop_buy_bike(trek_a)
summitcity.shop_buy_bike(trek_b)
summitcity.shop_buy_bike(trek_c)

# summitcity.print_inventory()

# trek.print_factory_inv()

# Have shop sell a bike model
# summitcity.shop_sell_bike(trek_a)

# summitcity.print_inventory()

# raise SystemExit

# Make some customers with a 'name, budget'
billy = Customer('Billy',1000) # Make Customer ** Name, Budget
ray = Customer('Ray',500) # Make Customer ** Name, Budget
wanda = Customer('Wanda',200) # Make Customer ** Name, Budget

# Customer buys a bike


billy.cust_buy_bike(summitcity,trek_c)

summitcity.print_weight()


