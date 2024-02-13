# 8.3-8.5
def make_shirt(size='large', text='I love Python'):
    """Display information about a shirt"""
    print(f'The size of the shirt is {size}, and "{text}" is written on it.')
make_shirt()
make_shirt('medium')
make_shirt(size='medium', text='Cybersecurity')

print('\n')

def describe_city(city, country='America'):
    """Display information about a city"""
    print(f'{city.title()} is in {country.title()}')
describe_city(city='Anderson')
describe_city(city='New York')
describe_city(city='London', country='England')