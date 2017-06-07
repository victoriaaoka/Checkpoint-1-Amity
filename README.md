## BC17 checkpoint 1 <br /> [![Build Status](https://travis-ci.org/victoriaaoka/Checkpoint-1-Amity.svg?branch=task0)](https://travis-ci.org/victoriaaoka/Checkpoint-1-Amity) [![Coverage Status](https://coveralls.io/repos/github/victoriaaoka/Checkpoint-1-Amity/badge.svg?branch=task0)](https://coveralls.io/github/victoriaaoka/Checkpoint-1-Amity?branch=task0)
### Introduction
The Amity is one of Andela Kenya's facilities that has several rooms. A room can be either a Living Space or an Office Space. An Office Space can accomodate a maximum of 6 people and the Living Space can accomodate a maximum of 4. When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in. When a new Staff joins they are assigned an office space only. This application seeks to digitize and randomize the room allocation process. Here is a link to the demo video. https://asciinema.org/a/ebwb9fdop1dufzrfbb8pm20p3
### Installation and setup
- prepare a directory for the project:

  `$ mkdir -p ~/Amity`
  
  `$ cd ~/Amity`
  
- Create and activate a virtual environment for the project:

  `$ virtualenv --python=python3 amity-venv`
  
  `$ source amity-venv/bin/activate`
  
- Clone the repository into the project directory:

  `$ git clone https://github.com/victoriaaoka/Checkpoint-1-Amity.git`
  
- While in the virtual environment, navigate to the project directory and install the required packages:

  `pip install -r requirements.txt`
  
- Run the application:

  `python3 run.py`
  
  Hurray! Its time to interact with the application by running the following commands.
  
### Application Commands:
- `create_room <room_type> <room_names>` - creates a new room (office or livingspace).

- `add_person <person_id> <first_name> <last_name> (FELLOW|STAFF) [<wants_accom>]` - adds a new fellow/staff.

- `load_people <file_name>` - adds new fellow/staff from a txt file.

- `print_allocations [<file_name>]` - Prints a list of all rooms and their occupants to a txt file. It prints the list on the screen if file name is not specified.

- `print_room <room_name>` - prints a list of the specified room's occupants.

-  `reallocate_person <person_id> <new_room>` - Reallocates a person a room.

- `print_unallocated [<filename>]` - Prints a list of fellows/staff who have not been allocated rooms to a txt file when file_name is provided.

- `allocate_unallocated <person_id> <room_type>` - Allocates rooms to the people in the office and livivngspace waitinglists.

- `disallocate_person <person_id> <room_type>` - Removes a person from a room.

- `print_people` - Prints all the people in the Amity.

- `print_rooms` - Prints all the rooms in the Amity with their occupants.

- `delete_person <person_id>` - Deletes a person completely from the Amity.

- `delete_room <room_name>` - Deletes a room completely from the Amity.

- `save_state <database_name>` saves the current state of the application to the specified database.

- `load_state <database_name>` loads data from an exisitng SQL database.

And that is all about the Amity space allocation app! I'll really appreciate any feedback regarding the project.

  
 
