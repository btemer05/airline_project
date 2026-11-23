import airline
import reports


# Prints all the menu options from the Week 1 plan.
def show_menu():
    print("1. View Flights")
    print("2. Book Passenger")
    print("3. Cancel a Booking")
    print("4. Add Flight")
    print("5. Booking Report")
    print("6. Charts")
    print("7. Save and Exit")


# Runs the menu loop until the user chooses to save and exit.
def main():
    airline.load_bookings()
    airline.load_flights()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            airline.view_flights()
        elif choice == "2":
            airline.book_passenger()
        elif choice == "4":
            airline.add_flight()
        elif choice == "5":
            reports.show_report(airline.bookings)
        elif choice == "6":
            reports.make_charts(airline.flights, airline.bookings)
        elif choice == "3":
            print("Coming soon\n")
        elif choice == "7":
            airline.save_flights()
            airline.save_bookings()
            print("Data saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.\n")


if __name__ == "__main__":
    main()
