introString = input("Enter your introduction : ")
characterCount = 0
wordCount = 1
for i in introString :
    characterCount = characterCount + 1
    if(i == " ") :
        wordCount = wordCount + 1
print("Number Of Words in the string : ", wordCount) 
print("Number Of characters in the string : ", characterCount) 
