# AirBnB_clone - The Console
## Summary
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
## Command Interpreter(Console)
It is exactly the same as shell but limited to a specific use-case. In this case, we want to be able to manage the objects of our project:

        + Create a new object (ex: a new User or a new Place)
        + Retrieve an object from a file, a database etc…
        + Do operations on objects (count, compute stats, etc…)
        + Update attributes of an object
        + Destroy an object
## Example of using the Console in interactive and non-interactive way:
Interactive:

              $ ./console.py
              (hbnb) help

              Documented commands (type help <topic>):
              ========================================
              EOF  help  quit

              (hbnb) 
              (hbnb) 
              (hbnb) quit
              $
              
Non-Interactive:

               $ echo "help" | ./console.py
               (hbnb)

               Documented commands (type help <topic>):
               ========================================
               EOF  help  quit
               (hbnb) 
               $
               $ cat test_help
               help
               $
               $ cat test_help | ./console.py
               (hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

##Created Classes
The following classes are included in this projet:
        + BaseModel
        + User
        + State
        + City
        + Amenity
        + Place
        + Review
##Authors
+ samuel12451
+ emmakotey
