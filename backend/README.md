# The solution will take PDF documents, extract information from them, classify the documents

### 1. Start Backend - Create a virtual environment

```shell
cd backend/
sudo apt install python3.13-venv
sudo apt-get install python3.13-dev

python3.13 -m venv x_venv
source x_venv/bin/activate
cp .envExample .env # add your LITELLM_KEY (openai api key)
pip install -r requirements.txt
cd app
python -B -m uvicorn main:app --reload --log-level info
```

