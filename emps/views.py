 
from django.shortcuts import render

# Create your views here.
from email import message
from django.shortcuts import render
from os import name
from django.shortcuts import render
from django.shortcuts import render
from django.template import Context, loader
from rest_framework import generics

from emps.premiumcalculation import calculate_rmf_premium
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
from rest_framework.views import APIView
from django.conf import settings
from django.core.files import File
from django.http import FileResponse
from .dboperations import      add_mtc_factors_db, get_all_commodities_by_quote_id_db, get_all_data_for_usic_db, get_commodities_base_rate, get_departmen_db, get_ins_quotes_json_data_by_quote_id, get_lossratio_by_quote_id_coverage_db, get_mtc_cargo_factor, get_mtc_deductable_factor, get_mtc_fleet_factor, get_mtc_years_if_experience, get_mtcnew_factors_db, get_mtp_base_rate_, ins_approvals_post  
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['GET'])
def get_departments_list(request):
    res=get_departmen_db()
    data={"result":res}
    print(data,"the backend values are ")

    return   Response(data, status=status.HTTP_200_OK) 
@api_view(['POST'])
def get_all_data_for_usic(request):

        data = json.loads(request.body.decode("utf-8"))
        print(data,"the print data is ")
        _quote_id=data["_quote_id"]

    
        

        res= get_all_data_for_usic_db(_quote_id)
       # print(res["quote_estimate_json]"the data is ")
        print(len(res["quote_submit_data"]["vehicles"]),"the len is ")
        print(res["quote_submit_data"]["vehicles"],"the res data is ")
        no_of_units_ssig=[]
        for index in range(len(res["quote_submit_data"]["vehicles"])):
             

            for i in res["quote_submit_data"]["vehicles"][index]:
          
                if i=='model':
                    print(i,"the i is ")
                    print(res["quote_submit_data"]["vehicles"][index]["model"],"i think the value will get ")
                    if res["quote_submit_data"]["vehicles"][index]["model"]=='TRUCK' or res["quote_submit_data"]["vehicles"][index]["model"]=='TRACTOR':
                        no_of_units_ssig.append(res["quote_submit_data"]["vehicles"][index]["model"])
                    print(no_of_units_ssig,"the no_of_units_db are ")
                    print(len(no_of_units_ssig),"the no_of_units_ssig ")
    #                 print(res["quote_submit_data"]["vehicles"][index]["model"])
   # res["quote_submit_data"]["vehicles"][0].keys()
    #    #print(res["liability"][0],"the liability values are ")
                 
        data={"result": res,"list_of_units":no_of_units_ssig,"length_of_units":len(no_of_units_ssig)}    
        return   Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def mtc_cargo_factor(request):
    req_data = json.loads(request.body.decode("utf-8"))
    cargo_limit = req_data["limit"]
   
    db_data  =get_mtc_cargo_factor(cargo_limit)
    res =db_data
    cargo_factor = res[0]["cargo_limit_factor"]
    print(cargo_factor,"the cargo_factor ")
    data = {"mtc factor": cargo_factor }
    return Response(data, status=status.HTTP_200_OK)
@api_view(['POST'])
def mtc_years_of_experience(request):
    req_data = json.loads(request.body.decode("utf-8"))
    years_of_exp = req_data["id"]
   
    db_data  =get_mtc_years_if_experience(years_of_exp)
    res =db_data
    print(res)
    description = res[0]["years_of_experience_exp"]
    factor = res[0]["years_of_experience_factor"]
   
    data = {"description": description, "Factor" :factor}
    return Response(data, status=status.HTTP_200_OK) 
    
@api_view(['GET'])
def get_mtc_factors(request):
    res=get_mtcnew_factors_db()
    data={"result":res}

    return   Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def mtc_deductable_factor(request):
    req_data = json.loads(request.body.decode("utf-8"))
    deductable_limit = req_data["deductable_limit"]
   
    db_data  = get_mtc_deductable_factor(deductable_limit)
    res =db_data[0]["fleet_factor_factor"]
    print(res,"the res mts deu")
    data = {"mtc factor": res }
    return Response(data, status=status.HTTP_200_OK) 

@api_view(['POST'])
def mtc_get_commodities_by_quote_id(request):
    req_data = json.loads(request.body.decode("utf-8"))
    quote_id = req_data["quote_id"]
   
    commodities  = get_all_commodities_by_quote_id_db(quote_id)
    print(commodities,"the commodites are")
    base_rate_lst=[]
    
        #base_rate_lst.append(base_rate)
    for i in commodities:
        print(i,type(i),"the i values are")
        base_rate=get_commodities_base_rate(i)
        if base_rate==None:
            base_rate=1
        base_rate_lst.append(base_rate)
        
        print(base_rate_lst,"the base_rate_lst is ")
        print(max(base_rate_lst),"the max value is ")
    data = {"mtc factor": commodities,"base_rate":max(base_rate_lst) }
    return Response(data, status=status.HTTP_200_OK) 

