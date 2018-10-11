# We want to find the house index prices for all 50 states. 
# Here we're starting with Alaska

import quandl
import pandas as pd 

df = quandl.get("FMAC/HPI_AK", authtoken="zonZF9csdsgtmNbgxFGw=api_key")
#api_key = "zonZF9csdsgtmNbgxFGw"
# api_key = open("zonZF9csdsgtmNbgxFGw",'r').read()

#df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
#print(df.head())

fifty_states = pd.read_html('https://www.infoplease.com/state-abbreviations-and-state-postal-codes')

# This is a list:
#print(fifty_states[0])
# This is a dataframe:
#print(fifty_states[0])
# This is a column:
print(fifty_states[0][0])

for abbv in fifty_states[0][0][1:]:
	print("FMAC/HPI_"+str(abbv))