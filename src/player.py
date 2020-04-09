
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, user, current_room):
        self.user = user
        self.current_room = current_room
        self.player_items = []
    
    def change_current_room(self, changed_room):
        self.current_room = changed_room

    def see_inventory(self):
        return(f"Your items: {self.player_items}")

    def add_item(self, item):
        self.player_items.append(item)
        return(f"{self.player_items}")


# person = Player('Gabe', 'myRoom')
# print(person.user)
