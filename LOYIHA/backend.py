from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()

# WebSocket aloqasi uchun foydalanuvchilarni saqlash
active_connections: List[WebSocket] = []

# Asosiy sahifa - frontendni ko'rsatish
@app.get("/", response_class=HTMLResponse)
async def get():
    with open("index.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

# WebSocket ulanishi - xabarlarni yuborish
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    
    try:
        while True:
            message = await websocket.receive_text()
            # Xabarni barcha aloqalarga yuborish
            for connection in active_connections:
                if connection != websocket:
                    await connection.send_text(message)
    except WebSocketDisconnect:
        active_connections.remove(websocket)
