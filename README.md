# MQTT Retriever

Goal is to provide a simple way to download and store the base64 encoded zip from Zigbee2MQTT backup function on disk. It first request the zip file from mqtt via sending a message to the topic and then waits for a new message on the respone topic. Once it received the message it decodes it and stored it on disk as a zip file.

Sources:

- <https://stackoverflow.com/questions/22402679/write-decoded-from-base64-string-to-file>
- <https://stackoverflow.com/questions/61043898/how-to-handle-the-loop-stop-paho-mqtt>
- <https://python.plainenglish.io/mqtt-beginners-guide-in-python-38590c8328ae>
- <http://www.steves-internet-guide.com/into-mqtt-python-client/>
- <https://mosquitto.org/man/mosquitto_sub-1.html>
- <http://www.steves-internet-guide.com/mosquitto_pub-sub-clients/>
- <https://github.com/Koenkk/zigbee2mqtt/discussions/12731>
- <https://www.zigbee2mqtt.io/guide/usage/mqtt_topics_and_messages.html#zigbee2mqtt-bridge-request>
