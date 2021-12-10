cd app/
# Start rasa server with nlu model
rasa run -m Rasa-Restaurant-Bot/models --endpoints endpoints.yml --credentials credentials.yml
