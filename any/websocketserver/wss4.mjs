// a websocket server implementing chat function
import  { WebSocketServer } from 'ws';
const wss = new WebSocketServer({host:"192.168.43.117",port:8083})

wss.on('connection',con=>{
    console.log('connection established')
    con.on('message',data=>{
        console.log('received %s',data)
        con.send('have read your msg')
    })
    con.on('close',()=>{
        console.log('conn has closed')
    })
})

