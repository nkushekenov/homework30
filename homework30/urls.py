from django.contrib import admin
from django.urls import path, include
from HW30.views import person_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('HW30/', include('HW30.urls')),
    path('', person_list, name='home'),
    path('person_list/', person_list, name='person_list/'),
]