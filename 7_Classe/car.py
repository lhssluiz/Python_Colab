class Car():
  '''A simple sample to represent a car'''
  
  def __init__(self,make,model,year):
    '''Initiate the attributes that decribe a car'''
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_decriptive_name(self):
    '''Return a decriptive name, elegantly formatted'''
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()
  
  def read_odometer(self):
    '''Shows a sentence with the car's miles'''
    print("This car has " + str(self.odometer_reading) + " miles on it.")
  
  def update_odometer(self,mileage):
    '''Method to update odometer and rejects minor values than the current'''
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")
  
  def increment_odometer(self,miles):
    '''Sum que amount specified to the reading value'''
    self.odometer_reading += miles

class Battery():
  '''A try to simply modelate a battery'''

  def __init__(self, battery_size=70):
    '''initialize the attributes of the battery'''
    self.battery_size = battery_size
  
  def describe_battery(self):
    '''Presents a sentence to shows the capacity of the battery'''
    print("This car has a " + str(self.battery_size) + "-kWh battery.")
  
  def get_range(self):
    '''Shows a sentence aobut the distance that 
    the car is capable to run with this battery level'''
    if self.battery_size == 70:
      range = 240
    elif self.battery_size == 85:
      range = 270
    message = "This car can go approximately " + str(range) 
    message += " miles on a full charge."
    print(message) 
    #A way to present two lines of text
  
  def upgrade_battery(self):
    if self.battery_size != 85:
      self.battery_size = 85

class ElectricCar(Car):
  '''Represents specific aspects of electric vehicles
  Then initialize the attributes for electric cars'''

  def __init__(self,make,model,year):
    '''Initialize the attributes of dad's class'''
    super().__init__(make, model,year)
    self.battery = Battery()