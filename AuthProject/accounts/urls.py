from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.login_page,name='login'),
    path('dashboard/',views.dashboard_page,name='dashboard'),
    path('logout/',views.logout_page,name='logout'),
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="password_change.html",
            success_url="/dashboard/",
        ),
        name="password_change",
    ),

    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="password_reset.html"
        ),
        name="password_reset",
    ),

    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]