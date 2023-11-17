df = pd.merge(roster, df13, on='Name', how='left')
df = pd.merge(df, df14, on='Name', how='left')
df = pd.merge(df, df15, on='Name', how='left')
df = pd.merge(df, df17, on='Name', how='left')
df.fillna(0,inplace=True)
df['Total'] = df.iloc[:,1:].sum(axis=1)
df
