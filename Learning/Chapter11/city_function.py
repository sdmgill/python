def get_city_country(city, country, population):
    """Format a City, Country combo"""
    formatted_city = city + ', ' + country + ' - population ' + str(population)
    return formatted_city.title()