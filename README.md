# vllm-docker
repo showing how to launch vllm with docker.

we pull the dockerfile:

docker pull vllm/vllm-openai:latest

run with these commands

docker run --gpus=all -v /home/sos00/.cache/huggingface:/models -e HF_HOME=/models -p 8000:8000 vllm/vllm-openai:latest --model TheBloke/Llama-2-7b-Chat-AWQ --quantization awq --dtype half --max-model-len 4096 

view models like this:

curl http://localhost:8000/v1/models \



query like this

curl http://localhost:8000/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
"model": "TheBloke/Llama-2-7b-Chat-AWQ",
"max_tokens" : 250,
"temperature" : 0.5,
"messages": [
{"role": "system", "content": "You are a helpful assistant."},
{"role": "user", "content": "Who won the world series in 2020?"}
]
}'
