import pandas as pd
import numpy as np
df= pd.read_csv("data/Untitled Folder/monthly_expenses_250.csv")
df.head()
df.info()
df.describe()
df.isnull().sum()
%matplotlib inline
import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Automatically find the exact path of the CSV file in JupyterLite
target_file = 'monthly_expenses_250.csv'
found_path = None

for root, dirs, files in os.walk('.'):
    if target_file in files:
        found_path = os.path.join(root, target_file)
        break

if not found_path:
    print("Available files in current directory:", os.listdir('.'))
    raise FileNotFoundError(f"Could not find {target_file}. Check the list printed above!")

print(f"Loading file from: {found_path}")

# 2. Read CSV safely across encodings (handles ₹ or ? symbols)
try:
    df = pd.read_csv(found_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(found_path, encoding='latin1')

# 3. Strip all non-numeric characters (₹, ?, commas, spaces) and convert to int
df['Monthly Expense'] = (
    df['Monthly Expense']
    .astype(str)
    .str.replace(r'[^\d]', '', regex=True)
    .astype(int)
)

# 4. Plot the histogram
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df['Monthly Expense'], bins=20, color='steelblue', edgecolor='black')
ax.set_title('Distribution of Monthly Expenses')
ax.set_xlabel('Monthly Expense')
ax.set_ylabel('Number of People')
plt.show()
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load your dataset (make sure the CSV is in the same folder as your notebook)
df = pd.read_csv('your_file.csv')

# 2. Set clean visual styling with a white background
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6), facecolor='white')

# 3. Calculate average monthly expense per job and sort highest to lowest
avg_expense = df.groupby('Job')['Monthly Expense'].mean().sort_values(ascending=False)

# 4. Create a horizontal bar chart
sns.barplot(x=avg_expense.values, y=avg_expense.index, palette='viridis')

plt.title('Average Monthly Expense by Job Role', fontsize=14, fontweight='bold')
plt.xlabel('Average Monthly Expense (₹)', fontsize=12)
plt.ylabel('Job Role', fontsize=12)
plt.tight_layout()

# 5. Force VS Code to render the graph
plt.show()