def make_album(album_artist, album_title, album_tracks = ''):
    album = {
        'artist' : album_artist,
        'title' : album_title
        }
    if album_tracks:
        album['tracks'] = album_tracks
    return album

sabrina = make_album(
    album_artist = "Sabrina Carpenter",
    album_title = "Man's Best Friend",
    album_tracks = 12
    )
    
bruno = make_album(
    album_artist = "Bruno Mars",
    album_title = "The Romantic",
    )

harry = make_album(
    album_artist = "Harry Styles",
    album_title = "Kiss All The Time Disco, Occasionally",
    ) 

print(sabrina)
print(bruno)
print(harry)