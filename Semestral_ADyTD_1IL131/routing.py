from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
from django_plotly_dash.routing import application as django_plotly_dash_application

application = ProtocolTypeRouter({
    "http": URLRouter([
        path('django_plotly_dash/',
             URLRouter(django_plotly_dash_application.urlpatterns)),
    ]),
})
