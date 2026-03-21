import pandas as pd

data = {
    "state": ["State1", "State2", "State3", "State4", "State5"],
    "area": [120000, 90000, 150000, 110000, 80000],
    "population": [5000000, 7000000, 6000000, 8000000, 4000000]
}

df = pd.DataFrame(data)

while True:
    print("\n1.Display All States\n2.State with Largest Area\n3.State with Largest Population\n4.Calculate Population Density\n5.State with Highest Density\n6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print(df)

    elif choice == "2":
        print(df.loc[df["area"].idxmax(), "state"])

    elif choice == "3":
        print(df.loc[df["population"].idxmax(), "state"])

    elif choice == "4":
        df["density"] = df["population"] / df["area"]
        print(df[["state", "density"]])

    elif choice == "5":
        if "density" not in df.columns:
            df["density"] = df["population"] / df["area"]
        print(df.loc[df["density"].idxmax(), "state"])

    elif choice == "6":
        break

    else:
        print("Invalid choice")