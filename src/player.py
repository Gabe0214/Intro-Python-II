
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, user, current_room):
        self.user = user
        self.current_room = current_room

    def change_current_room(self, changed_room):
        self.current_room = changed_room



# person = Player('Gabe', 'myRoom')
# print(person.user)
