import datetime

def convert_date(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y")
        return date_obj.strftime("%B %d, %Y")
    except ValueError:
        return "Invalid date format. Please use mm/dd/yyyy."

if __name__ == "__main__":
    print("\nDate conversion:")
    user_date = input("Enter the date (mm/dd/yyyy): ")
    print("Date Output:", convert_date(user_date))
