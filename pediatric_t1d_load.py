# Step 1️⃣: Load and preview the dataset
import kagglehub
import pandas as pd
from kagglehub import KaggleDatasetAdapter

# 1️⃣ 下载数据集并获取本地路径
path = kagglehub.dataset_download("yudalecture/pediatric-t1d-dataset")

# 2️⃣ 加载 CSV 文件（看目录里具体的文件名）
# 如果里面只有一个文件，可以自动推断
import os
for root, dirs, files in os.walk(path):
    for f in files:
        if f.endswith(".csv"):
            file_path = os.path.join(root, f)
            break

print("✅ Dataset file found at:", file_path)

# 3️⃣ 用 pandas 读取
df = pd.read_csv(file_path)

# 4️⃣ 查看基本信息
#print("\n📊 Shape of dataset:", df.shape)
#print("\n📋 Columns:", df.columns.tolist())
#print("\n🔍 First 5 records:")
#print(df.head())
# Step 2️⃣: 检查数据类型与缺失值
#print("\nData types:")
#print(df.dtypes)

#print("\nMissing values per column:")
#print(df.isnull().sum().sort_values(ascending=False))

import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x='JK', hue='Diagnosa', data=df)
plt.title("Sex vs Diabetes Diagnosis")
plt.savefig("sex_vs_diagnosis.png", dpi=300, bbox_inches='tight')
plt.show()

sns.boxplot(x='Diagnosa', y='HbA1c', data=df)
plt.title("HbA1c levels by Diagnosis")
plt.savefig("hba1c_vs_diagnosis.png", dpi=300, bbox_inches='tight')
plt.show()