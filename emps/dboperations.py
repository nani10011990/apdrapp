from django.db import connections
from .models import *
import psycopg2

ps_connection = psycopg2.connect(user="falconadmin",
                                     password="Nta@2022$$!",
                                     host="falcondbnew2022.postgres.database.azure.com",
                                     port="5432",
                                     database="falcondbnew2022")

dbConnection= connections['default'].cursor()


 

def get_usic_safer_factor_db(safer_id,quote_id):
    safer_factor=1
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_usic_safer_factor_json(%s,%s);", (safer_id,quote_id,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            
            if len(rows)>0:
               factor=rows[0][0].get('factor')
               description=rows[0][0].get('description')
            
                
            #else:
            #    logstatus='FAILURE'            
            #return logstatus
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   {"factor":factor,"description":description}

def get_usic_fmcsa_factor_db(yrs_in_business_id,alert_id):
    fmcsa_factor=1
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_usic_fmcsa_factor_json(%s,%s);", (yrs_in_business_id,alert_id,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            
            if len(rows)>0:
               fmcsa_alerts=rows[0][0].get('fmcsa_alerts')
               fmcsa_factor=rows[0][0].get('factor')
               
                
            #else:
            #    logstatus='FAILURE'            
            #return logstatus
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   {"fmcsa_alerts":fmcsa_alerts,"fmcsa_factor":fmcsa_factor}

def get_usic_years_of_experience_factor_db(_id):
    years_experience_factor=1
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_usic_years_of_experience_factor_json(%s);", (_id,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            print(rows[0],"the rows value")
            if len(rows)>0:
               years_experience_factor=rows[0][0].get('years_of_experience_factor')
               tier=rows[0][0].get('tier')
            print(tier,"the factor value")
            #else:
            #    logstatus='FAILURE'            
            #return logstatus
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   {"years_experience_factor":years_experience_factor,"tier":tier}

def get_usic_al_deductible_factor_db(description):
    al_deductible_factor=1
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_usic_al_deductible_factor_json(%s);", (description,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            
            if len(rows)>0:
               al_deductible_factor=rows[0][0].get('factor')
               al_deductible=rows[0][0].get('description')
             
            #else:
            #    logstatus='FAILURE'            
            #return logstatus
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   {"al_deductible_factor":al_deductible_factor,"al_deductible":al_deductible}

def get_usic_ilf_factor_db():
    ilf_fcator=1
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_usic_ilf_factor_json();", ())
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            
            if len(rows)>0:
               ilf_factor=rows[0][0].get('ilf_factor')
                
            #else:
            #    logstatus='FAILURE'            
            #return logstatus
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return ilf_factor


def get_lcm_usic_factor_db():
    lcm_fcator=1
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_lcm_usic_factor_json();", ())
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            
            if len(rows)>0:
               lcm_factor=rows[0][0].get('lcm_factor')
                
            #else:
            #    logstatus='FAILURE'            
            #return logstatus
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return lcm_factor


def get_primary_usic_factor():
    primary_factor=1
    
    #udf_get_primary_factor_json
    
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_primary_usic_factor_json();", ())
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            
            if len(rows)>0:
               primary_factor=rows[0][0].get('primary_factor')
                
            #else:
            #    logstatus='FAILURE'            
            #return logstatus
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return  primary_factor
    
 

def get_usic_commission_tier_db(_tier):
    al_deductible_factor=1
    print(_tier,"the _tier db")
    print(type(_tier))
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_usic_commission(%s);", (_tier,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            print(rows[0],"the db values ")
            
            if len(rows)>0:
               commission_tier=rows[0][0].get('commission')
               print(commission_tier)
        
              
             
            #else:
            #    logstatus='FAILURE'            
            #return logstatus
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   commission_tier


def get_usic_fleet_factor_db(_id):
    al_deductible_factor=1
   
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_usic_fleet_factor(%s);", (_id,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            print(rows[0],"the db values ")
            
            if len(rows)>0:
               commission_tier=rows[0][0].get('factor')   
      
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   commission_tier


def get_usic_liability_limit_factor_db(liability_limit):
    al_deductible_factor=1
   
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_usic_liability__factor_json(%s);", (liability_limit,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
          #  print(rows[0],"the db values ")
            
            if len(rows)>0:
              liability_factor=rows[0][0].get('factor')   
      
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   liability_factor


