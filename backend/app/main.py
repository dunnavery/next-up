from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
	return {"message": "Hello World"}


@app.get("/books")
async def get_books():
	return {
		"books": []
	}


