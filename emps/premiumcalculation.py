from datetime import date
import datetime
from .models import *
from .dboperations import    add_usic_factors_db

def calculate_rmf_premium(years_experience_factor,safer_factor,al_deductible_factor,ilf_factor,lcm_factor,primary_factor,
    fmcsa_factor,state_zone_factor,liability_limit_usic_factor,fleet_factor,uw_credit_debit_factor):
  
                
       

  
        
             
    return round( years_experience_factor*safer_factor*al_deductible_factor*ilf_factor*lcm_factor*primary_factor*fmcsa_factor*state_zone_factor*liability_limit_usic_factor*fleet_factor*uw_credit_debit_factor , 3)

def calculate_apd_rmf(base_rate_factor,loss_exp_factor,total_incurred_factor,radius_factor,years_of_experience_factor):


    return  base_rate_factor*loss_exp_factor*total_incurred_factor*radius_factor*years_of_experience_factor     