def get_usic_state_zone_regional_factor_db(_state):
    al_deductible_factor=1
   
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_usic_usic_state_zone(%s);", (_state,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
          #  print(rows[0],"the db values ")
            
            if len(rows)>0:
              zone=rows[0][0].get('zone')   
              state_zone_factor=rows[0][0].get('factor')  
      
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   {"zone":zone,"state_zone_factor":state_zone_factor}

def get_hired_auto_db(_id):
    al_deductible_factor=1
   
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_ins_usic_basis_primary_excess(%s);", (_id,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
          #  print(rows[0],"the db values ")
            
            if len(rows)>0:
              zone=rows[0][0].get('zone')   
              min_premium=rows[0][0].get('min_premium')  
      
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return  min_premium

def get_usic_hired_auto_premium_db(id,basis,cost_of_hire,limit,no_of_units):
   
    try:
            print(id,basis,cost_of_hire,limit,no_of_units,"all data")
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_ins_usic_hired_auto_premium(%s,%s,%s,%s,%s);", (id,basis,cost_of_hire,limit,no_of_units,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
          #  print(rows[0],"the db values ")
            
            if len(rows)>0:
                min_units=rows[0][0].get('min_units')  
                max_units=rows[0][0].get('max_units')
                per_unit=rows[0][0].get('per_unit')
                min_premium=rows[0][0].get('min_premium') 
                factor=rows[0][0].get('factor')  
    
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return  {"min units":min_units,"max_units":max_units,"per_unit":per_unit,"min_premium":min_premium,"factor":factor}

def get_usic_state_city_by_zipcode_db(zipcode):
    al_deductible_factor=1
   
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_usic_state_city_by_zipcode(%s);", (zipcode,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            print(rows[0],"the db values ")
            
            if len(rows)>0:
              state=rows[0][0].get('state')   
              city=rows[0][0].get('city')   
              
      
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   {"state":state,"city":city}

def get_usic_states_factor_db(state):
    al_deductible_factor=1
   
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_ins_usic_states_factor(%s);", (state,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            print(rows[0],"the db values ")
            
            if len(rows)>0:
              factor=rows[0][0].get('factor')   
   
            
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   factor


def get_ins_quotes_json_data_by_quote_id(quote_id):
    """_summary_

    Args:
        commodity (_type_): _description_
    """
    dbConnection= connections['default'].cursor()
   
    try:
        query= dbConnection.execute(f"""select udf_get_ins_quotes_json_data_by_quote_id({quote_id});""")
        rows=dbConnection.fetchall()
                                           
    except (Exception, psycopg2.DatabaseError) as error:
           print(error)
    finally:
            dbConnection.close() 
    return rows

    

