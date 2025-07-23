import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('mtcars.csv')
plt.figure(figsize=(8, 5))
plt.hist(df['mpg'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of mpg')
plt.xlabel('mpg')
plt.ylabel('Frequency')
plt.show()