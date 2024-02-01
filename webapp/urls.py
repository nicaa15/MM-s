from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name="homepage"),
    path('about/', views.about_page, name="aboutpage"),
    path('contact/', views.contact_page, name="contactpage"),
    path('bloglist/', views.bloglist_page, name="bloglistpage"),
    path('webapp/blogpost/<int:id>/', views.blogpost_page, name="blogpostpage"),
    path('form/', views.form_page, name="formpage"),
    path('admin/', views.admin_page, name="adminpage"),
    path('login/', views.login_page, name="loginpage"),
    path('addproject/', views.addproject_page, name="addprojectpage"),
    path('addprojectsss/', views.addproject, name="addprojectpagesssss"),
    path("loginuser/", views.LoginUser, name="login"),
    path('addblog/', views.addblog, name="addblogblog"),
    path('addcontact/', views.addcontact, name="addcontact"),
    path('donation/', views.adddonation_page, name="donationpage"),
    path('adddonation/', views.adddonation, name="adddonation"),
    path('update/<int:blog_id>/', views.edit_blog, name='update'),
    path('uprec/<int:blog_id>/', views.uprec, name="uprec"),
    path('logoutuser/', views.logout_user, name='logout_user'),
    path('adminbloglist/', views.adminbloglist_page, name="adminbloglistpage"),
    path('delete_blog/<int:blog_id>/',views.delete_blog, name='delete_blog'),
    path('delete_bloguser/<int:blog_id>/',views.delete_bloguser, name='delete_bloguser'),
    path('webapp/adminblogpost/<int:id>/', views.adminblogpost, name='adminblogpostpage'),
    path('webapp/editblogpostpage/<int:id>/', views.editblogpostpage, name='editblogpostpage'),
    path('webapp/editblogpost/<int:id>/', views.editblogpost, name='editblogpost'),
path('delete_blogs/<int:blog_id>/',views.delete_blogs, name='delete_blogs'),
    path('delete_project/<int:blog_id>/', views.delete_project, name='delete_project'),

    path('webapp/editprojectpage/<int:id>/', views.editprojectpage, name='editprojectpage'),
    path('webapp/editprojectpost/<int:id>/', views.editprojectpost, name='editprojectpost'),

]

# Add the following lines to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
