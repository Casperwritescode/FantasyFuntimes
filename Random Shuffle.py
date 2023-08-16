#Import Random Shuffle
from random import shuffle

#Define League Managers
Managers=['Ian','Phil','Lori','Joe','Matty','Duncan','Max','John','Andy','Alex','TJ','Casper']

#Execute Draft order shuffle
shuffle(Managers)

# Initialize an empty dictionary for draft order
Draft_Order = {}
for i, manager in enumerate(Managers, start=1):
    Draft_Order[i] = manager

#print Draft_Order results5
print(Draft_Order)