import datetime

def print_header():
    print('-----------------------')
    print('\t Birthday App')
    print('-----------------------' + '\n')


def get_birthday_from_user():
    print("Input information when you were born: ")
    year = int(input("Year [YYYY]"))
    month = int(input("Month [MM]"))
    day = int(input("Day [DD]: "))

    birthday = datetime.datetime(year, month, day)
    return birthday


def compute_days_between_dates(original_date, now):
    birthday_this_year = datetime.datetime(now.year, original_date.month, original_date.day)
    timedelta = now - birthday_this_year
    # days = int(timedelta.total_seconds() / 60 /60 /24)
    return timedelta.days


def print_birthday_information(days):
    if days < 0:
        print(f'Your birthday is in {abs(days)} days!')
    elif days > 0:
        print(f"You had your birthday already this year! {days} days ago.")
    else:
        print("Happy birthday!")


def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)

main()