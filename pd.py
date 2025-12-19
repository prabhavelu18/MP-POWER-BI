import pandas as pd
df = pd.read_csv("C:\\Users\\venma\\OneDrive\\Tài liệu\\desktop\\NewCompanyDetails.csv")
df = df.drop_duplicates()
df = df.dropna()
df['revenue'] = df['revenue'].replace(r'[^0-9]', '',regex=True).astype(int)
df.to_csv("muthuprabha.csv",index=False)
print("dd")
print("df")
