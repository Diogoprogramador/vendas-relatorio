import pandas as pd
import matplotlib.pyplot as plt
import os

# Caminho da pasta onde estão os arquivos CSV
pasta_vendas = 'vendas/'

# Lista de estados (cidades) de interesse
estados = ['Belo Horizonte', 'Curitiba', 'Fortaleza', 'Goiás', 'Porto Alegre', 'Recife', 'Rio de Janeiro', 'Salvador', 'São Paulo']

# Lista para armazenar os DataFrames de cada arquivo CSV
lista_df_vendas = []
lista_df_devolucoes = []

# Iterar sobre todos os arquivos CSV na pasta
for arquivo in os.listdir(pasta_vendas):
    if arquivo.endswith('.csv'):
        caminho_arquivo = os.path.join(pasta_vendas, arquivo)

        # Verificar se o arquivo é de vendas ou devoluções
        if 'Vendas' in arquivo:
            # Carregar o CSV de vendas
            df_vendas = pd.read_csv(caminho_arquivo)

            # Adicionar a coluna 'Estado' com base no nome do arquivo
            estado = arquivo.split(' - ')[1].replace('.csv', '')  # Extrai a cidade do nome do arquivo
            if estado in estados:
                df_vendas['Estado'] = estado

                # Calcular o valor das vendas
                df_vendas['Valor_Venda'] = df_vendas['Quantidade Vendida'] * df_vendas['Preco Unitario']
                lista_df_vendas.append(df_vendas)

        elif 'Devolucoes' in arquivo:
            # Carregar o CSV de devoluções
            df_devolucoes = pd.read_csv(caminho_arquivo)

            # Adicionar a coluna 'Estado' com base no nome do arquivo
            estado = arquivo.split(' - ')[1].replace('.csv', '')  # Extrai a cidade do nome do arquivo
            if estado in estados:
                df_devolucoes['Estado'] = estado

                # Calcular o valor das devoluções
                df_devolucoes['Valor_Devolucao'] = df_devolucoes['Quantidade Devolvida'] * df_devolucoes['Preço Unitário']
                lista_df_devolucoes.append(df_devolucoes)

# Concatenar todos os DataFrames de vendas e devoluções em dois únicos DataFrames
df_vendas_unificado = pd.concat(lista_df_vendas, ignore_index=True)
df_devolucoes_unificado = pd.concat(lista_df_devolucoes, ignore_index=True)

# Agrupar os dados de vendas por estado
df_vendas_estado = df_vendas_unificado.groupby('Estado').agg({'Valor_Venda': 'sum'}).reset_index()

# Agrupar os dados de devoluções por estado
df_devolucoes_estado = df_devolucoes_unificado.groupby('Estado').agg({'Valor_Devolucao': 'sum'}).reset_index()

# Agrupar os dados de vendas e devoluções juntos
df_estado_completo = pd.merge(df_vendas_estado, df_devolucoes_estado, on='Estado', how='outer')

# Ordenar os DataFrames por valor de venda (decrescente)
df_estado_completo = df_estado_completo.sort_values(by='Valor_Venda', ascending=False)

# Exibir totais agregados
total_vendas = df_vendas_unificado['Valor_Venda'].sum()
total_devolucoes = df_devolucoes_unificado['Valor_Devolucao'].sum()

# Calcular as porcentagens de vendas e devoluções
df_estado_completo['Porcentagem_Venda'] = (df_estado_completo['Valor_Venda'] / total_vendas) * 100
df_estado_completo['Porcentagem_Devolucao'] = (df_estado_completo['Valor_Devolucao'] / total_devolucoes) * 100

# 1) Gráfico de Vendas e Devoluções Totais (Valores Absolutos)
plt.figure(figsize=(8, 6))
plt.bar(['Vendas Totais', 'Devoluções Totais'], [total_vendas, total_devolucoes], color=['#0c1063', '#d263cb'])

# Adicionar os valores sobre as barras
for bar in plt.gca().patches:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01 * total_vendas,
             f'R$ {int(bar.get_height()):,}', ha='center', va='bottom', fontsize=10)

plt.xlabel('Categorias')
plt.ylabel('Valores (R$)')
plt.title('Totais de Vendas e Devoluções (Todos os Estados)')
plt.tight_layout()
plt.show()

# 2) Gráfico de Vendas e Devoluções por Estado - Valores Absolutos (Vertical)
bar_width = 0.35
index = range(len(df_estado_completo))

plt.figure(figsize=(12, 6))
bars_vendas = plt.bar(index, df_estado_completo['Valor_Venda'], bar_width, color='#0c1063', label='Vendas')
bars_devolucoes = plt.bar([i + bar_width for i in index], df_estado_completo['Valor_Devolucao'], bar_width, color='#d263cb', label='Devoluções')

