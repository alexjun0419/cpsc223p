from weather import *

def main():
    filename = "weather_data.json"
    data = read_data(filename=filename)

    while True:
        print("*** TUFFY TITAN WEATHER LOGGER MAIN MENU")
        print("1. Set data filename")
        print("2. Add weather data")
        print("3. Print daily report")
        print("4. Print historical report")
        print("9. Exit the program")

        choice = input("Enter menu choice: ")

        if choice == '1':
            filename = input("Enter data filename: ")
            data = read_data(filename=filename)

        elif choice == '2':
            date = input("Enter date (YYYYMMDD): ")
            time = input("Enter time (hhmmss): ")
            temperature = int(input("Enter temperature: "))
            humidity = int(input("Enter humidity: "))
            rainfall = float(input("Enter rainfall: "))

            key = date + time
            data[key] = {'t': temperature, 'h': humidity, 'r': rainfall}
            write_data(data=data, filename=filename)

        elif choice == '3':
            date = input("Enter date (YYYYMMDD): ")
            print(report_daily(data=data, date=date))

        elif choice == '4':
            print(report_historical(data=data))

        elif choice == '9':
            break

if __name__ == "__main__":
    main()
