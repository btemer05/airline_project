import matplotlib.pyplot as plt
import airline


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
        empty.append(airline.FIRST_SEATS + airline.ECON_SEATS - info["first_booked"] - info["econ_booked"])

    plt.figure()
    plt.bar(codes, empty)
    plt.title("Empty Seats by Flight")
    plt.xlabel("Flight (destination)")
    plt.ylabel("Empty seats")
    plt.savefig("empty_seats_by_flight.png")

    print("Charts saved as revenue_by_flight.png and empty_seats_by_flight.png.\n")
    plt.show()
