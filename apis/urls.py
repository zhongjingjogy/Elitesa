from django.conf.urls import include, url
import apis.views

urlpatterns = [
    url(r'^news_list$', apis.views.news_list),
]
