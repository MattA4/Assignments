import time

# function to ask play again or not
def play_again():
    print("\nDo you want to play again? (y or n)")
  
    # convert the player's input to lower_case
    answer = input(">").lower()

    if "y" in answer:
        # if player typed "yes" or "y" start the game from the beginning
        start()
    else:
        # if user types anything besides "yes" or "y", exit() the program
        exit()

# game_over function accepts an argument called "reason"
def game_over(reason):
    # print the "reason" in a new line (\n)
    time.sleep(2)
    print("\n" + reason)
    time.sleep(3)
    print("Game Over!")
    # ask player to play again or not by activating play_again() function
    play_again()

#water_fall()
def water_fall():
    print("\nYou see light at the end of the tunnel!")
    time.sleep(1)
    print("\nYou reach the end of the tunnel, and are stood behind a waterfall, overlooking the jungle.")
    time.sleep(1)
    print("There's a pool of water at the bottom of the waterfall (of course).")
    time.sleep(1)
    print("It's awfully far down though...")
    time.sleep(1)
    print("So what's it going to be adventurer? Back the way you came, or swim with the fish? (1 or 2)")
    print("1) Back up the tunnel. That's too high to jump!")
    print("2) Jump down! You're not weighed down with stolen loot, so surely won't sink and drown... right?")

    # take input()
    answer = input(">")
  
    if answer == "1":
        print("\nAs you walk back up the tunnel you hear faint grumbling ahead.")
        time.sleep(1)
        print("Probably nothing though...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Or it could be a red-eyed beast and a pack of wolves...")
        time.sleep(1)
        game_over("You really should've shut the door behind you in the room full of amulets, adventurer! You have been followed through the cave system.")
    elif answer == "2":
        print("\nYou spash down into the pool at the bottom of the waterfall.")
        time.sleep(1)
        print("It's very refreshing in this humid jungle. And free of any ill-gotten gains, you easily swim to shore.")
        time.sleep(1)
        print("Congratulations adventurer, you escaped the caves unscathed!")
        time.sleep(2)
        print("Until next time...")
        # activate play_again() function
        play_again()
    else:
        # call game_over() with "reason"
        game_over("Unfortunately that was not an option... please be more careful with your responses next time...")
    
    

#skele_room()
def skele_room():
    print("\nAt last, a reasonably well lit room!")
    time.sleep(1)
    print("Although how the torches lining the walls are still lit is beyond me...")
    time.sleep(1)
    print("Very spooky... Magic maybe?")
    time.sleep(1)
    print("After what you've seen so far though, nothing seems particularly abnormal at this point...")
    time.sleep(1)
    print("Like the upright skeleton holding a spear... Doesn't phase you at all, adventurer")
    time.sleep(1)
    print("There's a tunnel to the left of the skelton, and a tunnel to the right of it, which you can hear the sound of rushing water coming from. \nWhat will you do? (1, 2, or 3)")
    print("1) Take the spear. It could be useful should you come across anything else unscrupulous in this cave system")
    print("2) Go down the tunnel to the right. Running water must be a good thing, right?")
    print("3) Go down the tunnel to the left. Best avoid the water... wouldn't want to drown...")

    # take input()
    answer = input(">")
    if answer == "1":
        # the player is dead!
        game_over("\nYou pull the spear from the skeleton, it's fingers snapping away. \nThis triggers the collapse of all tunnels leading from this room... Oops!")
    elif answer == "2":
        # lead him to the water_fall()
        print("\nYou venture down the tunnel. It starts getting wetter on the floor as you go along...")
        water_fall()
    elif answer == '3':
        #trap door
        print("\nYou venture down the tunnel... it seems to go on forever...")
        game_over("Until you fall through a trap door. You are now stuck in a pit, sorry adventurer!")
    else:
        # else call game_over() function with the "reason" argument
        game_over("Unfortunately that was not an option... please be more careful with your responses next time...")
  
    
