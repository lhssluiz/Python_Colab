{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"class_theory.py","provenance":[],"authorship_tag":"ABX9TyPjDl/wctBWfjOjaTbKdSzl"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","metadata":{"id":"DTf6ayj5ofOd"},"source":["5h - 9/Abr\n","2h - 10/Abr\n","\n","A class acts as a set of instructions to create an instance\n","\n","Na programação orientada a objetos, escrevemos classes que representam entidades e situações do mundo real, e criamos objetos com base nessas classes. Quando escrevemos uma classe, definimos o comportamento geral que toda uma categoria de objetos pode ter.\n","Quando criamos objetos individuais a partir da classe, cada objeto será automaticamente equipado com o comportamento geral; então você poderá dar a cada objeto as características únicas que desejar. \n","Criar um objeto a partir de uma classe é uma operação conhecida como *instanciação*, assim, trabalhamos com instâncias de uma classe\n","\n","###### Method __init__() - The constructor\n","\n","The method __init__() is a special method in Python that execute automatically always that a instance based in Dog is created.\n","\n","it has 3 parameter, where *self* is obligated and always come before the others. When python calls the method, it'll pass the argument self automatically. All the calling of a method associated to a class pass *self*, that is a reference to the instance in itself automatically; it gives access to the others attributes and methods of the the individual instance.\n","\n","When we create a instance of Dog, Python will call the method __init__() from the class Dog; we'll give a name and a age as argument and self is passed automatically, thuus it's not necessary to specify it. Then, we'll need to provide values only to the other values and not for self.\n","\n","The variables defined has the prefix *self*. ANy variable prefixed with self, it's available to all the methos in the class. With this, we can access these variables trough any instance created from the class.\n","\n","_self.name = name_ uses the value saved in the parameter name, and then, store it in the variable name, that so, is associated to a created instance. \n","\n","Variables like this are called **attributes**\n","\n","The class Dog, has other 2 methods defined. As those methos don't need additional informations as a name and a age, we simply define it with the parameter _self_. The instances that we'll created then will have access to these methos. In other words it'll have the capacity to sit and roll_over.\n","\n","#### Resuming:\n","- Attributes are the variables \n","- Methos are behaviours (the functions)\n","\n","Class, it's like to create a \"built-in type\" that you design. Then, it's a design for the type of the varilables and methos. Thus, any instance from it will behave like it was design \"defined inside the class\". Imagine, that when you create a variable a = 5.5 it'll behave like a float. This is similar to what happen for a instance of a class, the instance, will behave like the class was defined. \n","\n","Integer, String, Float are classes as well. \n","Class is also treated as a template to create an object.\n","Init as a constructor initialize that \"being\" inside the class\n","\n","When you pass the object, you're passing the arguments in itself, this goes to *self*\n","\n","Reference: \n","https://www.youtube.com/watch?v=8O5kX73OkIY\n","\n","https://www.youtube.com/watch?v=SQXmC6PbZWk\n","\n","https://www.youtube.com/watch?v=WIP3-woodlU\n","\n","https://www.youtube.com/watch?v=ic6wdPxcHc0\n","\n","https://www.youtube.com/watch?v=9wd50TKv_OQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=63\n","\n","https://youtu.be/9wd50TKv_OQ It's a good reference to show the behaviours of classes and why to create a new one -> to have new behaviour"]},{"cell_type":"markdown","metadata":{"id":"-8zl8luBm0qj"},"source":["#### Why Classes\n","1. Modularity for easier troubleshooting: When working with object-oriented programming languages, you know exactly where to look. “Oh, the car object broke down? The problem must be in the Car class!” You don’t have to muck through anything else.\n","\n","2. **Reuse of code through inheritance**\n","Suppose that in addition to your Car object, one colleague needs a RaceCar object, and another needs a Limousine object. Everyone builds their objects separately but discover commonalities between them. In fact, each object is really just a different kind of Car. This is where the inheritance technique saves time: Create one generic class (Car), and then define the subclasses (RaceCar and Limousine) that are to inherit the generic class’s traits.\n","A class is a way of organizing information about a type of data so a programmer can reuse elements when making multiple instances of that data type"]},{"cell_type":"markdown","metadata":{"id":"h42gIzt_pXKi"},"source":["#### Size of a object\n","Always when you initialize (instance a object) a class, a space on the memory will be allocated to that constructuion. The size will depends of the amount of variable"]},{"cell_type":"markdown","metadata":{"id":"8sK3Thfqqi_l"},"source":["#### Self\n","It's who reference to the right objects. So, when instance a object and call a class, the self will understand that what to pass to the class and whom to call. Ex:\n","c1.update()\n","_Info:_ update is a method inside a class\n","\n","name_object.method(who is calling, others)"]},{"cell_type":"markdown","metadata":{"id":"w3uNvlzAsoHg"},"source":["#### Instance variables and Static variables\n","To define a static variable, you need to create it out of the methods and in the class, this will be global inside the class, it'll go for everyone in the class.\n","\n","The instance ones, are the varilable inside a method"]},{"cell_type":"markdown","metadata":{"id":"XR6daNBRtTKO"},"source":["#### Types of methods\n","- Instance Methods: If you want to work with this method, you use _self_\n","- Class methods: If you want to use this methogs, you use _cls_. This type of method, execute to anything in the class, it's global for the class. To define as a class methof you also need to use _@classmethod_\n","- Static methods: A method that doesn't deal with the variables and other methods inside the class"]},{"cell_type":"markdown","metadata":{"id":"mM19iJVkzmop"},"source":["#### Classs inside a class\n","You create norally inside the Outer class. But create another one will give similar result, it has a specific usage"]},{"cell_type":"markdown","metadata":{"id":"4YO9O2DC1dy9"},"source":["#### Inheritance - When you want to use existing feature in other class\n","You can pass the values from one parent class - decided by you - to a child class - also decided by you - only adding tho the child class the name of the parent class. \n","Sub class can access all the features from the super classl, but the inverse cannot happen\n","Ex:\n","\n","class A: #super class\n","  def do_something()\n","\n","class B(A): #sub class\n","  def do_other_something()\n","\n","In this case, everything the A is capable to to, it'll go also to B, since we defined B as a child of A.\n","\n","Also has the multilevel inheritance, when you add to a class a already child class. Then, it'll behave like the parent of it and the parent of the defined child one\n","\n","class A:\n","  def do_something()\n","\n","class B(A):\n","  def do_other_something()\n","\n","class C(B):\n","  def do_other2_somehint()\n","\n","C can behave like B and consequently like A\n","\n","#### Multiple inheritance\n","It's possible to get the behaviour of more than one class, to do so, you need just to define as a argument all the classes you want to get the behaviour\n","\n","Ex:\n","class C(A,B):\n","  def do_A_and_B_behaviour()"]},{"cell_type":"markdown","metadata":{"id":"B8M-izwQ5zEx"},"source":["#### inheritance of constructor\n","\n","super().__init__()\n","\n","You can call the constructor of both classes. It need to be defined in the subclass"]},{"cell_type":"markdown","metadata":{"id":"2iuHBOW--xut"},"source":[""]}]}