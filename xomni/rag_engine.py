import os
from groq import Groq
from django.conf import settings
from testprofiles.models import LinkItem
from django.db.models import Q

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_relevant_context(query):
    """
    Retrieves relevant items from LinkItem to provide as context.
    """
    # Simple keyword matching for RAG
    link_items = LinkItem.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )[:5]
    
    context_str = "Relevant Platform Resources:\n"
    for item in link_items:
        context_str += f"- [{item.section}] {item.title}: {item.description} (URL: {item.url})\n"
    
    return context_str

def get_xomni_response(query, chat_history=[]):
    """
    Calls Groq with RAG context and history.
    """
    context = get_relevant_context(query)
    
    system_prompt = f"""
    You are Xomni, the AI companion for CreatorsOmniverse.
    Your goal is to help users navigate the platform and learn effectively.
    Use the following context from our platform database to answer accurately:
    
    {context}
    
    If the user asks about something not in the context, use your general knowledge but mention that it might not be a direct platform resource.
    Be encouraging, professional, and concise.
    """
    
    messages = [{"role": "system", "content": system_prompt}]
    
    # Add history
    for msg in chat_history[-5:]: # Keep last 5 exchanges
        messages.append(msg)
        
    messages.append({"role": "user", "content": query})
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Oops! I'm having trouble thinking right now. Error: {str(e)}"
