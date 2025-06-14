from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact_view, name='contact'),
    path('terms-of-service/', views.terms_of_service_view, name='terms_of_service'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('shipping-information/', views.shipping_information_view, name='shipping_information'),
    path('refund-policy/', views.refund_policy_view, name='refund_policy'),\
    path('about-us/', views.about_us_view, name='about_us'),
    path('products/', views.product_list_view, name='product_list'),
    path('products/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('profile/', views.profile_page_view, name='profile_page'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/change-password/', views.password_change_view, name='password_change'), # New password change URL
]