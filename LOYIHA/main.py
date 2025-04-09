from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import json
from typing import List

app = FastAPI()

# WebSocket ulanishlarini saqlash
connections: List[WebSocket] = []

@app.get("/")
async def get():
    html = """
    <html>
        <head>
            <title>WebSocket Chat</title>
        </head>
        <body>
            <h1>Welcome to WebSocket Chat</h1>
            <p>Open your browser console to see WebSocket events.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # WebSocketga ulangan barcha foydalanuvchilarga xabar yuborish
            for connection in connections:
                if connection != websocket:
                    await connection.send_text(data)
    except WebSocketDisconnect:
        connections.remove(websocket)
        print(f"A client disconnected from the WebSocket")
