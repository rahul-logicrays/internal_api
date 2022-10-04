from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('get_data/', views.GetSalesHistoryView.as_view(), name='get_data'),
]
