import subprocess
import psutil

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
