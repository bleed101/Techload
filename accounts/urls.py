from django.urls import path
from .import views
from .views import PostListView,PostDetailView,PostCreateView,update,delete

urlpatterns=[
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("about",views.about,name="about"),
    path("blogs",PostListView.as_view(),name="blogs"),
    path("post/<int:pk>/",PostDetailView.as_view(),name="post"),
    path("submit",PostCreateView.as_view(),name="submit"),
    path("post/update/<int:id>",update.as_view(),name="update"),
    path("post/delete/<int:id>",delete.as_view(),name="delete"),
    # path('post/genre/<str:memlk>',sort.as_Vew)
]