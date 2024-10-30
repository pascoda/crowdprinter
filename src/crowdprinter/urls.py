"""crowdprinter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import include
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", views.PrintJobListView.as_view()),
    path("myprints", views.MyPrintAttempts.as_view(), name="my_printattempts"),
    path(
        "printjob/<slug>/",
        include(
            [
                path("", views.PrintJobDetailView.as_view(), name="printjob_detail"),
                path("stl", views.ServeStlView.as_view(), name="printjob_stl"),
                path(
                    "file/<fileid>/gcode",
                    views.ServeGcodeFileView.as_view(),
                    name="printjob_gcode",
                ),
                path(
                    "file/<fileid>/3mf",
                    views.Serve3mfFileView.as_view(),
                    name="printjob_3mf",
                ),
                path("render", views.ServeRenderView.as_view(), name="printjob_render"),
                path("take", views.take_print_job, name="printjob_take"),
                path("give_back", views.give_back_print_job, name="printjob_give_back"),
                path("done", views.printjob_done, name="printjob_done"),
            ]
        ),
    ),
]
