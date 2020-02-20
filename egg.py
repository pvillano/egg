from collections import defaultdict
from itertools import product, chain

"""
This whole thing started with the following question:

    Can you determine where all the eggs are in a carton without looking inside?
    
"""


def flatten(list_of_lists):
    """Flatten one level of nesting"""
    return chain.from_iterable(list_of_lists)


def equivalence_classes(items, key):
    """Separate items into equivalence classes using function key"""
    seen = defaultdict(list)
    for item in items:
        key_value = key(item)
        seen[key_value].append(item)
    return seen


def egg_coords(carton):
    """Yields the coordinates where there are eggs"""
    for y, row in enumerate(carton):
        for x, value in enumerate(row):
            if value:
                yield x, y, 0


def mass(carton):
    return sum(flatten(carton))


def central_moment(carton):
    moment_list = [0, 0, 0]
    for big_x in egg_coords(carton):
        for i in range(3):
            moment_list[i] += big_x[i]
    return tuple(moment_list)


def inertia_tensor(carton):
    inertia_tensor = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    for big_x in egg_coords(carton):
        for i, j in product(range(3), range(3)):
            if i == j:
                for k in range(3):
                    inertia_tensor[i][j] += big_x[k] ** 2
            inertia_tensor[i][j] -= big_x[i] * big_x[j]
    return tuple([tuple(x) for x in inertia_tensor])


def distinguishable_carton(carton):
    return mass(carton), central_moment(carton), inertia_tensor(carton)


def print_equivalence_classes(classes_dict):
    for key, carton_list in classes_dict.items():
        if len(carton_list) > 1:
            print(key)
            for carton in carton_list:
                for row in carton:
                    print(row)
                print()

if __name__ == "__main__":
    rows = 2
    columns = 6
    cartons = product(product([0, 1], repeat=columns), repeat=rows)
    grouped_cartons = equivalence_classes(cartons, distinguishable_carton)

    sings = {k: v for (k, v) in grouped_cartons.items() if len(v) == 1}
    dupes = {k: v for (k, v) in grouped_cartons.items() if len(v) == 2}
    trips = {k: v for (k, v) in grouped_cartons.items() if len(v) == 3}

    print_equivalence_classes(sings)
    print_equivalence_classes(dupes)
    print_equivalence_classes(trips)

    print("number of equivalence classes", len(grouped_cartons))
    print("unique arrangements", len(sings))
    print("paired arrangements", len(dupes))
    print("triplet arrangements", len(trips))

