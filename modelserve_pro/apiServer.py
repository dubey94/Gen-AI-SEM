from flask import Flask, request, jsonify

app = Flask(__name__)
model_cache = ModelCache()
model_manager = ModelManager()

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    model_name = data["model_name"]
    prompt = data["prompt"]

    if model_manager.is_model_running(model_name):
        # Send prompt to the serving engine and get the result
        result = send_prompt_to_model(model_name, prompt)
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Model is not running"}), 400

@app.route("/add_model", methods=["POST"])
def add_model():
    data = request.json
    model_name = data["model_name"]
    gpu_id = data["gpu_id"]

    model_path = model_cache.cache_model(model_name)
    pid = model_manager.start_model(model_name, model_path, gpu_id)
    return jsonify({"message": f"Model {model_name} started on GPU {gpu_id}", "pid": pid})

@app.route("/remove_model", methods=["POST"])
def remove_model():
    data = request.json
    model_name = data["model_name"]

    model_manager.stop_model(model_name)
    return jsonify({"message": f"Model {model_name} stopped"})
