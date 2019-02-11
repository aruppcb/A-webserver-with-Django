from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^hsc$', display_HSC, name="display_HSC"),
    url(r'^ppc', display_PPC, name="display_PPC"),
    url(r'^bidopt', display_Bidopt, name="display_Bidopt"),

    url(r'^add_hsc$', add_HSC, name="add_HSC"),
    url(r'^add_ppc$', add_PPC, name="add_PPC"),
    url(r'^add_bidopt$', add_Bidopt, name="add_Bidopt"),

    url(r'^hsc/edit_item/(?P<pk>\d+)$', edit_HSC, name="edit_HSC"),
    url(r'^ppc/edit_item/(?P<pk>\d+)$', edit_PPC, name="edit_PPC"),
    url(r'^bidopt/edit_item/(?P<pk>\d+)$', edit_Bidopt, name="edit_Bidopt"),

    url(r'^hsc/delete/(?P<pk>\d+)$', delete_HSC, name="delete_HSC"),
    url(r'^ppc/delete/(?P<pk>\d+)$', delete_PPC, name="delete_PPC"),
    url(r'^bidopt/delete/(?P<pk>\d+)$', delete_Bidopt, name="delete_Bidopt")

]