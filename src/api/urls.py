from django.urls import path
from src.api.views import (
    BlogView,
)

app_name = 'blog'

urlpatterns = [
    path('blog/', BlogView.as_view())
 ]