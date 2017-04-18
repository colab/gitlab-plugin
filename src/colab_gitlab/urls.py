
from django.conf.urls import patterns, url
from django.views.defaults import permission_denied

from .views import GitlabProxyView

urlpatterns = patterns(
    '',
    # Gitlab URLs
    url(r'^profile$', permission_denied, name='gitlab_profile'),
    url(r'^(?P<path>.*)$', GitlabProxyView.as_view(), name='gitlab'),
)