@api_view(['POST'])
def get_base_rate_by_quote_id(request):
    data = json.loads(request.body.decode("utf-8"))
    _quote_id=data['quote_id']
   
    print(_quote_id)
    
    b=get_mtp_base_rate_(_quote_id)
    c=[]
    for i in b:
        c.append(i['baseprice'])
    
    if len(c)>1:
        c=(max(c))
    
        base_rate=c
    else:
        base_rate=1425
    data={"result":base_rate}
    #res={"base rate":c}
    
    return   Response(data, status=status.HTTP_200_OK) 
@api_view(['POST'])
def mtc_fleet_factor(request):
    req_data = json.loads(request.body.decode("utf-8"))
    no_units = req_data["no_units"]
   
    db_data  = get_mtc_fleet_factor(no_units)
    res =db_data
    fleet_factor = res[0]["fleet_factor_factor"]
    print(fleet_factor,"the fleet_factor is ")
   
    data = {"fleet factor": fleet_factor }
    return Response(data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def get_loss_ratio(request):
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
def rmf__mtc_calculations(request):
    req_data = json.loads(request.body.decode("utf-8"))
    years_of_exp = req_data["years_of_exp"]
 
    cargo_limit = req_data["cargo_limit"]
    RateControlFactor=float(req_data["RateControlFactor"])
    UW_Credit_Debit=float(req_data["UW_Credit_Debit"])
    no_of_units=float(req_data["no_of_units"])
    years_of_exp_data =get_mtc_years_if_experience(years_of_exp)
    res =years_of_exp_data
     
    
    years_experience_factor = res[0]["years_of_experience_factor"]

# mtc _deduc
    req_data = json.loads(request.body.decode("utf-8"))
    deductable_limit = req_data["deductable_limit"]
   
    db_data  = get_mtc_deductable_factor(deductable_limit)
    mtc_deductable_factor =float(db_data[0]["fleet_factor_factor"])
    print(mtc_deductable_factor,type(mtc_deductable_factor),"the res mts deu")
#end mtc deductible
#driver factor
    print(no_of_units,type(no_of_units),"the no_of_units units are")
    
    quote_id = req_data['quote_id']

    #loss ratio
    # b=get_lossratio_by_quote_id_coverage_db(quote_id,1)
    # c=[]
    # if len(b)>0:
    #     c=1.20
    # else:
    #     c=1
    
    # loss_frequency_factor=int(c)
    # print(loss_frequency_factor,"the loss_frequency_factor is")
    loss_ratio= req_data["loss_ratio"]
    print(loss_ratio,"the loss_ratio")
    loss_frequency_factor=float(loss_ratio)
    #base_rate
     
    commodities  = get_all_commodities_by_quote_id_db(quote_id)
    print(commodities,"the commodites are")
    base_rate_lst=[]
    
        #base_rate_lst.append(base_rate)
    for i in commodities:
        print(i,type(i),"the i values are")
        base_rate=get_commodities_base_rate(i)
        if base_rate==None:
            base_rate=1
        base_rate_lst.append(base_rate)
    base_rate=max(base_rate_lst)
        
         
    
    #end base rate
    get_drivers = get_ins_quotes_json_data_by_quote_id(quote_id)
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

       
    db_data  =get_mtc_cargo_factor(cargo_limit)
    res =db_data
    cargo_factor = res[0]["cargo_limit_factor"]
    print(cargo_factor,"the cargo_factor ")
    #fleet factor
    db_data= get_mtc_fleet_factor(2)
    res =db_data
    fleet_factor = res[0]["fleet_factor_factor"]
    print(fleet_factor,"the fleet_factor is ")
    #end fleet factor
    rmf_factors=calculate_rmf_premium( years_experience_factor,cargo_factor,mtc_deductable_factor,RateControlFactor,UW_Credit_Debit,driver_factor,loss_frequency_factor,fleet_factor)
    per_unit_price=round(rmf_factors*base_rate,0)
    total_cargo_premium=int(per_unit_price*no_of_units)
    print(total_cargo_premium,"the total_cargo_premium is ")
    
    usr=usic_factor_modals(years_experience_factor,cargo_factor,rmf_factors,mtc_deductable_factor,RateControlFactor,UW_Credit_Debit,driver_factor,base_rate,loss_frequency_factor,total_cargo_premium,fleet_factor,per_unit_price )
    add_all_usic_factors=add_mtc_factors_db(usr)
     
 
    print(rmf_factors,"the rmf_factors value is ")
    data={"rmf_calculation":rmf_factors}
    


    return Response(data, status=status.HTTP_200_OK)

