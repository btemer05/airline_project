import csv
import os
flights = {}
FLIGHTS_FILE = "flights.csv"
def load_flights():
    with open(FLIGHTS_FILE, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            flights[row["flight"]] = {
                "first_price": float(row["first_price"]),
                "econ_price": float(row["econ_price"]),
                "first_booked": int(row["first_booked"]),
                "econ_booked": int(row["econ_booked"]),
            }

def view_flights():
    print("Available Flights:")
    for airport, prices in flights.items():
        print(f" - {airport}: First Class - ${prices['first_price']}, Economy - ${prices['econ_price']}")
def save_flights():
    with open(FLIGHTS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["flight", "first_price", "econ_price", "first_booked", "econ_booked"])
        for code, info in flights.items():
            writer.writerow([code, f"{info['first_price']:.2f}", f"{info['econ_price']:.2f}",
                             info["first_booked"], info["econ_booked"]])       
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
    load_flights()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            view_flights()
        elif choice == "4":
            add_flight()
        elif choice == "7":
            save_flights()
            print("Data saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.\n")

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