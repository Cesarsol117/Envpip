import store
from fastapi import FastAPI

app = FastAPI()

def get_list():
    return [1,2,3]

@app.get('/')

def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()