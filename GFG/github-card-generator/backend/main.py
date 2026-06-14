from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mcp_server import mcp

app = FastAPI()

# Allow your frontend page to safely communicate with this backend port
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "GitHub Dev Card Generator Backend"}

def process_card_generation(username: str):
    try:
        result = mcp.get_tool("scrape_github")(username=username)
        return {"status": "Success", "data": result}
    except Exception as e:
        try:
            from mcp_server import scrape_github
            result = scrape_github(username)
            return {"status": "Success", "data": result}
        except Exception as inner_e:
            return {"status": "Error", "message": f"Could not run card tool: {str(inner_e)}"}

@app.get("/generate-card")
async def generate_card_get(username: str):
    return process_card_generation(username)

@app.post("/generate-card")
async def generate_card_post(username: str):
    return process_card_generation(username)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)