def make_album(album_artist, album_title, album_tracks=''):
    '''Create a dicionary with album informations.'''
    album = {
        'artist' : album_artist,
        'title' : album_title
        }
    if album_tracks:
        album['tracks'] = album_tracks
    return album

while True:

    artist_var = input(
        "What's the name of your favorite artist?" + 
        "(Type 'q' and Enter for exit)\n"
    )
    if artist_var == 'q':
        break


    title_var = input(
        "What is the name of the famous album from your favorite artist?" + 
        "(Type 'q' and Enter for exit)\n"
    )
    if title_var == 'q':
        break


    tracks_var = input(
        "How many tracks does this album have?(Press enter to skip)" +
        "(Type 'q' and Enter for exit)\n"
        )
    if tracks_var == 'q':
        break
    
# Printing, but not saving.
    album_var = make_album(artist_var, title_var, tracks_var)
    print(album_var)