Income = int(input("How much is your income ? "))
print ("""1_Tax and insurance percentage.Choose number one.1
2_Tax and insurance amount.Choose number two.
""")


def calculator():

    choose = int(input("Choose the option you want. 1 or 2 : "))

    if choose < 1 or choose > 2 :
        print("error")
        calculator()
        
    else:
        if choose == 1:
            your_insurance = float(input("How much do you pay for insurance ? "))
            One_percent_of_income:float = Income / 100
            Tax_percentage:float = your_insurance / One_percent_of_income
            print (Tax_percentage)

        
        if choose ==2:
            your_insurance = float(input("How much (percentage) do you pay for insurance ? "))
            One_percent_of_income:float = Income / 100
            Taxـamount:float = your_insurance * One_percent_of_income
            print(Taxـamount)



calculator()



                
                  
                
