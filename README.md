# AirBnB clone - The console

![HBnB Logo](https://i.ibb.co/MMvC1rY/65f4a1dd9c51265f49d0.png)

### Project Description
This is our first project and prototype clone of AirBnB.

### Requirements & Installation
Have experience in python3, a linux terminal CLI (Command-Line Interface) that will work as the enviroment of the project.

For install and setup our prototype you will need to first clone it with this command:
```
sudo git clone https://github.com/alejogonza/AirBnB_clone.git
```
then paste it on your terminal and press enter.

## How to use
Opening the console you'll need to navigate to the project folder name as "AirBnB" then enter ./console.py in your terminal the user will meet a prompt labelled "(hbnb)" in your interface, all set and ready for usage.

### List of Commands
| **Command name** | **Description** |
| ---------------- | --------------- |
|[all] | Shows all objects of one type or all types |
|[create] | Creates an object |
|[destroy] | Deletes an object based on class name and ID (Saves the change into the JSON file) |
|[help] | Shows the description of all commands |
|[quit/EOF] | Exit the console |
|[show] | shows an object based on class name & ID |
|[update] | Updates an object based on the class name and ID by adding or updating attribute (Saves the change into the JSON file) |

### Supported Classes
 - BaseModel
 - User
 - State
 - City
 - Amenity
 - Place
 - Review

### Example of how to use the console
```
➜  AirBnB_clone git:(master) ✗ sudo ./console.py
(hbnb) create User
052e6ea1-2072-4fe4-9f50-ab73559904e8
(hbnb) show User Traceback (most recent call last):
(hbnb) quit
➜  AirBnB_clone git:(master) ✗ sudo ./console.py
(hbnb) destroy User
** instance id missing **
(hbnb) destroy User 052e6ea1-2072-4fe4-9f50-ab73559904e8
(hbnb) all
[[BaseModel] (76245c41-79a1-423a-a77a-f5a9f78ad08e) {'created_at': datetime.datetime(2019, 11, 13, 23, 0, 12, 723784), 'updated_at': datetime.datetime(2019, 11, 13, 23, 0, 12, 723784), 'name': 'Holberton', 'id': '76245c41-79a1-423a-a77a-f5a9f78ad08e', 'my_number': 98}, [BaseModel] (3888a04f-f227-4f94-8530-24f913a325e5) {'created_at': datetime.datetime(2019, 11, 13, 23, 0, 12, 724266), 'updated_at': datetime.datetime(2019, 11, 13, 23, 0, 12, 724280), 'id': '3888a04f-f227-4f94-8530-24f913a325e5'}, [BaseModel] (9e711c10-7532-4a1f-af09-910f57f2a713) {'created_at': datetime.datetime(2019, 11, 13, 23, 0, 12, 724034), 'updated_at': datetime.datetime(2019, 11, 13, 23, 0, 12, 724034), 'id': '9e711c10-7532-4a1f-af09-910f57f2a713'}]
(hbnb) exit
*** Unknown syntax: exit
(hbnb) quit
➜  AirBnB_clone git:(master) ✗
```

## Built with
python3 (3.4.3)

### Authors
Alejandro Gonzalez Serna - @alejogonza
David Bravo Beltran - @dbravo0