def add_usic_factors_db(usic_factor_modals):
       user_id=-1
       print(usic_factor_modals.years_experience_factor,
            usic_factor_modals.safer_factor,
            usic_factor_modals.al_deductible_factor,
            usic_factor_modals.ilf_factor,
            usic_factor_modals.lcm_factor,
            usic_factor_modals.primary_factor,
            usic_factor_modals.fmcsa_factor,
            usic_factor_modals.state_zone_factor,
            usic_factor_modals.liability_limit_usic_factor,
            usic_factor_modals.fleet_factor,
            usic_factor_modals.uw_credit_debit_factor,
            usic_factor_modals.rmf_factors,"the db factors ")
   
       try: 
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select public.udf_usic_factors(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", (usic_factor_modals.years_experience_factor,
            usic_factor_modals.safer_factor,
            usic_factor_modals.al_deductible_factor,
            usic_factor_modals.ilf_factor,
            usic_factor_modals.lcm_factor,
            usic_factor_modals.primary_factor,
            usic_factor_modals.fmcsa_factor,
            usic_factor_modals.state_zone_factor,
            usic_factor_modals.liability_limit_usic_factor,
            usic_factor_modals.fleet_factor,
            usic_factor_modals.uw_credit_debit_factor,
            usic_factor_modals.rmf_factors,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            print(rows[0],"the db values ")
            print(len(rows),"the rows length ")
            if len(rows)>0:
              user_id=rows[0][0]
              if user_id>-1 :
                    res="SUCCESS"
              else:
                    res="FAILURE"
               
      
           
        
       except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           print(error)
           res="Internal Server Error"
       return  res

def get_all_lobs():
       data=[]
    
   
       try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_ins_bill_from_type();", )
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
          #  print(rows[0],"the db values ")
            
            if len(rows)>0:
              for r in rows:
                     data.append(r[0])
              
      
           
        
       except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
       return  data
def  get_usic_factors_db():
        data=[]
        try:
            
            
            query= dbConnection.mogrify("SELECT public.udf_usic_factors_get();", ())
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
           
            if len(rows)>0:
              for r in rows:
                data.append(r[0])
              
            #    logstatus='FAILURE'            
            #return logstatus
           
        
        except (Exception, psycopg2.DatabaseError) as error:
           print(error)
           #u_id=-1
        print(data)       
        return   data

def get_no_of_units_ins_vehicles_db(quoteid):
    al_deductible_factor=1
   
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_no_of_units_from_ins_vehicles(%s);", (quoteid,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            print(rows[0],"the db values ")
            
            if len(rows)>0:
              count=rows[0][0].get('count')   

           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   count

def get_um_limit_db(state,limit):
    try:    

            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select  public.udf_get_usic_um_premium_json(%s,%s);",(state,limit,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
          #  print(rows[0],"the db values ")
            if len(rows)>0:
               cost_per_unit=rows[0][0].get('cost_per_unit')     
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   cost_per_unit



def get_lossratio_by_quote_id_coverage_db(quote_id,coverage):
    result=[]
    try:
        dbConnection= connections['default'].cursor()
        query=dbConnection.mogrify("select udf_get_lossfrequency_by_quoteid_coverage_f(%s,%s);", (quote_id,coverage))
        dbConnection.execute(query)
        rows= dbConnection.fetchall()
        if len(rows)>0:
            for item in rows:
                result.append(item[0])
    


    except (Exception, psycopg2.DatabaseError) as error:

        s_id = -1

    return result

def ins_approvals_post(quote_id,approval_id):
    result=[]
    try:
        dbConnection= connections['default'].cursor()
        query=dbConnection.mogrify("select udf_ins_quotes_approvals(%s,%s);", (quote_id,approval_id))
        dbConnection.execute(query)
        print("*****************************************")
        rows= dbConnection.fetchall()
        if len(rows)>0:
            for item in rows:
                result.append(item[0])
    


    except (Exception, psycopg2.DatabaseError) as error:

        s_id = -1

    return result

def get_udf_get_al_base_rate_zone_by_state_json(state):
    """_summary_

    Args:
        commodity (_type_): _description_
    """
    dbConnection= connections['default'].cursor()
    base_rate=[]  
   
    try:
        query= dbConnection.execute(f"""select udf_get_al_base_rate_zone_by_state_json('{state}');""")
        rows=dbConnection.fetchall()
        for row in rows:
            base_rate.append(row[0]) 
                                           
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        dbConnection.close() 

    return base_rate 

def get_all_data_for_usic_db(_quote_id):
    al_deductible_factor=1
   
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_usic_all_data(%s);", (_quote_id,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
          #  print(rows[0],"the db values ")
           
            if len(rows)>0:
             
              quote_estimate_json=rows[0][0].get('quote_estimate_json')  
              quote_submit_data=rows[0][0].get('quote_submit_data')  
              quote_add_date=rows[0][0].get('quote_add_date')
              endorement_effective_date=rows[0][0].get('endorement_effective_date')  
               
     
     
           
       
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return  {"quote_estimate_json":quote_estimate_json,"quote_submit_data":quote_submit_data,"quote_add_date":quote_add_date,"endorement_effective_date":endorement_effective_date}

def get_current_approval_db(quote_id):
    result = []

    try:

        dbConnection= connections['default'].cursor()
        query = dbConnection.mogrify("select  udf_get_current_approva_status(%s);", (quote_id,))
        dbConnection.execute(query)
        rows = dbConnection.fetchall()

        if len(rows) > 0:
            for item in rows:
                result.append(item[0])

    except (Exception, psycopg2.DatabaseError) as error:
        s_id = -1
    return result

def get_usic_pip_limit_db(limit,state):
    safer_factor=1
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_usic_pip(%s,%s);", (limit,state,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            
            if len(rows)>0:
               per_unit=rows[0][0].get('per_unit_price')
                
            #else:
            #    logstatus='FAILURE'            
            #return logstatus
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   {"per_unit_price":per_unit}

#SN AL RATERS FROM HERE ---------------------------------------------------------------------------------------------------------------------------------


def get_sn_local_intermediate_db(radius,category):
    safer_factor=1
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_sn_local_intermediate_json(%s,%s);", (radius,category,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            
            if len(rows)>0:
               base_rate=rows[0][0].get('rate')
                
            #else:
            #    logstatus='FAILURE'            
            #return logstatus
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   {"Base_rate":base_rate}

def get_rate_by_org_code_db(origination_zone_code,destination):
    result=[]
    try:
        dbConnection= connections['default'].cursor()
        query=dbConnection.mogrify("select udf_get_highlander_rate_(%s,%s);", (origination_zone_code,destination))
        dbConnection.execute(query)
        rows= dbConnection.fetchall()
        if len(rows)>0:
            rate=rows[0][0].get('rate')


    except (Exception, psycopg2.DatabaseError) as error:

        s_id = -1

    return rate

#corrections needs to be done in the data base function-------------------------------------------------------------------
def get_vehicle_factor_by_weight_and_model_db(weight,model):
    result=[]
    try:
        dbConnection= connections['default'].cursor()
        query=dbConnection.mogrify("select udf_vehicle_factor_by_weight_(%s,%s);", (weight,model,))
        dbConnection.execute(query)
        rows= dbConnection.fetchall()
        if len(rows)>0:
            for item in rows:
                result.append(item[0])
    


    except (Exception, psycopg2.DatabaseError) as error:

        s_id = -1

    return result
#----------------------------------------------------------------------------------------------------------------

def get_data_by_zip_code_db(zip):
    result=[]
    try:
        dbConnection= connections['default'].cursor()
        query=dbConnection.mogrify("select udf_get_data_by_zip_code_(%s);", (zip,))
        dbConnection.execute(query)
        rows= dbConnection.fetchall()
        if len(rows)>0:
            city=rows[0][0].get('city')
            country=rows[0][0].get('country')
            category=rows[0][0].get('category')
            originating_zone_code=rows[0][0].get('originating_zone_code')
            originating_zone=rows[0][0].get('originating_zone')
            
    except (Exception, psycopg2.DatabaseError) as error:

        s_id = -1

    return {"city":city,"country":country,"category":category,"originating_zone_code":originating_zone_code,"originating_zone":originating_zone}

def get_ins_highlander_al_deductible_factor(deductible):
    try:       
        dbConnection= connections['default'].cursor()
        query= dbConnection.mogrify(f"""select udf_get_highlander_al_deductible_factor_json({deductible});""")
        dbConnection.execute(query)           
        rows=dbConnection.fetchall()
        if len(rows)>0:
            factor=rows[0][0]   
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        factor= -1          
    return factor


def get_range_from_ins_highlander_pollution_factor_json(description, range):
    data = []
    try:       
        dbConnection= connections['default'].cursor()
        query= dbConnection.mogrify(f"""select udf_get_range_from_ins_highlander_pollution_factor_json('{description}', {range});""")
        dbConnection.execute(query)           
        rows=dbConnection.fetchall()
        if len(rows)>0:
            data.append({
                "range":range,
                "description":rows[0][0]['description'],
            })
        else:
            data.append({
                "error": "Value is over the range."
            }) 
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)           
    return data


