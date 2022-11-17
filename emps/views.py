import collections
from unittest import result
from django.shortcuts import render
# Create your views here.
from email import message
from django.shortcuts import render
from os import name
from django.shortcuts import render
from django.shortcuts import render
from django.template import Context, loader
from rest_framework import generics
from .models import *
import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import json
from datetime import datetime
from django.http import JsonResponse
from fpdf import FPDF 
from .premiumcalculation import *
from django.conf import settings
from django.core.files import File
from django.http import FileResponse
from .dboperations import      add_apdr_factors_db, get_all_lobs, get_apd_base_rate_factor_json, get_apd_broker_fee, get_apd_data_for_incurred_factor_db, get_apd_deductible_factor_json, get_apd_lossratio_by_quote_id_coverage_db, get_apd_radius_factor_db, get_apd_state_factor_json, get_apd_tiv_factor_db, get_apd_towing_charges, get_apdr_factors_db, get_current_approval_db, get_data_by_zip_code_db, get_highlander_al_safer_factor_json, get_highlander_auto_hired, get_hired_auto_db, get_ins_highlander_al_deductible_factor, get_ins_quotes_json_data_by_quote_id, get_lcm_usic_factor_db, get_lossratio_by_quote_id_coverage_db, get_no_of_units_ins_vehicles_db, get_primary_usic_factor, get_range_from_ins_highlander_pollution_factor_json, get_rate_by_org_code_db, get_sn_local_intermediate_db, get_sum_of_statedamount_by_quoteid_json, get_udf_al_uim_premium_db, get_udf_al_um_premium_db, get_udf_get_al_base_rate_zone_by_state_json, get_um_limit_db,   get_usic_al_deductible_factor_db, get_usic_commission_tier_db, get_usic_factors_db, get_usic_fleet_factor_db, get_usic_fmcsa_factor_db, get_usic_hired_auto_premium_db, get_usic_ilf_factor_db, get_usic_liability_limit_factor_db, get_usic_pip_limit_db, get_usic_safer_factor_db, get_usic_state_city_by_zipcode_db, get_usic_state_zone_regional_factor_db, get_usic_states_factor_db, get_usic_years_of_experience_factor_db, get_vehicle_factor_by_weight_and_model_db, get_yrs_of_exp_db, ins_approvals_post
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

 

@api_view(['POST'])
def get_usic_years_of_experience_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    
    
    _id=data["_id"]

    years_of_business_factor=get_usic_years_of_experience_factor_db(_id)
    print(years_of_business_factor,"the business")
 
    res=years_of_business_factor
     

    data = {"result": res}
    #data = {"result": res,"result2":res1,"result3":res2,"result3":res3,"result4":res4,"result5":res5}

     
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_usic_safer_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    
    
    safer_id=data["safer_id"]
    quote_id=data["quote_id"]
    #quote_id=data["quote_id"]
    #d=get_usic_safer_factor_db(safer_id,quote_id)
    #safer_factor_val=d["factor"]
    #safer_description=d["description"]


    if safer_id==4 :
        d=ins_approvals_post(quote_id,4)
        approval_id=get_current_approval_db(quote_id)
        print(d,"the d value is ")
        print("Manager Approval is required.")
        res={"Manager Approval is required.":d,"Approvals":approval_id}

    else:
        d=get_usic_safer_factor_db(safer_id,quote_id)
        safer_factor_val=d["factor"]
        safer_description=d["description"]
        res={"safer factors result":d}

       
    
    #res2={"safer_description":safer_description,"safer_factor_val":safer_factor_val}
    #res3=approval_id
    #print(years_of_business_factor[0][0],"the safer factor")
    data = {"Result":res}
    #data = {"result": res,"result2":res1,"result3":res2,"result3":res3,"result4":res4,"result5":res5}

     
    return Response(data, status=status.HTTP_200_OK)

   
    


@api_view(['POST'])
def get_usic_al_deductible_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    
    
    al_deductible=data["al_deductible"]
    data_al_deductible=get_usic_al_deductible_factor_db(al_deductible)
    #print(years_of_business_factor[0][0],"the safer factor")
    res=data_al_deductible
     
 

    data = {"result": res}
    
    #data = {"result": res,"result2":res1,"result3":res2,"result3":res3,"result4":res4,"result5":res5}

     
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_usic_fmcsa_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    
    yrs_in_business_id=data["yrs_in_business_id"]
    alert_id=data["alert_id"]
     
    fmcsa_factors=get_usic_fmcsa_factor_db(yrs_in_business_id,alert_id)
 
    res=fmcsa_factors
     
 

    data = {"result": res}
    
     

     
    return Response(data, status=status.HTTP_200_OK) 

@api_view(['POST'])
def get_usic_commission_tier(request):
    data = json.loads(request.body.decode("utf-8"))
    
    #tier=data["_tier"]
    _id=data["years_of_exp_id"]
    unit_price=data["unit_price"]
    unit_price=int(unit_price)
    
 
    
     
  
    years_of_business_factor=get_usic_years_of_experience_factor_db(_id)
    #print(years_of_business_factor["tier"],"the tier is ")

    if unit_price>9500 and years_of_business_factor["tier"]=='B':
        tier='B'
        commission_tier_usic=get_usic_commission_tier_db(tier)
 
       
    elif unit_price>9500  :
        tier='B'
        commission_tier_usic=get_usic_commission_tier_db(tier)
        # unit_price<9500 and years_of_business_factor["tier"]!='B':
    else:
        tier='A'
        commission_tier_usic=get_usic_commission_tier_db(tier)
    
    res=commission_tier_usic
    #res=commission_tier_usic2

    data = {"result": res}
    
    

     
    return Response(data, status=status.HTTP_200_OK) 


