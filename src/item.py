class Item:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def item_des(self):
        print(f'{self.name}, {self.description}')