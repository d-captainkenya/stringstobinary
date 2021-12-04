import sys              # A simple script to convert a string to binary.
                        # All characters are assumed to be strings.
                        # some special characters not supported.
import pyfiglet
# run 'pip install pyfiglet'

def disp():
    print("\n"+"*"*65) 
    print(pyfiglet.figlet_format("     Dcap_str_bin"))
    print("*\t\t\tD_captainkenya\t\t\t\t*")
    print("*\t\t    Dcaptainkenya@gmail.com\t\t\t*")
    print("*\t      https://www.D-captainkenya.github.io\t\t*")
    print("*"*65)
    get_string()

def usage():
    print("Convert a string to binary!")
    print("\nUSAGE:")
    print("\tpython stringtobin.py string")
    print("EXAMPLE\n\t  python stringtobin.py Pluto is far away\n")
    sys.exit(1)

def get_string():                   # get string input arguments
    n = len(sys.argv)
    if n < 1:
        usage()
    elif n > 1:
        stringlist = sys.argv[1:]
        string = " ".join(stringlist)
        print("\nOriginal string\n>",str(string))
        print("-"*70)
        to_bin(string)
    else:
        usage()
        sys.exit()
    
def to_bin(string):                 # binary conversion
    bins = ''.join(format(ord(x), '08b') for x in string)
    binout = [(bins[i:i+8]) for i in range(0, len(bins), 8)]
    binary = " ".join(binout)
    print("String in binary\n>",str(binary))
    print("-"*70,"\n")

if __name__ == "__main__":
    disp()
