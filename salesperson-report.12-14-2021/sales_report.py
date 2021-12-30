"""Generate sales report showing total melons each salesperson sold."""

salespeople = [] #initiates salespeople variable
melons_sold = [] #initiates melons_sold variable

f = open('sales-report.txt') #opens and reads file 
for line in f:
    line = line.rstrip()
    entries = line.split('|')

#lines 7-9 splits the info by each | divider, also strips them of whitespace. 
# this could be simplified by writing it as follows:
#  df = pd.read_csv("sales-report.txt", sep="|") which would do the same thing and would put the info in a neat dataframe format 
  
    salesperson = entries[0] # sets the salesperson variable as the first index value in entries
    melons = int(entries[2]) # sets the melons variable as the third index value in entries, converted to an integer.

#lines 15-16 could be simplified by defining columns in the dataframe, like this: df.columns = ([salesperson], [revenue], [NumOfMelons])

    if salesperson in salespeople: #if the value in entries[0] is in the salespeople [],
        position = salespeople.index(salesperson) #.index gives us a way to identify specific rows

        melons_sold[position] += melons #melons_sold[whoever the sales person is], add a melon for each sale 
    else:
        salespeople.append(salesperson) #add that salesperson to the df
        melons_sold.append(melons) #add their melon tally to the melons_sold

for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') #print whatever salespersons' name sold however many melons they sold

#calculating the melons sold by each person could be simplified by:
# df.groupby(["salesperson"]).sum().sort_values("NumOfMelons", ascending=False)

