# Python-MVC-Template
A simple MVC template for all Python repositories that wants to create an application using this architecture.


*********************
##  USAGE

You should replace all the modules that contains "my_\<name>" and classes that contains "My\<Name>" with the respective names of your modules/classes

This includes the following files:

* App/src/Entities/my_entity.py 
    * And it's class "MyEntity" (with, for example, "Person" or "Animal");
* App/src/MVC/Model/MySQL.py
    * And it's class "MyDatabase" (with, for example, "MySQL" or "MongoDB").
* App/tests/Entities/test_my_entity.py
    * And it's class "TestMyEntity" (with the same name as you choose for your "MyEntity" Class).
* App/tests/MVC/Model/test_MySQL.py
    * And it's class "TestMyDatabase" (with the same name as you choose for your "MyDatabase" Class).