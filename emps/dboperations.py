from django.db import connections
from .models import *
import psycopg2


ps_connection = psycopg2.connect(user="falconadmin",
                                     password="Nta@2022$$!",
                                     host="falcondbnew2022.postgres.database.azure.com",
                                     port="5432",
                                     database="falcondbnew2022")


dbConnection= connections['default'].cursor()

def  get_departmen_db():
        data=[]
        try:
            
            
            query= dbConnection.mogrify("SELECT public.test_adepartment_retrive_data();", ())
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
            print(rows,"the rows retrive ")
     
            if len(rows)>0:
              for r in rows:
               # print(r[0])
                data.append(r[0])
              
            #    logstatus='FAILURE'            
            #return logstatus
           
        
        except (Exception, psycopg2.DatabaseError) as error:
           print(error)
           #u_id=-1
               
        return   data
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
def get_mtc_cargo_factor(limit):    
     
    try:
        dbConnection= connections['default'].cursor()
        query = dbConnection.mogrify("select udf_get_mtc_cargo_limit_factor(%s);", (limit,))
        dbConnection.execute(query)
        rows = dbConnection.fetchall()
        
        result = []
     
        if len(rows) >0:
            for item in rows:
                result.append(item[0])
    except(Exception, psycopg2.DatabaseError) as error:
        s_id = -1
    
    return result      
def get_mtc_years_if_experience(state):
    try:
        dbConnection= connections['default'].cursor()
        query = dbConnection.mogrify("select udf_mtc_get_years_of_experience(%s);", (state,))
        dbConnection.execute(query)
        rows = dbConnection.fetchall()
        result = []
     
        if len(rows) >0:
            for item in rows:
                result.append(item[0])
            
    except(Exception, psycopg2.DatabaseError) as error:
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

def add_mtc_factors_db(usic_factor_modals):
       user_id=-1
         
       try: 
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("select public.udf_add_newmtc_clculations(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s );", (usic_factor_modals.years_experience_factor ,
            usic_factor_modals.cargo_factor,
            usic_factor_modals.rmf_factors,  
            usic_factor_modals.mtc_deductable_factor,
            usic_factor_modals.RateControlFactor,
            usic_factor_modals.UW_Credit_Debit,
            usic_factor_modals.driver_factor,
            usic_factor_modals.base_rate,
            usic_factor_modals.loss_frequency_factor,
            usic_factor_modals.total_cargo_premium,
            usic_factor_modals.fleet_factor,
            usic_factor_modals.per_unit_price
                              
             ))
            dbConnection.execute(query)
            rows=dbConnection.fetchall()
            #print(type(rows))
            #print(type(rows[0]))
           # print(rows[0],"the db values ")
            #print(len(rows),"the rows length ")
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

def  get_mtcnew_factors_db():
        data=[]
        try:
            
            dbConnection= connections['default'].cursor()
            query= dbConnection.mogrify("SELECT public.udf_get_newmtc_factors();", ())
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



def get_mtc_deductable_factor(limit):
    try:
        dbConnection= connections['default'].cursor()
        query = dbConnection.mogrify("select udf_get_mtc_deductable_factor(%s);", (limit,))
        dbConnection.execute(query)
        rows = dbConnection.fetchall()
        result = []
     
        if len(rows) > 0:
            for item in rows:
                result.append(item[0])
    except(Exception, psycopg2.DatabaseError) as error:
        s_id = -1 
    return result 

def get_mtp_base_rate_(quote_id):
       
    result = []

    try:
        
        dbConnection= connections['default'].cursor()
        query = dbConnection.mogrify("select udf_get_commodity_and_base_price(%s);", (quote_id,))
        
        dbConnection.execute(query)

        rows = dbConnection.fetchall()
        
        if len(rows) > 0:
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

def get_mtc_fleet_factor(units):
    try:
        dbConnection= connections['default'].cursor()
        query = dbConnection.mogrify("select udf_get_mtc_fleet_factor(%s);", (units,))
        dbConnection.execute(query)
        rows = dbConnection.fetchall()
       
        result = []
     
        if len(rows) > 0:
            for item in rows:
                result.append(item[0])
    except(Exception, psycopg2.DatabaseError) as error:
        s_id = -1 
    return result  

def get_all_commodities_by_quote_id_db(quote_id):
       
    result = []

    try:
        
        dbConnection= connections['default'].cursor()
        query = dbConnection.mogrify("select udf_mtc_commodities_by_quote_id(%s);", (quote_id,))
        
        dbConnection.execute(query)

        rows = dbConnection.fetchall()
        
        if len(rows) > 0:
             for item in rows:
                 result.append(item[0].get('commodity_name'))
        # if len(rows)>0:
        #        safer_factor=rows[0][0].get('commodity_name')
               
            
        print(result,"the result is")


    except (Exception, psycopg2.DatabaseError) as error:

        s_id = -1

    return result

def get_commodities_base_rate(commodity_type):
       
    result = []

    try:
        print(commodity_type,"the commodity_type")
        dbConnection= connections['default'].cursor()
        query = dbConnection.mogrify("select udf_get_commodity_base_rate_mtc(%s);", (commodity_type,))
        
        dbConnection.execute(query)

        rows = dbConnection.fetchall()
        
        if len(rows) > 0:
            base_rate=rows[0][0].get('MTC_BASERATE')
        # if len(rows)>0:
        #        safer_factor=rows[0][0].get('commodity_name')
               
            
        print(base_rate,"the result is")


    except (Exception, psycopg2.DatabaseError) as error:

        s_id = -1

    return base_rate