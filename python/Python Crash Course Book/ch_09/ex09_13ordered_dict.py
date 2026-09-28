from collections import OrderedDict

glossary = OrderedDict()

glossary['Traceback'] = 'A explanation from errors'
glossary['Conditionals'] = 'Decisions based in True or False answers'
glossary['Tuples'] = "List which we can't altered"
glossary['PEP 8'] = "Official list of good conducts for programming"
glossary['List Comprehension'] = 'Lists compose for instructions, like a math function'
glossary['List Indices'] = 'Position of elements in a list'
glossary['Conjuntion'] = 'A list withou repeated elements'
glossary['Float'] = 'Numbers with decimal parts'
glossary['Slices'] = 'Parts of a list'

for word, meaning in glossary.items():
    print('\n\tMeaning of ' + word + "\n" + meaning)