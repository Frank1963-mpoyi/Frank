
#from django.conf import settings 
#from django.conf.urls.static import static
from django.urls import path
#from mitongo.views import Restaurant_Create, Restaurant_take, Restaurant_Update
from mitongo.views import *


app_name = 'mitongo'
urlpatterns = [
    path('exercise', exercise_frontend),
    path('<int:pk>/retreive', mpoyi_retreive, name='mpoyi_retreive'),
    path('<int:pk>/update',  Restaurant_Update, name ='Restaurant'),
    path('create', Restaurant_Create, name = 'create_view' ),
    path('mpoyi', registerPage, name = 'login'),
    path('loginpage', loginPage, name ='loginPage'),
    path('', Restaurant, name = 'Restaurant'),
    path('<int:pk>',RestaurantListView.as_view(), name ='Restaurant_Update'),
    path('<int:pk>/detail',RestaurantDetail.as_view() , name ='Restaurant_take'),
    path('<int:pk>/delete', RestaurantDelete.as_view(), name = 'Restaurant_Create'),
    path('<int:pk>/update', RestaurantUpdate.as_view(), name ='RestaurantUpdate'),
    path('<int:pk>/create', RestaurantCreate.as_view(), name ='RestaurantCreate'),
]

#urlpatterns = urlpatterns + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# review please 