import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import style 
style.use('ggplot')
# Import numpy to make an array of data at bottom
import numpy as np 


# Lets say you have a website and these are the analytics for the website
# These r dictionaries
web_stats = {'Day': [1,2,3,4,5,6,],
			'Visitors':[43, 53, 34, 45, 64, 34],
			'Bounce_Rate': [65, 72, 62, 64, 54, 66]}

df = pd.DataFrame(web_stats)
# To virtually see the data plotted, pandas allows by pringting out the variable that you 
# created called "df". This does something as excel but better bc python can hold more data 
# work faster than excel.
# The column on the far left is the index
#print(df)

# You can reference a specific section like the 1st 5 rows by referencing df.head
#print(df.head())

# To call the last 5 rows 
#print(df.tail())

# To print the last 2 columns
#print(df.tail(2))


# Lets set an index
#print(df.set_index('Day'))

#print(df.head())

# Here's another way 
#df.set_index('Day', inplace=true)
#print(df.head())

# TO reference a specific column
#print(df['Visitors'])
#print(df.Visitors)

# To reference a list of columns
#print(df[['Bounce_Rate', 'Visitors']])

 # To Convert these to a list 
print(df.Visitors.tolist())

print(np.array(df[['Bounce_Rate','Visitors']]))