def get_highlander_al_safer_factor_json(description):
    try:       
        dbConnection= connections['default'].cursor()
        query= dbConnection.mogrify(f"""select udf_get_highlander_al_safer_factor_json('{description}');""")
        dbConnection.execute(query)           
        rows=dbConnection.fetchall()
        if len(rows)>0:
            factor=rows[0][0]   
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        factor= -1          
    return factor

def get_udf_al_um_premium_db(limit,no_of_units) :
    try:    
          result = {}
          dbConnection= connections['default'].cursor()
          query= dbConnection.mogrify("select public.udf_get_high_al_um_premium(%s,%s);",(limit,no_of_units))
          dbConnection.execute(query)
          rows=dbConnection.fetchall()
        #  print(rows[0],"the db values ")
          if len(rows)>0:
            result['per_unit_factor'] = rows[0][0].get('per_unit_factor') 
            result['per_unit_premium'] = rows[0][0].get('per_unit_premium') 
            result['total_premimum'] = rows[0][0].get('total_premium')  
             
          return  result
    except (Exception, psycopg2.DatabaseError) as error:
          print(error) 

def get_udf_al_uim_premium_db(limit,no_of_units) :
    try:    
          result = {}
          dbConnection= connections['default'].cursor()
          query= dbConnection.mogrify("select public.udf_get_high_al_uim_premium(%s,%s);",(limit,no_of_units))
          dbConnection.execute(query)
          rows=dbConnection.fetchall()
        #  print(rows[0],"the db values ")
          if len(rows)>0:
            result['per_unit_factor'] = rows[0][0].get('per_unit_factor') 
            result['per_unit_premium'] = rows[0][0].get('per_unit_premium')
            result['total_premium'] = rows[0][0].get('total_uim_premium')     
          return  result
    except (Exception, psycopg2.DatabaseError) as error:
          print(error) 

