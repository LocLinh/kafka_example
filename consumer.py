from kafka import KafkaConsumer
import json
import sql_db

consumer = KafkaConsumer('data', bootstrap_servers='localhost:9092')
connection = sql_db.init_db()
i = 0
batch_size = 1000
batch_data = []

while True:
    messages = consumer.poll(timeout_ms=20_000)
    i += 1
    if messages:
        for message in messages.values():
            for item in message:
                msg = json.loads(item.value.decode('ascii'))
                batch_data.append((msg['key'],
                                   float(msg['accuracy'][:8]) if msg['accuracy'] != 'nan' else 0.0, 
                                   float(msg['f1_score'][:8]) if msg['f1_score'] != 'nan' else 0.0, 
                                   float(msg['date_score'][:8]) if msg['date_score'] != 'nan' else 0.0,
                                   float(msg['final_score'][:8]) if msg['final_score'] != 'nan' else 0.0))
                if i > batch_size:
                    with connection.cursor() as cursor:
                        cursor.fast_executemany = True
                        sql = 'insert into model_evaluate values (?, ?, ?, ?, ?)'
                        cursor.executemany(sql, batch_data)
                    
                    print(f"done insert {i} records")
                    i = 0
                    batch_data = []
    else:
        with connection.cursor() as cursor:
            cursor.fast_executemany = True
            sql = 'insert into model_evaluate values (?, ?, ?, ?, ?)'
            cursor.executemany(sql, batch_data)
        
        print(f"done insert {i} records")
        i = 0
        batch_data = []
        print("done everything")
        connection.close()
        break