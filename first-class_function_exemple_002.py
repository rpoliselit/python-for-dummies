def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element
    msg = f"Could not find an element with {expected}."
    raise RuntimeError(msg)

friends = [
    {'name' : 'Nelmo', "age": 28},
    {"name" : 'Rodrigo', 'age': 30},
    {"name" : 'Raphael', 'age': 31},
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, 'Rodrigo', get_friend_name))
