magicians_names = ['Mister M', 'Patrick Jane', 'Harry Houdini']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for position in range(0, len(magicians)): # len for any list size
        magicians[position] = 'The Great ' + magicians[position]
    return magicians

great_magicians = make_great(magicians = magicians_names[:])
show_magicians(magicians = magicians_names)
show_magicians(magicians = great_magicians)