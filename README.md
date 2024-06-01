# Gen-AI : ModelServe Pro

# About
This project involves creating a Service Engine Manager (SEM) for managing multiple variants of Language models. Below are the detailed requirements:

# Requirements
  Select Models and Serving Engine:
  
   - Choose any two variants of Llama models (e.g., llama2:7b) or fine-tuned Llama-based models (e.g., llama2:7b-instruct) from a model repository (e.g., HuggingFace).
   - Select a serving engine (e.g., Vllm).
  
# Develop a Serving Engine Manager:

  **Main Functionality:**
   - Cache Models: Given a list of model names (n > 1), cache them from the model repository.
   - API Server: Run a simple API server with a "/generate" endpoint that receives the model name and prompt, returning the generation result from the serving engine (Note: the model should already be running within the serving engine).
   - Add and Remove Methods: Implement methods to add (i.e., run) a model or remove (i.e., stop) a running model.
  
 **Scheduler:**
  - Add Functionality: If there is not enough available GPU memory, wait until a model is removed. Check available resources (e.g., GPU memory) every 10 seconds.
  - Two-Level Scheduling:
    - Serving Engine Scheduler: Schedules generation tasks.
    - Serving Engine Manager Scheduler: Schedules models to be run with available resources.
      
BONUS Implementation:

- Fault Handling: Implement a solution to handle situations where a model running on the selected serving engine fails. The goal is to ensure generation results are sent back for user prompts.
- Graceful Shutdown: Implement a method to gracefully shut down a model that is no longer supported by the serving engine manager.
Dynamic Model Addition: Add a new model to the serving engine manager without stopping the whole system (assuming the serving engine supports the new model).

**Constraints**:
Hardware: 2 GPUs, each with 24GB RAM.

**Assumptions**:
Make any necessary assumptions to complete the task, and explicitly state them in your solution.

**Notes**
- The focus is on architectural choices rather than end results.
- Provide architectural design diagrams.
- You may implement just the interfaces for some functionalities if time is constrained.

==================================================================== Architecture & Design Details =======================================================================

**Assumptions:**
1. Serving Engine: We'll use VLLM as the serving engine.
2. Models: We'll select llama2:7b or llama2:7b-instruct from HuggingFace.
3. GPUs: We have 2 GPUs, each with 24GB of RAM. ( I will check on this if feasible without paying with free credits )
4. Serving Engine Constraints: Each instance of the serving engine can run only one model at a time.
5. Environment: The solution will be implemented in Python using Gen-AI frameworks

**Core Components of HLD ( High Level Design )**

- API Server
- Model Manager
- Model Cache
- Serving Engine
- Scheduler

  <img width="862" alt="image" src="https://github.com/dubey94/Gen-AI-SEM/assets/38418826/332725ae-5504-471e-92a4-568c4f427c94">

  ![image](https://github.com/dubey94/Gen-AI-SEM/assets/38418826/6e007f77-da37-4dbd-9c84-187fd8c9fbac)

  <img width="826" alt="image" src="https://github.com/dubey94/Gen-AI-SEM/assets/38418826/7cdb8072-f896-4015-9542-8af85a06f1cf">

  <img width="946" alt="image" src="https://github.com/dubey94/Gen-AI-SEM/assets/38418826/00d239b3-d7cf-4978-b186-a97dc616c4b0">


  <img width="933" alt="image" src="https://github.com/dubey94/Gen-AI-SEM/assets/38418826/13f65275-d418-4ebc-8b77-8c660fcd3c63">


  <img width="838" alt="image" src="https://github.com/dubey94/Gen-AI-SEM/assets/38418826/a86c7517-b1cd-4fb5-b448-dd2cc3b0d86f">


   <img width="757" alt="image" src="https://github.com/dubey94/Gen-AI-SEM/assets/38418826/c004e81d-10c0-457c-94e4-b3b6d8214fe9">

   <img width="856" alt="image" src="https://github.com/dubey94/Gen-AI-SEM/assets/38418826/22b23bac-4f4e-4939-96b5-7d47869bea16">
   

