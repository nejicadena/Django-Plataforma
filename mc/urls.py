from django.urls import path
from .views import colePageView

urlpatterns = [
    path('colectivo/', colePageView.as_view(), name="colectivo"),
    # path('mc/', MCPageView.as_view(), name="mc")
]