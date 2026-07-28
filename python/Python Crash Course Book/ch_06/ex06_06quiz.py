favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
guests = ['sarah', 'gustavo', 'jen', 'isaque']
for guest in guests:
    if guest in favorite_languages.keys():
        print(guest.title() + ', thanks for the vote!')
    else:
        print(guest.title() + ', vote for your favorite languague, please.')