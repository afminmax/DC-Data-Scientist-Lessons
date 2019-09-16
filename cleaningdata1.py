import pandas as pd

df = pd.read_csv('airquality.csv')
df.head()

# MELTING PRACTICE! - Turning columns into rows.

# value_vars are columns we want to convert to rows.
# id_vars are columns we dont' want to convert to rows.
airquality_melt = pd.melt(frame=df, id_vars=['Month', 'Day'])
airquality_melt.head()

## This time make meaningful column names:
airquality_melt = pd.melt(frame=df, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')
airquality_melt.head()

## PIVOTING PRACTICE! - Turining rows into columns.
# the index parameter - the columns you don't want pivoted.
# the columns parameter - the columns you want to pivot.
# the values parameter - the values to be used when the column is pivoted.

airquality_pivot = airquality_melt.pivot_table(index=['Month','Day'],
 columns='measurement',values='reading')

airquality_pivot.head()
# slight problem with indexing on the pivot....

# we need to reset the index
# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot_reset
airquality_pivot_reset = airquality_pivot.reset_index()
print(airquality_pivot_reset.head())

## MAKING COLUMNS LOOK RIGHT
tb = pd.read_csv('tb.csv')
tb.info()
tb.head()
# the goal is to turn column 'm014' into a gender column 'm'

tb_melt = pd.melt(frame=tb, id_vars=['country','year'])
tb_melt['gender'] = tb_melt.variable.str[0]
tb_melt.info()
tb_melt['age_group']=tb_melt.variable.str[1:]
tb_melt.info()
tb_melt.head()


## SPLITTING COLUMNS
# the goal is to split the columns with underscores
# Melt ebola: ebola_melt
ebola_melt = pd.melt(frame=ebola, id_vars=['Date','Day'],var_name='type_country', value_name='counts')

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

# Create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())