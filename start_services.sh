cd app/
# Start rasa server with nlu model
rasa run -m models --endpoints endpoints.yml --credentials credentials.yml
