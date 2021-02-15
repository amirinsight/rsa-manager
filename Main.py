# AmirhosseinZare(of course! as always!)
# Importing the big modules
import Generator
import Decoder
import Encoder

def welcome():
    print(" ________________________________________________________________________________ \n"
          "|  __ \  / ____|   /\     |  __ \ |  __ \  / __ \      | ||  ____|/ ____||__   __|\n"
          "| |__) || (___    /  \    | |__) || |__) || |  | |     | || |__  | |        | |  |\n"
          "|  _  /  \___ \  / /\ \   |  ___/ |  _  / | |  | | _   | ||  __| | |        | |  |\n"
          "| | \ \  ____) |/ ____ \  | |     | | \ \ | |__| || |__| || |____| |____    | |  |\n"
          "|_|  \_\|_____//_/    \_\ |_|     |_|  \_\ \____/  \____/ |______|\_____|   |_|  |\n"
          "|               +-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                |\n"
          "|               |M|a|d|e| |b|y|:| |A|m|i|r|h|o|s|s|e|i|n|Z|a|r|e|                |\n"
          "|               +-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                |\n"
          " -------------------------------------------------------------------------------- \n"
          "1: Generate Key\n"
          "2: Encrypt Message\n"
          "3: Decrypt Message\n"
          "4: Exit Program\n"
          "Select a number and press enter:")


def manager():
    while True:
        try:
            choice = int(input(""))
            if choice == 1:
                Generator.generate()
            elif choice == 2:
                Encoder.encrypt()
            elif choice == 3:
                Decoder.decrypt()
            elif choice == 4:
                quit()
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input.")


welcome()
manager()