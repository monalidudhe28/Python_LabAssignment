prices_input = input("Enter the prices of sold items separated by spaces: ")

prices = tuple(map(float, prices_input.split()))

print(len(prices))

if len(prices) > 0:
    print(min(prices))
    print(max(prices))
    print(tuple(sorted(prices)))
    print(prices.count(max(prices)))
else:
    print("No items sold.")