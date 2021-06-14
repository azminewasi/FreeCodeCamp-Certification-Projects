def add_time(start, duration, wday=False):

  from math import floor

  weekday=["saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
  wd_c=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]

  st=start.split()
  stt=st[0].split(":")
  dtt=duration.split(":")
  ampm=st[1]
  if ampm=="PM":
    stt_f=[int(stt[0])+12,int(stt[1])]
  else:
    stt_f=[int(stt[0]),int(stt[1])]

  dtt_f=[int(dtt[0]),int(dtt[1])]
  
  day=floor(dtt_f[0]/24)
  dtt_f[0]=dtt_f[0]%24

  ad=[dtt_f[0]+stt_f[0],dtt_f[1]+stt_f[1]]
  if ad[1]>=60:
    ad[0]=ad[0]+floor(ad[1]/60)
    ad[1]=ad[1]%60
  if ad[0]>=24:
    day=day+floor(ad[0]/24)
    ad[0]=ad[0]%24
  
  if ad[0]>=12:
    ampm="PM"
    ad[0]=ad[0]-12
  else:
    ampm="AM"
  if ad[0]==0:
    ad[0]=12

  day_str=''
  if day==0:
    day_str=""
  elif (day==1):
    day_str=" (next day)"
  else:
    day_str=" ("+str(day)+" days later)"
  
  new_time=str(ad[0])+":"+str(ad[1]).zfill(2)+" "+ampm+day_str  
  
  if wday!=False:
    wday=wday.lower()
    wday_n=weekday.index(wday)
    wday_n=((wday_n+day+1)%7)-1
    new_time=str(ad[0])+":"+str(ad[1]).zfill(2)+" "+ampm+", "+wd_c[wday_n]+day_str  

  return new_time