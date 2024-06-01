import os
from huggingface_hub import snapshot_download

class ModelCache:
    def __init__(self, cache_dir="model_cache"):
        self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)

    def cache_model(self, model_name):
        model_path = os.path.join(self.cache_dir, model_name)
        if not os.path.exists(model_path):
            snapshot_download(repo_id=model_name, cache_dir=model_path)
        return model_path
