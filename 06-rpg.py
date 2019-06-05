#!/usr/bin/python3
""" building the map of the house """

import 



def showInstructions():
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
    go [direction]
    get [item]
    ''')


def showStatus()
   #print the player's current status
   print('---------------------')
   print('You are in the ' + currentRoom)
   #print the current inventory
   print('Inventory : ' +str(inventory))
   #print as item if there is one
   if "item" in rooms[currentrRoom]:
       print('You see a ' +rooms[currentRoom]['item'])
   print("-------------------------------------")


#an Inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = { 
             'Hall' : {
                   'south' : 'Kitchen'
                },
                
             'Kitchen' : {
                   'north' : 'Hall'
               }
            

         }

#start the player in the Hall
currentRoom ='Hall'

showInstructions()


#loop forever

While True:
    
    showStatus()
#get the player's next 'move'
#.split() breaks it up into an list array 
#eg typing 'go east' would give the list:
#['go','east']
move = ''
while move == '';
 move = input('>')

move = move.lower().split()

#if they type 'go' first
if move[0] == 'go':


