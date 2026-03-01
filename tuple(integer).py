user_input = input("Enter a series of integers separated by spaces: ")

numbers = tuple(map(int, user_input.split()))

print("Total number of items:", len(numbers))

if len(numbers) > 0:
    print("Last item:", numbers[-1])
else:
    print("Tuple is empty.")

print("Tuple in reverse order:", numbers[::-1])

if 5 in numbers:
    print("Yes")
else:
    print("No")

if len(numbers) > 2:
    modified = numbers[1:-1]
    sorted_modified = tuple(sorted(modified))
    print("Sorted tuple after removing first and last items:", sorted_modified)
else:
    print("Not enough elements to remove first and last items.")