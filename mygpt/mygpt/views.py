from  django.shortcuts import render
from dotenv import load_dotenv
import os,openai
from django.http import JsonResponse
load_dotenv()

API_KEY = os.getenv("OPENAI_KEY",None)
MSGS = []
def chatBot(request):
    
    botReply = None
    if  API_KEY is  not None  and request.method == "POST":
        print("Replyiinnnggg")
        openai.api_key =  API_KEY
        userInp = request.POST.get('userinp')
        
        prompt  = {"role":"user","content":userInp}
        MSGS.append(prompt)
        
        
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = MSGS
        )
       
        botReply = resp['choices'][0]['message']['content']
        MSGS.append({"role":"assistant","content":botReply})
        return JsonResponse({'message': botReply})
    else:
        print(f"No post")
    
    return render(request,'index.html',{"response":botReply})