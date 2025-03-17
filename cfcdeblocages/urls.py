
from django.contrib import admin
from django.urls import path, include
from cfcdeblocagesmiseenplace import views
from cfcdeblocagesmiseenplace.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cfcdeblocagesmiseenplace.urls')),
    path('afficher-csv/', views.display_csv, name='display_csv'),
    path('home/', views.home, name='home'),  # Pour afficher tous les dossiers
    path('dossier/<str:unitcode>/', views.dossier_detail, name='dossier_detail'),  # Pour afficher un dossier spécifique
    path('dossier/<path:unitcode>/', views.dossier_detail, name='dossier_detail'),
    

]