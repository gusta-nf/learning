def build_profile(first, last, **info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', 
location='princeton', field='physics')
print(user_profile)

user_gustavo = build_profile('gustavo', 'fernandez', 
location='angra', field='computer science', occupation='student')
print(user_gustavo)