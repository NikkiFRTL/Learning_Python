
def city_country(city, country, population=''):
    if population:
        formatted = f'{city} {country} - population {population}'
        return formatted.title()
    else:
        formatted = f'{city} {country}'
        return formatted.title()