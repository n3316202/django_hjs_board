"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pybo import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('pybo/', include('pybo.urls')), # pybo/로 매핑해야 한다. 이렇게 뒤에 슬래시를 붙여주면 브라우저 주소창에 http://localhost:8000/pybo 라고 입력해도 자동으로 http://localhost:8000/pybo/ 처럼 변환
]

