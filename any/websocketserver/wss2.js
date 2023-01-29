// a more simple websocket server
const ws = require('ws')
const wss = new ws.Server({port:8083})

wss.on('connection',con=>{
    console.log('connection established')

    con.on('close',()=>{
        console.log('conn has closed')
    })
})

