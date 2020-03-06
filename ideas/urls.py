from django.urls import path
from .views import IdeasList, IdeaDetail, SubmissionCreate

urlpatterns = [
    path("", IdeasList.as_view(), name='idea-list'),
    path('<slug:slug>/', IdeaDetail.as_view(), name="idea-detail"),
    path('<slug:slug>/add-submission/', SubmissionCreate.as_view(), name="submission-add")

    ]
