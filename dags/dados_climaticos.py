from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.macros import ds_add
import os
from os.path import join
import pandas as pd
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configuração padrão da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': pendulum.datetime(2025, 6, 4, tz="UTC"),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    "dados_climaticos",
    default_args=default_args,
    description='Pipeline de dados climáticos',
    schedule_interval='0 0 * * 3',  # Toda quarta-feira à meia-noite
    catchup=False,  # Evita execuções retroativas
    tags=['clima', 'dados'],
) as dag:
    
    # Tarefa 1: Criar pasta
    tarefa_1 = BashOperator(
        task_id='cria_pasta',
        bash_command='mkdir -p "/home/rapha_dtengineer/Documents/datapipeline/semana={{data_interval_end.strftime(\'%Y-%m-%d\')}}"'
    )
   
    def extrai_dados(data_interval_end, **context):
        """
        Extrai dados climáticos da API Visual Crossing
        """
        try:
            city = 'Boston'
            key = os.getenv("API_KEY")
            
            if not key:
                raise ValueError("API_KEY não encontrada nas variáveis de ambiente")
            
            # 7 dias após data_interval_end
            data_fim = ds_add(data_interval_end, 7)
            
            # URL da API
            URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{data_interval_end}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv'
            
            print(f"Fazendo requisição para: {URL}")
            
            # Ler dados da API
            dados = pd.read_csv(URL)
            
            # Definir caminho do arquivo
            filepath = f'/home/rapha_dtengineer/Documents/datapipeline/semana={data_interval_end}/'
            
            # Verificar se o diretório existe
            os.makedirs(filepath, exist_ok=True)
            
            # Salvar arquivos CSV
            dados.to_csv(filepath + 'dados_brutos.csv', index=False)
            dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(filepath + 'temperaturas.csv', index=False)
            dados[['datetime', 'description', 'icon']].to_csv(filepath + 'condicoes.csv', index=False)
            
            print(f"Dados salvos em: {filepath}")
            return f"Sucesso: {len(dados)} registros processados"
            
        except Exception as e:
            print(f"Erro na extração de dados: {str(e)}")
            raise
    
    # Tarefa 2: Extrair dados
    tarefa_2 = PythonOperator(
        task_id='extrai_dados',
        python_callable=extrai_dados,
        op_kwargs={'data_interval_end': '{{data_interval_end.strftime(\'%Y-%m-%d\')}}'},
        provide_context=True
    )
    
    # Definir dependências
    tarefa_1 >> tarefa_2