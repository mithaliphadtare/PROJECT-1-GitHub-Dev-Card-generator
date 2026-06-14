import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import requests

# 1. Load your API Key from the .env file
load_dotenv()

# 2. Initialize FastMCP Server
mcp = FastMCP("Github Card Generator")

@mcp.tool()
def scrape_github(username: str) -> str:
    """
    Scrapes basic profile information for a given GitHub username.
    """
    try:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"User: {data.get('login')}\nBio: {data.get('bio')}\nPublic Repos: {data.get('public_repos')}\nFollowers: {data.get('followers')}"
        return f"Failed to fetch data for username: {username} (Status Code: {response.status_code})"
    except Exception as e:
        return f"Error scraping GitHub: {str(e)}"

if __name__ == "__main__":
    # Run the server cleanly using standard input/output (stdio)
    mcp.run(transport="stdio")