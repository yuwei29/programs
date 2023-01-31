import { ChatGPTAPIBrowser } from 'chatgpt'
import * as readline from 'readline'

async function example() {
  // use puppeteer to bypass cloudflare (headful because of captchas)
  const api = new ChatGPTAPIBrowser({
    email: process.env.OPENAI_EMAIL,
    password: process.env.OPENAI_PASSWORD,
    debug: false,
    minimize: true
  })

  await api.initSession()
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
  });
  // const result = await api.sendMessage('Hello World!')
  // console.log(result.response)
  // while(true){}
  let result = await api.sendMessage('hello, my friend. nice to meet you')
  console.log(result.response)
  const conversationId = result.conversationId
  let preMsgId = result.messageId
  for await (const line of rl) {
    if(line=='q') break;
    result = await api.sendMessage(line,{ 
      conversationId: conversationId,
      parentMessageId: preMsgId
     })
    console.log(result.response)
    preMsgId = result.messageId
  }
  await api.closeSession()
}

function cli(){
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
  });
  
  rl.on('line', (line) => {
      console.log(line);
  });
  
  rl.once('close', () => {
       // end of input
   });
}

async function eg(){
  const rl = readline.createInterface({ input:process.stdin, output:process.stdout });
  for await (const line of rl) {
    // Each line in input.txt will be successively available here as `line`.
    console.log(`Line from user: ${line}`);
    if(line=='q') break;
  }
}

example()