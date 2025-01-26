import requests
import json
from datetime import datetime
from kafka import KafkaProducer
from airflow import DAG
from airflow.operators.python import PythonOperator

def get_data():
    res = requests.get('https://randomuser.me/api/')
    return res.json()['results'][0]

def format_data(res):
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{(location['street']['number'])} {location['street']['name']} {location['city']}, {location['state']}, {location['country']}"
    data['postcode'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']
    return data

def stream_data():
    try:
        res = get_data()
        formatted_res = format_data(res)
        producer = KafkaProducer(
            bootstrap_servers=['broker:29092'],
            max_block_ms=5000,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')  
        )
        producer.send('user_created', formatted_res)
        producer.flush()  
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


default_args = {
    'owner': 'prototype',
    'start_date': datetime(2023, 9, 3, 10, 00)
}

with DAG('user_automation',
         default_args=default_args,
         schedule='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_API',
        python_callable=stream_data
    )

streaming_task
