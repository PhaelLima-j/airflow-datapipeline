# Weather Data Pipeline with Apache Airflow

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Airflow](https://img.shields.io/badge/Apache%20Airflow-2.0+-red.svg)

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

