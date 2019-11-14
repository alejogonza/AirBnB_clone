# AirBnB clone - The console

![HBnB Logo](https://i.ibb.co/MMvC1rY/65f4a1dd9c51265f49d0.png)

## Project Description :page_facing_up:
This is our first project and prototype clone of AirBnB.

## Requirements & Installation :memo:
Have experience in python3, a linux terminal CLI (Command-Line Interface) that will work as the enviroment of the project.

For install and setup our prototype you will need to first clone it with this command:
```
sudo git clone https://github.com/alejogonza/AirBnB_clone.git
```
then paste it on your terminal and press enter.

## How to use :wrench:
Opening the console you'll need to navigate to the project folder name as "AirBnB" then enter ./console.py in your terminal the user will meet a prompt labelled "(hbnb)" in your interface, all set and ready for usage.

### List of Commands
| **Command name** | **Description** |
| ---------------- | --------------- |
|[all] | Shows all objects of one type or all types |
|[create] | Creates an object |
|[destroy] | Deletes an object based on class name and ID (Saves the change into the JSON file) |
|[help] | Shows the description of all commands |
|[quit/EOF] | Exit the console |
|[show] | Shows an object based on class name & ID |
|[update] | Updates an object based on the class name and ID by adding or updating attribute (Saves the change into the JSON file) |
|["class".all()] | Retrieve all instances of a class |
|["class".count()] | Retrieve the number of instances of a class |
|["class".destroy("id")] | Destroy an instance based on his ID |
|["class".update("id", "attribute name", "attribute value")] | Destroy an instance based on his ID |
|["class".update("id", "dictionary representation")] | Update an instance based on his ID with a dictionary|

## Supported Classes :clipboard:
 - BaseModel
 - User
 - State
 - City
 - Amenity
 - Place
 - Review

### Example of how to use the console
```
ferox@ferox-PC:~/Desktop/AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create User
0343c4d2-e8ed-4f4f-8882-e6210707296a
(hbnb)
(hbnb) all
[[User] (0343c4d2-e8ed-4f4f-8882-e6210707296a) {'updated_at': datetime.datetime(2019, 11, 13, 22, 19, 13, 374454), 'id': '0343c4d2-e8ed-4f4f-8882-e6210707296a', 'created_at': datetime.datetime(2019, 11, 13, 22, 19, 13, 374417)}]
(hbnb)
(hbnb) show User 0343c4d2-e8ed-4f4f-8882-e6210707296a
[User] (0343c4d2-e8ed-4f4f-8882-e6210707296a) {'created_at': datetime.datetime(2019, 11, 13, 22, 19, 13, 374417), 'updated_at': datetime.datetime(2019, 11, 13, 22, 19, 13, 374454), 'id': '0343c4d2-e8ed-4f4f-8882-e6210707296a'}
(hbnb)
(hbnb) update User 0343c4d2-e8ed-4f4f-8882-e6210707296a first_name Alejandro
(hbnb) show User 0343c4d2-e8ed-4f4f-8882-e6210707296a
[User] (0343c4d2-e8ed-4f4f-8882-e6210707296a) {'first_name': 'Alejandro', 'id': '0343c4d2-e8ed-4f4f-8882-e6210707296a', 'created_at': datetime.datetime(2019, 11, 13, 22, 19, 13, 374417), 'updated_at': datetime.datetime(2019, 11, 13, 22, 21, 28, 532452)}
(hbnb)
(hbnb) destroy User 0343c4d2-e8ed-4f4f-8882-e6210707296a
(hbnb) all
[]
(hbnb) EOF
ferox@ferox-PC:~/Desktop/AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) quit
ferox@ferox-PC:~/Desktop/AirBnB_clone$ ./console.py
(hbnb)
(hbnb) User.all()
[[User] (0de49b2f-0fd8-4167-9112-5024732cca9d) {'updated_at': datetime.datetime(2019, 11, 13, 22, 24, 47, 718248), 'id': '0de49b2f-0fd8-4167-9112-5024732cca9d', 'created_at': datetime.datetime(2019, 11, 13, 22, 24, 47, 718211)}]
(hbnb) 
(hbnb) User.count()
1
(hbnb) 
(hbnb) User.update("0de49b2f-0fd8-4167-9112-5024732cca9d", {'first_name': "Alejandro", "age": 18})
(hbnb) 
(hbnb) User.destroy("0de49b2f-0fd8-4167-9112-5024732cca9d")
(hbnb) 
(hbnb) User.count()
0
(hbnb) quit
ferox@ferox-PC:~/Desktop/AirBnB_clone$

```

### Built with
python3 (3.4.3)

## Authors
Alejandro Gonzalez Serna - @alejogonza
David Bravo Beltran - @dbravo0
