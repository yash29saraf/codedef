from django.conf.urls import url,include
from googform.views import yourself,recorded,contacts

urlpatterns = [
	url(r'^yourself/$',yourself),
	url(r'^recorded/$',recorded),
	url(r'^contacts/$',contacts),
	#url(r'^admin/', admin.site.urls),
]
