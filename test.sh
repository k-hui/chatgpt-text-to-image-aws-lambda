# example 1
curl -d '{"prompt":"How to draw a cat?"}' \
  -H "Content-Type: application/json" \
  -X POST http://localhost:8000/chat

# example 2
curl -d '{"prompt":"AI cover image?"}' \
  -H "Content-Type: application/json" \
  -X POST http://localhost:8000/image
