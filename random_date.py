import random
import time 
def get_random_date(startdt,enddt):
    print("printing random date between",startdt, "and",enddt)
    randomGenrator= random.random()
    dateformat= '%m/%d/%Y'
    starttime=time.mktime(time.strptime(startdt,dateformat))
    endtime=time.mktime(time.strptime(enddt,dateformat))
    randomtime=starttime + randomGenrator * (endtime-starttime)
    randomdate= time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("random date =",get_random_date,"05/20/2013","12/04/2012")