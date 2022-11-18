def calculate_rmf_premium(years_experience_factor,cargo_factor,mtc_deductable_factor,RateControlFactor,UW_Credit_Debit,driver_factor,loss_frequency_factor,fleet_factor):
    
    return round(years_experience_factor*cargo_factor*mtc_deductable_factor*RateControlFactor*UW_Credit_Debit*driver_factor*loss_frequency_factor*fleet_factor,3)
   