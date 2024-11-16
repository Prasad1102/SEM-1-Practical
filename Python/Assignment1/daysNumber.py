def convert_days(days):
    days_in_year = 365
    days_in_month = 30

    years = days // days_in_year
    remaining_days = days % days_in_year
    months = remaining_days // days_in_month
    days = remaining_days % days_in_month

    print(f"{years} years, {months} months, and {days} days")

days_input = int(input("Enter the number of days: "))
convert_days(days_input)

# prasadshelke@Prasads-MacBook-Air Assignment1 main % python3 daysNumber.py 
# Enter the number of days: 200 
# 0 years, 6 months, and 20 days
# prasadshelke@Prasads-MacBook-Air Assignment1 main % python3 daysNumber.py
# Enter the number of days: 365
# 1 years, 0 months, and 0 days
# prasadshelke@Prasads-MacBook-Air Assignment1 main % 