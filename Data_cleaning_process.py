import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Step 1: Load dataset
df = pd.read_csv("water_potability.csv")   # file must be in your working directory

# Step 2: Preview dataset
print("Original Dataset Preview:")
print(df.head())
print("\nShape before cleaning:", df.shape)
print("\nMissing values before cleaning:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Step 3: Remove duplicate rows
df = df.drop_duplicates()

# Step 4: Remove constant columns (no variance)
for col in df.columns:
    if df[col].nunique() == 1:
        df = df.drop(columns=[col])
        print(f"Removed constant column: {col}")

# Step 5: Drop columns with too many missing values (>40%)
threshold = 0.4
df = df.dropna(axis=1, thresh=int((1-threshold) * len(df)))

# Step 6: Remove highly correlated features (redundant info)
corr_matrix = df.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]
if to_drop:
    print(f"Removed highly correlated columns: {to_drop}")
    df = df.drop(columns=to_drop)

# Step 7: Separate features (X) and target (y)
X = df.drop("Potability", axis=1)
y = df["Potability"]

# Step 8: Handle missing values with median imputation
imputer = SimpleImputer(strategy="median")
X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# Step 9: Scale numerical features
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X_imputed), columns=X_imputed.columns)

# Step 10: Recombine with target variable
df_cleaned = pd.concat([X_scaled, y.reset_index(drop=True)], axis=1)

# Step 11: Save cleaned dataset
df_cleaned.to_csv("water_potability_cleaned.csv", index=False)
# Step 12: Show summary after cleaning
print("\n✅ Cleaning Complete!")
print("Shape after cleaning:", df_cleaned.shape)
print("Remaining columns:", df_cleaned.columns.tolist())
print("\nPreview of cleaned dataset:")
print(df_cleaned.head())
print("Missing values after cleaning:\n", df_cleaned.isnull().sum())
print("Duplicate rows after cleaning:", df_cleaned.duplicated().sum())
print(df_cleaned.describe().T)
print("Columns after cleaning:", df_cleaned.columns.tolist())
print("Shape after cleaning:", df_cleaned.shape)
print(df_cleaned.head())
# Check for missing values
print("Missing values:\n", df_cleaned.isnull().sum())

# Check for duplicates
print("Duplicates:", df_cleaned.duplicated().sum())

# Compare a column before and after scaling
print("\nBefore scaling (first 5 values of 'ph'):\n", df['ph'].head())
print("\nAfter scaling (first 5 values of 'ph'):\n", df_cleaned['ph'].head())

# Summary stats after scaling
print("\nSummary stats after scaling:\n", df_cleaned.describe().T)
df_cleaned.head()
