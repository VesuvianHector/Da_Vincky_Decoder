from art import *
import zipfile
from tqdm import tqdm
from itertools import chain, product
                                                                 
#I had a full commented version but i accidently deleted it i will be reduing that over the next few days

#Made by JTH/Vesuvian Hecktor
#Runs either very fast or very slow idk why

#Definitions!!!!

def ZipListAttack():# Dictionary Attack
    print("*" * 60)       
    print("The password list path you want to use \nmust be available in the current directory")
    passlist = (input("Exact Name\Path of file here: "))
    print("*" * 60)
    print("The password list path you want to use \nmust be available in the current directory")
    Xipfile = (input("Exact Name\Path of .zip file here: ")) 
    Xipfile = zipfile.ZipFile(Xipfile)
    snake = len(list(open(passlist, "rb")))
    print("Total passwords to test:",snake)# total number of passwords in list
    with open(passlist, "rb") as passlist:
        for word in tqdm(passlist, total=snake, unit="cobra"):
            try:
                zipfile.extractall(pwd=cobra.strip())
            except:
                continue
            else:
                print("[+] YAY!!!!!!!!!!! \nPassword found:", word.decode().strip())
                break
    print("[-] Password not found, try other wordlist.")

def ZipBruteAttack2(length, charset):
    passlist = (list(ListCreate(length, charset)))
    Xipfile = (input("Exact Name\Path of .zip file here: ")) 
    Xipfile = zipfile.ZipFile(Xipfile)
    snake = len(list(ListCreate(length, charset)))
    print("Total passwords to test:",snake)# total number of passwords in list
    with (list(ListCreate(length, charset))) as passlist:
        for word in tqdm(passlist, total=snake, unit="cobra"):
            try:
                zipfile.extractall(pwd=cobra.strip())
            except:
                continue
            else:
                print("[+] YAY!!!!!!!!!!! \nPassword found:", word.decode().strip())
                break
    print("[-] Password not found, try other wordlist.")

def ListCreate(length, charset):#List Creation
   return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, length + 1)))
        

def Body():
    print("Enter the number of the action you would like to preform")
    print("Dictionary Attack on Zipfile:   1")
    print("Brute Force on Zipfile:         2")
    print("Make Dictionary/Password list:  3")
    action = int(input("ENTER HERE: "))
    
    if action   == 1:# Dictionary Attack on Zip selection
        ZipListAttack()
        
    if action   == 2:# BruteForce Attack on Zip selection
        print ("Please do not go to heavy as you can cause memory errors using this")
        charset = str(input("List of charecters here: "))
        length  = int(input("how many chars?: "))
        print ("Below is the total combination of passwords")
        print (list(ListCreate(length, charset)))
        ZipBruteAttack2(length, charset)
        
    if action == 3:# List Generation
        print ("Please do not go to heavy as you can cause memory errors and Storage Errors using this")
        charset = str(input("List of charecters here: "))
        length  = int(input("how many chars?: "))
        file = str(input("Name of your new file we cover the .txt so don't worry\nOperation will fail if there's not enough storage or if the file name already exists\nHere:"))
        BruteList = list(ListCreate(length, charset))
        print(BruteList)
        BruteList1 = [str(item) for item in BruteList]
        BruteList = map(lambda x:x+'\n', BruteList1)
        FILE = file + ".txt"
        List = open(FILE, "x")
        List.writelines(BruteList)
       
    else:
        print("Invalid Input, Try Again")
        Body()# Semi Loop lmao 
            


# Header
header = text2art("Da_Vincky_Decoder", font = 'gothic')
print(header)
print("Welcome to The Da Vincky Decoder\nMade by JTH/Vesuvian Hecktor")
print("This bruteforcer is just the basline for a zip brute forcer using the folowing modules \n *zipfile \n *tqdm \n *Itertools \n *art \nPlease make sure you have these updated and installed")
# Body and Selection
Body()









    
            
