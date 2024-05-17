from huggingface_hub import snapshot_download
snapshot_download(
    repo_id="TheBloke/Mistral-7B-Instruct-v0.2-AWQ",
    local_dir="models/TheBloke/Mistral-7B-Instruct-v0.2-AWQ",
    local_dir_use_symlinks=False,
    #filename = "Meta-Llama-3-8B-Instruct-Q5_K_M.gguf")
)