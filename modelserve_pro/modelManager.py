import subprocess
import psutil
import logging

class ModelManager:
    def __init__(self):
        self.running_models = {}

    def start_model(self, model_name, model_path, gpu_id):
        command = f"vllm start --model {model_path} --gpu {gpu_id}"
        process = subprocess.Popen(command, shell=True)
        self.running_models[model_name] = process
        return process.pid

    def stop_model(self, model_name):
        if model_name in self.running_models:
            process = self.running_models[model_name]
            process.terminate()
            process.wait()
            del self.running_models[model_name]

    def is_model_running(self, model_name):
        return model_name in self.running_models

    def monitor_models(self):
        for model_name, process in self.running_models.items():
            if process.poll() is not None:  # Process has terminated
                logging.error(f"Model {model_name} has failed. Restarting...")
                self.stop_model(model_name)
                # Restart the model on the same GPU (assuming the GPU ID is known)
                self.start_model(model_name, model_cache.cache_model(model_name), gpu_id)
