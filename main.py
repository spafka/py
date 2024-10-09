import pandas as pd

df = pd.read_excel('./入学测试题_10.xlsx', sheet_name=1)



for index, row in df.iterrows():
    # 在这里处理每一行的数据
    print("第" + str(index) + "行", row['name'], row['age'])
