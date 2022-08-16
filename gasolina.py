import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv')
# gasolina_df.head() 
with sns.axes_style('whitegrid'):
  grafico_gasolina = sns.lineplot(data=gasolina_df, x='dia', y='venda', palette='pastel')
  grafico_gasolina.set(title='Preço médio da gasolina no mês de Julho de 2021 em SP',
  xlabel='Dias',
  ylabel='Preço médio (R$)')

grafico = grafico_gasolina.get_figure()
grafico.savefig('gasolina.png')