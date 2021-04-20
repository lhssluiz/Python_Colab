class Restaurant:

  def __init__(self,name,description):
    self.name = name
    self.description = description
  
  def describe_restaurant(self):
        print("The restarant " + self.name + " has this cuisine type " + self.description +"." )

  def open_restaurant(self):
    print("The restaurant " + self.name + " is open!")


class IceCreamStand(Restaurant):
  '''Represents a Ice Cream Stand
  Also takes Restaurant as a superclass'''
  def __init__(self, name,description):
    super().__init__(name,description)
    self.flavors = ['cupuaçu','açaí','tapioca']
  
  def show_flavors(self):
    for flavors in self.flavors:
      print(flavors.title())