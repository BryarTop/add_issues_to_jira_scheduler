import xml_template as xt
import pandas as pd 
import numpy as np
import xml.dom.minidom as minidom 

filepath = '/Users/bryar.topham/Documents/CS/My Data Sources/python/work/jira_xml_import/'
file = 'finished_import_template.csv'

df = pd.read_csv(filepath + file, encoding='UTF-8', sep= ',')
df = df.replace(np.nan,'') #insert blank values in place of nan
master_xml_string = ''

def build_params(data_f, row_idx):
    rtn_list = []
    for i in range(4,27):
        if i not in [21,24,25]: 
            rtn_list.append(data_f.iloc[row_idx,i])
    return rtn_list

def convert_to_xml(xml_str):
    doc = minidom.parseString(xml_str)
    return doc.toxml()

master_xml_string += xt.make_header()
for idx in range(len(df)):
    master_xml_string += xt.make_scheduled_issue_info(df.iloc[idx,0])
    cadence = xt.__make_interval_helper__(df.iloc[idx,15])
    master_xml_string += xt.make_interval(df.iloc[idx,1],cadence)
    master_xml_string += xt.define_body_elements()
    master_xml_string += xt.define_body_params(*build_params(df,idx))
    break
master_xml_string += xt.make_footer()

with open("output.txt","w") as text_file:
    text_file.write(master_xml_string)
#export xmlstring as xmldoc

