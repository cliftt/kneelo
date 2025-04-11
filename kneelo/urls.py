from django.contrib import admin
from django.urls import path
from orders import views
from django.conf import settings
from django.conf.urls.static import static

# подключаем views напрямую

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),  # главная страница
    path('api/create-order/', views.create_order),  # API при отправке формы
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)