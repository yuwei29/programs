// a websocket server using 'import' syntax
import  { WebSocketServer } from 'ws';
const wss = new WebSocketServer({port:8083})

wss.on('connection',con=>{
    console.log('connection established')

    con.on('close',()=>{
        console.log('conn has closed')
    })
})

