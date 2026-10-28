# Cab Booking & Fare Management System

rides = []   # list of dictionaries, stored in memory


def display_menu():
    print("\n====================================")
    print("       CAB BOOKING SYSTEM")
    print("====================================")
    print("1. Book Ride")
    print("2. View Ride History")
    print("3. Search Ride")
    print("4. Revenue Report")
    print("5. Exit")
    print("====================================")


def calculate_fare(distance):
    if distance <= 5:
        rate = 15
    elif distance <= 15:
        rate = 12
    else:
        rate = 10
    return 50 + distance * rate      # base fare Rs.50 + distance cost


def book_ride():
    name = input("Customer Name : ")
    pickup = input("Pickup Location : ")
    drop = input("Destination : ")
    try:
        distance = float(input("Distance (KM) : "))
    except ValueError:
        print("Invalid distance! Enter a number.")
        return
    if name == "" or distance <= 0:
        print("Name cannot be empty and distance must be above 0.")
        return

    fare = calculate_fare(distance)
    ride = {"name": name, "pickup": pickup, "drop": drop,
            "distance": distance, "fare": fare}
    rides.append(ride)
    print("Ride booked! Fare: Rs.", fare)


def view_rides():
    if len(rides) == 0:
        print("No rides booked yet.")
        return
    print(f"{'Customer':<12}{'Pickup':<12}{'Destination':<14}{'Distance':<10}{'Fare'}")
    for r in rides:
        print(f"{r['name']:<12}{r['pickup']:<12}{r['drop']:<14}{r['distance']:<10}Rs.{r['fare']}")


def search_ride():
    name = input("Enter customer name to search: ")
    found = False
    for r in rides:
        if r["name"].lower() == name.lower():
            print("Name:", r["name"], "| From:", r["pickup"], "| To:", r["drop"],
                  "| Distance:", r["distance"], "KM | Fare: Rs.", r["fare"])
            found = True
    if not found:
        print("No ride found for", name)


def revenue_report():
    if len(rides) == 0:
        print("No rides booked yet.")
        return
    total_rides = len(rides)
    total_revenue = sum(r["fare"] for r in rides)
    total_distance = sum(r["distance"] for r in rides)
    longest = max(rides, key=lambda r: r["distance"])
    highest = max(rides, key=lambda r: r["fare"])

    print("\n========= REVENUE REPORT =========")
    print("Total Rides      :", total_rides)
    print("Total Revenue    : Rs.", total_revenue)
    print("Average Fare     : Rs.", round(total_revenue / total_rides, 2))
    print("Average Distance :", round(total_distance / total_rides, 2), "KM")
    print("Longest Ride     :", longest["name"], "-", longest["distance"], "KM")
    print("Highest Fare     :", highest["name"], "- Rs.", highest["fare"])
    print("==================================")


# Main program
while True:
    display_menu()
    choice = input("Enter Your Choice: ")
    if choice == "1":
        book_ride()
    elif choice == "2":
        view_rides()
    elif choice == "3":
        search_ride()
    elif choice == "4":
        revenue_report()
    elif choice == "5":
        print("Thank you! Goodbye.")
        break
    else:
        print("Invalid choice! Please enter 1 to 5.")