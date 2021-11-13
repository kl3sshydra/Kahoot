# Importing Libraries

from kahoot import client
from colorama import Fore, Style
import random

# Starting and Setting up the Bot Attack

print(Fore.RED + " @@@  @@@  @@@@@@  @@@  @@@  @@@@@@   @@@@@@  @@@@@@@      @@@@@@@   @@@@@@  @@@@@@@\n @@!  !@@ @@!  @@@ @@!  @@@ @@!  @@@ @@!  @@@   @@!        @@!  @@@ @@!  @@@   @@!  \n @!@@!@!  @!@!@!@! @!@!@!@! @!@  !@! @!@  !@!   @!!        @!@!@!@  @!@  !@!   @!!  \n !!: :!!  !!:  !!! !!:  !!! !!:  !!! !!:  !!!   !!:        !!:  !!! !!:  !!!   !!:  \n !:   :::  :   : :  :   : :  : :. :   : :. :     :         :: : ::   : :. :     :                                                                                      \n")
print(Fore.RED + "If you enjoy the Tool, please consider leaving a Star on Github: https://github.com/xssinjection/Kahoot.")
username = input(Fore.RED + " Tell me your bots username, please. > ")
code = input(Fore.RED + " Tell me the Kahoot Code, please. > ")
def joinHandle():
  pass

# Converts String Type into Int Type

int(code)

# Bot Attack

bot = client()
this_variable_should_go_up_lol = 0
while this_variable_should_go_up_lol < 1000000:
    this_variable_should_go_up_lol += 1
    random_int = random.randint(10000, 1010000)
    random_int = str(random_int)
    botname = username + " - " + random_int
    bot.join(code, botname)
    bot.on("joined",joinHandle)
    random_int = int(random_int)