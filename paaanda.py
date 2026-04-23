import pandas as pd
# mydata ={
#     'cars':["BMW","AUDI","TOYOTA"],
#     'passings':[3,7,2]
# }
# df=pd.DataFrame(mydata)
# print(df)

# data={
#     "calories":[420,380,390],
#     "duration":[50,40,45]   
# }
# df=pd.DataFrame(data)
# print(df)   
# print(df.loc[2])
# print(df.loc[1])
x={1:"one",2:"two",3:"three"}
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Harikirshnan', 'Sappzy', 'Niranjan', 'Vishnu', 'Sreehari']
scores = [85, 92, 78, 90, 88, 95, 80, 82, 91, 89]
df=pd.DataFrame({'students':students,'scores':scores})
print(df.loc[[0,7]])