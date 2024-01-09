from django.urls import path,include
from modelview import views

urlpatterns = [
    path('',views.callnew),
    path('sec',views.secall)
]