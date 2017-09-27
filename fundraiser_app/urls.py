from django.conf.urls import url
from fundraiser_app import views

urlpatterns = [
    url(r'^$', views.FMItemListView.as_view(), name='fmitem_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^fmitem/(?P<pk>\d+)$', views.FMItemDetailView.as_view(), name='fmitem_detail'),
    url(r'^fmitem/new$', views.FMItemCreateView.as_view(), name='fmitem_new'),
    url(r'^fmitem/(?P<pk>\d+)/edit$', views.FMItemUpdateView.as_view(), name='fmitem_edit'),
    url(r'^fmitem/(?P<pk>\d+)/remove$', views.FMItemDeleteView.as_view(), name='fmitem_remove'),
    url(r'^fmitem/(?P<pk>\d+)/publish/$', views.fmitem_publish, name='fmitem_publish'),
]
