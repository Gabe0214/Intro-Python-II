
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, user, current_room):
        self.user = user
        self.current_room = current_room

    # def __str__(self):
    #     return(f"Welcome, {self.user}! You're currently in {self.current_room}")


# person = Player('Gabe', 'myRoom')
# print(person.user)
