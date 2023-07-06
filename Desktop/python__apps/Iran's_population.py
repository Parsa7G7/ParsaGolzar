print("""The work of this calculator is 
to predict the future population of Iran 
and it is designed according to the latest
 statistics of the past years of this country.""")

future_years = int(input("how many future year: "))


#Population statistics of 2022
population = 84948786
men = 42922830
women = 42025955

#Statistics of people born in 2022
latestـstatistics = 893786
the_boys = 70125
the_girls = 66838


# Output counter
total = (latestـstatistics * future_years) + population
total_men = (the_boys * future_years) + men
total_women = (the_girls * the_girls) + women

populationـdict = {"total":total}
dic_of_men = {"total men":total_men}
dict_of_women = {"total women":total_women}

all = [populationـdict,dic_of_men,dict_of_women,]


# the users choice 
print("""
1_population
2_men
3_women
4_all
""")
user_chose = int(input("Which episode do you want to see?(Please write the number of the section you want): "))

if user_chose > 4 or user_chose < 1:
        print("error")

else:  

    if user_chose == 1:
        print(populationـdict)

    if user_chose == 2:
        print(dic_of_men)

    if user_chose == 3:
        print(dict_of_women)

    if user_chose == 4:
        print(all)


