@api_view(['POST'])
def get_usic_fleet_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    
    no_of_units=data["no_of_units"]
    if no_of_units<10 and 0<no_of_units:
        _id=1

        fleet_factor=get_usic_fleet_factor_db(_id)
    
    elif  no_of_units>10 and no_of_units<9999:
         _id=2
         fleet_factor=get_usic_fleet_factor_db(_id)

    res=fleet_factor

    data = {"result": res}    

     
    return Response(data, status=status.HTTP_200_OK) 

@api_view(['POST'])
def get_usic_liability_limit_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    
    liability_usic_limit=data["liability_limit"]
     
     
    liability_limit_factor=get_usic_liability_limit_factor_db(liability_usic_limit)
 
    res=liability_limit_factor    

    data = {"result": res}
     
    return Response(data, status=status.HTTP_200_OK) 


@api_view(['POST'])
def get_hired_auto(request):
    data = json.loads(request.body.decode("utf-8"))

    id=data["id"]
    basis=data["basis"]
    cost_of_hire=data["cost_of_hire"]
    limit=data["liability_limit"]
    no_of_units=data["no_of_units"]
    print(id,basis,cost_of_hire,limit,no_of_units,"all data")

    _total_premium=get_usic_hired_auto_premium_db(id,basis,cost_of_hire,limit)
    print(_total_premium,"_total_premium values")

    min_units =_total_premium["min_units"]
    print(min_units,"min_unitsmin_units")
    max_units =_total_premium["max_units"]
    per_unit =_total_premium["per_unit"]
    min_premium =_total_premium["min_premium"]
     
    if limit==1000000 and no_of_units>min_units and no_of_units<=max_units:
        id=id
        total_premium=no_of_units*per_unit
    elif limit==750000 and no_of_units>min_units and no_of_units<=max_units:
        id=id
        total_premium=no_of_units*per_unit
    
    elif limit==1000000 and no_of_units>min_units and no_of_units<=max_units:
        total_premium=no_of_units*per_unit
    elif limit==750000 and no_of_units>min_units and no_of_units<=max_units:
        total_premium=no_of_units*per_unit
     
    if total_premium<=min_premium:
        total_premium=min_premium
    
    hired_auto=total_premium
 
    res=hired_auto    

    data = {"hired_auto_premium": res}
     
    return Response(data, status=status.HTTP_200_OK) 

@api_view(['POST'])
def get_usic_state_city_by_zipcode(request):
    data = json.loads(request.body.decode("utf-8"))
    zipcode=data["zipcode"]
    print(zipcode,"the zipcode")
    state_city=get_usic_state_city_by_zipcode_db(zipcode)
    print(state_city," is ")
    print(state_city["state"],"the state is ")
    res=state_city
    data={"result":res}
    return Response(data, status=status.HTTP_200_OK) 

@api_view(['POST'])
def get_usic_state_zone_regional_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    zipcode=data["zipcode"]
    state_by_zipcode=get_usic_state_city_by_zipcode_db(zipcode)
    _state=state_by_zipcode["state"]
    print(_state,"the stae value is _state ")
    
    #_state=data["_state"]

    state_zone=get_usic_state_zone_regional_factor_db(_state)
    res=state_zone    

    data = {"result": res}
     
    return Response(data, status=status.HTTP_200_OK) 

@api_view(['POST'])
def get_usic_state_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    zipcode=data["zipcode"]
    state_by_zipcode=get_usic_state_city_by_zipcode_db(zipcode)
    _state=state_by_zipcode["state"]
    print(_state,"the stae value is _state ")
    
    #_state=data["_state"]

    state=get_usic_states_factor_db(_state)
    res=state    

    data = {"result": res}
     
    return Response(data, status=status.HTTP_200_OK) 
    

@api_view(['POST'])
def get_no_of_units_ins_vehicles(request):
    data = json.loads(request.body.decode("utf-8"))
    quoteid=data["quoteid"]
 
    count=get_no_of_units_ins_vehicles_db(quoteid)
    res=count
    data={"result":res}
    return Response(data, status=status.HTTP_200_OK) 


