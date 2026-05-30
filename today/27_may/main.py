from fastapi import FastAPI

app = FastAPI()

@app.get("/")
@app.get("/home")
@app.get("/start")
def home():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)


# # FUNCTION
# def name_of_the_function(a, b, c, d, e)