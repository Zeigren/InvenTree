"""
Top-level URL lookup for InvenTree application.

Passes URL lookup downstream to each app as required.
"""


from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from build.api import build_api_urls
from build.urls import build_urls
from common.api import common_api_urls
from common.urls import common_urls
from company.api import company_api_urls
from company.urls import company_urls, price_break_urls, supplier_part_urls
from order.api import po_api_urls
from order.urls import order_urls
from part.api import bom_api_urls, part_api_urls
from part.urls import part_urls
from qr_code import urls as qr_code_urls
from rest_framework.documentation import include_docs_urls
from stock.api import stock_api_urls
from stock.urls import stock_urls
from users.urls import user_urls

from .views import (
    DatabaseStatsView,
    EditUserView,
    IndexView,
    InfoView,
    SearchView,
    SetPasswordView,
    SettingsView,
)

admin.site.site_header = "InvenTree Admin"

apipatterns = [
    url(r"^common/", include(common_api_urls)),
    url(r"^part/", include(part_api_urls)),
    url(r"^bom/", include(bom_api_urls)),
    url(r"^company/", include(company_api_urls)),
    url(r"^stock/", include(stock_api_urls)),
    url(r"^build/", include(build_api_urls)),
    url(r"^po/", include(po_api_urls)),
    # User URLs
    url(r"^user/", include(user_urls)),
    # InvenTree information endpoint
    url(r"^$", InfoView.as_view(), name="inventree-info"),
]

settings_urls = [
    url(
        r"^user/?",
        SettingsView.as_view(template_name="InvenTree/settings/user.html"),
        name="settings-user",
    ),
    url(
        r"^currency/?",
        SettingsView.as_view(template_name="InvenTree/settings/currency.html"),
        name="settings-currency",
    ),
    url(
        r"^part/?",
        SettingsView.as_view(template_name="InvenTree/settings/part.html"),
        name="settings-part",
    ),
    url(
        r"^other/?",
        SettingsView.as_view(template_name="InvenTree/settings/other.html"),
        name="settings-other",
    ),
    # Catch any other urls
    url(
        r"^.*$",
        SettingsView.as_view(template_name="InvenTree/settings/user.html"),
        name="settings",
    ),
]

urlpatterns = [
    url(r"^part/", include(part_urls)),
    url(r"^supplier-part/", include(supplier_part_urls)),
    url(r"^price-break/", include(price_break_urls)),
    url(r"^common/", include(common_urls)),
    url(r"^stock/", include(stock_urls)),
    url(r"^company/", include(company_urls)),
    url(r"^order/", include(order_urls)),
    url(r"^build/", include(build_urls)),
    url(r"^auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^login/", auth_views.LoginView.as_view(), name="login"),
    url(
        r"^logout/",
        auth_views.LogoutView.as_view(template_name="registration/logout.html"),
        name="logout",
    ),
    url(r"^settings/", include(settings_urls)),
    url(r"^edit-user/", EditUserView.as_view(), name="edit-user"),
    url(r"^set-password/", SetPasswordView.as_view(), name="set-password"),
    url(r"^admin/", admin.site.urls, name="inventree-admin"),
    url(r"^qr_code/", include(qr_code_urls, namespace="qr_code")),
    url(r"^index/", IndexView.as_view(), name="index"),
    url(r"^search/", SearchView.as_view(), name="search"),
    url(r"^stats/", DatabaseStatsView.as_view(), name="stats"),
    url(r"^api/", include(apipatterns)),
    url(r"^api-doc/", include_docs_urls(title="InvenTree API")),
    url(r"^markdownx/", include("markdownx.urls")),
]

# Static file access
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # Media file access
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Send any unknown URLs to the parts page
urlpatterns += [
    url(r"^.*$", RedirectView.as_view(url="/index/", permanent=False), name="index")
]
