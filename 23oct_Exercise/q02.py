# Q2. Long city names


cities = ["Lahore", "Multan", "Karachi", "Quetta", "Peshawar", "Bahawalpur"]

for city in cities:
    if len(city) > 6:
        print(f"{city} has '{len(city)}' letter")