# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc, exits = {
        'n_to':[],
        'e_to':[],
        's_to':[],
        'w_to':[]
    }):
            self.name = name
            self.desc = desc
            self.exits = exits


    def __str__(self):
        return f"{self.name}\n\nDescription: {self.desc}"

    def __repr__(self):
        return f"{self.name}"
