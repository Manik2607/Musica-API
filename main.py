from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import scraper

app = FastAPI(
    title="Musica API",
    description="Musica API is a simple API that allows you to search and download music from the internet.",
    version="1.0.0",
    redoc_url=None,
    deprecated=False
)


# allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"]
)

@app.get("/search/{query}")
async def get_search_results(query: str) -> List[dict]:
    return await scraper.search(query)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)