from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Example</title>
    </head>
    <body>
        <h1>WebSocket Example</h1>
        <button onclick="connectWebSocket()">Connect</button>
        <script>
            function connectWebSocket() {
                const ws = new WebSocket("ws://localhost:8000/ws");
                ws.onmessage = function(event) {
                    alert("Message from server: " + event.data);
                };
                ws.onopen = function() {
                    ws.send("Hello Server !!!");
                };
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data} asshole...")

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", host="localhost", port=8000, reload=True)
