import numpy as np
import pandas as pd
df = pd.read_csv("orders-by-type.txt", sep="|")  #opens file and assigns the data to a dataframe
# print(df)
df.columns = ['Index', 'MelonType', 'QtySold'] #defines the column names for the dataframes
# print(df)
m = df.groupby('MelonType')['QtySold']  #groups the quantities of melons sold by the melon type
melons_sold = m.sum()  #sums the quantities of melons sold
# print(melons_sold)
print("*" * 80, "\n") #prints line to separate returned data

melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }  #assigns the prices for the melons and assigns the prices to the melon types

for melon_type, melon_count in melons_sold.items():  #iterating through the rows and assigning variables to each item
    price = melon_prices[melon_type]  #defining variable for price
    melon_revenue = price * melons_sold[melon_type]  #calculating revenue for each melon type

    print(f"We sold {melon_count} {melon_type} melons at ${price:.2f} each for a total of ${melon_revenue:,.2f}.", "\n")

print("*" * 80, "\n") #prints line to separate returned data

orderTypes = pd.read_csv("orders-with-sales.txt", sep="|")  #opens file and assigns the data to a dataframe
# print(orderTypes)
orderTypes.columns = ['Index', 'SalesId', 'SalesRep', 'OrderTotal'] #defines the column names for the dataframes
# print(orderTypes)

s = orderTypes[orderTypes['SalesId'] > 0] #assigns variable to rows that meet the conditional
# print(s)
p_sales = s.sum()  #assigns variable to the sum of these rows
phone_sales = p_sales['OrderTotal']  #assigns variable to the specified summed row
# print(phone_sales['OrderTotal'])

o = orderTypes[orderTypes['SalesId'] == 0]  #assigns variable to rows that meet the conditional
# print(o)
o_sales = o.sum()  #assigns variable to the sum of these rows
online_sales = o_sales['OrderTotal']  #assigns variable to the specified summed row

print(f"Salespeople generated ${phone_sales:,.2f} in revenue.", "\n")
print(f"Internet sales generated ${online_sales:,.2f} in revenue.", "\n")

if phone_sales > online_sales:  #compares the values of the variables to perform the specified action

# if sales[1] > sales[0]:
    print("Guess there's some value to those salespeople after all.", "\n")
else:
    print("Time to fire the sales team! Online sales rule all!", "\n")
print("*" * 80)