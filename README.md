
# 🚀 Simple Dagster Job Example
This project demonstrates how to build and run a **Dagster job** with two dependent nodes using:

-  **Python**: 3.10.2

-  **Dagster**: 1.11.1

-  **Package Manager**: [`uv`](https://github.com/astral-sh/uv) (a fast Python dependency manager)
___
## 📦 Setup Instructions
  
  
### 1. Clone the Repository
  
```bash
git  clone https://github.com/Mitsuki16/simple_dagster_job_example
cd simple_dagster_job_example
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
.venv/Scripts/activate # On Windows  
# OR  
source .venv/bin/activate # On macOS/Linux`
```

### 3. Install Dependencies Using `uv`

```bash
`uv pip install dagster==1.11.1`

```
### 4. Run the Job

To execute the job via the command prompt:
```bash
`dg run` 
```
You should see logs showing the generated number list and their computed sum.

### 5: Access Dagster Web UI

Navigate to the following link in your browser to view the Dagster Web UI:

[http://localhost:3000/overview](http://localhost:3000/overview)
<br>
<br>

## ⚙️ Dagster Assets Overview
This example includes two nodes: 
[Assets Link](https://github.com/Mitsuki16/simple_dagster_job_example/blob/main/src/simple_dagster_job/defs/assets.py)

### 🟢 Node 1 – `Hello`
- **Category**: Initial Node for Execution  
- **Description**: The primary node that logs the text `'Hello'`.

### 🔵 Node 2 – `World`
- **Category**: Subsequent Node  
- **Description**: This node depends on the execution of `Hello` and logs the text `'World'`.

---
## 🎉 Simple Dagster Job Executed Status


![Simple Dagster Job Success Image](https://github.com/user-attachments/assets/dd93daa9-eff6-4c8a-b323-3c837bd04517)

----------
