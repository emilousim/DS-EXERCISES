import numpy as np
import pandas as pd
df = pd.read_csv("orders-by-type.txt", sep="|") 
#reads file into a dataframe.
df.columns = ['Index', 'MelonType', 'NumSold']
#sets each columns' name 
# print(df)
mels = df.groupby('MelonType')['NumSold']
#groups numbers of melons sold by melon type
melons_sold = mels.sum()
print(melons_sold)
#sums number sold

melon_prices = {"Musk" : 1.15, "Hybrid" : 1.30, "Watermelon" : 1.75, "Winter" : 4.00} #assigns each melon's price value

for melon_type, melon_count in melons_sold.items(): 
    #runs through each row and assigns variables to each melon
    price = melon_prices[melon_type] #setting up a variable for price
    melon_revenue = price * melons_sold[melon_type] #calculates revenue earned for each type
    
    print(f"We sold {melon_count} {melon_type} melons at ${price:.2f} each for a total of ${melon_revenue:,.2f}.", "\n")

orderTypes = pd.read_csv("orders-with-sales.txt", sep="|") #reads sales orders file into a df
# print(orderTypes)
orderTypes.columns = ["Index", "SalesId", "SalesRep", 'OrderTotal']
#sets column names
# print(orderTypes)

s = orderTypes[orderTypes['SalesId'] > 0] #variable for rows meeting the conditional
# print(s)

p_sales = s.sum() #assigns variable to sum of s
phone_sales = p_sales['OrderTotal'] #assigns variable to specific summed row

o = orderTypes[orderTypes['SalesId'] == 0 ] #assigns variable to rows meeting the conditional

o_sales = o.sum()
online_sales = o_sales['OrderTotal'] # assigns variable to specified summed row

print(f"Salespeople generated ${phone_sales:,.2f} in revenue.", "\n")
print(f"Internet sales generated ${online_sales:,.2f} in revenue.", "\n")

if phone_sales > online_sales:
    print("Guess we gotta keep the salespeople")
else:
    print("Time to fire the sales team! The internet will rule us all.")

