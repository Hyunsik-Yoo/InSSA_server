from django.conf.urls import url
from inssa import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^inssa/score/$',views.get_ranking),
]

urlpatterns = format_suffix_patterns(urlpatterns)
