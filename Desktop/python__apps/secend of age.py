print("Enter your full age . Enter your exact age at the beginning of the year, then  month, and day.")
Seconds_of_a_year = 31536000
Seconds_of_a_month = 2592000
Seconds_of_a_day = 86400


year = float(input("enter your age year  :"))
month = float(input("enter your age month :"))
day = float(input("enter your age day :"))

secends_year = Seconds_of_a_year * year
secends_month = Seconds_of_a_month * month
secends_day = Seconds_of_a_day * day
total_secends = secends_year + secends_month + secends_day


Seconds_of_the_year = {"Seconds of your year":secends_year}
Seconds_of_the_month = {"Seconds of your month":secends_month}
Seconds_of_the_day = {"Seconds of your day":secends_day}
Total_seconds_of_age = {"Total seconds of your age":total_secends}

full_second = [Seconds_of_the_year,Seconds_of_the_month,Seconds_of_the_day,Total_seconds_of_age]

print(full_second)