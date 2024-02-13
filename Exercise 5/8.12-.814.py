def sandwhich(*ingredients):
    print(ingredients)

sandwhich('ham','cheese')
sandwhich('turkey','pickles','mayo')
sandwhich('beef')

print('\n')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('JonMichael', 'Williams', location='Anderson', field='cybersecurity', hobby='video games')
print(user_profile)

print('\n')

def car_info(manufacturer, model, **additional_info):
    additional_info['manufacturer'] = manufacturer
    additional_info['model'] = model
    return additional_info

car =car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)