cities = []

while True:
    city = input("Enter the name of a city (or type 'stop' in lower-case to finish): ")
    if city.lower() == 'stop':
        break   
    population = len(city) * 1000000
    cities.append((city, population))

cities.sort(key=lambda x: x[1], reverse=True)

print("\nCities sorted by population (largest to smallest):")
for city, population in cities:
    print(f"{city}: {population} citizens")