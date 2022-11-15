from django.db import models

 
class usic_factor_modals:
    def __init__(self,years_experience_factor,safer_factor,al_deductible_factor,ilf_factor,lcm_factor,primary_factor,fmcsa_factor,state_zone_factor,liability_limit_usic_factor,fleet_factor,uw_credit_debit_factor,rmf_factors):
        self.years_experience_factor=years_experience_factor
        self.safer_factor=safer_factor
        self.al_deductible_factor=al_deductible_factor
        self.ilf_factor=ilf_factor
        self.lcm_factor=lcm_factor
        self.primary_factor=primary_factor
        self.fmcsa_factor=fmcsa_factor
        self.state_zone_factor=state_zone_factor
        self.liability_limit_usic_factor=liability_limit_usic_factor
        self.fleet_factor=fleet_factor
        self.uw_credit_debit_factor=uw_credit_debit_factor
        self.rmf_factors=rmf_factors

class usic_factor_modals:
     def __init__(self,min_units,max_units,per_unit,min_premium):
        self.min_units=min_units
        self.max_units=max_units
        self.per_unit=per_unit
        self.min_premium=min_premium


# class usic_factor_modals:
#     def __init__(self,years_experience_factor):
#         self.years_experience_factor=years_experience_factor
        

    
         