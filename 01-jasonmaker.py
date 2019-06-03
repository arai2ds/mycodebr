#!/usr/bin/python3
'''
Author:Anand Rai | leraning json with oython '''

# with python,the jasonbatteries are in the box , but you need to plug them in
import json

def main():
    videogames =[{"game1":"red dead redemption","game2":"witcher","game3":"starcraft","game4":"faster than light"},{"game1":"paperboy","game2":"donkey kong"}]

    # show the values of videogames
    print(videogames)
    
    # create a local file
    with open("videogames.jason","w") as vidfile: # w= write,r read ,a =append,b binary
        json.dump(videogames,vidfile)




if __name__=="__main__": 
    
    main()
