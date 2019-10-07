from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from . import settings
from .views import home_view, signup

urlpatterns = [
    url(r'^$', home_view, name='home'),
    url('admin/', admin.site.urls),
    url(r'^notes/', include(('notes.urls', 'notes'), namespace='notes')),
    url(r'^signup/', signup, name='signup'),
    url(r'^logout/', views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]

