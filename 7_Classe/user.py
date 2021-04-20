from admin_privileges import Admin
from admin_privileges import Privileges


class User:

  def __init__(self,first_name,last_name,id_info,log_attempts):
    self.name = first_name
    self.surname = last_name
    self.id = id_info
    self.login_attempts = log_attempts
  
  def describe_user(self):
    '''Describe the user informations'''
    print("This are all the informations, about me: ")
    print("\t-" + self.name)
    print("\t-" + self.surname)
    print("\t-" + str(self.id))
  
  def greet_user(self):
    '''Shows a greeting to the user'''
    print("Hello "+ self.name + " " + self.surname + " I'm glad to see you here!")
  
  def increment_login_attempts(self):
    '''Increment the login attempts of a user'''
    self.login_attempts += 1
  
  def reset_login_attempts(self):
    '''Back the login attempts to zero'''
    self.login_attempts = 0