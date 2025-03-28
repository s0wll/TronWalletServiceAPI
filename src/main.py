import sys
from pathlib import Path

from fastapi import FastAPI
import uvicorn

sys.path.append(str(Path(__file__).parent.parent))

from src.api.wallet_info import router as router_wallet_info


app = FastAPI()

app.include_router(router_wallet_info)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
