from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, GetDataByNameView

urlpatterns = {
    url(r'^userdata/$', CreateView.as_view(), name='create'),
    url(r'^userdata/(?P<name>[A-Za-z]+)/$', GetDataByNameView.as_view(), name='get_by_name'),
}

urlpatterns = format_suffix_patterns(urlpatterns)