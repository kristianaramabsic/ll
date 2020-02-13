from django.urls import path
from .views import HomePageView, AboutPageView, PostPageView


urlpatterns = [
    path ('', HomePageView.as_view(), name='homepage'),
    path ('about', AboutPageView.as_view(), name='about'),
    path ('post/<int:pk>/', PostPageView.as_view(), name='post_detail'),
]