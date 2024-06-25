# Matthew A Keaton

def show_instructions():
    # print a main menu and the commands
    print('Save The Princess Text Adventure Game')
    print('-' * 23)
    print('Collect 6 items to win the game, or be defeated by the Evil Prince.')
    print('Move commands: South, North, East, West')
    print("Add to Inventory: 'get item'")
    print('-' * 23)

show_instructions()

# define player status
def player_status(current_room, inventory, rooms):
    print('You are in the {}'.format(current_room))
    print('Inventory:', inventory)
    print('This room has', rooms[current_room]['item'])
    print('-' * 23)

#move commands from user
moves = ['North', 'South', 'East', 'West', 'Exit']


#create an inventory and link rooms
def main():
    inventory = []
    rooms = {
        'Great Chambers': {'direction': {'South': 'Blacksmith Forge', 'North': 'Prince Chamber', 'West': 'Master Bedroom', 'East': 'Secret Vault'}, 'item': 'no item'},
        'Prince Chamber': {'direction': {'South': 'Great Chambers', 'East': 'Alchemy Lab'}, 'item': 'Map'},
        'Alchemy Lab': {'direction': {'West': 'Prince Chamber'}, 'item': 'Potion'},
        'Master Bedroom': {'direction': {'East': 'Great Chambers'}, 'item': 'Amulet'},
        'Secret Vault': {'direction': {'West': 'Great Chambers', 'North': 'Princes Keep'}, 'item': 'Lock Picking Kit'},
        'Princes Keep': {'direction': {'South': 'Secret Vault'}, 'item': 'Evil Prince'}, # villian room
        'Blacksmith Forge': {'direction': {'North': 'Great Chambers', 'East': 'Cellar'}, 'item': 'Master Sword'},
        'Cellar': {'direction': {'West': 'Blacksmith Forge'}, 'item': 'Armor'}
    }

    #starting room
    current_room = 'Great Chambers'


    #output instructions
    show_instructions()

    # main loop
    while True:
        player_status(current_room, inventory, rooms)

        player_move = input('Enter your move:')


        if 'item' in rooms[current_room]:
            if player_move == 'get item':
                item = input("Enter '{}' to retrieve this item: ".format(rooms[current_room]['item'])).strip()

                if item in rooms[current_room]['item']:
                    print("You retrieved the: '{}'".format(item))
                    inventory.append(item)


        if current_room == 'Princes Keep':
            print('You have reached the final boss!')
            if len(inventory) == 6:
                print('Congratulations! You rescued the princess and saved the kingdom!')
                break
            else:
                print('Game over! Please try again.')
                break
        if player_move == "Exit":
            print('Thank you for playing the game!')
            break
        elif player_move in moves:
            current_room = rooms[current_room]['direction'][player_move]

        else:
            print('invalid command!')


main()