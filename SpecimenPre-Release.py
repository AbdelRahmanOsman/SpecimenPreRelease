#The error checking function for the scores
def numericalErrorChecking(Input,Max,Min):
    if Input.isdigit() and Min<=int(Input)<=Max: #the conversion to an int is done only after the Input is insured to be a digit, otherwise errors will occur
            print("Valid")
            Validated= int(Input)
    else:
        while True:
            print("Invalid, please retype your score")
            Input = input()
            if Input.isdigit() and Min<=int(Input)<=Max:
                print("Valid")
                Validated= int(Input)
                break
    return Validated

#The error checking function for the names
def nameErrorChecking(Input):
    splitWord = list(Input) #splits the word and stores it in an array
    index = 0
    while if not splitWord[index].isspace:
        index = index + 1
    indexSecondName = index + 1
    print(splitWord[indexSecondName])
    if Input.replace(' ','').isalpha() and splitWord[indexSecondName].isupper() and splitWord[0].isupper():   
        print("valid")
        Validated = Input
    else:
        while True:
            print("Invalid, please retype the students name.")
            Input = input()
            splitWord = Input.split() #splits the word and stores it in an array
            index = 0
            while not splitWord[index].isspace:
                index = index + 1

            indexSecondName = index + 1
            if Input.replace(' ','').isalpha() and splitWord[indexSecondName].isupper() and splitWord[0].isupper()():
                print("valid")
                Validated = Input
                break
    return Validated
     
#declaring the two-dimensional arrays for the students information
names = []
test1 = []
test2 = []
test3 = []
total = []
topScoresIndex = [] #this holds the index values of the top total scorers, which since the names of these
#top scorers hold the same index value the names of the top scorers can be found

#this is a variable that allows the program to work for diferent numbers of students, the
#specimen pre-release specifies 30 students however for testing purposes this number can be brought down
NumberStudents = 30 

studentNumber = 1 #this is not set to 0 as the question, "What is the name of student 0?", does not make sense
while studentNumber <=NumberStudents:

    #Asking for the student name
    print ("What is the name of student number", studentNumber, "?")
    NameInput = input()
    Name = nameErrorChecking(NameInput) #storing the validated value in a variable and passing an argument, that is the intial input
    #adding the value to the array
    names.append(Name)

    #asking for the the students score for test number 1
    print ("What is the score of student number", studentNumber, "on test 1?")
    Input1 = input()
    Score1 = numericalErrorChecking(Input1,20,0) #passes three arguments input, maximum score and minimum score
    #adding the value to the array
    test1.append(Score1)

    #asking for the the students score for test number 2
    print ("What is the score of student number", studentNumber, "on test 2?")
    Input2 = input()
    Score2 = numericalErrorChecking(Input2,25,0)  #passes three arguments input, maximum score and minimum score
    #adding the value to the array
    test2.append(Score2)


    #asking for the the students score for test number 3
    print ("What is the score of student number", studentNumber, "on test 3?")

    Input3 = input()
    Score3= numericalErrorChecking(Input3,35 ,0)  #passes three arguments input, maximum score and minimum score
    #adding the value to the array
    test3.append(Score3)
    studentNumber = studentNumber+1

#sums coresponding indexs in the array to make a new array called total
total = [sum(i) for i in zip(test1,test2,test3)]
#the zip function creates a two dimensional array, where each element in theese three arrays are grouped together like so, [i,i,i],[i,i,i].[i,i,i]......
#the sum function sums all the i's to create a 1 dimensional array [i+i+i],[i+i+i],[i+i+i], called total that was defined at the top of this program.

#prints the name of the student followed by their totals score
index = 0
while index <NumberStudents:
    print("Name-", names[index])
    print("Total score-", total[index])
    index = index + 1

#Calculates and prints the class average
average= sum(total)/NumberStudents
print("Class average score-", average)

#This finds the index of the top scorers and stores it in an array
index = 0
while index < NumberStudents:
    if total[index] == max(total):
        topScoresIndex.append(index)
    index = index + 1

    
print("The following people have acheived the highest score of", max(total))

index=0
while index < len(topScoresIndex): # the len function returns the length of the array of top scorers
    print(names[topScoresIndex[index]])
    index = index + 1
