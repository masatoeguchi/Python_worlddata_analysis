#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:17:25 2018

@author: HULT international Business school, Data Science:Python Team9
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 13:30:34 2018

"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

world_file = 'world_data_hult_regions.xlsx'
"""We make file variable above so that we can call in like below."""
world_df = pd.read_excel(world_file)

region_file = "Team Analysis2.csv"
region_df = pd.read_csv(region_file)

"""Check the data set"""

world_df.shape
world_df.describe


"""World doesn't belong to anywhere. We drop it."""

world_df = world_df[world_df["country_name"] != "World"]

"""Income index is completed column so we coverted it into numerical value.
To get the level of incomes for regions, we put number's to each income level
Low_income = 1, Lower middle = 2, Upper_middle = 3, High income = 4
This roop makes income_index column at last and gives number for it"""

for row in enumerate(world_df.loc[ : , 'income_group']):
    if row[1] == "Low income":
        world_df.loc[row[0],'income_index'] = 1
        print(row[1])
    elif row[1] == "Lower middle income":
        world_df.loc[row[0],'income_index'] = 2
        print(row[1])
    elif row[1] == "Upper middle income":
        world_df.loc[row[0],'income_index'] = 3
        print(row[1])
    elif row[1] == "High income":
        world_df.loc[row[0],'income_index'] = 4
        print(row[1])
      
"""We checked every column with too much missing value  n > 50""" 
print(world_df.isnull().sum())
    
"""We drop incidence_hiv, adult_literacy_pct, homicides_per_100k, tax_revenue_pct_gdp"""

world_df_dropped = pd.DataFrame.copy(world_df)
world_df_dropped.drop(['incidence_hiv','homicides_per_100k', 'tax_revenue_pct_gdp', 'adult_literacy_pct'], axis=1, inplace=True)
world_df_dropped.isnull().sum()

"""Decide whether to use median or mean to imputate missing data based on skewness or normal distribution."""

#access_to_electricity_pop -> median
world_df_dropped['access_to_electricity_pop'].hist()

plt.xlabel("access_to_electricity_pop")
plt.show()
#access_to_electricity_rural -> median
world_df_dropped['access_to_electricity_rural'].hist()

plt.xlabel("access_to_electricity_rural")
plt.show()
#access_to_electricity_urban -> median
world_df_dropped['access_to_electricity_urban'].hist()

plt.xlabel("access_to_electricity_urban")
plt.show()
#CO2_emissions_per_capita) -> median
world_df_dropped['CO2_emissions_per_capita)'].hist()

plt.xlabel("CO2_emissions_per_capita)")
plt.show()
#compulsory_edu_yrs -> mean
world_df_dropped['compulsory_edu_yrs'].hist()

plt.xlabel("compulsory_edu_yrs")
plt.show()
#pct_female_employment -> median
world_df_dropped['pct_female_employment'].hist()

plt.xlabel("pct_female_employment")
plt.show()
#pct_male_employment -> median
world_df_dropped['pct_male_employment'].hist()

plt.xlabel("pct_male_employment")
plt.show()

#pct_agriculture_employment -> median
world_df_dropped['pct_agriculture_employment'].hist()

plt.xlabel("pct_agriculture_employment")
plt.show()
#pct_industry_employment -> median
world_df_dropped['pct_industry_employment'].hist()

plt.xlabel("pct_industry_employment")
plt.show()
#pct_services_employment -> median
world_df_dropped['pct_services_employment'].hist()

plt.xlabel("pct_services_employment")
plt.show()
#exports_pct_gdp -> median
world_df_dropped['exports_pct_gdp'].hist()

plt.xlabel("exports_pct_gdp")
plt.show()
#fdi_pct_gdp -> median
world_df_dropped['fdi_pct_gdp'].hist()

plt.xlabel("fdi_pct_gdp")
plt.show()
#gdp_usd -> median
world_df_dropped['gdp_usd'].hist()

plt.xlabel("gdp_usd")
plt.show()
#gdp_growth_pct -> mean
world_df_dropped['gdp_growth_pct'].hist()

