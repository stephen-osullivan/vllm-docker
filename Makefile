docker-vllm: 
	docker run --gpus=all -v $(pwd)/models:/models -e HF_HOME=/models -p 8000:8000 \
		vllm/vllm-openai:latest --model TheBloke/Mistral-7B-Instruct-v0.2-AWQ  --quantization awq --max-model-len 1024