# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 01:30:51 2021

@author: Asus
"""

import csv

def write_into_csv(info_list):
    with open('student_info_csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact number","E-mail ID"])
        
        writer.writerow(info_list)
if __name__ == '__main__':
    condition =True
    
    while(condition):
        student_info=input("enter the student information as (name age cintact_number email):")
        
        student_info_list= student_info.split(' ')
        
        
        print("the entered information is- \nName:{}\nAge:{}\nContact_number:{}\ne-mail:{}"
              .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input("is the entered information correcr(yes/no)?")
        if choice_check=="yes":
             write_into_csv(student_info_list)
             
             condition_check=input("do you want to enter information for another student(yes/no)?")
             if condition== "yes":
                 condition= True
             elif condition_check=="no":
                condition= False
           
        elif choice_check=="no":
            print("\nPlease re-enter the information")
            
            
        
        
            