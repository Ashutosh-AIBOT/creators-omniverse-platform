from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .rag_engine import get_xomni_response

def chatbot_page(request):
    """Renders the beautiful Xomni Chat interface."""
    return render(request, 'xomni/index.html')

@csrf_exempt
def chat_api(request):
    """API endpoint for Xomni Chat."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            history = data.get("history", [])
            
            if not user_message:
                return JsonResponse({"error": "No message provided"}, status=400)
            
            ai_response = get_xomni_response(user_message, history)
            
            return JsonResponse({"response": ai_response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid request"}, status=405)