from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
      
     
    path('getfmcsafactor',views.get_usic_fmcsa_factor,name='get_usic_fmcsa_factor'),
    path('getaldeductiblefactor',views.get_usic_al_deductible_factor,name='get_usic_al_deductible_factor'),
    path('commissiontier',views.get_usic_commission_tier,name='get_usic_commission_tier'),
    path('getfleetfactor',views.get_usic_fleet_factor,name='get_usic_fleet_factor'),
    
    path('usicstatezone',views.get_usic_state_zone_regional_factor,name='get_usic_state_zone_regional_factor'),
    path('hiredauto',views.get_hired_auto,name='get_hired_auto'),
    path('getlobsviews',views.get_lobs_views,name='get_lobs_views'),
    path('getusicfactorsall',views.get_usic_factors,name='get_usic_factors'),
    path('rmfcalculation',views.rmf_calculations,name='rmf_calculations'),
 
   
  
    path('getYearsOfexpFactors',views.get_usic_years_of_experience_factor,name='get_usic_years_of_experience_factor'),
    path('getfactorsaferbyid',views.get_usic_safer_factor,name='get_usic_safer_factor'),
    path('getusicstatecitybyzipcode',views.get_usic_state_city_by_zipcode,name='get_usic_state_city_by_zipcode'),
    path('getnoofunitsinsvehicles',views.get_no_of_units_ins_vehicles,name='get_no_of_units_ins_vehicles'),
    path('getusicstate',views.get_usic_state_factor,name='get_usic_state_factor'),
    path('umpremium',views.get_um_premium,name='get_um_premium'),
    path('getumlimit',views.get_um_limit,name='get_um_limit'),
    path('getlossratio',views.get_loss_ratio,name='loss_ratio'),
    path('getusicpiplimit',views.get_usic_pip_limit,name='get_usic_pip_limit'),
    #SN AL RATERS FROM HERE ---------------------------------------------------------------------------------------------------------------------------------
    path('getsnlocalintermediate',views.get_sn_local_intermediate,name='get_sn_local_intermediate'),
    path('getratebyorgcode',views.get_rate_by_org_code,name='get_rate_by_org_code'),
    path('getvehiclefactors',views.get_vehicle_factor_by_weight_and_model,name='get_vehicle_factor_by_weight_and_model'),
    path('getdatabyzipcode',views.get_data_by_zip_code,name='get_data_by_zip_code'),
    path('gethighlanderaldeductiblefactor',views.get_highlander_al_deductible_factor,name='get_highlander_al_deductible_factor'),
    path('getrangevalidationhighlanderpollution',views.get_range_validation_highlander_pollution_factor,name='get_range_validation_highlander_pollution_factor'),
    path('gethighlanderalsaferfactor',views.get_highlander_al_safer_factor,name='get_highlander_al_safer_factor'),
    path('al_um_premium', views.get_al_um_premium, name ='get_al_um_premium'),
    path('al_uim_premium', views.get_al_uim_premium, name ='get_al_uim_premium'),
    path('getpremuim',views.hired_auto_premium_cost,name = 'hired_auto_premium_cost'),
#From here APD Raters starts----------------------------------------------------------------------------------------------------------------
    path('getusicquotedetails',views.get_all_data_for_usic,name="get_all_data_for_usic"),
    path('getyrsofexp',views.get_yrs_of_exp,name='get_yrs_of_exp'),
    path('getbrokerfee',views.apd_broker_fee,name = 'apd_broker_fee'),
    path('gettowingcharges',views.apd_towing_charges,name = 'apd_towing_charges'),
    path('getapdlossfrequency',views.get_apd_loss_ratio_factor,name='get_apd_loss_ratio_factor'),
    path('getapdtotalincurredfactor',views.get_apd_total_incurred_factor,name='get_apd_total_incurred_factor'),
    path('calculatedriverfactor',views.calculate_driver_factor,name='calculate_driver_factor'),
    path('getapdbaseratefactor',views.get_apd_base_rate_factor,name='get_apd_base_rate_factor'),
    path('getapdrallfactors',views.get_apdr_factors,name='get_apdr_factors'),
    path('getapddeductiblefactor',views.get_apd_deductible_factor,name='get_apd_deductible_factor'),
    path('getapdstatefactor',views.get_apd_state_factor,name='get_apd_state_factor'),
    path('apdrmfcalculations',views.apd_rmf_calculations,name='apd_rmf_calculations'),
    path('getapdradiusfactor',views.get_apd_radius_factor,name='get_apd_radius_factor'),
    path('gettivfactor',views.get_apd_tiv_factor,name='get_tiv_factor'),
    path('getabrfactor',views.apd_abr_calculations,name = 'apd_abr_calculations')

]