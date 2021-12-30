"""Generate sales report showing total melons each salesperson sold."""
import pandas as pd
salespeople = []
melons_sold = []

df = pd.read_csv("sales-report.txt", sep="|") 

df.columns = ['salesperson', 'revenue', 'NumOfMelons']

#calculating the melons sold by each person could be simplified by:

newDF = df.groupby(['salesperson']).sum().sort_values("NumOfMelons", ascending=False)

#print whatever salespersons' name sold however many melons they sold