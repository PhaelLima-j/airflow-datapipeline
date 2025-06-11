# Weather Data Pipeline with Apache Airflow

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Airflow](https://img.shields.io/badge/Apache%20Airflow-2.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Um pipeline de dados automatizado que coleta, processa e armazena dados climáticos usando Apache Airflow. O projeto extrai dados meteorológicos da API Visual Crossing Weather de forma semanal e organiza os dados em diferentes formatos CSV para análise.

## 🌟 Funcionalidades

- **Extração Automatizada**: Coleta dados climáticos semanalmente
- **Processamento de Dados**: Separa dados em categorias (temperaturas e condições)
- **Organização Temporal**: Estrutura os dados por semanas
- **Monitoramento**: Interface visual do Airflow para acompanhar execuções
- **Tratamento de Erros**: Logs detalhados e recuperação automática

## 🏗️ Arquitetura

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Visual        │    │   Apache         │    │   File System  │
│   Crossing API  │───▶│   Airflow        │───▶│   (CSV Files)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### Fluxo do Pipeline:

1. **Criação de Diretório**: Cria pasta semanal com timestamp
2. **Extração de Dados**: Faz requisição à API para dados de 7 dias
3. **Processamento**: Separa dados em três arquivos:
   - `dados_brutos.csv`: Dataset completo
   - `temperaturas.csv`: Temperaturas mínima, média e máxima
   - `condicoes.csv`: Descrição e ícones do clima

## 📋 Pré-requisitos

- Python 3.8+
- Apache Airflow 2.0+
- Conta na [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api)

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/weather-data-pipeline.git
cd weather-data-pipeline
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env com sua API key
nano .env
```

### 4. Configure o Airflow

```bash
# Inicialize o banco de dados do Airflow
airflow db init

# Crie um usuário admin
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com
```

### 5. Copie a DAG para o diretório do Airflow

```bash
cp dags/dados_climaticos.py $AIRFLOW_HOME/dags/
```

## ⚙️ Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
API_KEY=sua_chave_da_visual_crossing_api
AIRFLOW_HOME=/caminho/para/airflow
```

### Configuração da DAG

A DAG está configurada para:
- **Execução**: Toda segunda-feira à meia-noite
- **Cidade**: Boston (pode ser alterada no código)
- **Período**: Coleta dados de 7 dias
- **Fuso Horário**: UTC

## 🏃‍♂️ Executando

### 1. Inicie os serviços do Airflow

```bash
# Terminal 1 - Webserver
airflow webserver --port 8080

# Terminal 2 - Scheduler
airflow scheduler
```

### 2. Acesse a interface web

Abra seu navegador em: `http://localhost:8080`

### 3. Ative a DAG

- Encontre a DAG `dados_climaticos`
- Clique no toggle para ativá-la
- Monitore as execuções na interface

## 📂 Estrutura do Projeto

```
weather-data-pipeline/
├── README.md                 # Este arquivo
├── requirements.txt          # Dependências Python
├── .env.example             # Template de variáveis de ambiente
├── .gitignore               # Arquivos ignorados pelo Git
├── dags/
│   └── dados_climaticos.py  # DAG principal do Airflow
├── docs/
│   └── setup.md            # Documentação adicional
└── tests/
    └── test_dag.py         # Testes unitários
```

## 📊 Dados Coletados

### dados_brutos.csv
Dataset completo com todas as métricas disponíveis da API.

### temperaturas.csv
```csv
datetime,tempmin,temp,tempmax
2025-06-04,15.2,22.1,28.9
```

### condicoes.csv
```csv
datetime,description,icon
2025-06-04,Partly cloudy,partly-cloudy-day
```

## 🛠️ Personalização

### Alterar Cidade
```python
# Em dados_climaticos.py, linha ~45
city = 'Boston'  # Altere para sua cidade desejada
```

### Alterar Frequência
```python
# Em dados_climaticos.py, linha ~25
schedule_interval='0 0 * * 1',  # Cron expression
```

### Adicionar Métricas
```python
# Adicione mais colunas na extração
dados[['datetime', 'humidity', 'windspeed']].to_csv(filepath + 'clima_extra.csv')
```

## 🧪 Testes

Execute os testes unitários:

```bash
# Teste da DAG
python -m pytest tests/test_dag.py

# Teste manual da DAG
airflow dags test dados_climaticos 2025-06-04
```

## 📝 Logs

Os logs do Airflow ficam em:
- **Interface Web**: `Admin > Logs`
- **Arquivos**: `$AIRFLOW_HOME/logs/dados_climaticos/`

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📜 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🎯 Próximos Passos

- [ ] Adicionar mais cidades
- [ ] Implementar alertas por email
- [ ] Criar dashboard de visualização
- [ ] Adicionar testes de integração
- [ ] Dockerizar o projeto
- [ ] Implementar armazenamento em banco de dados

## 📞 Contato

Seu Nome - [seu.email@exemplo.com](mailto:seu.email@exemplo.com)

Link do Projeto: [https://github.com/seu-usuario/weather-data-pipeline](https://github.com/seu-usuario/weather-data-pipeline)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!
