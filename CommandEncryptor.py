#  _________                                           .___        
#  \_   ___ \  ____   _____   _____ _____    ____    __| _/        
#  /    \  \/ /  _ \ /     \ /     \\__  \  /    \  / __ |         
#  \     \___(  <_> )  Y Y  \  Y Y  \/ __ \|   |  \/ /_/ |         
#   \______  /\____/|__|_|  /__|_|  (____  /___|  /\____ |         
#          \/             \/      \/     \/     \/      \/         
#  ___________                                   __                
#  \_   _____/ ____   ___________ ___.__._______/  |_  ___________ 
#   |    __)_ /    \_/ ___\_  __ <   |  |\____ \   __\/  _ \_  __ \
#   |        \   |  \  \___|  | \/\___  ||  |_> >  | (  <_> )  | \/
#  /_______  /___|  /\___  >__|   / ____||   __/|__|  \____/|__|   
#          \/     \/     \/       \/     |__|                    

goal = "YOUR COMMAND HERE" # <-- change this to your command you want to encrypt

# the encrypted command will be saved to "EncryptedCommand.bat"
# run the batch file to run the command

# the batch file should not get detected by any virus defenders
# --unless you run it?--
# anyway it works on windows and maybe on unix systems too
# i havent tested any batch files on unix systems yet so i cant tell

# have fun i think

# zoe 



#-----------------------------------------------------------------------
import random
import string

goal_list = []
random_shit_list = []

def RandomShit(lenght):
    alphabet = string.ascii_letters
    while True:
        random_shit = ""
        while not len(random_shit) == lenght:
            rand_char = alphabet[random.randrange(0, len(alphabet))]
            random_shit += str(rand_char)
        else: 
            if not random_shit in random_shit_list:
                return random_shit

def DefineChars():
    global goal_list
    with open("EncryptedCommand.bat", "w") as f:
        set_op = RandomShit(random.randrange(20, 100))
        eq_op = RandomShit(random.randrange(20, 100))
        empty_op = RandomShit(random.randrange(20, 100))
        f.write(f"set {set_op}=set\n")
        f.write(f"%{set_op}% {empty_op}= \n")
        f.write(f"%{set_op}%%{empty_op}%{eq_op}==\n")
        for char in goal:
            char_name = RandomShit(random.randrange(20, 100))
            f.write(f"%{set_op}%%{empty_op}%{char_name}%{eq_op}%{char}\n")
            goal_list.append(char_name)
    f.close()

def CombineToCommand():
    command = ""
    for shit in goal_list:
        command += f"%{shit}%"
    with open("EncryptedCommand.bat", "a") as f:
        f.write(command)

DefineChars()
CombineToCommand()