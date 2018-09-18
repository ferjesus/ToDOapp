# import psycopg2
from CBase import *
from CSql import *
import json

# ============================================
# Clase que gestiona las tareas
# ============================================
class CTarea(CBase):

    def __init__(self):
        self.pcParams = None
        self.pcData   = None
        self.laParams = []


    # ------------------------------------------
    # CONSULTA DE TAREAS
    # ------------------------------------------
    def omConsultaTareas(self):
        self.loSql = CSql()
        llOK = self.loSql.omConnect()
        if not llOK:
           self.pcError = self.loSql.pcError
           return False
        llOk = self.mxConsultaTareas()
        self.loSql.omDisconnect()
        return llOk


    def mxConsultaTareas(self):
        print '1111111'
        laDatos = []
        lcSql = "SELECT cCodTar, cDescri, cEstado, TO_CHAR(DFECHA, 'DD-MM-YYYY') FROM A01TTAR"
        R1 = self.loSql.omExecRS(lcSql)
        if not R1:
           print lcSql
           self.pcError = '{"ERROR": "SENTENCIA SQL  INVALIDA"}'
           return False
        i = 0
        for laFila in R1:
            i += 1
            laTmp = {"CCODTAR": laFila[0], "CDESCRI": laFila[1].strip(),"CESTADO": laFila[2].strip(),"DFECHA": laFila[3]}
            laDatos.append(laTmp)
        if i == 0:
           self.pcError = '{"ERROR": "NO SE ENCUENTRA DATOS"}'
           return False
        self.pcData = json.dumps(laDatos)
        return True
    # ------------------------------------------
    # Registro de Tarea
    # ------------------------------------------
    def omRegistroTarea(self):
        llOk = self.mxValParamRegistroTarea()
        if not llOk:
            return False
        self.loSql = CSql()
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.mxRegistroTarea()
        self.loSql.omDisconnect()
        return llOk

    def mxValParamRegistroTarea(self):
        try:
           self.laParams = json.loads(self.pcParam)
        except:
           self.pcError = '{"ERROR": "ERROR EN PARAMETROS JSON"}'
           return False
        if not 'CNRORUC' in self.laParams:
           self.pcError = '{"ERROR": "PARAMETRO DESCRI NO DEFINIDO"}'
           return False
        return True

    def mxRegistroTarea(self):
        lcSql = "SELECT P_A01TTAR_1('%s');"%(self.pcParam)
        print lcSql
        R1 = self.loSql.omExecRS(lcSql)
        if not R1:
           print lcSql
           self.pcError = '{"ERROR": "SENTENCIA SQL (02) INVALIDA"}'
           return False
        self.pcData = R1[0][0]
        llOk = True
        try:
           laTmp = json.loads(self.pcData)
        except:
           print self.pcData
           self.pcError = '{"ERROR": "VALOR DE RETORNO DE SENTENCIA SQL (02) INVALIDO"}'
           return False
        if 'ERROR' in laTmp:
           self.pcError = self.pcData
           return False
        return True






    