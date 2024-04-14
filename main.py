from fastapi import FastAPI

app = FastAPI()

@app.route('/')
def index():
    return "Habib Public School"

@app.route('/about')
def about():
    return "Habib Public School"