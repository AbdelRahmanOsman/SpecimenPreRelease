def numericalErrorChecking(Input,Max,Min):
    if Input.isdigit() and Min<=int(Input)<=Max:
            print("Valid")
    else:
        while True:
            print("Invalid, please retype your score")
            Input = input()
            if Input.isdigit() and Min<=int(Input)<=Max:
                print("Valid")
                break
    return Input


Input1 = numericalErrorChecking("",13,0)

    
