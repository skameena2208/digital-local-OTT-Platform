"""
URL configuration for digital_ott project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from digitalottapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('apartment',views.apartment,name="apartment"),
    path('blog',views.blog,name="blog"),
    path('elements',views.elements,name="elements"),
    path('project',views.project,name="project"),
    path('services',views.services,name="services"),
    path('single_blog',views.single_blog,name="single_blog"),
    path('contact',views.contact,name="contact"),
    path('customerlogin', views.customer_login,name="customerlogin"),
    path('customer_registered', views.customer_registered,name="customer_registered"),
    path('customer_home', views.customer_home, name="customer_home"),
    path('customer_profile', views.customer_profile, name="customer_profile"),
    path('customer_view_movies', views.customer_view_movies, name="customer_view_movies"),
    path('customer_view_webseries', views.customer_view_webseries, name="customer_view_webseries"),
    path('customer_view_serials', views.customer_view_serials, name="customer_view_serials"),
    path('customer_logout', views.customer_logout, name="customer_logout"),
    path('accept_customer/<int:id>', views.accept_customer, name="accept_customer"),
    path('reject_customer/<int:id>', views.reject_customer, name="reject_customer"),
    path('customer_edit', views.customer_edit, name="customer_edit"),
    path('customer_update', views.customer_update, name="customer_update"),
    path('customer_change_password', views.customer_change_password, name="customer_change_password"),
    path('admin_login', views.admin_login, name="admin_login"),
    path('admin_home', views.admin_home, name="admin_home"),
    path('admin_view_contact', views.admin_view_contact, name="admin_view_contact"),
    path('admin_view_customer', views.admin_view_customer, name="admin_view_customer"),
    path('admin_logout', views.admin_logout, name="admin_logout"),
    path('admin_change_password', views.admin_change_password, name="admin_change_password"),
    path('customer_deactivate/<int:id>',views.customer_deactivate,name="customer_deactivate"),
    path('add_notification',views.add_notification,name="add_notification"),
    path('view_notification', views.view_notification, name="view_notification"),
    path('notification_edit/<int:id>', views.notification_edit, name="notification_edit"),
    path('notification_update', views.notification_update, name="notification_update"),
    path('view_notification_delete/<int:id>', views.view_notification_delete, name="view_notification_delete"),
    path('admin_add_category', views.admin_add_category, name="admin_add_category"),
    path('admin_view_category', views.admin_view_category, name="admin_view_category"),
    path('category_edit/<int:id>', views.category_edit, name="category_edit"),
    path('category_update', views.category_update, name="category_update"),
    path('view_category_delete/<int:id>', views.view_category_delete, name="view_category_delete"),
    path('add_movie',views.add_movie,name="add_movie"),
    path('view_movie', views.view_movie, name="view_movie"),
    path('movie_edit/<int:id>', views.movie_edit, name="movie_edit"),
    path('movie_update', views.movie_update, name="movie_update"),
    path('view_movie_delete/<int:id>', views.view_movie_delete, name="view_movie_delete"),
    path('add_webseries',views.add_web_series,name="add_webseries"),
    path('view_webseries', views.view_webseries, name="view_webseries"),
    path('webseries_edit/<int:id>', views.webseries_edit, name="webseries_edit"),
    path('webseries_update', views.webseries_update, name="webseries_update"),
    path('view_webseries_delete/<int:id>', views.view_webseries_delete, name="view_webseries_delete"),
    path('add_serials', views.add_serials, name="add_serials"),
    path('view_serials', views.view_serial, name="view_serials"),
    path('serial_edit/<int:id>', views.serial_edit, name="serial_edit"),
    path('serial_update', views.serial_update, name="serial_update"),
    path('view_serial_delete/<int:id>', views.view_serial_delete, name="view_serial_delete"),
    path('webseries_add_episode/<int:id>', views.webseries_add_episode, name='webseries_add_episode'),
    path('view_webseries_episodes/<int:id>', views.view_webseries_episodes, name="view_webseries_episodes"),
    path('serial_add_episode/<int:id>', views.serial_add_episode, name='serial_add_episode'),
    path('view_serials_episodes/<int:id>', views.view_serials_episodes, name="view_serials_episodes"),
    path('customer_view_webseries_episodes/<int:id>', views.customer_view_webseries_episodes, name="customer_view_webseries_episodes"),
    path('customer_view_serials_episodes/<int:id>', views.customer_view_serials_episodes,name="customer_view_serials_episodes"),
    path('add_movie_review/<int:id>',views.add_movie_review,name="add_movie_review"),
    path('view_movie_review', views.view_movie_review, name="view_movie_review"),
    path('add_webseries_review/<int:id>',views.add_webseries_review,name="add_webseries_review"),
    path('view_webseries_review', views.view_webseries_review, name="view_webseries_review"),
    path('add_serial_review/<int:id>',views.add_serial_review,name="add_serial_review"),
    path('view_serial_review', views.view_serial_review, name="view_serial_review"),
    path('add_plan', views.add_plan, name="add_plan"),
    path('view_plan', views.view_plan, name="view_plan"),
    path('customer_view_plans', views.customer_view_plans, name="customer_view_plans"),
    path('buy_plan/<int:id>', views.buy_plan, name="buy_plan"),
    path('admin_view_subscribers/', views.admin_view_subscribers, name='admin_view_subscribers'),
    path('customer_view_history/', views.customer_view_history, name='customer_view_history'),
    path('plan_delete/<int:id>', views.plan_delete, name="plan_delete"),
    path('customer_view_movie_reviews/<int:id>', views.customer_view_movie_reviews, name="customer_view_movie_reviews"),
    path('customer_view_webseries_reviews/<int:id>', views.customer_view_webseries_reviews, name="customer_view_webseries_reviews"),
    path('customer_view_serial_reviews/<int:id>', views.customer_view_serial_reviews, name="customer_view_serial_reviews"),


]
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
