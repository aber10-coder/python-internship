from fastapi import FastAPI
app=FastAPI()

@app.get("/square/{n}")
def square(n:int):
    return{
        "input":n,
        "result":n*n
    }
