from django.conf.urls import url
from django.urls import path
from blogapp.views import blog_list,blog_detail,log_in,sign_up,new_post,delete_post,edit_post,log_out,comment
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogapp'

urlpatterns = [
	path('',blog_list,name = 'blog_list'),
	path('<int:post_id>',blog_detail,name = 'blog_detail'),
	path('log_in',log_in,name='log_in'),
	path('sign_up',sign_up,name='sign_up'),
	path('new_post',new_post,name='new_post'),
	path('<int:post_id>/comment/',comment,name='comment'),
	path('<int:post_id>/edit_post/',edit_post,name='edit_post'),
	path('<int:post_id>/delete_post/',delete_post,name='delete_post'),
	path('logout',log_out,name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