def get_highlander_auto_hired():

    try:
        dbConnection= connections['default'].cursor()
        query = dbConnection.mogrify("select udf_get_highland_hired_auto_premium_json();", ())
        dbConnection.execute(query)
        rows = dbConnection.fetchall()
        result = []

     
        if len(rows) > 0:
            for item in rows:
                result.append(item[0])
    except(Exception, psycopg2.DatabaseError) as error:

        s_id = -1

    return result 

#From here APD Raters starts----------------------------------------------------------------------------------------------------------------
#Not yet updated the code in the server runned and sucessfully executed in local-----------------------------------------------------------

def get_yrs_of_exp_db(years_id):
    safer_factor=1
    try:
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select udf_get_apd_years_of_experience_json(%s);", (years_id,))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            
            if len(rows)>0:
               factor=rows[0][0].get('factor')
               description=rows[0][0].get('description')
            
                
            #else:
            #    logstatus='FAILURE'            
            #return logstatus
           
        
    except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           
    return   {"factor":factor,"description":description}


#----------------------------------------------------------------------------------------------------------------------------------------------

def get_apd_broker_fee(pd_premium):

    
    try:
        dbConnection= connections['default'].cursor()
        query = dbConnection.mogrify("select udf_get_apd_broker_fee_json(%s);", (pd_premium,))
        dbConnection.execute(query)
        rows = dbConnection.fetchall()
        print(rows)
        result = []
     
        if len(rows) > 0:
            for item in rows:
                result.append(item[0])
    except(Exception, psycopg2.DatabaseError) as error:

        s_id = -1
    
    return result


def get_apd_towing_charges(towing_limit):
    try:
        dbConnection= connections['default'].cursor()
        query = dbConnection.mogrify("select udf_get_apd_towing_charges(%s);", (towing_limit,))
        dbConnection.execute(query)
        rows = dbConnection.fetchall()
        print(rows)
        result = []
     
        if len(rows) > 0:
            for item in rows:
                result.append(item[0])
    except(Exception, psycopg2.DatabaseError) as error:

        s_id = -1
    
    return result


def get_apd_lossratio_by_quote_id_coverage_db(quote_id,coverage):
    result=[]
    try:
        dbConnection= connections['default'].cursor()
        query=dbConnection.mogrify("select get_lossratio_by_quoteid_coverage_(%s,%s);", (quote_id,coverage))
        dbConnection.execute(query)
        rows= dbConnection.fetchall()
        if len(rows)>0:
            for item in rows:
                result.append(item[0])
    


    except (Exception, psycopg2.DatabaseError) as error:

        s_id = -1

    return result



def get_apd_data_for_incurred_factor_db(quote_id,coverage):
    result=[]
    try:
        dbConnection= connections['default'].cursor()
        query=dbConnection.mogrify("select get_data_by_quoteid_coverage_(%s,%s);", (quote_id,coverage))
        dbConnection.execute(query)
        rows= dbConnection.fetchall()
        if len(rows)>0:
            for item in rows:
                result.append(item[0])
    


    except (Exception, psycopg2.DatabaseError) as error:

        s_id = -1

    return result

def get_ins_quotes_json_data_by_quote_id(quote_id):
    #FOR DRIVER FACTOR
    dbConnection= connections['default'].cursor()
   
    try:
        query= dbConnection.execute(f"""select udf_get_ins_quotes_json_data_by_quote_id({quote_id});""")
        rows=dbConnection.fetchall()
                                           
    except (Exception, psycopg2.DatabaseError) as error:
           print(error)
    finally:
            dbConnection.close() 
    return rows

def get_sum_of_statedamount_by_quoteid_json(quote_id):
    try:       
        dbConnection= connections['default'].cursor()
        query= dbConnection.mogrify(f"""select udf_get_sum_of_statedamount_by_quoteid_json('{quote_id}');""")
        dbConnection.execute(query)           
        rows=dbConnection.fetchall()
        if len(rows)>0:
            sum_of_statedamount=rows[0][0]   
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sum_of_statedamount= -1          
    return sum_of_statedamount

