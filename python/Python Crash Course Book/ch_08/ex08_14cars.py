def make_car(made, model, **info):
    '''Create a dicionary with car informations, with model and made default.'''
    data = {}
    data['made'] = made
    data['model'] = model
    for keys, values in info.items():
        data[keys] = values
    return data

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)