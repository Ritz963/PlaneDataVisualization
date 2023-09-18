import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Airplane_Strikes_Dataset.csv')

column_to_analyze = df['Engine Type']

letter_counts = column_to_analyze.str.lower().str.replace(r'[^a-z]', '', regex=True).value_counts()

plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
letter_counts.plot(kind='bar')
plt.title('Engine Type Strike Frequency')
plt.xlabel('Engine Type')
plt.ylabel('Frequency')
plt.show()


plt.show()

# data = (3, 6, 9, 12)

# fig, simple_chart = plt.subplots()

# simple_chart.plot(data)

# plt.show()