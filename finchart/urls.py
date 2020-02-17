from django.urls import path

from . import views

app_name = 'finchart'

urlpatterns = [
    # IndexTemplateViewから IndexViewに変更
    path('', views.IndexView.as_view(), name='index'),
    path('company/<int:pk>', views.CompanyView.as_view(), name='company'),
    path('fstatement_detail/<int:pk>', views.FstatementView.as_view(), name='fstatement'),
]
