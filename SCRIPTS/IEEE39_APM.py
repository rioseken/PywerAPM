import pandas as pd
from time import time
from math import sqrt
import matplotlib.pyplot as plt
import datetime
import sys
sys.path.insert(0,'APM/BIN/')


# Import real time contingencies assessment
from ST_AM_Contingencies_Analysis import Real_Time_Contingencies as RTC_A
from ST_AM_Contingencies_Ploty import  Plot_All_Days_Hour_Data
from ST_AM_Contingencies_Ploty import  Plot_Stack


# Performance assessment Settings

file_tags              = 'APM/DATA/IEEE39_Asset_Data.xlsx'
asset_portfolio_source = 'APM/DATA/IEEE39_Asset_Data.xlsx'
net_file               = 'APM/DATA/IEEE39NODES.xlsx'
date_beg               = datetime.datetime(2020, 1, 1,1) 
load_growth            = 0.02                              # Assumed load growth per year       
h_end                  = 5*24*365                          # Assumed period of planning 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                               #
#                 Normal Operating conditions                   #
#                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Create contingencies assessment object
Cont_A = RTC_A(net_file,file_tags)
#->Cont_A.Load_Growth_Update(load_growth) 
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # Run base line # # # # # # # # #

#->df_base_line,df_load = Cont_A.Run_Case_Load_growth(Cont_A.net,load_growth,date_beg,h_end)
#sys.exit()

#df_base_line,df_load = Cont_A.Run_Case_Base(Cont_A.net)
#->S_base = sqrt((Cont_A.net.load['p_mw']**2+  Cont_A.net.load['q_mvar']**2).max())
#->S_base = Cont_A.net.trafo['sn_mva'].max()

# # # # # # # # Plot line base # # # # #
#->Plot_Stack(df_load,'RESULTS/IEEE36_Base_Case_')
#->sys.exit()
#->Plot_All_Days_Hour_Data(df_base_line,'RESULTS/IEEE36_Base_TR_Case_',S_base=S_base,LN=False)
#->Plot_All_Days_Hour_Data(df_base_line,'RESULTS/IEEE36_Base_LN_Case_',S_base=S_base,TR=False)
#->Plot_All_Days_Hour_Data(df_base_line,'RESULTS/IEEE36_Base_BU_Case_',TR=False,LN=False,BU=True)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                               #
#                Historical records of condition                #
#                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Asset porfolio 
from APM_Module import APM 
Assets  = APM(asset_portfolio_source,load_growth)


from ST_AM_Contingencies_Ploty import Plot_Asset_Condition_Assessment


