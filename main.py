import csv
import os
import matplotlib.pyplot as plt
flights = {}
FLIGHTS_FILE = "flights.csv"
BOOKINGS_FILE = "bookings.csv"
bookings = []
FIRST_SEATS = 10
ECON_SEATS = 30
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
    print("\nAvailable Flights:")
    for code, info in flights.items():
        first_left = FIRST_SEATS - info["first_booked"]
        econ_left = ECON_SEATS - info["econ_booked"]
        print(f" - {code}: First Class ${info['first_price']:.2f} ({first_left} seats left), "
              f"Economy ${info['econ_price']:.2f} ({econ_left} seats left)")
    print()
    
def save_flights():
    with open(FLIGHTS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["flight", "first_price", "econ_price", "first_booked", "econ_booked"])
        for code, info in flights.items():
            writer.writerow([code, f"{info['first_price']:.2f}", f"{info['econ_price']:.2f}",
                             info["first_booked"], info["econ_booked"]])       
def show_menu():
    print("1. View Flights")
    print("2. Book Passenger")
    print("3. Cancel a Booking")
    print("4. Add Flight")
    print("5. Booking Report")
    print("6. Charts")
    print("7. Save and Exit")

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
    load_bookings()
    load_flights()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            view_flights()
        elif choice == "2":
            book_passenger()
        elif choice == "4":
            add_flight()
        elif choice == "5":
            show_report(bookings)
        elif choice == "6":
            make_charts(flights, bookings)
        elif choice == "3":
            print("Coming soon\n")
        elif choice == "7":
            save_flights()
            save_bookings()
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

def load_bookings():
    with open(BOOKINGS_FILE, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            bookings.append({
                "flight": row["flight"],
                "passenger": row["passenger"],
                "seat_class": row["seat_class"],
                "fare": float(row["fare"]),
            })
def save_bookings():
    with open(BOOKINGS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["flight", "passenger", "seat_class", "fare"])
        for b in bookings:
            writer.writerow([b["flight"], b["passenger"], b["seat_class"], f"{b['fare']:.2f}"])
# Books a passenger: checks the input, raises the booked count, and records the booking.
def book_passenger():
    code = input("Flight (destination code): ").strip().upper()
    if code not in flights:
        print("That flight does not exist.\n")
        return

    name = input("Passenger name: ").strip()
    if name == "":
        print("You must enter a name.\n")
        return
    for b in bookings:
        if b["flight"] == code and b["passenger"].lower() == name.lower():
            print(f"{name} is already booked on {code}.\n")
            return

    seat_class = input("Seat class (first/economy): ").strip().lower()
    if seat_class == "first":
        if flights[code]["first_booked"] >= FIRST_SEATS:
            print("First class is full on that flight.\n")
            return
        fare = flights[code]["first_price"]
        flights[code]["first_booked"] += 1
    elif seat_class == "economy":
        if flights[code]["econ_booked"] >= ECON_SEATS:
            print("Economy is full on that flight.\n")
            return
        fare = flights[code]["econ_price"]
        flights[code]["econ_booked"] += 1
    else:
        print("Seat class must be first or economy.\n")
        return

    bookings.append({"flight": code, "passenger": name, "seat_class": seat_class, "fare": fare})
    print(f"Booked {name} on {code} in {seat_class} for ${fare:.2f}.\n")


# Builds a dictionary of total revenue for each flight, like {"DEN": 438.00}.
def revenue_by_flight(bookings):
    totals = {}
    for b in bookings:
        code = b["flight"]
        if code in totals:
            totals[code] += b["fare"]
        else:
            totals[code] = b["fare"]
    return totals


# Prints a summary of all bookings, or a message if there are none.
def show_report(bookings):
    if len(bookings) == 0:
        print("No bookings yet. Book a passenger first.\n")
        return

    total_revenue = 0
    first_count = 0
    econ_count = 0
    for b in bookings:
        total_revenue += b["fare"]
        if b["seat_class"] == "first":
            first_count += 1
        else:
            econ_count += 1

    count = len(bookings)
    average = total_revenue / count
    revenue = revenue_by_flight(bookings)

    top_code = ""
    top_amount = 0
    for code, amount in revenue.items():
        if amount > top_amount:
            top_code = code
            top_amount = amount

    print("\n--- Booking Report ---")
    print(f"Bookings recorded:  {count}")
    print(f"First class:        {first_count}")
    print(f"Economy:            {econ_count}")
    print(f"Total revenue:      ${total_revenue:.2f}")
    print(f"Average fare:       ${average:.2f}")
    print(f"Top flight:         {top_code} (${top_amount:.2f})")
    print("\nRevenue by flight:")
    for code, amount in revenue.items():
        print(f"   {code} ${amount:.2f}")
    print()


# Draws two bar charts, saves them as .png files, and shows them.
def make_charts(flights, bookings):
    if len(bookings) == 0:
        print("No bookings yet, so there is nothing to chart.\n")
        return

    # Chart 1: total revenue for each flight
    revenue = revenue_by_flight(bookings)
    codes = []
    amounts = []
    for code, amount in revenue.items():
        codes.append(code)
        amounts.append(amount)

    plt.figure()
    plt.bar(codes, amounts)
    plt.title("Total Revenue by Flight")
    plt.xlabel("Flight (destination)")
    plt.ylabel("Revenue ($)")
    plt.savefig("revenue_by_flight.png")

    # Chart 2: empty seats on each flight
    codes = []
    empty = []
    for code, info in flights.items():
        codes.append(code)
        empty.append(FIRST_SEATS + ECON_SEATS - info["first_booked"] - info["econ_booked"])

    plt.figure()
    plt.bar(codes, empty)
    plt.title("Empty Seats by Flight")
    plt.xlabel("Flight (destination)")
    plt.ylabel("Empty seats")
    plt.savefig("empty_seats_by_flight.png")

    print("Charts saved as revenue_by_flight.png and empty_seats_by_flight.png.\n")
    plt.show()


if __name__ == "__main__":
    main()