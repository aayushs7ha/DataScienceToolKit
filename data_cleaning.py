def dataframe_cleaner(df):
    df = df.loc[:,df.columns != 'Unnamed: 0' ]
    df = df[df.gpslatitude != 0.0]
    df = df.query("ignitionOn == False")
    df.reset_index(drop=True,inplace=True)
    return df

 df = dataframe_cleaner(dataframe)

# removing unnamed columns

df = dataframe.loc[:,dataframe.columns != 'Unnamed: 0' ]

# accessing dictionary from a list 

final_state_dict = dict((key,d[key]) for d in final_state for key in d)
