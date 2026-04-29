import pandas as pd

# 方式一：从字典创建 DataFrame
data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 22, 28, 24],
    '城市': ['北京', '上海', '北京', '广州'],
    '分数': [88, 92, 85, 95]
}
df = pd.DataFrame(data)
# 多条件过滤（分数>90 且 在北京）用 & 表示“且”，| 表示“或”
mask = (df['分数'] > 90) & (df['城市'] == '北京')
result = df[mask]
print(result)

# 计算平均分
mean_score = df['分数'].mean()
print("平均分:", mean_score)
# 按城市分组，计算每个城市的平均分
city_avg = df.groupby('城市')['分数'].mean()
print("各城市平均分:\n", city_avg)
