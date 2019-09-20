import pandas as pd

tipsdf = pd.read_csv('tips.csv')

tipsdf.info()

bill_mean = tipsdf.total_bill.mean()
bill_mean 

# Create the new DataFrame: tracks
tracks = billboard[['year', 'artist', 'track', 'time']]

# Print info of tracks
print(tracks.info())

# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()

# Print info of tracks
print(tracks_no_duplicates.info())


#### USING ASSERT TO TEST VALUES

# Assert that there are no missing values
assert pd.notnull(ebola).all().all()

# Assert that all values are >= 0
assert (ebola >= 0).all().all()
