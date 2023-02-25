# example 1
curl -d '{"prompt":"Describe an elf"}' \
  -H "Content-Type: application/json" \
  -X POST http://localhost:8000/chat
