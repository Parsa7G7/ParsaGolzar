x = 10
while x > 2:
    print("""
    1_+
    2_-
    3_*
    4_/
    5_//
    6_%
        """)


    choose = int(input("choose yourthe operation : "))

    if choose < 1 or choose > 6: 
                print("error")
                

    number1 = int(input("write frist number : "))
    number2 = int(input("write your secend number :"))


    if choose == 1:
        end = number1 + number2
        print(end)


    if choose == 2:
        end = number1 - number2
        print(end)

    if choose == 3:
        end = number1 * number2
        print(end)


    if choose == 4:
        end = number1 / number2
        print(end)


    if choose == 5:
        first = number2 // 100
        end = number1 // first
        print(end)

    if choose == 6:
        first = number2 / 100
        end = number1 / first
        print(end)

    repetition = input("Do you want to use the calculator again?") 
    
    if (repetition[0] == 'n' or repetition[0] == 'N'):
         break
    if (repetition[0] == 'y' or repetition[0] == 'Y'):
         continue


    