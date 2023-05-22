from time import sleep
from json import dumps
from kafka import KafkaProducer
import read_data
import constants

data_file = 'output2.txt'
topic_name='data'

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))
data = read_data.read_file(data_file)

message = {}
for i, line in enumerate(data):
    item_line = (i + 1) % constants.BREAK_LINE
    match item_line:
        case constants.MODEL_KEY_LINE:
            message['key'] = line.replace('Model parameters of key=', '').replace(' :\n', '')
        case constants.ACCURACY_LINE:
            message['accuracy'] = line.replace('\n', '')
        case constants.F1_SCORE_LINE:
            message['f1_score'] = line.replace('\n', '')
        case constants.DATE_SCORE_LINE:
            message['date_score'] = line.replace('\n', '')
        case constants.FINAL_SCORE_LINE:
            message['final_score'] = line.replace('\n', '')
        case 0:
            print(message)
            producer.send(topic_name, value=message)
            message = {}