import pandas as pd

F_DC = 'data/16_diecasting.csv'

df = pd.read_csv(F_DC)

Q1 = df['사이클타임'].quantile(0.25)
Q3 = df['사이클타임'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

ct_clipped = df['사이클타임'].clip(lower=lower, upper=upper)
print(round(ct_clipped.min(), 2), round(ct_clipped.max(), 2),
      round(ct_clipped.mean(), 2))          # 20.6 58.61 28.28

