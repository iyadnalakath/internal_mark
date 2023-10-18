from . import views
from django.db import router
from django.urls import path
from rest_framework_nested import routers




urlpatterns = [

]

urlpatterns =  urlpatterns
router = routers.DefaultRouter()
router.register("subject", views.SubjectViews,basename="subject"),
router.register("semester", views.SemesterViews,basename="semester"),
router.register("teacher/registration", views.TeacherRegistrationView,basename="teacher"),
router.register("student/add", views.StudentRegistrationView,basename="student"),
# router.register("event_management_users", views.EventManagementUsersView)
# router.register('eventteamlistsubcatagory',views.EventManagementSubcategoryViewSet,basename='MyModel')


urlpatterns = router.urls + urlpatterns
