import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

months = df['month_number']

plt.figure()
plt.plot(months, df['total_profit'])
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.title("Total Profit by Month")
plt.show()

plt.figure()
plt.plot(months, df['facecream'], label='Face Cream')
plt.plot(months, df['facewash'], label='Face Wash')
plt.plot(months, df['toothpaste'], label='Toothpaste')
plt.plot(months, df['bathingsoap'], label='Bathing Soap')
plt.plot(months, df['shampoo'], label='Shampoo')
plt.plot(months, df['moisturizer'], label='Moisturizer')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Product Sales Data")
plt.legend()
plt.show()

plt.figure()
width = 0.35
plt.bar(months - width/2, df['facecream'], width, label='Face Cream')
plt.bar(months + width/2, df['facewash'], width, label='Face Wash')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Face Cream and Face Wash Sales")
plt.legend()
plt.show()

total_sales = [
    df['facecream'].sum(),
    df['facewash'].sum(),
    df['toothpaste'].sum(),
    df['bathingsoap'].sum(),
    df['shampoo'].sum(),
    df['moisturizer'].sum()
]

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.figure()
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Total Sales Distribution")
plt.show()