import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv')
# gasolina_df.head() 
with sns.axes_style('whitegrid'):
  grafico_gasolina = sns.lineplot(data=gasolina_df, x='dia', y='venda')
  grafico_gasolina.set(title='Preço médio da gasolina em SP em Julho de 2021',
  xlabel='Dias',
  ylabel='Preço médio (R$)')

grafico = grafico_gasolina.get_figure()
grafico.savefig('gasolina.png')