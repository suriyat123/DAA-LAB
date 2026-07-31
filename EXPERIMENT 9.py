
def first_fit_decreasing(items, capacity):
    # Sort items in decreasing order
    items.sort(reverse=True)

    bins = []

    for item in items:
        placed = False

        # Try to place item in an existing bin
        for b in bins:
            if sum(b) + item <= capacity:
                b.append(item)
                placed = True
                break

        # If item doesn't fit, create a new bin
        if not placed:
            bins.append([item])

    return bins


# Main Program
items = [8, 5, 7, 6, 2, 4, 1, 3]
capacity = 10

bins = first_fit_decreasing(items, capacity)

print("Items:", items)
print("Bin Capacity:", capacity)

print("\nBins:")
for i, b in enumerate(bins, start=1):
    print(f"Bin {i}: {b}  (Used: {sum(b)}/{capacity})")

print("\nTotal Bins Required:", len(bins))

