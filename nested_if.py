myanmar = float(input("Enter Marks for Myanmar"))
eng = float(input("Enter Marks for English"))
maths = float(input("Enter Marks for Maths"))

if myanmar >= 40:  
    print('Exam Pass')
        if eng >= 40:
            print('Exam Pass')
        else:
            print('Fail')
            if maths >= 40:
                print('Exam Pass')
            else:
                print('Fail')
else:
    print('Fail')