@api_view(['GET'])
def get_um_premium(request):
    data = json.loads(request.body.decode("utf-8"))
    zipcode=data["zipcode"]
    state_by_zipcode=get_usic_state_city_by_zipcode_db(zipcode)
    limit=data["limit"]
    state=state_by_zipcode["state"]
    quoteid=data["quoteid"]
    #no_of_units = data["no_of_units"]
    um_limit=get_um_limit_db(state,limit)
    count=get_no_of_units_ins_vehicles_db(quoteid)
    um_premium=um_limit * count
    data={"um_premium":um_premium}

    return   Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_um_limit(request):
    data = json.loads(request.body.decode("utf-8"))
    limit=data["limit"]
    state=data["state"]
    quoteid = data["quoteid"]
    #no_of_units = data["no_of_units"]
    no_of_units =data["no_of_units"]
    res=get_um_limit_db(state,limit,no_of_units)

    return   Response(res, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_loss_ratio(request):
    data = json.loads(request.body.decode("utf-8"))
    
    _quote_id=data['quote_id']
    #_coverage=data['coverage']
    
    


    b=get_lossratio_by_quote_id_coverage_db(_quote_id,1)
    c=[]
    if len(b)>0:
        c=1.20
    else:
        c=1
        
    
    
    res={"LOSS_RATIO":c}

    
    for i in b:
        if i['loss_ratio']>35:
            
          d=ins_approvals_post(_quote_id,1)

    
    
    return   Response({"result":res}) 

@api_view(['POST'])
def get_base_rate_of_ins_al_base_rate(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    data = json.loads(request.body.decode("utf-8"))
    zip_code = data['zip_code']
    
    state = get_usic_state_city_by_zipcode_db(zip_code)
    
    base_rate_obj = get_udf_get_al_base_rate_zone_by_state_json(state[0]['state'])
    base_rate = []
    final_data = {
        "state":state[0]['state'],
        "baserate_zone": base_rate_obj
    }
    base_rate.append(final_data)

    return Response(base_rate, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_usic_pip_limit(request):
    data = json.loads(request.body.decode("utf-8"))
    
    zipcode=data["zipcode"]
    state_city=get_usic_state_city_by_zipcode_db(zipcode)
    limit=data["limit"]
    state=state_city["state"]

    usic_pip=get_usic_pip_limit_db(state,limit)
    print(usic_pip,"Per_unit_price")
 
    res=usic_pip
     

    data = {"Result": res}
    #data = {"result": res,"result2":res1,"result3":res2,"result3":res3,"result4":res4,"result5":res5}

     
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def rmf_calculations(request):
    
    data = json.loads(request.body.decode("utf-8"))
    years_of_business=data["years_of_exp_id"]
    safer_id=data["safer_id"]
    al_deductible=data["al_deductible"]
    yrs_in_business_id=data["yrs_in_business_id"]
    
    alert_id=data["alert_id"]
    _state=data["_state"]
    liability_usic_limit=data["liability_limit"]

    no_of_units=data["no_of_units"]  #for fleet policy

    #for commission tier
     
 

    #constant value for uw_credit_debit_factor
    uw_credit_debit_factor=data["uw_credit_debit_factor"]

    years_of_business_factor=get_usic_years_of_experience_factor_db(years_of_business)
    safer_factor_val=get_usic_safer_factor_db(safer_id)
    data_al_deductible=get_usic_al_deductible_factor_db(al_deductible)
    fmcsa_data=get_usic_fmcsa_factor_db(yrs_in_business_id,alert_id)
    state_zone_data=get_usic_state_zone_regional_factor_db(_state)
    liability_limit_usic_factor=get_usic_liability_limit_factor_db(liability_usic_limit)
     
 
    years_experience_factor=years_of_business_factor["years_experience_factor"]
    safer_factor=safer_factor_val["safer_factor"]
    safer_descrption=safer_factor_val["descrption"]
 
    al_deductible_factor=data_al_deductible["al_deductible_factor"]
    al_deductible_description=data_al_deductible["al_deductible"]
    fmcsa_factor=fmcsa_data["fmcsa_factor"]
    state_zone_factor=state_zone_data["state_zone_factor"]
    #liability_usic_factor=liability_limit_factor["liability_factor"]
    #fleet factor
    if no_of_units<10 and 0<no_of_units:
        _id=1

        fleet_factor_data=get_usic_fleet_factor_db(_id)
    
    elif  no_of_units>10 and no_of_units<9999:
         _id=2
         fleet_factor_data=get_usic_fleet_factor_db(_id)

    fleet_factor=fleet_factor_data 
   # print(fleet_factor,"the res value is ")


    #end fleet factor

    #commission tier need to enter years_of _exp and unit price
    

    ilf_factor=get_usic_ilf_factor_db()
    lcm_factor=get_lcm_usic_factor_db()
    primary_factor=get_primary_usic_factor()
    
    
   
    rmf_factors=calculate_rmf_premium( years_experience_factor,safer_factor,al_deductible_factor,ilf_factor,lcm_factor,primary_factor,
   
    fmcsa_factor,state_zone_factor,liability_limit_usic_factor,fleet_factor,uw_credit_debit_factor)
    rmf_factors=rmf_factors
    usr=usic_factor_modals(years_experience_factor,safer_factor,al_deductible_factor,ilf_factor,lcm_factor,primary_factor,
    fmcsa_factor,state_zone_factor,liability_limit_usic_factor,fleet_factor,uw_credit_debit_factor,rmf_factors)
    add_all_usic_factors=add_usic_factors_db(usr)
    print(add_all_usic_factors,"the add_all_usic_factors factors")
 
    data={"rmf_calculation":rmf_factors}


    return Response(data, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_lobs_views(request):
    res=get_all_lobs()
    data={"result":res}
    print(data,"the backend values are ")

    return   Response(data, status=status.HTTP_200_OK) 


@api_view(['GET'])
def get_usic_factors(request):
    res=get_usic_factors_db()
    data={"result":res}

    return   Response(data, status=status.HTTP_200_OK) 
 
#SN AL RATERS FROM HERE ---------------------------------------------------------------------------------------------------------------------------------

@api_view(['POST'])
def get_sn_local_intermediate(request):
    data = json.loads(request.body.decode("utf-8"))
    
    
    radius=data["radius"]
    category=data["category"]
    base_rate=get_sn_local_intermediate_db(radius,category)
    #print(years_of_business_factor[0][0],"the safer factor")
    res=base_rate
    data = {"Base Rate": res}
    #data = {"result": res,"result2":res1,"result3":res2,"result3":res3,"result4":res4,"result5":res5}
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_rate_by_org_code(request):
    data = json.loads(request.body.decode("utf-8"))
    _zipcode=data['zip']
    _destination=data['destination']
    zone_destination=get_data_by_zip_code_db(_zipcode)
    print(zone_destination,"the zone_destination")
    _origination_zone_code=int(zone_destination['originating_zone_code'])
    print("_origination_zone_code",_origination_zone_code)
    
    _id=get_rate_by_org_code_db(_origination_zone_code,_destination)

    return   Response({"Result":_id}) 

#correction needs to be done in the data base function-------------------------------------------------------------------
@api_view(['POST'])
def get_vehicle_factor_by_weight_and_model(request):
    data = json.loads(request.body.decode("utf-8"))

    _weight=data['weight']
    _model=data['model']
    _radius=data['radius']
    c=[]
    
   
    
    b=get_vehicle_factor_by_weight_and_model_db(_weight,_model)
    if len(b)>0:
        if _radius==1:
            c=b[0]['factor_48_states']
        elif _radius==2:
            c=b[0]['factor_local_int']

        else:
            c=("Radius entered is invalid")
        
    else:
        c=("Entered Weight input is not allowed with "+ _model)
    
    
    res={"factor":c}
    
    return   Response({"data":res})  
#----------------------------------------------------------------------------------------------------------------

@api_view(['POST'])
def get_data_by_zip_code(request):
    data = json.loads(request.body.decode("utf-8"))
    _zipcode=data['zip']
   
  
    
    _id=get_data_by_zip_code_db(_zipcode)
    res={"Data from entered zipcode":_id}
    
    return   Response({"Done":res}) 

@api_view(['POST'])
def get_highlander_al_deductible_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    deductible = data['deductible']

    factor = get_ins_highlander_al_deductible_factor(deductible)

    return Response(factor,status=status.HTTP_200_OK)

#not valid Pollution Factor API---------------------------------------------
@api_view(['POST'])
def get_range_validation_highlander_pollution_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    range = data['range']
    description = data['description']
    validation = get_range_from_ins_highlander_pollution_factor_json(description,range)
    
    return Response(validation,status=status.HTTP_200_OK)

#---------------------------------------------------------------

@api_view(['POST'])
def get_highlander_al_safer_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    description = data['description']

    factor = get_highlander_al_safer_factor_json(description)

    return Response(factor,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_al_um_premium(request):
    data = json.loads(request.body.decode("utf-8"))
    limit=data["limit"]
    no_of_units=data["no_of_units"]
    res = get_udf_al_um_premium_db(limit,no_of_units)
    data={"result":res}
    return   Response(res, status=status.HTTP_200_OK) 


@api_view(['GET'])
def get_al_uim_premium(request):
    data = json.loads(request.body.decode("utf-8"))
    limit=data["limit"]
    no_of_units=data["no_of_units"]
    res = get_udf_al_uim_premium_db(limit,no_of_units)
    return   Response(res, status=status.HTTP_200_OK)

@api_view(['POST'])
def hired_auto_premium_cost(request):
   
    req_data = json.loads(request.body.decode("utf-8"))
    limit = req_data["limit"]
    units_num = req_data["no_units"]
    coh = req_data["coh"]
    
   
    db_data  = get_highlander_auto_hired()
    res =db_data
    for i in res:
        if (limit == i['highlander_hired_auto_limit']):
            print(i)
            rate_per_m = i['highlander_hired_auto_per_m']
            #min_prem = i["highlander_hired_auto_min_prem"]
            ilf = i["highlander_hired_auto_ilf"]
    
    coh_per_unit = coh/units_num
    if(coh_per_unit <500):
        coh_per_unit =500
    Rate = (coh_per_unit/100)* rate_per_m * ilf
    
    premium = Rate * units_num

    data = {"Rate":round(Rate,3) ,"Total Premuim" :round(premium)}
    return Response(data, status=status.HTTP_200_OK)  

@api_view(['POST'])
def SN_rmf_calculations(request):
    
    data = json.loads(request.body.decode("utf-8"))
    radius=data["radius"]
    category=data["category"]
    base_rate=get_sn_local_intermediate_db(radius,category)
    al_deductible=data["al_deductible"]
    yrs_in_business_id=data["yrs_in_business_id"]
    
    alert_id=data["alert_id"]
    _state=data["_state"]
    liability_usic_limit=data["liability_limit"]

    no_of_units=data["no_of_units"]  #for fleet policy

    #for commission tier
     
 

    #constant value for uw_credit_debit_factor
    uw_credit_debit_factor=data["uw_credit_debit_factor"]


    data_al_deductible=get_usic_al_deductible_factor_db(al_deductible)
    fmcsa_data=get_usic_fmcsa_factor_db(yrs_in_business_id,alert_id)
    state_zone_data=get_usic_state_zone_regional_factor_db(_state)
    liability_limit_usic_factor=get_usic_liability_limit_factor_db(liability_usic_limit)
     
 
    years_experience_factor=years_of_business_factor["years_experience_factor"]

 
    al_deductible_factor=data_al_deductible["al_deductible_factor"]
    fmcsa_factor=fmcsa_data["fmcsa_factor"]
    state_zone_factor=state_zone_data["state_zone_factor"]
    #liability_usic_factor=liability_limit_factor["liability_factor"]
    #fleet factor
    if no_of_units<10 and 0<no_of_units:
        _id=1

        fleet_factor_data=get_usic_fleet_factor_db(_id)
    
    elif  no_of_units>10 and no_of_units<9999:
         _id=2
         fleet_factor_data=get_usic_fleet_factor_db(_id)

    fleet_factor=fleet_factor_data 
   # print(fleet_factor,"the res value is ")


    #end fleet factor

    #commission tier need to enter years_of _exp and unit price
    

    ilf_factor=get_usic_ilf_factor_db()
    lcm_factor=get_lcm_usic_factor_db()
    primary_factor=get_primary_usic_factor()
    
    
   
    rmf_factors=calculate_rmf_premium( years_experience_factor,safer_factor,al_deductible_factor,ilf_factor,lcm_factor,primary_factor,
   
    fmcsa_factor,state_zone_factor,liability_limit_usic_factor,fleet_factor,uw_credit_debit_factor)
    rmf_factors=rmf_factors
    usr=usic_factor_modals(years_experience_factor,safer_factor,al_deductible_factor,ilf_factor,lcm_factor,primary_factor,
    fmcsa_factor,state_zone_factor,liability_limit_usic_factor,fleet_factor,uw_credit_debit_factor,rmf_factors)
    add_all_usic_factors=add_usic_factors_db(usr)
    print(add_all_usic_factors,"the add_all_usic_factors factors")
 
    data={"rmf_calculation":rmf_factors}


    return Response(data, status=status.HTTP_200_OK)

#From here APD Raters starts----------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
def get_yrs_of_exp(request):
    data = json.loads(request.body.decode("utf-8"))
    years_id = data["years_id"]
    res  = get_yrs_of_exp_db(years_id)
    data={"result":res}
    return   Response(res, status=status.HTTP_200_OK)

@api_view(['POST'])
def apd_broker_fee(request):
   
    req_data = json.loads(request.body.decode("utf-8"))
    pd_premium = req_data["pd_premium"]
   
    db_data  = get_apd_broker_fee(pd_premium)
    res =db_data
    broker_fee = res[0]["apd_broker_fee_fee"]
    data = {"broker_fee": broker_fee }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def apd_towing_charges(request):
   
    data = json.loads(request.body.decode("utf-8"))
    towing_limit = data["towing_limit"]
   
    towing_charges = get_apd_towing_charges(towing_limit)
    res =towing_charges
    print(int(res[0]["apd_towing_charges"]),"the res value is ")
    data = {"towing charges": res }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_apd_loss_ratio_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    
       
    
    _quote_id=data['quote_id']
    print(_quote_id,"the _quote_id is")
    #_coverage=data['coverage']
    b=get_lossratio_by_quote_id_coverage_db(_quote_id,2)
    c=[]
    if len(b)>0:
        c=1.20
    else:
        c=1
    
    res=c
  
    for i in b:
        if i['loss_ratio']>35:
            # 1 is for Liability, for USIC we only have AL
          d=ins_approvals_post(_quote_id,4) 
          print(d,"the approval")
   
    data={"result": res} 
    return   Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_apd_total_incurred_factor(request):
    #
    data = json.loads(request.body.decode("utf-8"))
    
    _quote_id=data['quote_id']

    
    

    c=[]
    d=[]
    
    b=get_apd_data_for_incurred_factor_db(_quote_id,2)
    print(b,type(b),"the values are")

    if b==[]:
        c=1.00

    for i in b:
        d.append(i['total_incurred_amount']/i['units'])
        if i['total_incurred_amount']/i['units']<=50000:
            c.append(1.00)
            if len(c)>1:
                c=1.00

        else:
            c=[1.00,1.05,1.10,1.15]
            break


    res={"a":b,"per unit":d,"Total incurred factor":c}

    return   Response({"result":res})

@api_view(['POST'])
def get_apd_tiv_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    
    _quote_id=data["quote_id"]
    tiv=data["tiv"]
    factor=get_apd_tiv_factor_db(_quote_id,tiv)
    print("the tiv factor is ",factor,type(factor))
    data = {"Factor": factor}
    return Response(data, status=status.HTTP_200_OK)



@api_view(['POST'])
def calculate_driver_factor(request):
    #
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    data = json.loads(request.body.decode("utf-8"))
    _quote_id = data['quote_id']

    get_drivers = get_ins_quotes_json_data_by_quote_id(_quote_id)
    total_drivers_factors = 0

    # print(drivers[0][0]['quote_submit_data']['drivers'])

    drivers = get_drivers[0][0]['quote_submit_data']['drivers']
    print(drivers)
    for driver in drivers:
        initial_driver_factor = 1
        ## Based on Class A experience with experience
        if driver['licenseclasstype'] == "Class A" and int(driver['experience']) < 1:
            initial_driver_factor = 1.75
        elif driver['licenseclasstype'] == "Class A" and int(driver['experience'])  > 1 and int(driver['experience'])  < 2:
            initial_driver_factor = 1.20
        else:
            initial_driver_factor = 1

        ## Based on License State only NY
        if driver['licensestate'] == "NY":
            initial_driver_factor *= 1.25
        else:
            initial_driver_factor *= 1

        ## Based on age
        from datetime import datetime
        dob = datetime.strptime(driver['dob'], '%m/%d/%Y')
        age = int((datetime.today() - dob).days / 365.2425)
        print("Age----",age)
        if age < 22:
            initial_driver_factor *= 1.5
        elif age >= 22 and age < 25:
            initial_driver_factor *= 1.25
        elif age > 68:
            initial_driver_factor *= 1.5
        elif age > 65 and age <= 68:
            initial_driver_factor *= 1.25
        else:
            initial_driver_factor *= 1

        ## Based on Violations (Points)
        driver_score = driver['score']
        if driver_score <= 1:
            initial_driver_factor *=1
        elif driver_score <= 2:
            initial_driver_factor *= 1.05
        elif driver_score <= 3:
            initial_driver_factor *= 1.25
        elif driver_score <= 4:
            initial_driver_factor *= 1.4
        elif driver_score <= 5:
            initial_driver_factor *= 1.55
        elif driver_score <= 6:
            initial_driver_factor *= 1.75
        elif driver_score <= 7:
            initial_driver_factor *= 1.95
        else:
            initial_driver_factor *= 1
        print("0000-----",initial_driver_factor)
        
        total_drivers_factors += initial_driver_factor

    print("Len of Drivers---",len(drivers))
    print("----",total_drivers_factors/len(drivers))
    calculated_driver_factor = total_drivers_factors/len(drivers)
    data={"result":calculated_driver_factor}

    # update_factor = update_calculated_driver_factor_by_quote_id(quote_id, calculated_driver_factor)

    return   Response(data, status=status.HTTP_200_OK) 

@api_view(['POST'])
def get_apd_base_rate_factor(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    data = json.loads(request.body.decode("utf-8"))
    quote_id = data['quote_id']
    
    sum_of_statedamount = get_sum_of_statedamount_by_quoteid_json(quote_id)
    
    factor = get_apd_base_rate_factor_json(sum_of_statedamount['sum'])
    return Response(factor, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_apd_deductible_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    deductible = data['deductible']

    range = get_apd_deductible_factor_json(deductible)

    return Response(range,status=status.HTTP_200_OK)

@api_view(['POST'])
def get_apd_state_factor(request):
    data = json.loads(request.body.decode("utf-8"))
    state = data['state']

    factor = get_apd_state_factor_json(state)

    return Response(factor,status=status.HTTP_200_OK)

@api_view(['POST'])
def get_apd_radius_factor(request):
    req_data = json.loads(request.body.decode("utf-8"))
    radius_id = req_data["radius_id"]
   
    radius_factor  = get_apd_radius_factor_db(radius_id)
    res =radius_factor
 
    data = {"radius factor": res }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def apd_rmf_calculations(request):
    data = json.loads(request.body.decode("utf-8"))
    _quote_id=data['quote_id']
    years_id = data["years_id"]
    radius_id=data["radius_id"]
    uw_debit_credit=data["uw_debit_credit"]
    tiv=data["tiv"]
    deductible = data["deductible"]
    state = data["state"]
#rate control factor---------------------------------------------------------------------------------------------------------
    #rate_control_factor=1
#years of experience ----------------------------------------------------------------------------------------------
    years_experience_val = get_yrs_of_exp_db(years_id)
    years_of_experience_factor=years_experience_val["factor"]
    #years_of_experience_factor=float(years_of_experience_factor)
    print("the years of experience factor are",years_of_experience_factor,type(years_of_experience_factor))
#los ratio factor---------------------------------------------------------------------------------------------------
    b=get_apd_lossratio_by_quote_id_coverage_db(_quote_id,2)
    
    
    c=[]
    
  
    for i in b :
        
        if i['loss_ratio']<=10:
            c.append(1.00)
        elif i['loss_ratio']>10 and i['loss_ratio']<=25:
            c.append(1.05)
        elif i['loss_ratio']>25 and i['loss_ratio']<=50:
            c.append(1.10)
        elif i['loss_ratio']>50 :
            c.append(1.20)
              

    if len(c)>1:
        c=(max(c))
    else:
        pass
    
    print(c,"the array value")
    loss_exp_factor=c
    print(loss_exp_factor,"the loss_exp_factor")
    loss_exp_factor=loss_exp_factor

    print(type(loss_exp_factor),"loss exp factor value",loss_exp_factor)
#total incurred factor -----------------------------------------------------------------


#driver
    get_drivers = get_ins_quotes_json_data_by_quote_id(1000344)
    total_drivers_factors = 0

    # print(drivers[0][0]['quote_submit_data']['drivers'])

    drivers = get_drivers[0][0]['quote_submit_data']['drivers']
    print(drivers)
    for driver in drivers:
        initial_driver_factor = 1
        ## Based on Class A experience with experience
        if driver['licenseclasstype'] == "Class A" and int(driver['experience']) < 1:
            initial_driver_factor = 1.75
        elif driver['licenseclasstype'] == "Class A" and int(driver['experience'])  > 1 and int(driver['experience'])  < 2:
            initial_driver_factor = 1.20
        else:
            initial_driver_factor = 1

        ## Based on License State only NY
        if driver['licensestate'] == "NY":
            initial_driver_factor *= 1.25
        else:
            initial_driver_factor *= 1

        ## Based on age
        from datetime import datetime
        dob = datetime.strptime(driver['dob'], '%m/%d/%Y')
        age = int((datetime.today() - dob).days / 365.2425)
        print("Age----",age)
        if age < 22:
            initial_driver_factor *= 1.5
        elif age >= 22 and age < 25:
            initial_driver_factor *= 1.25
        elif age > 68:
            initial_driver_factor *= 1.5
        elif age > 65 and age <= 68:
            initial_driver_factor *= 1.25
        else:
            initial_driver_factor *= 1

        ## Based on Violations (Points)
        driver_score = driver['score']
        if driver_score <= 1:
            initial_driver_factor *=1
        elif driver_score <= 2:
            initial_driver_factor *= 1.05
        elif driver_score <= 3:
            initial_driver_factor *= 1.25
        elif driver_score <= 4:
            initial_driver_factor *= 1.4
        elif driver_score <= 5:
            initial_driver_factor *= 1.55
        elif driver_score <= 6:
            initial_driver_factor *= 1.75
        elif driver_score <= 7:
            initial_driver_factor *= 1.95
        else:
            initial_driver_factor *= 1
        print("0000-----",initial_driver_factor)
        
        total_drivers_factors += initial_driver_factor

    print("Len of Drivers---",len(drivers))
    print("----",total_drivers_factors/len(drivers))
    calculated_driver_factor = total_drivers_factors/len(drivers)
    driver_factor=calculated_driver_factor
    print(driver_factor,"driver_factor ok")
    print(type(driver_factor),"driver_factor")

#end driver
    c=[]

    d=[]
    
    
    b=get_apd_data_for_incurred_factor_db(_quote_id,2)
    for i in b:
        d.append(i['total_incurred_amount']/i['units'])
        if i['total_incurred_amount']/i['units']<=50000:
            c.append(1.00)
            if len(c)>1:
                c.append(1.00)

        else:
            c=[1.00,1.05,1.10,1.15]
            break

    total_incurred_factor=c[0]
    total_incurred_factor=float(total_incurred_factor)
    print(total_incurred_factor,"total_incurred_factor values are",type(total_incurred_factor))

#base rate-----------------------------------------------------------------------------------------------------------
    sum_of_statedamount = get_sum_of_statedamount_by_quoteid_json(_quote_id)
    
    factor = get_apd_base_rate_factor_json(sum_of_statedamount['sum'])
    base_rate_factor=factor["factor"]
    base_rate_factor=float(base_rate_factor)

    print("base rate values are:",base_rate_factor,type(base_rate_factor))
#Radius factor------------------------------------------------------------------------------------------------------------
    radius_factor_val= get_apd_radius_factor_db(radius_id)
    radius_factor =radius_factor_val["factor"]
    print("the radius factor values are:",radius_factor,type(radius_factor))
#tiv factor---------------------------------------------------------------------------------------------------------------------
    factor_val=get_apd_tiv_factor_db(_quote_id,tiv)
    print("the factor tiv",factor_val)
    tiv_factor=factor_val
    #tiv_factor=float(tiv_factor)
    print("tiv factor",tiv_factor,type(tiv_factor))

    deductible_rate = get_apd_deductible_factor_json(deductible)["rate"]
    print('deductible_rate',deductible_rate)

    state_factor = get_apd_state_factor_json(state)["factor"]
    print("state factor",state_factor)
    
#-----------------------------------------------------------------------------------------------------------------------------

 #   print(base_rate_factor,"base_rate_factor")
    #print(loss_exp_factor,"loss_exp_factor")
 #   print(total_incurred_factor,"total_incurred_factor")
   # print(radius_factor,"radius_factor")
    rmf_factors=loss_exp_factor*total_incurred_factor*driver_factor*radius_factor*years_of_experience_factor*base_rate_factor*rate_control_factor*int(uw_debit_credit)*tiv_factor
    rmf_factors = rmf_factors + deductible_rate +state_factor

    data={"rmf_calculation":rmf_factors}
    print("rmf calculations are",data)


    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_apdr_factors(request):
    res=get_apdr_factors_db()
    data={"result":res}
    return   Response(data, status=status.HTTP_200_OK) 
@api_view(['POST'])
def apd_abr_calculations(request):
    data = json.loads(request.body.decode("utf-8"))
    _quote_id=data['quote_id']
    years_id = data["years_id"]
    radius_id=data["radius_id"]
    uw_debit_credit=data["uw_debit_credit"]
    tiv=data["tiv"]
    deductible = data["deductible"]
    state = data["state"]
    towing_limit = data["towing_limit"]
    #pd_premium = data["pd_premium"]
    rate_control_factor=float(data["rate_control_factor"])
   # print("the quote id is",_quote_id,type(_quote_id),"years id value is ",years_id,type(years_id),"radius id value is",radius_id,type(radius_id),"uw debit credit factor is",uw_debit_credit,type(uw_debit_credit),"tiv value is ",tiv,type(tiv),"deductibel factor is",deductible,type(deductible),"state value is",state,type(state),"the towing limit is",towing_limit,type(towing_limit),"the pd premium",pd_premium,type(pd_premium))

#rate control factor---------------------------------------------------------------------------------------------------------
    #rate_control_factor=1
#years of experience ----------------------------------------------------------------------------------------------
    years_experience_val = get_yrs_of_exp_db(years_id)
    years_of_experience_factor=years_experience_val["factor"]
    #years_of_experience_factor=float(years_of_experience_factor)
    print("the years of experience factor are",years_of_experience_factor,type(years_of_experience_factor))
#los ratio factor---------------------------------------------------------------------------------------------------
    # b=get_apd_lossratio_by_quote_id_coverage_db(_quote_id,2)
    
    # c=[]
    
    # if b==[]:
    #     c=1.00
    # else:
    #     for i in b :
        
    #         if i['loss_ratio']<=10:
    #             c.append(1.00)
    #         elif i['loss_ratio']>10 and i['loss_ratio']<=25:
    #             c.append(1.05)
    #         elif i['loss_ratio']>25 and i['loss_ratio']<=50:
    #             c.append(1.10)
    #         elif i['loss_ratio']>50 :
    #             c.append(1.20)
    #         if len(c)>1:
    #             c=(max(c))
    #         else:
    #             pass
              
    
    # print(c,"the array value")
    loss_ratio= data["loss_ratio"]
    print(loss_ratio,"the loss_ratio")
    loss_exp_factor=float(loss_ratio)
 

    print(type(loss_exp_factor),"loss exp factor value",loss_exp_factor)
#total incurred factor -----------------------------------------------------------------


#driver
    get_drivers = get_ins_quotes_json_data_by_quote_id(1000344)
    total_drivers_factors = 0

    # print(drivers[0][0]['quote_submit_data']['drivers'])

    drivers = get_drivers[0][0]['quote_submit_data']['drivers']
    print(drivers)
    for driver in drivers:
        initial_driver_factor = 1
        ## Based on Class A experience with experience
        if driver['licenseclasstype'] == "Class A" and int(driver['experience']) < 1:
            initial_driver_factor = 1.75
        elif driver['licenseclasstype'] == "Class A" and int(driver['experience'])  > 1 and int(driver['experience'])  < 2:
            initial_driver_factor = 1.20
        else:
            initial_driver_factor = 1

        ## Based on License State only NY
        if driver['licensestate'] == "NY":
            initial_driver_factor *= 1.25
        else:
            initial_driver_factor *= 1

        ## Based on age
        from datetime import datetime
        dob = datetime.strptime(driver['dob'], '%m/%d/%Y')
        age = int((datetime.today() - dob).days / 365.2425)
        print("Age----",age)
        if age < 22:
            initial_driver_factor *= 1.5
        elif age >= 22 and age < 25:
            initial_driver_factor *= 1.25
        elif age > 68:
            initial_driver_factor *= 1.5
        elif age > 65 and age <= 68:
            initial_driver_factor *= 1.25
        else:
            initial_driver_factor *= 1

        ## Based on Violations (Points)
        driver_score = driver['score']
        if driver_score <= 1:
            initial_driver_factor *=1
        elif driver_score <= 2:
            initial_driver_factor *= 1.05
        elif driver_score <= 3:
            initial_driver_factor *= 1.25
        elif driver_score <= 4:
            initial_driver_factor *= 1.4
        elif driver_score <= 5:
            initial_driver_factor *= 1.55
        elif driver_score <= 6:
            initial_driver_factor *= 1.75
        elif driver_score <= 7:
            initial_driver_factor *= 1.95
        else:
            initial_driver_factor *= 1
        print("0000-----",initial_driver_factor)
        
        total_drivers_factors += initial_driver_factor

    print("Len of Drivers---",len(drivers))
    print("----",total_drivers_factors/len(drivers))
    calculated_driver_factor = total_drivers_factors/len(drivers)
    driver_factor=calculated_driver_factor
    print(driver_factor,"driver_factor ok")
    print(type(driver_factor),"driver_factor")

#end driver
    c=[]

    d=[]
    
    
    b=get_apd_data_for_incurred_factor_db(_quote_id,2)
    print(b,"the b value is ")
    if b==[]:
        total_incurred_factor=1

    for i in b:
        d.append(i['total_incurred_amount']/i['units'])
        if i['total_incurred_amount']/i['units']<=50000:
            c.append(1.00)
            if len(c)>1:
                c.append(1.00)

        else:
            c=[1.00,1.05,1.10,1.15]
            break

        total_incurred_factor=c[0]
        total_incurred_factor=float(total_incurred_factor)
    #print(total_incurred_factor,"total_incurred_factor values are",type(total_incurred_factor))

#base rate-----------------------------------------------------------------------------------------------------------
    sum_of_statedamount = get_sum_of_statedamount_by_quoteid_json(_quote_id)
    
    factor = get_apd_base_rate_factor_json(sum_of_statedamount['sum'])
    if factor==-1:
        base_rate_factor=1
    else:
        base_rate_factor=factor["factor"]
     
        base_rate_factor=float(base_rate_factor)

    print("base rate values are:",base_rate_factor,type(base_rate_factor))
#Radius factor------------------------------------------------------------------------------------------------------------
    radius_factor_val= get_apd_radius_factor_db(radius_id)
    radius_factor =radius_factor_val["factor"]
    print("the radius factor values are:",radius_factor,type(radius_factor))
#tiv factor---------------------------------------------------------------------------------------------------------------------
    factor_val=get_apd_tiv_factor_db(_quote_id,tiv)
    print("the factor tiv",factor_val)
    tiv_factor=factor_val
    #tiv_factor=float(tiv_factor)
    print("tiv factor",tiv_factor,type(tiv_factor))

    deductible_rate = get_apd_deductible_factor_json(deductible)["rate"]
    print('deductible_rate',deductible_rate,type(deductible_rate))
    if state=='CA'or state=='NJ' or state=='FL' or state=='IL':
        state_factor = get_apd_state_factor_json(state)
    else:
        state_factor=0
    print(state_factor,"stat fjkll")
    print("state factor",state_factor)
    
#-----------------------------------------------------------------------------------------------------------------------------

 #   print(base_rate_factor,"base_rate_factor")
    #print(loss_exp_factor,"loss_exp_factor")
 #   print(total_incurred_factor,"total_incurred_factor")
   # print(radius_factor,"radius_factor")
    abr_rmf_calculation=round(loss_exp_factor*total_incurred_factor*driver_factor*radius_factor*years_of_experience_factor*base_rate_factor*rate_control_factor*float(uw_debit_credit)*tiv_factor,3)
    abr_calculation = round(abr_rmf_calculation + deductible_rate +state_factor,3)

    abr_rmf=abr_calculation
#total premium----------------------------------------------------------------------------------------------------------------   
    
    
    total_premium=round((abr_calculation*float(tiv))/100,0)
#premium fees------------------------------------------------------------------------------------------------------------------
    broker_fee=get_apd_broker_fee(int(total_premium))
    towing_fee=get_apd_towing_charges(towing_limit)
    broker_fee=int(broker_fee[0]["apd_broker_fee_fee"])
    towing_fee=int(towing_fee[0]["apd_towing_charges"])
    apd_premium=round(total_premium+broker_fee+towing_fee,0)
    usr=apdr_factor_modals(loss_exp_factor,total_incurred_factor,driver_factor,radius_factor,
    years_of_experience_factor,base_rate_factor,rate_control_factor,uw_debit_credit,tiv_factor,abr_rmf_calculation,deductible_rate,state_factor,abr_calculation ,total_premium,broker_fee,towing_fee,apd_premium,abr_rmf)
    apdr_all_data=add_apdr_factors_db(usr)
    print("broker fees",broker_fee,type(broker_fee),"towing fee",towing_fee,type(towing_fee))
    print("apd premium is",apd_premium,type(apd_premium))
    data={"abr_calculation":abr_calculation,"total_premium":total_premium,"apd_premium":apd_premium}
    print("abr calculations are",data)


    return Response(data, status=status.HTTP_200_OK)




    
