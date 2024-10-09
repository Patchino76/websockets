from typing import Annotated
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi import (
    Cookie,
    Depends,
    FastAPI,
    Query,
    WebSocket,
    WebSocketException,
    status,
)
app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <label>Item ID: <input type="text" id="itemId" autocomplete="off" value="foo"/></label>
            <label>Token: <input type="text" id="token" autocomplete="off" value="some-key-token"/></label>
            <button onclick="connect(event)">Connect</button>
            <hr>
            <label>Message: <input type="text" id="messageText" autocomplete="off"/></label>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
        var ws = null;
function connect(event) {
    var itemId = document.getElementById("itemId");
    var token = document.getElementById("token");
    var ws = new WebSocket("ws://localhost:8000/items/" + itemId.value + "/ws?token=" + token.value);
    ws.onmessage = function(event) {
        var messages = document.getElementById('messages');
        var message = document.createElement('li');
        var content = document.createTextNode(event.data);
        message.appendChild(content);
        messages.appendChild(message);
    };
    window.ws = ws;
    event.preventDefault();
}
            function sendMessage(event) {
                event.preventDefault()
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


async def get_cookie_or_token(
    websocket: WebSocket,
    session: Annotated[str | None, Cookie()] = None,
    token: Annotated[str | None, Query()] = None,
):
    if session is None and token is None:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    return session or token


@app.websocket("/items/{item_id}/ws")
async def websocket_endpoint(
    *,
    websocket: WebSocket,
    item_id: str,
    q: int | None = None,
    cookie_or_token: Annotated[str, Depends(get_cookie_or_token)],
):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(
            f"Session cookie or query token value is: {cookie_or_token}"
        )
        if q is not None:
            await websocket.send_text(f"Query parameter q is: {q}")
        await websocket.send_text(f"Message text was: {data}, for item ID: {item_id}")

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", host="localhost", port=8000, reload=True)
