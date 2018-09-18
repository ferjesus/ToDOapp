import datetime
from datetime import timedelta


class CBase:

   def __init__(self):
       self.pcError = None
       self.loSql   = None

class CDate(CBase):
   pcClave = None
   
   def valDate(self, p_cFecha):
       llOk = True
       try:
          ldFecha = datetime.datetime.strptime(p_cFecha, "%Y-%m-%d").date()
       except:
          llOk = False
       return llOk
  
   def add(self, p_cFecha, p_nDias):
       llOk = self.valDate(p_cFecha)
       if not llOk:
          return None
       ldFecha = self.mxValDate(p_cFecha)
       ldFecha = ldFecha + timedelta(days = p_nDias)
       return ldFecha.strftime('%Y-%m-%d')
      
   def diff(self, p_cFecha1, p_cFecha2):
       llOk = self.valDate(p_cFecha1)
       if not llOk:
          return None
       llOk = self.valDate(p_cFecha2)
       if not llOk:
          return None
       ldFecha1 = self.mxValDate(p_cFecha1)
       ldFecha2 = self.mxValDate(p_cFecha2)
       d = ldFecha1 - ldFecha2
       return d.days

   def dow(self, p_cFecha):
       llOk = self.valDate(p_cFecha)
       if not llOk:
          return None
       ldFecha = self.mxValDate(p_cFecha)
       return ldFecha.weekday()

   def day(self, p_cFecha):
       llOk = self.valDate(p_cFecha)
       if not llOk:
          return None
       ldFecha = self.mxValDate(p_cFecha)
       return int(ldFecha.strftime('%d'))

   def month(self, p_cFecha):
       llOk = self.valDate(p_cFecha)
       if not llOk:
          return None
       ldFecha = self.mxValDate(p_cFecha)
       return int(ldFecha.strftime('%m'))

