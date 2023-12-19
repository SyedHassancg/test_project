# Test Project
## Installation 
### Clone Project 
```shell
git clone project_link
```

### change directory
```shell
cd test_project
```

### Create a new Virtual Environment
```shell
python3 -m venv venv
```

### Activate Virtual Environment
```shell
source venv/bin/activate
```

### Setup project
```shell
pip install -r requirements.txt
```

### Run Server
```shell
uvicorn app:app --reload
```
You can access server here http://127.0.0.1:8000 and swagger docs here http://127.0.0.1:8000/docs.