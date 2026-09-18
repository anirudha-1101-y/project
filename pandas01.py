"""
import pandas as pd
data= pd.Series([10,20,30])
print(data)
"""
"""
import pandas as pd
data=[
    ["rahul",20],
    ["ani",24],
    ["dhruv",54]

]
df=pd.DataFrame(data,columns=["name","age"])
print(df)
"""

import pandas as pd 
df= pd.read_csv("student.csv")
print(df)