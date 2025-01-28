import os
import pandas as pd

os.chdir("../test_data")
data_dir = os.getcwd()
# print(data_dir)

columns = ["lang", "art_name", "entity", "start", "end", "class1", "classes2"]
new_data = list()
for dr in os.listdir():
    print(dr)
    os.chdir(dr)
    file_path = str(os.getcwd()) + "/subtask-1-entity-mentions.txt"
    print(file_path)
    with open(file_path, "r") as file:
        content = file.read()
    rows = content.split("\n")
    for r in rows:
        a = r.split("\t")
        # print(a)
        if a != [""]:
            d = dict()
            d["lang"] = str(dr)
            d["art_name"] = a[0]
            d["entity"] = a[1]
            d["start"] = a[2]
            d["end"] = a[3]
            # d["class1"] = a[4]
            # d["classes2"] = [i for i in a[5:]]
            file_path2 = str(os.getcwd()) + "/subtask-1-documents/" + a[0]
            with open(file_path2, "r") as file2:
                content2 = file2.read()
            d["text"] = content2
            # print(d)
            new_data.append(d)
    os.chdir("..")
df = pd.DataFrame(new_data)
print(df.head())
# os.chdir("..")
os.chdir("../merged_data")
df.to_parquet("subtask1_submisson.parquet", index=False)
