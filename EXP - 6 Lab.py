
#
regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
colors = ["Red", "Green", "Blue"]

neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

assignment = {}
attempts = 0

def is_safe(region, color):
    for neighbor in neighbors[region]:
        if assignment.get(neighbor) == color:
            return False
    return True

def solve(index):
    global attempts

    if index == len(regions):
        return True

    region = regions[index]

    for color in colors:
        attempts += 1

        if is_safe(region, color):
            assignment[region] = color

            if solve(index + 1):
                return True

            del assignment[region]  # Backtrack

    return False

if solve(0):
    print("Map Colouring Assignment:")
    for region in regions:
        print(region, ":", assignment[region])

    valid = all(
        assignment[r] != assignment[n]
        for r in regions
        for n in neighbors[r]
    )

    print("All constraints satisfied:", valid)
    print("Assignments attempted:", attempts)
else:
    print("No valid colouring found.")
