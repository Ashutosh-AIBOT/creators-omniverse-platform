import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# 1. Set settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# 2. Initialize Django apps early
django.setup()

# 3. Create HTTP application
django_asgi_app = get_asgi_application()

# 4. Import routing AFTER django.setup() to avoid AppRegistryNotReady
import communities.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            communities.routing.websocket_urlpatterns
        )
    ),
})
