import pandas as pd
import numpy as np

# data = pd.Series([0, 2, 3, 4, 566, 99])
# data.index = ["first", "second", "third", "forth", "fifth", "sixth"]

# data = pd.Series({"s01": "sun", "s02": "han"})

# data = pd.Series([0.2] * 10)
# data = pd.Series(0.2, index=range(10))

# 访问数据
# data = pd.Series([10, 9, 8, 7, 5], index=["5", "4", "3", "2", "1"])
# print(data.values)
# print(data.index)

# 日期转换
# dates = pd.Series(["2024-5-22", "2024-02-11", "2024-02-22", "2024-02-21", "2024-12-21"])
# dates = pd.to_datetime(dates, errors="coerce")
# dates = dates - pd.to_datetime("2020-1-1")
# print(dates)

# 日期生成
# date_list = pd.date_range("2023/1/1", periods=12, freq="M")  # B 为工作日
# print(date_list)

# dataframe
# data = [["Tom", 18], ["Jerry", 22], ["Jack", 21], ["Rose", 16]]
# data_df = pd.DataFrame(data, index=["s1", "s2", "s3", "s4"])
# print(data_df)
# 常用构建dataframe方法
# data = {"name": pd.Series(["sun", "han", "yi", "yue"]), "age": pd.Series([32, 33, 2]), }
# data = pd.DataFrame(data)
# print(data)

# 接口测试
# data = pd.DataFrame({
#     "one": pd.Series([1, 2, 3], index=["a", "b", "c"]),
#     "two": pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"]),
#     "three": pd.Series([1, 3, 4], index=["a", "c", "d"]),
# })
#
# print(data.iloc[:, :-1])

# 列的添加

# data = np.floor(np.random.normal(85, 3, (6, 3)))
# 85：期望值  3：标准差  （6，3）：6行3列
# print(data)

# 处理普通文本  read_csv()
# dtype_info = {
#     "names": ["total", "variable_1", "variable_2", "variable_3", "variable_4", "Y", ],
#     "formats": ["int64", "int64", "int64", "int64", "int64", "int64"]
# }
#
# names = ["total", "variable_1", "variable_2", "variable_3", "variable_4", "Y"]
# data = pd.read_csv("./train_set.csv", header=None, names=names)
# print(data)

# 输出到csv
# data.to_csv("./to.csv")

# 读取excle
# data = pd.read_excel("./test.xlsx")
# print(data)

# 读取json
# data = pd.read_json("./movie_ratings.json")
# data = np.nan_to_num(np.array(data.loc[:, "张三"]))
# print(data)
# weights = [1, 1, 10, 10, 10, 10, 10]
# result = np.average(data, weights=weights)
# print(result)

# 标准差
data = pd.read_json("./movie_ratings.json")
print(data.std())
