SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
DORKY_LINE_LENGTH = 80

print("*" * DORKY_LINE_LENGTH)
f = open("orders-by-type.txt") #opens txt file for us to pull data from
melon_tallies = {0} # setting base tally at 0

for l in f:
    data = l.split("|")
    melon_type = data[1] # set melon_type data as the second index before |
    melon_count = int(data[2]) # sets melon_count as the starting number in the third index separated by |

    melon_tallies[melon_type] += melon_count
    #sets the tally at zero for the different melon types, melon_count will add or subtract depending on sales

#everything between here and the open clause is where we are starting tallies setting our variables, and splitting up the information by the usage of |

f.close() # closing txt file

melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }

total_revenue = 0

for melon_type in melon_tallies:
    price = melon_prices[melon_type]
    revenue = price * melon_tallies[melon_type]
    total_revenue += revenue

    # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue))

    print(f"We sold {melon_tallies[melon_type]} {melon_type} melons at {price:.2f} each for a total of {revenue:.2f}")
print("******************************************")
f = open("orders-with-sales.txt")
sales = [0, 0]
for line in f:
    d = line.split("|")
    if d[1] == "0":
        sales[0] += float(d[3])
    else:
        sales[1] += float(d[3])
print(f"Salespeople generated ${sales[1]:.2f} in revenue.")
print(f"Internet sales generated ${sales[0]:.2f} in revenue.")
if sales[1] > sales[0]:
    print("Guess there's some value to those salespeople after all.")
else:
    print("Time to fire the sales team! Online sales rule all!")
print("******************************************")
