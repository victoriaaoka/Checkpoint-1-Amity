# Dojo Space Allocation Application

The Dojo is one of Andela Kenya's facilities that has several rooms. A room can be either a Living Space or an Office Space.
An Office Space can accomodate a maximum of 6 people and the Living Space can accomodate a maximum of 4.
When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in.
When a new Staff joins they are assigned an office space only. This application is digitizes and randomizes the room allocation system.

## Usage

### Create Room

Command: ```create_room <room_type> <room_name>```

This command allows one to create rooms in the dojo.

The room_type can either be 'office' or 'living space'.

Multiple rooms can be created by entering the room names and separating them with a comma.

### Add Person

Command: ```add_person <person_id> <person_name> <FELLOW|STAFF> [wants_accommodation]```

Adds a person to the system and allocates the person to a random room. 
wants_accommodation here is an optional argument which can be either Y or N.
The default value if it is not provided is N.
