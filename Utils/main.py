from strUtils import revString,panagram,palindrome,disStrLength,disStrLenWithoutSpaces,displayVowels,sepcialChar



if __name__ =='__main__':
    str1=input("Enter  a string:")
    while True:
        
        print(" 1.display the string length \n 2. display string length without spaces\n 3. display all vowels\n 4. display whether string is palindrome or not \n 5. display whether string is panagram or not \n 6.display count of special characters: space , . ? ; : * % $ # @ ! * ( ) _ - \n  6.display reverse of a string.\n Exit")
        ch=int(input("\nEnter your Choice:"))
        if ch==1:
            res=disStrLength(str1)
            print(f" Entered String Length is {res}")
        
        elif ch==2:
            res=disStrLenWithoutSpaces(str1)
            print(f"String Length without spaces {res}")

        elif  ch==3:
           res= displayVowels(str1)
           print(f"Vowels present in the string are {res }")

        elif ch==4:
           res= palindrome(str1)
           print("Given string is {res}")

        elif ch==5:
           res= panagram(str1)
           print("Given string is {res}")

        elif ch==6:
            res=sepcialChar(str1)
            print(f"Special Character present in the string are {res}")

        elif ch==7:
           res= revString(str1)
           print(f"Reverse of a {str1} is {res}")



        elif ch== -1:
          break;

        else:
            print("Invalid choice!!")





