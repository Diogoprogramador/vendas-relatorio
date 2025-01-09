# Análise de Vendas e Devoluções por Estado

Este repositório contém um script Python que realiza a análise de dados de vendas e devoluções a partir de arquivos CSV. O código processa os dados, calcula valores e gera gráficos que mostram as vendas e devoluções totais, bem como por estado (cidade), tanto em valores absolutos quanto em porcentagens.

## Descrição

O script faz o seguinte:

1. **Carrega os arquivos CSV** com informações de vendas e devoluções de diferentes estados.
2. **Processa e calcula os valores** de vendas e devoluções com base nas colunas de quantidade e preço unitário.
3. **Agrupa os dados** por estado e calcula os totais de vendas e devoluções para cada um.
4. **Gera gráficos** usando a biblioteca `matplotlib`, para visualizar:
   - Totais de vendas e devoluções.
   - Vendas e devoluções por estado, tanto em valores absolutos quanto em porcentagens.
5. **Exibe os resultados** de maneira visual através de gráficos para facilitar a análise comparativa entre estados.

## Requisitos

Antes de executar o script, você precisará garantir que tem as seguintes bibliotecas instaladas:

- `pandas`: Para manipulação de dados.
- `matplotlib`: Para criação dos gráficos.
- `os`: Para manipulação de arquivos.

Para instalar essas dependências, você pode usar o `pip`:

```bash
pip install pandas matplotlib
Estrutura do Repositório
bash
Copiar código
├── vendas/               # Pasta contendo os arquivos CSV de vendas e devoluções
│   ├── Vendas - Belo Horizonte.csv
│   ├── Vendas - Curitiba.csv
│   ├── Devolucoes - Belo Horizonte.csv
│   ├── Devolucoes - Curitiba.csv
│   └── ...               # Outros arquivos CSV de vendas e devoluções
├── main.py               # Script Python que processa os dados e gera os gráficos
├── README.md             # Este arquivo
Como Executar
Prepare seus arquivos CSV: Coloque os arquivos de vendas e devoluções na pasta vendas/ com o seguinte formato de nome:

Arquivos de vendas: Vendas - [Estado].csv
Arquivos de devoluções: Devolucoes - [Estado].csv
Execute o script Python:

No terminal, execute o script Python da seguinte maneira:

bash
Copiar código
python main.py
Ver os resultados: O script gerará gráficos mostrando as vendas e devoluções por estado, tanto em valores absolutos quanto em porcentagens.

Personalização
A lista de estados de interesse está definida no código. Se você quiser adicionar ou remover estados, basta editar a variável estados no código.
Se necessário, ajuste o caminho da pasta onde os arquivos CSV estão localizados, alterando a variável pasta_vendas no código.
Contribuições
Se você deseja contribuir para este projeto, sinta-se à vontade para abrir uma pull request. Antes de contribuir, por favor, leia o código e garanta que as modificações sejam compatíveis com o estilo e a estrutura do projeto.
