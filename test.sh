# example 1
curl -d '{"prompt":"How to draw a cat?"}' \
  -H "Content-Type: application/json" \
  -X POST http://localhost:8000

# example 2
curl -d '{"prompt":"What is the weather today in London?","model":"text-davinci-002","temperature":0.5}' \
  -H "Content-Type: application/json" \
  -X POST http://localhost:8000
