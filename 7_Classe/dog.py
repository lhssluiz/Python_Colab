{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"dog.py","provenance":[],"authorship_tag":"ABX9TyM8V3xYC66RJpWqXibtknWF"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","metadata":{"id":"Fdw7Ap8Q-c0r"},"source":["## All the theory from this you you'll find in the file clas_theory.py"]},{"cell_type":"code","metadata":{"id":"oKq5A2_Di0rv","executionInfo":{"status":"ok","timestamp":1618069063508,"user_tz":180,"elapsed":971,"user":{"displayName":"Luiz Henrique","photoUrl":"https://lh3.googleusercontent.com/a-/AOh14GhQXe9GFDUIP3eqb9DI5wBQYAYy0_5U_zhD6TlAmdk=s64","userId":"14516069777358681975"}}},"source":["class Dog():\n","  '''It's a simple try to model a dog'''\n","  def __init__(self,name,age):\n","    self.name = name\n","    self.age = age\n","  \n","  def sit(self):\n","    '''Simulates a dog sitting in a answer to a command'''\n","    print(self.name.title() + \" is now sitting.\")\n","\n","  def roll_over(self):\n","    '''Simulates a dog rolling over in a answer to a command'''\n","    print(self.name.title() + \" rolled over!\")\n","\n","# Start by the definition of the class, with the reserved word class\n","# The convention is to use the first letter in capital format\n","# A function as a part of a class, it's called a method\n","# The method _init_() is a special method in Python that execute automatically\n","# always that a instance based in Dog is created"],"execution_count":2,"outputs":[]},{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"mN-crzNRl3BY","executionInfo":{"status":"ok","timestamp":1618069293231,"user_tz":180,"elapsed":841,"user":{"displayName":"Luiz Henrique","photoUrl":"https://lh3.googleusercontent.com/a-/AOh14GhQXe9GFDUIP3eqb9DI5wBQYAYy0_5U_zhD6TlAmdk=s64","userId":"14516069777358681975"}},"outputId":"77b82437-a7b9-4f0f-c2d5-e57fb69826ac"},"source":["'''my_dog is self in this case\n","The name and the age is given by the other arguments\n","\n","init creates an instance (a space in the memory) to store\n","self, name and age. It hasn't a specific _return_, but it \n","return the automatically the instance that represents this dog\n","'''\n","my_dog = Dog('willie',6)\n","\n","print(\"My dog's name is \" + my_dog.name.title() + \".\")\n","print(\"My dog is \" + str(my_dog.age) + \" years old.\")"],"execution_count":4,"outputs":[{"output_type":"stream","text":["My dog's name is Willie.\n","My dog is 6 years old.\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"p7VIWfwIdL8V","executionInfo":{"status":"ok","timestamp":1618069623831,"user_tz":180,"elapsed":710,"user":{"displayName":"Luiz Henrique","photoUrl":"https://lh3.googleusercontent.com/a-/AOh14GhQXe9GFDUIP3eqb9DI5wBQYAYy0_5U_zhD6TlAmdk=s64","userId":"14516069777358681975"}},"outputId":"dc4112b9-7691-486e-e5dd-4e24280e04ad"},"source":["## Calling the methods inside the class\n","#\n","# Specify the name of the instance created, then the method separated by (.)\n","my_dog.sit()\n","my_dog.roll_over()"],"execution_count":6,"outputs":[{"output_type":"stream","text":["Willie is now sitting.\n","Willie rolled over!\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"ASOL3xt0eHK6","executionInfo":{"status":"ok","timestamp":1618069898816,"user_tz":180,"elapsed":873,"user":{"displayName":"Luiz Henrique","photoUrl":"https://lh3.googleusercontent.com/a-/AOh14GhQXe9GFDUIP3eqb9DI5wBQYAYy0_5U_zhD6TlAmdk=s64","userId":"14516069777358681975"}},"outputId":"fae23f7c-7f7d-4b6b-93b0-a9847f2ae4c6"},"source":["your_dog = Dog('wilson',17)\n","print(\"My dog's name is \" + my_dog.name.title() + \".\")\n","print(\"My dog is \" + str(my_dog.age) + \" years old.\")\n","print(\"\\n\")\n","print(\"My dog's name is \" + your_dog.name.title() + \".\")\n","print(\"My dog is \" + str(your_dog.age) + \" years old.\")"],"execution_count":10,"outputs":[{"output_type":"stream","text":["My dog's name is Willie.\n","My dog is 6 years old.\n","\n","\n","My dog's name is Wilson.\n","My dog is 17 years old.\n"],"name":"stdout"}]},{"cell_type":"markdown","metadata":{"id":"hR7PJ0JKfS6v"},"source":["## Faça você mesmo"]}]}