# aztec room
def aztec_room():
    # some prompts
    print("\nYou are now in a room filled with open chests overflowing with aztec amulets!")
    time.sleep(1)
    print("And there is a door too! Barely visible through the stacks of chests, but it surely leads somewhere...")
    time.sleep(1)
    print("What will you do? (1 or 2)")
    print("1) Take some amulets... After all, there's loads of them, a few going missing can't hurt, right..?")
    print("2) Just go through the door.")

    # take input()
    answer = input(">")
  
    if answer == "1":
        # the player is dead, call game_over() function with the "reason"
        game_over("\nThey were cursed amulets! Evil spirits swarm the cave to make sure the amulets stay put...")
    elif answer == "2":
            print("\nProbably best not to take something that doesn't belong to you eh? \nVery honest of you, adventurer. Onwards!")
            skele_room()
    else:
        # call game_over() with "reason"
        game_over("Unfortunately that was not an option... please be more careful with your responses next time...")

# beast room
def beast_room():
    # some prompts
    # '\n' is to print the line in a new line
    print("\nYou enter a larger cave, but can barely see anything.")
    time.sleep(1)
    print("You take an old torch from a holder on the the wall beside you and light it.")
    time.sleep(1)
    print("You can now see a large, hairy beast across the cave.")
    time.sleep(1)
    print("Maybe Bigfoot? Or Bigfoot's larger, scarier, red-eyed cousin?")
    time.sleep(1)
    print("Either way, it looks... hungry.")
    time.sleep(1)
    print("The beast advances towards you.\nBehind the beast there is another tunnel. What will you do? (1 or 2)")
    print("1) Wave the torch in the beast's face. Maybe it's scared of fire? Maybe it will just make it angry...")
    print("2) Dash for the tunnel! The beast is too big to match your pace... surely?")

    # take input()
    answer = input(">")

    if answer == "1":
        print('\nIt worked! The beast backed away far enough to give you chance to exit through the tunnel')
        # lead him to the aztec_room()
        aztec_room()
    elif answer == "2":
        # the player is dead, call game_over() with "reason"
        game_over("\nAlthough large, the beast was not too slow to grab you...\nUp close it looks even hungrier.")
    else:
        # game_over() with "reason"
        game_over("Unfortunately that was not an option... please be more careful with your responses next time...")

# wolf room
def wolf_room():
    # give some prompts
    # '\n' is to print the line in a new line
    print("\nYou find yourself in a cave with a sleeping pack of wolves.")
    time.sleep(1)
    print("On the  other side of the wolves from you is a passageway.")
    time.sleep(1)
    print('Closer to you along the left wall of the cave is a smaller passageway')
    time.sleep(1)
    print("One of the wolves wakes up and walks up to you. Only a few feet away from you, you can see the wolf more clearly, and it looks...")
    time.sleep(2)
    print('Menacing...')
    time.sleep(2)
    print("What will you do? (1, 2, or 3)")
    print("1) Try and escape back up tunnel you entered through.")
    print("2) Slowly and quietly walk past the wolf and their sleeping pack to the passagway opposite you")
    print("3) Make a dart for the passagway on the left")

    # take input()
    answer = input(">")
  
    if answer == "1":
        # the player is dead!
        game_over("\nYou get halfway up the tunnel when you feel the wolf's teeth around your calf. You are dragged back to the rest of the hungry pack")
    elif answer == "2":
        # lead him to the aztec_room()
        print("\nYou slip past the pack of wolves, while the wolf that took interest in you merely watches on...")
        aztec_room()
    elif answer == '3':
        #to the beast
        print("\nYou make it into the smaller passageway, and there doesn't appear to be anything following you...")
        beast_room()
    else:
        # else call game_over() function with the "reason" argument
        game_over("Unfortunately that was not an option... please be more careful with your responses next time...")

def start():
    # give some prompts.
    print("\nHello adventurer! You have entered an underground cave system through an abondoned mineshaft.")
    time.sleep(1)
    print('You are standing in a gloomy cave.')
    time.sleep(1)
    print('You can just make out that there are tunnels on the opposite wall to the left and right')
    time.sleep(1)
    print('Which one do you take? (l or r)')
  
    # convert the player's input() to lower_case
    answer = input(">").lower()

    if "r" in answer:
        # if player typed "left" or "l" lead him to wolf_room()
        wolf_room()
    elif "l" in answer:
        # else if player typed "right" or "r" lead him to beast_room()
        beast_room()
    else:
        # else call game_over() function with the "reason" argument
        game_over("Unfortunately that was not an option... please be more careful with your responses next time...")


# start the game
start()