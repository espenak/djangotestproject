from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import include

urlpatterns = patterns('',
    (r'^my_example/', include('my_example.urls')),
)
