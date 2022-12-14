from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.kasperHome, name="kasperHome"),
    path('aboutMe/', views.aboutMe, name="aboutMe"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="contact"),
    path('blogEdit/', views.blogEdit, name="blogEdit"),
    path('delete/<post_id>', views.deletePost, name="deletePost"),
    path('blogEdit/add/', views.addPost, name="addPost"),
    path('blogEdit/edit/<post_id>', views.editPost, name="editPost"),
    path('gallery/', views.gallery, name="gallery"),
    path('login/', views.loginPage, name="login"),
    path('sign-up/', views.signUp, name="sign-up"),
    path('logout/', views.logoutPage, name="logout"),
    path('requested/', views.requestedAppointments, name="requested"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)