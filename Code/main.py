from  tqdm.auto import tqdm
import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.shared import Cm, Inches
from docx.shared import Pt
import math
import numpy as np
import matplotlib.pyplot as plt
import os
from queue import PriorityQueue


def main():
    document = docx.Document("test3.docx")
    output_error = "All Errors found:"
    name_list = check_dir()
    queue = priority_queue(name_list)
    user_dict= get_user_data()
    compressor_name_tup, motor_power_tup,  rated_flow_tup, manufacturing_year_tup = get_user_data()
    n= len(compressor_name_tup)
    compressor_table(n, compressor_name,motor_power,rated_flow,manufacturing_year )
    for i in compressor_names:
        if i not in name_list:
            output_error+ =(f"\nError: compressor {i} not in directory folder")
            continue
        
        
    
