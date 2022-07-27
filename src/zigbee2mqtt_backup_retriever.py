import paho.mqtt.client as mqtt
import base64
import logging
import json
import time
from datetime import datetime
import os

logger = logging.getLogger("MQTT Retriever")
logging.basicConfig(level=logging.INFO)
retrieval_end = False

def on_message(client: mqtt.Client, userdata, msg):
    global retrieval_end
    zip_path = os.getenv('ZIP_PATH', os.getcwd())
    filename_template = os.getenv('FILENAME_TEMPLATE', "zigbee2mqtt_backup")
    filename = f"{filename_template}_{datetime.now().strftime('%Y%m%d%H%M')}.zip"
    filepath = os.path.join(zip_path, filename)
    decoded_message = str(msg.payload.decode("utf-8"))
    msg = json.loads(decoded_message)
    if msg["status"].lower() == "ok":
        logger.info("Message retrieval successful.")
        decoded = base64.b64decode(msg["data"]["zip"])
        with open(filepath, 'wb') as fout:
            fout.write(decoded)
        logger.info("Base64 string decoded and stored as zip at: %s", filepath)
        retrieval_end = True
    else:
        logger.error("An error occured.")
        retrieval_end = True


client = mqtt.Client("zigbee2mqtt_backup_retriever")
client.connect(os.getenv('MQTT_HOST', 'localhost'), 1883)
msg = ""
info = client.publish(
    topic='zigbee2mqtt/bridge/request/backup',
    payload=msg.encode('utf-8'),
    qos=0,
)
client.message_callback_add('zigbee2mqtt/bridge/response/backup', on_message)
client.subscribe('zigbee2mqtt/bridge/response/backup')

client.loop_start()
logger.info("Message is published: %s", info.is_published())

timeout_counter = 0
while not retrieval_end:
    timeout_counter += 1
    if timeout_counter > 30:
        break
    time.sleep(2)
client.unsubscribe('zigbee2mqtt/bridge/response/backup')
client.disconnect()
client.loop_stop()
