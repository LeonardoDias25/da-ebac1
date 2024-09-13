import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('gasolina.csv')
sns.lineplot(data=df, x='dia', y='venda')
plt.savefig('gasolina.png')
plt.title('Preço médio da gasolina')
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.show()