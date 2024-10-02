# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:37:50 2024

@author: akhta
"""

class Doctor():
    def __init__(self):
        print("this is parent class doctor")
    def BMI(weight,height):
        bmi = weight/(height*height)
        print("your BMI is" + str(bmi))
    def heart_rate(heartrate):
        if(heartrate>60 and heartrate<100):
            print("your heart rate is normal")
        else:
            print("your heart rate is not normal")
            
class Patient(Doctor):
    def __init__(self,name,weight,height,heartrate):
        print("this is patient class")
        self.patientname = name
        self.patientweight = weight
        self.patientheight = height
        self.patientheartrate = heartrate
    def healthcheck(self):
        print("Patient name: " , self.patientname)
        Doctor.BMI(self.patientweight,self.patientheight)
        Doctor.heart_rate(self.patientheartrate)
        
patient1 = Patient("Mumtaz",62,5.4,80)
patient1.healthcheck()
    
            
        