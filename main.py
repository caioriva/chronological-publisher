from flask import Flask
from google.cloud import pubsub

import datetime

project='chronological-publisher'
topic='hour-messages'

app = Flask(__name__)

@app.route('/publish', methods=['GET'])
def publish():
    publisher = pubsub.PublisherClient()
    
    topic_path = publisher.topic_path(project, topic)
    message = getPath()

    publisher.publish(topic_path, data=message.encode('utf-8'))

    return '{project} - {topic} - {message}'.format(project=project, topic=topic, message=message)


def getPath():
    now = datetime.datetime.now()
    
    return '/{year}/{month}/{day}/{hour}/'.format(year=now.year, month=now.month, day=now.day, hour=now.hour)