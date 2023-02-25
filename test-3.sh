# example 1
curl -d '{"prompt":"Describe 3 different Goblin characters"}' \
  -H "Content-Type: application/json" \
  -X POST http://localhost:8000/top_results
