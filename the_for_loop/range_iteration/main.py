# List of countries
countries = ['Wales', 'Denmark', 'Belgium', 'Japan', 'South Korea', 'South Africa',
             'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico',
             'Turkey', 'Greece', 'Netherlands', 'Finland', 'Monako', 'United Arab Emirates',
             'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile',
             'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'Luxemburg',
             'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary',
             'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# Prepare your list
your_travel_list = []

# Iterate over even indexes using correct range call
for i in range(0, len(countries), 2):
    your_travel_list.append(countries[i])

# Testing
print("Your Travel List:",your_travel_list)