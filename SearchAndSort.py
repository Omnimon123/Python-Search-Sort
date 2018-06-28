"""
Soumen Nath
ICS4U
SoumenNath_SearchAndSort.py
Description: This program will create a character in the game for the user and allow them to use 4 different search algorithms. The program will also display all the characters that are stored in the file.
"""
#import following modules
import os; import random; import time
#all the items and attributes required for the character profile
cAttributes = [['fighter', 'wizard', 'thief', 'healer', 'ranger'], ['human', 'elf', 'dwarf', 'halfling', 'gnome'], ['cool bow', 'wicked axe', 'slick dagger', 'shiny sword', 'mysterious claws', 'vicous lance', 'mystical staff', 'grand grimoire'], ['red potion', 'blue potion', 'green potion'], ['gems', 'coins', 'artifact'], ['food', 'herb'], ['sceptre', 'scroll', 'ring', 'none'], ['torch', 'lamp', 'key', 'map', 'none']]
#Character class that creates the character for the user
class Character:
    #constructor
    def  __init__(self):
        #initialize the variables
        self.fname = input("\nPlease enter your character's first name: ")
        self.lname = input("Please enter your character's last name: ")
        self.cClass = random.choice(cAttributes[0])
        self.race = random.choice(cAttributes[1])
        self.stats = {'Strength': random.choice(range(1,21)), 'Constitution': random.choice(range(1,21)), 'Dexterity': random.choice(range(1,21)), 'Intelligence': random.choice(range(1,21)), 'Wisdom': random.choice(range(1,21)),  'Charisma': random.choice(range(1,21))}
        self.beltSlot = random.choice(cAttributes[2])
        self.backSlot = random.choice(cAttributes[2])
        self.rHand = random.choice(cAttributes[6]+cAttributes[7])
        self.lHand = random.choice(cAttributes[6]+cAttributes[7])
        #list that cointains the pack items
        pack = []
        for i in range(10):
            pack.append(random.choice(cAttributes[3]+cAttributes[4]+cAttributes[5]+cAttributes[6]+cAttributes[7]))
        self.pack = pack
        #write the information from the character profile to the file
        with open('Character.txt', 'a') as file:
            file.write("\n\nAdventurer's Name: "+str(self.fname)+' '+str(self.lname)+'\nClass: '+str(self.cClass)+'\nRace: '+str(self.race)+'\n')
            for key, item in self.stats.items():
                file.write(str(key)+":"+str(item)+"\n")
            file.write('Back Slot: '+str(self.backSlot)+'\nBelt Slot: '+str(self.beltSlot)+'\nRight Hand: '+str(self.rHand)+'\nLeft Hand: '+str(self.lHand)+'\nPack: '+', '.join(pack))
    #linear search function
    def linearSearch(self):
           os.system('cls')
           print('The contents of the randomly generated pack are: ')
           for item in self.pack:
               print(item+', ', end='')
           item = input('\nPlease enter an item: ')
           position = 0; found = False; startTime = time.clock() #the time when the algorithm is sarting is recorded
           #checks each position in the list
           while position < len(self.pack) and not found:
               if self.pack[position] == item:
                   found = True
                   print('\n'+self.pack[position], 'is in the pack!\nLenght of time to complete linear search:', time.clock() - startTime) #The difference between the current time and start time is found to determine how long the algorithm took
               position += 1
           if found == False:
               print('Error, item not found in the list!\nLenght of time to complete linear search:', time.clock() - startTime)
           input('\nPlease press enter'); os.system('cls'); self.menu2()
    #binary search function
    def binarySearch(self):
        os.system('cls'); numberList = []
        #store the values of the stats in the list
        for values in self.stats.values():
            numberList.append(values)
        #sort the list
        numberList = sorted(numberList)
        print('The character stats are:')
        for key, value in self.stats.items():
            print(key+': '+str(value))
        choice = int(input('\nWhich stat are you looking for? (enter the number): '))
        bottom = 0; found = False; top = len(numberList)-1
        print('Sorted list of stats:', numberList)
        counter=0; startTime = time.clock() #the time when the algorithm is sarting is recorded
        #splits the list in half and keeps narrowing down the range until the right number is found
        while bottom<=top and not found:
            counter+=1
            middle = int((bottom+top)//2)
            if numberList[middle] == choice:
                found = True
                print(choice, 'is in the list of stats!\nLenght of time to complete binary search:', time.clock() - startTime)#The difference between the current time and start time is found to determine how long the algorithm took
                break
            elif numberList[middle] < choice:
                bottom = middle + 1
            else:
                top = middle - 1
            #prints the list after each pass
            print('List after pass '+str(counter)+':',numberList[bottom:top+1])
        if found == False:
            print('Error! The stat you are searching for is not in the list\nLenght of time to complete binary search:', time.clock() - startTime)
        input('\nPlease press enter'); os.system('cls'); self.menu2()
    #bubble sort function
    def bubbleSort(self):
        os.system('cls'); counter = 0; theList = []
        #store the stats in the list
        for key, value in self.stats.items():
          theList.append([key, value])
        print('Unsorted character stats:')
        for stat in theList:
          print(stat[0]+':', stat[1])
        print('\n\n')
        exhanges = True; startTime = time.clock() #the time when the algorithm is sarting is recorded
        #compares a value to the next value in the list. Then goes back to the start to repeat process.
        while exhanges:
          exhanges = False
          for element in range(len(theList)-1):
              if theList[element][1] > theList[element+1][1]:
                  counter+=1
                  exhanges = True
                  tempV = theList[element]
                  theList[element] = theList[element+1]
                  theList[element+1] = tempV
                  #prints the list after each pass
                  print('List after pass '+str(counter)+':',theList)
        print('\n\nLenght of time to complete bubble sort:', time.clock() - startTime)#The difference between the current time and start time is found to determine how long the algorithm took
        print('Sorted list of stats: ')
        for stat in theList:
          print(stat[0]+':', stat[1])
        input('\nPlease press enter'); os.system('cls'); self.menu2()
    #insertion sort function
    def insertionSort(self):
        os.system('cls'); theList = []
        #store the stats in the list
        for key, value in self.stats.items():
          theList.append([key, value])
        print('Unsorted character stats:')
        for stat in theList:
          print(stat[0]+':', stat[1])
        print('\n\n')
        startTime = time.clock() #the time when the algorithm is sarting is recorded
        #counter keeps track of each pass
        counter = 0
        #unlike bubbleSort one value is not just compared to the next value. Instead it is compared with all the necessary values until its rightful place is found. Then the for loop moves on.
        for i in range(1, len(theList)):
            tempV = theList[i]
            pos = i
            while pos > 0 and tempV[1] < theList[pos - 1][1]:
                theList[pos] = theList[pos - 1]
                pos -= 1
            theList[pos] = tempV
            counter+=1
            print('List after pass '+str(counter)+':',theList)
        print('\n\nLenght of time to complete insertion sort:', time.clock() - startTime)#The difference between the current time and start time is found to determine how long the algorithm took
        print('Sorted list of stats: ')
        for stat in theList:
          print(stat[0]+':', stat[1])
        input('\nPlease press enter'); os.system('cls'); self.menu2()
    #function to display the character
    def display(self):
        print("\n\nAdventurer's Name: "+str(self.fname)+' '+str(self.lname)+'\nClass: '+str(self.cClass)+'\nRace: '+str(self.race))
        for key, item in self.stats.items():
            print(str(key)+":"+str(item))
        print('Back Slot: '+str(self.backSlot)+'\nBelt Slot: '+str(self.beltSlot)+'\nRight Hand: '+str(self.rHand)+'\nLeft Hand: '+str(self.lHand)+'\nPack: '+', '.join(self.pack))
        input('\nPlease press enter'); os.system('cls'); self.menu2()
    #second menu that is accessed once a character is created
    def menu2(self):
        os.system('cls')
        print("Please choose an option:\n1-Linear search\n2-Biunary Search\n3-Bubble Sort\n4-Insertion Sort\n5-Display your character\n6-Return to the main menu")
        while True:
            try:
                decision = int(input('Please enter your selection: '))
            except ValueError:
                print('Error!'); continue
            if decision<1 or decision>6:
                print('Error!'); continue
            else:
                break
        #deploys the chosen algorithm
        if decision == 1:
            self.linearSearch()
        elif decision == 2:
            self.binarySearch()
        elif decision == 3:
            self.bubbleSort()
        elif decision == 4:
            self.insertionSort()
        elif decision == 5:
            self.display()
        #returns to the main menu if 6 is chosen
        elif decision == 6:
            input('\nPlease press enter'); os.system('cls'); menu()
#main menu function
def menu():
    print("\t\t\t\t\t--------------------------------\n\t\t\t\t\tWelcome to Dungeons and Dragons!\n\t\t\t\t\t--------------------------------\n1-View the characters from character.txt\n2-Generate a character\n3-Exit the program")
    while True:
        try:
            selection = int(input('Please enter your selection: '))
        except ValueError:
            print('Error!'); continue
        if selection<1 or selection>3:
            print('Error!'); continue
        else:
            break
    #if the user selects 1 then display all the characters from the file
    if selection == 1:
        os.system('cls')
        with open('Character.txt', 'r') as file:
            print(file.read())
        input('\nPlease press enter'); os.system('cls'); menu()
    #create a character if the user selects 2
    elif selection == 2:
        user =Character()
        user.menu2()
    #exit the program if the user selects 3
    elif selection == 3:
        os.system('cls'); input('Thank you for using this program!'); os.system('cls'); exit()
#if Character.txt exits then run the menu function. Otherwise, create the file with the first character profile
if os.path.exists('Character.txt'):
    menu()
elif os.path.exists('Character.txt') == False:
    with open('Character.txt', 'w') as file:
        file.write("Adventurer's name: Foo Bobo\nClass: Ranger\nRace: Gnome\nStrength: 16\nConstitution: 15\nDexterity: 18\nIntelligence:15\nWisdom: 15\nCharisma: 20\nBack Slot: short bow\nBelt Slot: small axe\nRight Hand: torch\nLeft Hand: empty\nPack: potion red, ring, food, coins, key, food, lamp, scroll, artifact, potion blue")
    file.close()
    menu()
