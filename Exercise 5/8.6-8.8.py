# 8.6-8.8
def city_country(city, country):
    """Display a city and a country"""
    print(f'{city.title()}, {country.title()}')
city_country('Santiago', 'Chile')
city_country('Anderson', 'USA')
city_country('London', 'England')

print('\n')

def make_album(artist_name,album_title,number=None):
    """Display information about an album"""
    album = {'Artist Name': artist_name, 'Album Title': album_title}
    if number:
        album['Songs'] = number
    return album
thriller = make_album('Michael Jackson', 'Thriller', '9')
back_in_black = make_album('AC/DC', 'Back in Black')
bodyguard = make_album('Whitney Houston', 'The Bodyguard')
print(thriller)
print(back_in_black)
print(bodyguard)

while True:
    print("\nPlease enter artist name and album:")
    print("(press 'q' to quit)")

    art_name = input('Artist Name:')
    if art_name == 'q':
        break

    al_title = input('Album Title:')
    if al_title == 'q':
        break

    artistalbum = make_album(art_name,al_title)
    print(artistalbum)