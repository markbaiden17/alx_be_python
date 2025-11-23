from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date(number_of_days):
    current_date = datetime.now()
    time_change = timedelta(days=number_of_days)
    future_date = current_date + time_change

    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

def main():
    display_current_datetime()

    print("-" * 30)

    try:
        days_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_input)

    except ValueError:
        print("Error! Please enter a valid number.")

main()