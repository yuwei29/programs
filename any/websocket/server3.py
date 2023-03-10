from SimpleWServer import SimpleWebSocketServer, WebSocket

clients = []
class SimpleChat(WebSocket):

    def handleMessage(self):
       for client in clients:
            client.sendMessage(self.address[0] + u' - ' + self.data)

    def handleConnected(self):
       print(self.address, 'connected')
       for client in clients:
          client.sendMessage(self.address[0] + u' - connected')
       clients.append(self)

    def handleClose(self):
       clients.remove(self)
       print(self.address, 'closed')
       for client in clients:
          client.sendMessage(self.address[0] + u' - disconnected')

server = SimpleWebSocketServer('192.168.43.162', 8763, SimpleChat)
server.serveforever()