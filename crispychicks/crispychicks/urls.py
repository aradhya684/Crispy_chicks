
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import views #here dot . means same package or file not form another folder
from products import urls #adding urls.py from products applcation
from cart import urls
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="homepage"),
    path('login/', views.user_login, name="loginpage"),
    path('logout/',views.logout_user,name="logoutpage"),
    path('register/', views.register, name="registerpage"),
    path('menu/',include('products.urls')),
    path('cart/',include('cart.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)