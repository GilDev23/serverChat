import asyncio
import websockets

# Set up a list to store connected clients
connected_clients = set()

async def chat(websocket, path):
    # Add the new client to the list of connected clients
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            # Broadcast the received message to all connected clients
            for client in connected_clients:
                await client.send(message)
    finally:
        # Remove the client from the list when the connection is closed
        connected_clients.remove(websocket)

# Start the WebSocket server
start_server = websockets.serve(chat, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