# Adicionar valores sobre as barras
for i, bar in enumerate(bars_vendas):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01 * total_vendas,
             f'R$ {int(df_estado_completo["Valor_Venda"][i]):,}', ha='center', va='bottom', fontsize=10)

for i, bar in enumerate(bars_devolucoes):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01 * total_devolucoes,
             f'R$ {int(df_estado_completo["Valor_Devolucao"][i]):,}', ha='center', va='bottom', fontsize=10)

plt.xlabel('Estado')
plt.ylabel('Valores (R$)')
plt.title('Vendas e Devoluções por Estado (Valores Absolutos)')
plt.xticks([i + bar_width / 2 for i in index], df_estado_completo['Estado'], rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

# 3) Gráfico de Vendas e Devoluções por Estado - Porcentagens (Vertical)
plt.figure(figsize=(12, 6))
bars_vendas_percent = plt.bar(index, df_estado_completo['Porcentagem_Venda'], bar_width, color='#0c1063', label='Vendas (%)')
bars_devolucoes_percent = plt.bar([i + bar_width for i in index], df_estado_completo['Porcentagem_Devolucao'], bar_width, color='#d263cb', label='Devoluções (%)')

# Adicionar valores sobre as barras
for i, bar in enumerate(bars_vendas_percent):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             f'{df_estado_completo["Porcentagem_Venda"][i]:.1f}%', ha='center', va='bottom', fontsize=10)

for i, bar in enumerate(bars_devolucoes_percent):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             f'{df_estado_completo["Porcentagem_Devolucao"][i]:.1f}%', ha='center', va='bottom', fontsize=10)

plt.xlabel('Estado')
plt.ylabel('Porcentagem (%)')
plt.title('Porcentagens de Vendas e Devoluções por Estado (Vertical)')
plt.xticks([i + bar_width / 2 for i in index], df_estado_completo['Estado'], rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

# 4) Gráfico de Vendas e Devoluções por Estado - Valores Absolutos (Horizontal)
plt.figure(figsize=(12, 6))
bars_vendas_horizontal = plt.barh(index, df_estado_completo['Valor_Venda'], bar_width, color='#0c1063', label='Vendas')
bars_devolucoes_horizontal = plt.barh([i + bar_width for i in index], df_estado_completo['Valor_Devolucao'], bar_width, color='#d263cb', label='Devoluções')

# Adicionar valores sobre as barras
for i, bar in enumerate(bars_vendas_horizontal):
    plt.text(bar.get_width() + 0.01 * total_vendas, bar.get_y() + bar.get_height() / 2,
             f'R$ {int(df_estado_completo["Valor_Venda"][i]):,}', va='center', fontsize=10)

for i, bar in enumerate(bars_devolucoes_horizontal):
    plt.text(bar.get_width() + 0.01 * total_devolucoes, bar.get_y() + bar.get_height() / 2,
             f'R$ {int(df_estado_completo["Valor_Devolucao"][i]):,}', va='center', fontsize=10)

plt.ylabel('Estado')
plt.xlabel('Valores (R$)')
plt.title('Vendas e Devoluções por Estado (Valores Absolutos - Horizontal)')
plt.yticks([i + bar_width / 2 for i in index], df_estado_completo['Estado'])
plt.legend()
plt.tight_layout()
plt.show()

# 5) Gráfico de Vendas e Devoluções por Estado - Porcentagens (Horizontal)
plt.figure(figsize=(12, 6))
bars_vendas_percent_horizontal = plt.barh(index, df_estado_completo['Porcentagem_Venda'], bar_width, color='#0c1063', label='Vendas (%)')
bars_devolucoes_percent_horizontal = plt.barh([i + bar_width for i in index], df_estado_completo['Porcentagem_Devolucao'], bar_width, color='#d263cb', label='Devoluções (%)')

# Adicionar valores sobre as barras
for i, bar in enumerate(bars_vendas_percent_horizontal):
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
             f'{df_estado_completo["Porcentagem_Venda"][i]:.1f}%', va='center', fontsize=10)

for i, bar in enumerate(bars_devolucoes_percent_horizontal):
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
             f'{df_estado_completo["Porcentagem_Devolucao"][i]:.1f}%', va='center', fontsize=10)

plt.ylabel('Estado')
plt.xlabel('Porcentagem (%)')
plt.title('Porcentagens de Vendas e Devoluções por Estado (Horizontal)')
plt.yticks([i + bar_width / 2 for i in index], df_estado_completo['Estado'])
plt.legend()
plt.tight_layout()
plt.show()