def get_apd_base_rate_factor_json(range):
    try:       
        dbConnection= connections['default'].cursor()
        query= dbConnection.mogrify(f"""select udf_get_apd_base_rate_factor_json('{range}');""")
        dbConnection.execute(query)           
        rows=dbConnection.fetchall()
        if len(rows)>0:
            factor=rows[0][0]   
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        factor= -1          
    return factor

def get_apd_deductible_factor_json(deductible):
    try:       
        dbConnection= connections['default'].cursor()
        query= dbConnection.mogrify(f"""select udf_get_apd_deductible_factor_json('{deductible}');""")
        dbConnection.execute(query)           
        rows=dbConnection.fetchall()
        if len(rows)>0:
            rate=rows[0][0]   
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        rate= -1          
    return rate

def get_apd_state_factor_json(state):
    try:       
        dbConnection= connections['default'].cursor()
        query= dbConnection.mogrify(f"""select udf_get_apd_state_factor_json('{state}');""")
        dbConnection.execute(query)           
        rows=dbConnection.fetchall()
        if len(rows)>0:
            factor=rows[0][0]   
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        factor= -1          
    return factor

def get_apd_radius_factor_db(radius_id):
    try:
        dbConnection= connections['default'].cursor()
        query = dbConnection.mogrify("select udf_get_apd_radius_factor(%s);", (radius_id,))
        dbConnection.execute(query)
        rows = dbConnection.fetchall()
        print(rows)
        result = []
     
        if len(rows) > 0:
            factor=rows[0][0].get('apd_radius_factor')
            range=rows[0][0].get('apd_radius_range')
    except(Exception, psycopg2.DatabaseError) as error:
        s_id = -1 
    return {"factor":factor,"range":range} 

def get_apd_tiv_factor_db(quote_id,tiv):
  safer_factor=1
  try:
          dbConnection= connections['default'].cursor()
          query= dbConnection.mogrify("select udf_get_apd_tiv_factor(%s,%s);", (quote_id,tiv,))
          dbConnection.execute(query)
          rows=dbConnection.fetchall()
          #print(type(rows))
          #print(type(rows[0]))
          
          if len(rows)>0:
             factor=rows[0][0].get('factor')
               #else:
          #    logstatus='FAILURE'            
          #return logstatus         
  
  except (Exception, psycopg2.DatabaseError) as error:           
           u_id=-1          
  return  factor


def  get_apdr_factors_db():
        data=[]
        try:
            
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("SELECT public.udf_apdr_factors_get();", ())
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
           
            if len(rows)>0:
              for r in rows:
                data.append(r[0])
            print(data,"the data sis ")       
        except (Exception, psycopg2.DatabaseError) as error:
           print(error)
           #u_id=-1
        print(data)       
        return   data
def add_apdr_factors_db(apdr_factor_modals):
       user_id=-1
       
   
       try: 
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select public.udf_apdr_factors(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s );", (apdr_factor_modals.loss_exp_factor,
            apdr_factor_modals.total_incurred_factor,
            apdr_factor_modals.driver_factor,
            apdr_factor_modals.radius_factor,
            apdr_factor_modals.years_of_experience_factor,
            apdr_factor_modals.base_rate_factor,
            apdr_factor_modals.rate_control_factor,
            apdr_factor_modals.uw_debit_credit,
            apdr_factor_modals.tiv_factor,
            apdr_factor_modals.abr_rmf_calculation,
            apdr_factor_modals.deductible_rate,
            apdr_factor_modals.state_factor,   
            apdr_factor_modals.abr_calculation,
            apdr_factor_modals.total_premium,   
            apdr_factor_modals.broker_fee,
            apdr_factor_modals.towing_fee,
            apdr_factor_modals.apd_premium,
            apdr_factor_modals.abr_rmf


        
        


            
             ))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            print(rows[0],"the db values ")
            print(len(rows),"the rows length ")
            if len(rows)>0:
              user_id=rows[0][0]
              if user_id>-1 :
                    res="SUCCESS"
              else:
                    res="FAILURE"
               
      
           
        
       except (Exception, psycopg2.DatabaseError) as error:
           
           u_id=-1
           print(error)
           res="Internal Server Error"
       return  res
