import serial
import os.path

def main()
     serialIO=init()
     while True :
       	r_rpm = rpm(serialIO)
       	r_ect = ect(serialIO)
       	r_eot = eot(serialIO)
	r_speed = speed(serialIO)
	r_volt = volt(serialIO)
       	r_stf1 = stf1(serialIO)
       	r_stf2 = stf2(serialIO)
       	r_ltf1 = ltf1(serialIO)
	r_ltf2 = ltf2(serialIO)
	r_fp = fp(serialIO)
   	r_tp = tp(serialIO)
	r_oxy1 = oxy1(serialIO)
	r_oxy2 = oxy2(serialIO)           
	r_ta = ta(serialIO)           

  	print "speed : " , r_speed , " km/h"
	print "rpm : " , r_rpm
	print "ect : " , r_ect , " C"
	print "eot : " , r_eot , " C"
	print "volt : ", r_volt , " V"
 	print "stf1 : " , r_stf1 , " %"
	print "stf2 : " , r_stf2 , " %"
	print "ltf1 : " , r_ltf1 , " %"
	print "ltf2 : " , r_ltf2 , " %"
	print "fp : ", r_fp , " KPa"
	print "tp : " , r_tp , " %"
	print "oxy1 : " , r_oxy1 , " ratio"
	print "oxy2 : ", r_oxy2 , " ratio"
	print "ta : ", r_ta , " TDC"

def init():
    try:
      serialIO = serial.Serial("/dev/tty"+dev, 38400, timeout=1)
      return serialIO
    except:
      print "Initialize Error!"

def speed(serialIO):
    #time.sleep(0.01)
    try:
        serialIO.write("01 0D \r")
        line_speed = serialIO.readline().split(" ")
        speed = int("0x"+line_speed[4], 16)
        return speed
    except:
        return 0

def rpm(serialIO):
    #time.sleep(0.03)
    try:
        serialIO.write("01 0C \r") 
        line_rpm = serialIO.readline().split(" ")
        rpm = int("0x"+line_rpm[4]+line_rpm[5], 16)/4
        return rpm
    except:
        return 0


def tp(serialIO):
    #time.sleep(0.07)
    try:
        serialIO.write("01 11 \r")
        line_tp = serialIO.readline().split(" ")
        tp = int("0x"+line_tp[4], 16)*100/255
        return tp
    except:
        return 0

def ect(serialIO):
    #time.sleep(0.07)
    try:
        serialIO.write("01 05 \r")
        line_ect = serialIO.readline().split(" ")
        ect = int("0x"+line_ect[4], 16)-40
        return ect
    except:
        return 0

def eot(serialIO):
    #time.sleep(0.07)
    try:
        serialIO.write("01 5C \r")
        line_eot = serialIO.readline().split(" ")
        eot = int("0x"+line_eot[4], 16)-40
        return eot
    except:
        return 0

def stf1(serialIO):
    #time.sleep(0.07)
    try:
        serialIO.write("01 06 \r")
        line_stf1 = serialIO.readline().split(" ")
        stf1 = int("0x"+line_stf1[4], 16)*100/128
        return stf1-100
    except:
        return 0

def ltf1(serialIO):
    #time.sleep(0.07)
    try:
        serialIO.write("01 07 \r")
        line_ltf1 = serialIO.readline().split(" ")
        ltf1 = int("0x"+line_ltf1[4], 16)*100/128
        return ltf1-100
    except:
        return 0

def stf2(serialIO):
    #time.sleep(0.07)
    try:
        serialIO.write("01 08 \r")
        line_stf2 = serialIO.readline().split(" ")
        stf2 = int("0x"+line_stf2[4], 16)*100/128
        return stf2-100
    except:
        return 0

def ltf2(serialIO):
    #time.sleep(0.07)
    try:
        serialIO.write("01 09 \r")
        line_ltf2 = serialIO.readline().split(" ")
        ltf2 = int("0x"+line_ltf2[4], 16)*100/128
        return ltf2-100
    except:
        return 0

def fp(serialIO):
    #time.sleep(0.07)
    try:
        serialIO.write("01 0A \r")
        line_fp = serialIO.readline().split(" ")
        fp = int("0x"+line_fp[4], 16)*3
        return fp
    except:
        return 0

def volt(serialIO):
    #time.sleep(0.07)
    try:
        serialIO.write("01 42 \r")
        line_volt = serialIO.readline().split(" ")
        volt = int("0x"+line_volt[4]+line_volt[5], 16)/1000
        return volt-100
    except:
        return 0

def oxy1(serialIO):
    #time.sleep(0.07)
    try:
        serialIO.write("01 34 \r")
        line_oxy1 = serialIO.readline().split(" ")
        oxy1 = int("0x"+line_oxy1[4]+line_oxy1[5], 16)/256
        return oxy1-128
    except:
        return 0

def oxy2(serialIO):
    #time.sleep(0.07)
    try:
        serialIO.write("01 35 \r")
        line_oxy2 = serialIO.readline().split(" ")
        oxy2 = int("0x"+line_oxy2[4]+line_oxy2[5], 16)/256
        return oxy2-128
    except:
        return 0

def ta(serialIO):
    #time.sleep(0.07)
    try:
        serialIO.write("01 0E \r")
        line_ta = serialIO.readline().split(" ")
        ta = int("0x"+line_ta[4], 16)/2
        return ta-64
    except:
        return 0





    


    

        
    
    
