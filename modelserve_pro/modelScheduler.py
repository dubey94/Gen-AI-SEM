class Scheduler:
    def __init__(self, model_manager):
        self.model_manager = model_manager

    def add_model(self, model_name, gpu_id):
        while not self.check_gpu_memory(gpu_id):
            time.sleep(10)
        self.model_manager.start_model(model_name, model_cache.cache_model(model_name), gpu_id)

    def check_gpu_memory(self, gpu_id):
        # Implement GPU memory check logic
        gpu_memory = psutil.virtual_memory()
        return gpu_memory.available > 16 * 1024 * 1024 * 1024  # Check if enough memory is available
