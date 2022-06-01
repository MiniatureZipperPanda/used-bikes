from django.urls import path
from seller import views

urlpatterns = [
    path('home', views.SellerHomeView.as_view(), name="sl-home"),
    path('bikes/add', views.AddBikeView.as_view(), name="add-bike"),
    path('bikes/all', views.ListBikeView.as_view(), name="list-bikes"),
    path('users/account/signup', views.SignUpView.as_view(), name="sign-up"),
    path('users/account/signin', views.SignInView.as_view(), name="sign-in"),
    path('users/account/sign-out', views.sign_out_view, name="sign-out"),
    path('bikes/change/<int:id>', views.EditBikeView.as_view(), name="edit-bikes"),
    path('bikes/details/<int:id>', views.DetailBikeView.as_view(), name="details-bikes"),
    path('bikes/delete/<int:id>', views.DeleteBikeView.as_view(), name="delete-bikes"),

]
