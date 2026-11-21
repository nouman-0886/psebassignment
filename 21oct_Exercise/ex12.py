# Exercise 12: Ride fare calculator


km = float(input("Enter distance in km: "))
hour = int(input("Enter hour (0-23): "))

# Calculate base fare
fare = 100 + (40 * km)

# Check if it's night (hour 22 or later, OR before 6)
if hour >= 22 or hour < 6:
    f_fare = fare + (fare * 0.20) 
    print(f"Final fare: Rs {f_fare} 'with 20% night surcharge'")
else:
    print(f"Your fare is: {fare}")

