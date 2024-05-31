# Gen-AI : SEM

# Description
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
- Fault Tolerance

  


  
