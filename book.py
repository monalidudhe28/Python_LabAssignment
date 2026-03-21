import pandas as pd

df = pd.read_csv("books.csv")

while True:
    print("\n1.Display All Books\n2.Books by Author\n3.Books by Publisher\n4.Cheapest and Costliest Book\n5.Sort by Year\n6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print(df)

    elif choice == "2":
        author = input("Enter author name: ")
        print(df[df["author"] == author])

    elif choice == "3":
        publisher = input("Enter publisher: ")
        print(df[df["publishing_house"] == publisher])

    elif choice == "4":
        min_price = df[df["price"] == df["price"].min()]
        max_price = df[df["price"] == df["price"].max()]
        print("Cheapest Book:")
        print(min_price[["title"]])
        print("Costliest Book:")
        print(max_price[["title"]])

    elif choice == "5":
        print(df.sort_values(by="publication_year"))

    elif choice == "6":
        break

    else:
        print("Invalid choice")