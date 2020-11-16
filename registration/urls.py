from django.urls import path
from .views import SingUpView, ProfileUpdate, registration, login

urlpatterns = [
    
    path('signup/' ,SingUpView.as_view(), name ='signup'),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('login/', login, name="login"),
    path('registration/', registration, name="registro"),
]
