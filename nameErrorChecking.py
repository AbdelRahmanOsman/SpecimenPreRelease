nameErrorChecking(Input):
    splitWord = list(Input) #splits the word and stores it in an array
    index = 0
    if ' ' in splitWord:
        while True:
            if splitWord[index] == ' ':
                break
            index=index+1
    indexSecondName = index+1
    
    print(splitWord[indexSecondName])
    if Input.replace(' ','').isalpha() and splitWord[indexSecondName].isupper() and splitWord[0].isupper():
        print("valid")
        Validated = Input
    else:
        while True:
            print("Invalid, please retype the students name.")
            Input = input()
            splitWord = list(Input) #splits the word and stores it in an array
            index = 0
            if ' ' in splitWord:
                while True:
                    if splitWord[index] == ' ':
                        break
                    index=index+1
            indexSecondName = index+1
            print(splitWord[indexSecondName])
            if Input.replace(' ','').isalpha() and splitWord[indexSecondName].isupper() and splitWord[0].isupper():
                print("valid")
                Validated = Input
                break
    return Validated

Name = nameErrorChecking("Bob James")

