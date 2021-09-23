import pandas as pd
dataframe1 = pd.read_csv("sample_submission.txt")
dataframe1.to_csv('sample_submission.csv',index = None)
