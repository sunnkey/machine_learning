import numpy as np


def open_csv(file_path, dtype_info):
    data = []
    try:
        with open(file_path, "r") as f:
            for line in f.readlines():
                data.append(tuple(line[:-1].split(",")))
    except FileNotFoundError:
        print(FileNotFoundError)
    finally:
        print("This block always runs, whether an exception occurred or not.")

    data = np.array(data, dtype=dtype_info)
    return data


dtype_info = {
    "names": ["cate", "3.1", "3.2", "3.3", "3.6", "y"],
    "formats": ['int64', 'int64', 'int64', 'int64', 'int64', 'int64']
}

np_data = open_csv("./train_set.csv", dtype_info)
print(np_data)