plt.xlabel("gdp_growth_pct")
plt.show()
#internet_usage_pct -> median
world_df_dropped['internet_usage_pct'].hist()

plt.xlabel("internet_usage_pct")
plt.show()
#child_mortality_per_1k -> median
world_df_dropped['child_mortality_per_1k'].hist()

plt.xlabel("child_mortality_per_1k")
plt.show()
#avg_air_pollution -> median
world_df_dropped['avg_air_pollution'].hist()

plt.xlabel("avg_air_pollution")
plt.show()
#women_in_parliament -> median
world_df_dropped['women_in_parliament'].hist()

plt.xlabel("women_in_parliament")
plt.show()
#unemployment_pct -> median
world_df_dropped['unemployment_pct'].hist()

plt.xlabel("unemployment_pct")
plt.show()
#urban_population_pct -> median
world_df_dropped['urban_population_pct'].hist()

plt.xlabel("urban_population_pct")
plt.show()
#urban_population_growth_pct -> mean
world_df_dropped['urban_population_growth_pct'].hist()

plt.xlabel("urban_population_growth_pct")
plt.show()

#outliers
region_df.boxplot(                    
column = ['CO2_emissions_per_capita)'],                                      
vert = False,                        
manage_xticks = True,                
patch_artist = False,                
meanline = True,                     
showmeans = True)                    


plt.title("CO2")       
plt.suptitle("")                  
plt.savefig('CO2.png')
plt.show()


"""Fill NAs out with mean or median"""
world_df_dropped_fill  = pd.DataFrame.copy(world_df_dropped)

col_mean = world_df_dropped_fill.loc[ : , ['compulsory_edu_yrs', 'gdp_growth_pct', 'urban_population_growth_pct']].mean()   
world_df_dropped_fill.loc[ : , ['compulsory_edu_yrs', 'gdp_growth_pct', 'urban_population_growth_pct']] = world_df_dropped_fill.loc[ : , ['compulsory_edu_yrs', 'gdp_growth_pct', 'urban_population_growth_pct']].fillna(col_mean)

col_median = world_df_dropped_fill.loc[ : , ['urban_population_pct','unemployment_pct','women_in_parliament','avg_air_pollution','child_mortality_per_1k','internet_usage_pct', 'gdp_usd','fdi_pct_gdp','exports_pct_gdp','pct_services_employment', 'pct_industry_employment','pct_agriculture_employment','pct_male_employment','pct_female_employment','CO2_emissions_per_capita)', 'access_to_electricity_urban','access_to_electricity_rural', 'access_to_electricity_pop']].median()   
world_df_dropped_fill.loc[ : , ['urban_population_pct','unemployment_pct','women_in_parliament','avg_air_pollution','child_mortality_per_1k','internet_usage_pct', 'gdp_usd','fdi_pct_gdp','exports_pct_gdp','pct_services_employment', 'pct_industry_employment','pct_agriculture_employment','pct_male_employment','pct_female_employment','CO2_emissions_per_capita)', 'access_to_electricity_urban','access_to_electricity_rural', 'access_to_electricity_pop']] = world_df_dropped_fill.loc[ : , ['urban_population_pct','unemployment_pct','women_in_parliament','avg_air_pollution','child_mortality_per_1k','internet_usage_pct', 'gdp_usd','fdi_pct_gdp','exports_pct_gdp','pct_services_employment', 'pct_industry_employment','pct_agriculture_employment','pct_male_employment','pct_female_employment','CO2_emissions_per_capita)', 'access_to_electricity_urban','access_to_electricity_rural', 'access_to_electricity_pop']].fillna(col_median)

world_df_dropped_fill.isnull().any()


""""Get means for all the sections"""
world_df_mean = world_df.groupby(['Hult_Team_Regions']).mean()


"""We will give rank for each region"""
world_df_rank = world_df_mean.rank()

"""Calcurate sum up all the ranks"""
world_df_rank.info()
world_df_rank.loc[:, 'CO2_emissions_per_capita)'] = world_df_rank['CO2_emissions_per_capita)'] - 13
world_df_rank.loc[:, 'child_mortality_per_1k'] = world_df_rank['child_mortality_per_1k'] - 13
world_df_rank.loc[:, 'unemployment_pct'] = world_df_rank['unemployment_pct'] - 13
world_df_rank_abs = world_df_rank.abs()


