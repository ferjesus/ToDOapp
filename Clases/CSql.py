import hashlib
import psycopg2
import json

class CSql():
    def __init__(self):
        # type: () -> object
        self.h = None

    def omConnect(self, p_cDB = None):
        llOk = True
        #lcConnect = "host=10.0.159.15 dbname=FTIA user=postgres password=postgres port=5432"
        if p_cDB == 1:
            lcConnect = "host=ec2-174-129-35-61.compute-1.amazonaws.com dbname=d54ven2n5jfj2l user=vqvkkupindvoln password=2f7843a76d0d57efd3403b737dd4a89de04723a6d13b29f4bb673d261990d3ea port=5432"
        else:
            lcConnect = "host=ec2-174-129-35-61.compute-1.amazonaws.com dbname=d54ven2n5jfj2l user=vqvkkupindvoln password=2f7843a76d0d57efd3403b737dd4a89de04723a6d13b29f4bb673d261990d3ea port=5432"
        #print 'Conectando ...'
        try:
           self.h = psycopg2.connect(lcConnect) 
        except psycopg2.DatabaseError:
           print ('Error conectando ...')
           llOk = False
           self.pcError = 'ERROR AL CONECTAR CON LA BASE DE DATOS11'
        return llOk

    def omExecRS(self, p_cSql):
        #print p_cSql
        lcCursor = self.h.cursor()
        try: 
          lcCursor.execute(p_cSql)

        except psycopg2.Error as e:
          print e
          return None

        RS = lcCursor.fetchall()
        '''
        if len(RS) == 0:
           RS = None

        try:
           i = RS[0]
        except:
           RS = None
        '''
        return RS

    def omExec(self, p_cSql):
#        print p_cSql
        llOk = True
        lcCursor = self.h.cursor()
        try:
           lcCursor.execute(p_cSql)
        except Exception as E:
           print (type(E) )    # the exception instance
           print (E.args)      # arguments stored in .args
           print (E)           # __str__ allows args to printed directly:
           print ('***')
           llOk = False
        return llOk

    def omDisconnect(self):
        self.h.close()

    def omCommit(self):
        self.h.commit()

