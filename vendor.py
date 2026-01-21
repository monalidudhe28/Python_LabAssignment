vendor_name = input("Enter Vendor Name: ")
year = input("Enter Year of Association: ")
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")
total_purchase = 0
print("\nEnter Monthly Purchase Amounts:")
for month in range(1, 13):
    amount = float(input(f"Month {month}: "))
    total_purchase += amount

print("\n--- Vendor Annual Purchase Report ---")
print("Vendor Name:", vendor_name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("Total Annual Purchase:", total_purchase)