"""We made rank for each section BUT didn't include gender employment because they show family worker rate"""
economics_rank = world_df_rank_abs["gdp_usd"] + world_df_rank_abs["income_index"] + world_df_rank_abs["gdp_usd"] + world_df_rank_abs["gdp_growth_pct"] + world_df_rank_abs["pct_agriculture_employment"] + world_df_rank_abs["pct_industry_employment"] + world_df_rank_abs["pct_services_employment"] + world_df_rank_abs["exports_pct_gdp"] + world_df_rank_abs["fdi_pct_gdp"] + world_df_rank_abs["unemployment_pct"]
print(economics_rank) # wanna sort()

#number's to be filled
wellbeing_rank = world_df_rank_abs["income_index"] + world_df_rank_abs["child_mortality_per_1k"]
print(wellbeing_rank)

development_rank = world_df_rank_abs["internet_usage_pct"] + world_df_rank_abs["access_to_electricity_pop"] + world_df_rank_abs["women_in_parliament"] + world_df_rank_abs["urban_population_pct"] + world_df_rank_abs["compulsory_edu_yrs"]
print(development_rank)


"""We want to know what is causing this"""

"""Correlation Analysis to see the relationship of every column"""
corr_world_df = world_df_dropped_fill.corr()


"""Divide reagions based on income with histgram insight"""
world_df_mean['income_index'].hist()


"""Income level looks affective to many columns. Let's futher investigate!"""

"""To investigate the affects of income level well, we divided them into 
4 groups depends on the income level

___________________________________________________________
group1

Northern Europe and Northern Americas    3.952381
Greater Mediteranian Region              3.785714
___________________________________________________________
group2

Southern Latin America / Caribbean       3.285714
Northern Latin America / Caribbean       3.285714
Europe                                   3.200000
___________________________________________________________
group3

Middle East & North Africa               2.952381
Nothern Asia and Northern Pacific        2.909091
Southern Asia and Southern Pacific       2.608696
Central Asia and some Europe             2.500000
___________________________________________________________
group4

Southern Africa                          2.133333
Central Aftica 1                         1.642857
Central Africa 2                         1.125000
"""


"""Devide them into groups"""

for row in enumerate(world_df_dropped_fill.loc[ : , 'Hult_Team_Regions']):
    if row[1] == "Greater Mediteranian Region" or row[1] == "Northern Europe and Northern Americas":
        world_df_dropped_fill.loc[row[0],'group_num'] = 1
        print(row[1])
    elif row[1] == "Southern Latin America / Caribbean" or row[1] == "Northern Latin America / Caribbean" or row[1] == "Europe":
        world_df_dropped_fill.loc[row[0],'group_num'] = 2
        print(row[1])
    elif row[1] == "Middle East & North Africa" or row[1] == "Nothern Asia and Northern Pacific" or row[1] == "Southern Asia and Southern Pacific" or row[1] == "Central Asia and some Europe":
        world_df_dropped_fill.loc[row[0],'group_num'] = 3
        print(row[1])
    elif row[1] == "Southern Africa" or row[1] == "Central Aftica 1" or row[1] == "Central Africa 2":
        world_df_dropped_fill.loc[row[0],'group_num'] = 4
        print(row[1])
    else:
        world_df_dropped_fill.loc[row[0],'group_num'] = "Error"
        print(row[1])


sns.barplot(x = world_df_dropped_fill['group_num'],
            y =  world_df_dropped_fill['pct_services_employment']
            )
plt.savefig('data1')

sns.barplot(x = world_df_dropped_fill['group_num'],
            y =  world_df_dropped_fill['internet_usage_pct']
            )
plt.savefig('data2')


sns.barplot(x = world_df_dropped_fill['group_num'],
            y =  world_df_dropped_fill['child_mortality_per_1k']
            )
plt.savefig('data3')


sns.barplot(x = world_df_dropped_fill['group_num'],
            y =  world_df_dropped_fill['urban_population_pct']
            )
plt.savefig('data4')





























