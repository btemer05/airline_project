flights = {
    "DEN": {"first_price": 289.00, "econ_price": 149.00, "first_booked": 8,  "econ_booked": 22},
    "SEA": {"first_price": 219.00, "econ_price": 109.00, "first_booked": 10, "econ_booked": 27},
    "SLC": {"first_price": 249.00, "econ_price": 129.00, "first_booked": 6,  "econ_booked": 18},
    "MSP": {"first_price": 329.00, "econ_price": 179.00, "first_booked": 4,  "econ_booked": 15},
    "PDX": {"first_price": 239.00, "econ_price": 119.00, "first_booked": 7,  "econ_booked": 20},
    "PHX": {"first_price": 309.00, "econ_price": 159.00, "first_booked": 9,  "econ_booked": 25},
}
def view_flights():
    print("Available Flights:")
    for airport, prices in flights.items():
        print(f" - {airport}: First Class - ${prices['first_price']}, Economy - ${prices['econ_price']}")
def show_menu():
    print("1. View Flights")
    print("2. coming soon")
    print("3. coming soon")
    print("4. Add Flight")
    print("5. coming soon")
    print("6. coming soon")
    print("7. Exit")

def add_flight():
    dest = input("Enter the destination airport code (e.g., DEN, SEA): ").strip().upper()
    if dest == "":
        print("You must enter a code.")
        return

    if dest in flights:
        print(f"{dest} already exists. Updating its prices.")
        flights[dest]["first_price"] = get_price("New first class price: ")
        flights[dest]["econ_price"] = get_price("New economy price: ")
        print(f"{dest} prices updated.")
    else:
        print(f"{dest} is a new flight.")
        first = get_price("First class price: ")
        econ = get_price("Economy price: ")
        flights[dest] = {
            "first_price": first,
            "econ_price": econ,
            "first_booked": 0,
            "econ_booked": 0,
        }
        print(f"{dest} added.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_flights()
        elif choice == "4":
            add_flight()
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
# Asks for a price and keeps asking until the user types a valid positive number.
def get_price(prompt):
    while True:
        text = input(prompt).strip()
        if text.replace(".", "", 1).isdigit():
            price = float(text)
            if price > 0:
                return price
            print("Price must be more than 0.")
        else:
            print("Please enter a number, like 149.00.")
if __name__ == "__main__":
    main()