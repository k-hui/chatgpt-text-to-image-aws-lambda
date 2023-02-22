# example 1
curl -d '{"prompt":"Describe a cat"}' \
  -H "Content-Type: application/json" \
  -X POST http://localhost:8000/chat
