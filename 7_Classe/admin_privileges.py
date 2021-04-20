from user import User

class Admin(User):
  '''This clas represents a special user
  with total power on the system'''

  def __init__(self,first_name,last_name,id_info,log_attempts):
    super().__init__(first_name,last_name,id_info,log_attempts)
    self.privileges_admin = Privileges()

#9.8
class Privileges():

  def __init__(self,privileges_admin=['can add post','can delete post','can be user']):
    self.privileges_admin = privileges_admin

  def show_privileges(self):
    print("These are all your rights: ")
    for rights in self.privileges_admin:
      print(rights)