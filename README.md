By: Nate Assefa, Tsion Abate, Dan Bezabhe


This is a flask-based chatbot deployed on Google Cloud that answers questions about historical and current weather using:

A local CSV file, created via a python ETL pipeline
A live public API (OpenWeatherMap)

## Supported Cities

This chatbot currently supports the following cities for both historical and current weather queries:

New York, Los Angeles, Tokyo

Messages need to include one of these cities to return a valid response. 


## Public Endpoint
You can send POST requests to the chatbot at: 

**http://34.136.163.228:8080/chat**

** How to test**
Use `curl` or Postman to send a POST request like this:

```bash
curl -X POST http://34.136.163.228:8080/chat \
-H "Content-Type: application/json" \
-d '{"message":"What was the temperature in Tokyo on 2000-01-01?"}'

```

Or, for live weather :

curl -X POST http://34.136.163.228:8080/chat \
-H "Content-Type: application/json" \
-d '{"message":"What is the current weather in New York?"}'


