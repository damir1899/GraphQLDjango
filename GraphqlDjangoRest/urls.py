from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers, permissions
from api_main.views import CategoryViewSet, PostViewSet


schema_view = get_schema_view(
    openapi.Info(
        title='Slug Product API',
        default_version='v1',
        description='API documentation for Slug Product',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(
            name='Damir',
            email='damin_99.99@mail.ru',
            url='https://github.com/damir1899'),
        license=openapi.License(
            name='BSD License'
        )
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
        # permissions.IsAuthenticated,
        # permissions.IsAdminUser
    ]
)

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'post', PostViewSet)

urlpatterns = [
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema_redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger_ui'),
    path('graphql/', include('graphql_main.urls')),
    path('api/', include(router.urls)), 
    path('', admin.site.urls),
    path('redoc/', include('django.contrib.admindocs.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)