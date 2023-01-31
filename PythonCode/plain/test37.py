from revChatGPT.ChatGPT import Chatbot
f = open('D:/personal/programs/PythonCode/plain/tempChatGPT_token.txt')
CHATTOKEN = f.read()
f.close()

chatbot = Chatbot({
  "session_token": CHATTOKEN
}, conversation_id=None, parent_id=None) # You can start a custom conversation

response = chatbot.ask("C++相比于Java有哪些优势", conversation_id=None, parent_id=None) 
# You can specify custom conversation and parent ids. Otherwise it uses the saved conversation 
# (yes. conversations are automatically saved)

print(response)
# {
#   "message": message,
#   "conversation_id": self.conversation_id,
#   "parent_id": self.parent_id,
# }