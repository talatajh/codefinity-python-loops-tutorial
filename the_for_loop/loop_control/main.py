# List of countries you are considering for travel
countries = ['Wales', 'Denmark', 'Belgium', 'Japan', 'South Korea', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']
travel_list = []
visa_required = ['China', 'India', 'Saudi Arabia', 'Brazil', 'United Arab Emirates', 'Egypt']
for country in countries:
    if country in visa_required:
        continue
    else:
        travel_list = travel_list + countries
    if len(travel_list) == 10:
        break
    
 
print('Visa-free travel destinations:', travel_list)