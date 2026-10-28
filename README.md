# 🚖 Cab Booking & Fare Management System

A simple menu-driven Python program to book cab rides, calculate fares, search bookings and view revenue reports. Built as a beginner project using **functions, loops, conditions, lists and dictionaries**. No database is used; all data is stored in memory while the program runs.

## ✨ Features

- **Book a Ride** – enter customer name, pickup, destination and distance; the fare is calculated automatically
- **View Ride History** – see all booked rides in a table
- **Search Ride** – find a booking by customer name (not case-sensitive)
- **Revenue Report** – total rides, total revenue, average fare, average distance, longest ride and highest fare
- **Input validation** – rejects empty names, non-numeric or zero/negative distances, and invalid menu choices

## 💰 Fare Rules

| Distance      | Rate per KM |
|---------------|-------------|
| 0 – 5 KM      | ₹15         |
| 6 – 15 KM     | ₹12         |
| Above 15 KM   | ₹10         |

**Total Fare = ₹50 (base fare) + Distance × Rate**

Examples:
- 8 KM → 50 + 8 × 12 = **₹146**
- 20 KM → 50 + 20 × 10 = **₹250**

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository:
   ```bash
   git clone https://github.com/<your-username>/cab-booking-system.git
   cd cab-booking-system
   ```
3. Run the program:
   ```bash
   python cab_system.py
   ```

## 🖥 Sample Output

```
====================================
       CAB BOOKING SYSTEM
====================================
1. Book Ride
2. View Ride History
3. Search Ride
4. Revenue Report
5. Exit
====================================
Enter Your Choice: 4

========= REVENUE REPORT =========
Total Rides      : 2
Total Revenue    : Rs. 396.0
Average Fare     : Rs. 198.0
Average Distance : 14.0 KM
Longest Ride     : Priya - 20.0 KM
Highest Fare     : Priya - Rs. 250.0
==================================
```

## 🧩 Functions Used

| Function | Purpose |
|----------|---------|
| `display_menu()` | Shows the main menu |
| `calculate_fare(distance)` | Returns the fare for a given distance |
| `book_ride()` | Takes ride details and stores them |
| `view_rides()` | Displays all booked rides |
| `search_ride()` | Searches rides by customer name |
| `revenue_report()` | Shows revenue and ride statistics |
