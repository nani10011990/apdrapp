from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getallfactors',views.get_mtc_factors,name='get_mtc_factors'),
    path('deptlist',views.get_departments_list,name='get_departments_list'),
    path('mtcdeductable',views.mtc_deductable_factor,name='mtc_deductable_factor'),
    path('getusicquotedetails',views.get_all_data_for_usic,name="get_all_data_for_usic"),
    path('mtclimit',views.mtc_cargo_factor,name="mtc_cargo_factor"),
    path('lossratio',views.get_loss_ratio,name="get_loss_ratio"),
    path('fleetfactor',views.mtc_fleet_factor,name="mtc_fleet_factor"),
    path('getallcommod',views.mtc_get_commodities_by_quote_id,name="mtc_get_commodities_by_quote_id"),
    path('basrateid',views.get_base_rate_by_quote_id,name="get_base_rate_by_quote_id"),
    path('mtcyearsoexp',views.mtc_years_of_experience,name="mtc_years_of_experience"),
    path('rmfmtccal',views.rmf__mtc_calculations,name="rmf__mtc_calculations")
    
     
]