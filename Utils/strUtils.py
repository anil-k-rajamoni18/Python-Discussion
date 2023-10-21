# Function to display string length #
def disStrLength(str1 : str)-> int :
    return len(str1)
    

# Function to display string length without spaces #
def disStrLenWithoutSpaces(str1 : str)-> int:
    spaces= str1.count(' ')
    length= len(str1)
    len_no_spaces= length-spaces
    return len_no_spaces
  
# Function to display all vowels #
def displayVowels(str1 : str)-> list[str]:
    vowels="AEIOUaeiou"
    str2=[]
    for i in str1:
        if i in vowels:
            str2.append(i)
    return str2
    
    


# Function to display whether string is pallindrome or not
def palindrome(str1: str)->bool:
   return  str1==str1[::-1]

#Function to display whether the string is panagram or not
def panagram(str1:str)-> bool:
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in str1.lower():
            return False
    return True

#Function to display count of special characters: space , . ? ; : * % $ # @ ! * ( ) _ - 
def sepcialChar(str1: str)-> list[str]:
    specialChar=", . ? ; : * % $ # @ ! * ( ) _ - "
    char=[]
    for i in str1:
        if i in specialChar:
            char.append(i)
    return char



# Function to display reverse of a string
def revString( str1: str)-> str:
    return str1[::-1]
    
    
    
    


