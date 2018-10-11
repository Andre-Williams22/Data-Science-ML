# This deals with housing prices the 77006 zip code
import pandas as pd
# Download the csv from a website and then copy it into the downloads folder and copy the name of csv in.
df = pd.read_csv('ZILLOW-Z77006_ZRIFAH.csv')
# This should give you a data set
print(df.head())
# This creates a new csv file
df.set_index('Date', inplace=True)
df.to_csv('newcsv2.csv')
 # This new one specifies date as the index
# df = pd.read_csv('newcsv2.csv', index_col=0)
# print(df.head())
# Rename columns based off of location if you have different data sets
# df.columns = ['Austin_HPI']
# print(df.head)

df.to_csv('newcsv3.csv')
df.to_csv('newcsv4.csv', header=False)

df = pd.read_csv('newcsv4.csv', names=['Date', 'Austin_HPI'], index_col=0)
print(df.head())

# To convert data from csv to html 
# df.to_html('example.html')

df = pd.read_csv('newcsv4.csv', names=['Date', 'Austin_HPI'])
print(df.head())
# to rename a single column
df.rename(columns={'Austin_HPI': '77006_HPI'}, inplace=True)

print(df.head())