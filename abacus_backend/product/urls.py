from django.urls import path
from signup.views import UserSignUp, UserSignIn, change_password, show_user_profile, update_user
from product.views import addProduct, updateProduct, viewProduct, viewAllProduct
urlpatterns = [
    path('add_product/', addProduct.as_view()),
    path('update_product/', updateProduct.as_view()),
    path('view_product/', viewProduct.as_view()),
    path('view_all_product/', viewAllProduct.as_view())
]
