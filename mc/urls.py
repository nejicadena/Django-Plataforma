from django.urls import path
from .views import colePageView, cole1PageView, cole2PageView, cole3PageView, cole4PageView, cole5PageView, cole6PageView, cole6PageView, cole8PageView, coleFinalPageView

urlpatterns = [
    path('colectivo/', colePageView.as_view(), name="colectivo"),
    path('colectivo_1/', cole1PageView.as_view(), name="colectivo_1"),
    path('colectivo_1/', cole2PageView.as_view(), name="colectivo_2"),
    path('colectivo_1/', cole3PageView.as_view(), name="colectivo_3"),
    path('colectivo_1/', cole4PageView.as_view(), name="colectivo_4"),
    path('colectivo_1/', cole5PageView.as_view(), name="colectivo_5"),
    path('colectivo_1/', cole6PageView.as_view(), name="colectivo_6"),
    path('colectivo_1/', cole8PageView.as_view(), name="colectivo_7"),
    path('colectivo_1/', coleFinalPageView.as_view(), name="colectivo_final"),
    

]