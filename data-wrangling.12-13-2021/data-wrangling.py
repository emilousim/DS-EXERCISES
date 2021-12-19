import pandas as pd
d = pd.read_csv("StreetSmArts_Murals.csv")
df = pd.DataFrame(d)

print("There are " + str((len(df))) + " rows in this dataframe.") 

df_mean = df["number_of_districts"].mean()
print("On average, murals fall within " + str(df_mean) + " cultural districts.")

visited = []
count = 0
for i in range(3, len(df['zip_code'])):
    if df['zip_code'][i] not in visited:
        visited.append(df['zip_code'][i])
        count += 1

print("Murals have been completed in " + str(count) + " different zipcodes throughout the San Francisco area.")

print("There have been " + str(len(df.index)) + " murals painted so far.")

newDf = df.sort_values(by="artist", ascending=True)
artists = (newDf['artist'])
noDupes = newDf.drop_duplicates(subset="artist", keep="first")
sorted = print(noDupes['artist'].tolist())

# because we're just wanting to look at information pertaining to the actual mural, we're dropping the number_of_districts column as well as the state because the program is a San Francisco specific program, resulting in all of the data being sourced in CA, we're also dropping the geom location, the police district, current supervisor districts, analysis neighborhoods, as well as neighborhoods because it's not needed info. 

to_drop = ['state', 'number_of_districts', 'the_geom', 'SF Find Neighborhoods', 'Current Police Districts', 'Current Supervisor Districts', 'Analysis Neighborhoods', 'Neighborhoods', 'supervisor_district']
df.drop(to_drop, inplace=True, axis=1)
print(df)

#There aren't really any 'outliers' within the dataset, since the numbers are not measurements but identifiers for other info

muralInfo = df[['artist', 'year', 'street_address']]
print(muralInfo)

cols = list(df.columns.values)
print(cols)
df = df[['artist', 'year', 'street_address', 'zip_code', 'city','cultural_districts']]
print(df)
df['full_address'] = df["street_address"].map(str) + ", " + df["city"].map(str) + ", " + "CA" + ", " + df["zip_code"].map(str)

drop_address = ["street_address", "city", "zip_code"]
df.drop(drop_address, inplace=True, axis=1)
print(df)