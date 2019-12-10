with open("day_6_input.txt", "r") as f:
    input = f.readlines()


def get_indirect_orbits(object, indirect_orbits):
    try:
        new_object = orbits[object]['d']
        indirect_orbits.append(new_object)
        return get_indirect_orbits(new_object, indirect_orbits)
    except KeyError:
        return indirect_orbits


orbits = {}

for i in input:
    orbiter = i.split(')')[1].rstrip('\n')
    orbitee = i.split(')')[0]
    if orbiter not in orbits:
        orbits[orbiter] = {'d': orbitee}

for o in orbits:
    orbits[o]['i'] = get_indirect_orbits(orbits[o]['d'], [])

count = len(orbits) + sum([len(orbits[o]['i']) for o in orbits])

print(count)
