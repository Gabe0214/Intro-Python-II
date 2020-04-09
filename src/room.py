# Implement a class to hold room information. This should have name and
# description attributes


class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
    
    def __str__(self):
        return(f"{self.name}. {self.description}")
    
    def store_item(self, item):
        self.items.append(item)
        return(f"this room has {self.items}")
        

# myRoom = Room('Dining', 'Where we eat')

# print(myRoom.n_to)

