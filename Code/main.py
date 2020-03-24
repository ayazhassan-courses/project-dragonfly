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
    name_list = check_dir()
    queue = priority_queue(name_list)
    user_dict= get_user_data()
    end_compressor_names = False
    for i in queues:
        if i == "mainline":
            end_compressor_names = True
        nested_list = getdata(i)
        getvalues(nested_list, min_limitflow)
        if end_compressor_names == False:
            compressor_table(n,i,user_dict[i][0],user_dict[i][1],user_dict[i][2] )   #(number of compressor , name of compressor ,motor power , rated_flow, manufacturing_year)
        if end_compressor_names == True:
    
