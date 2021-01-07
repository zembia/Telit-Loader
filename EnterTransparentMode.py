#Ejecutar con F5 y usar el Python Shell.
#para instalar pip install curses-menu
#from cursesmenu import SelectionMenu

import serial
from serial.tools import list_ports
from struct import unpack
import time
import os
import time
import sys

XPOS = float(0)
YPOS = float(0)
ZPOS = float(0)
temp = 0
ACCX = float(0)
ACCY = float(0)
ACCZ = float(0)
HORA = float(0)
MINUTOS = float(0)
SEGUNDOS = float(0)
MILESIMAS = float(0)
GYROX     = float(0)
GYROY     = float(0)
GYROZ     = float(0) 
LAT = float(0)
LON = float(0)
VELOCIDAD = float(0)
TEMPERATURE = 0

def PrintDir(): #Imprime directorios.
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(1));
    RS232.write(chr(0));
    Ristra = "Directorios:"+'\n' + '\r'
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'

def PrintFiles(): #Imprime archivos
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(2));
    RS232.write(chr(0));
    Ristra = "Archivos:"+'\n' + '\r'
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'
        
def EraseFiles(Erase): #Borra archivos
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(12));
    RS232.write(Erase);
    RS232.write(chr(0));
    Ristra = ''
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'  



def Change_Dir(Dir): #Cambia al directorio solicitado ("\\" para directorio raiz)
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(3));
    RS232.write(Dir);
    RS232.write(chr(0));
    Ristra = '';
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'  


def Get_Size(FileName):
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(4));
    RS232.write(FileName);
    RS232.write(chr(0));
    Ristra=''
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                break;
    except:
        print 'Error'
    
    return int(Ristra)

def Get_Mag():
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(9));
    RS232.write(chr(0));
    Ristra=''
    
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'
        
def Add_Mag_Offset(X,Y,Z):
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(10));

    X1 = int(X);
    X2 = int((X - int(X))*10);
    
    Y1 = int(Y);
    Y2 = int((Y - int(Y))*10);

    Z1 = int(Z);
    Z2 = int((Z - int(Z))*10);
    
    if (X1 <0):
        X1 = X1 + 256;
    if (X2 <0):   
        X2 = X2 + 256;

    if (Y1 <0):
        Y1 = Y1 + 256;
    if (Y2 <0):        
        Y2 = Y2 + 256;
    if (Z1 < 0):
        Z1 = Z1 + 256;
    if (Z2 <0):    
        Z2 = Z2 + 256;

        
    RS232.write(chr(X1));
    RS232.write(chr(X2));
    RS232.write(chr(Y1));
    RS232.write(chr(Y2));
    RS232.write(chr(Z1));
    RS232.write(chr(Z2));

    
    RS232.write(chr(0));
    Ristra=''
    
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'
        
def Save_ACC_Offset():
    
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(11));
    RS232.write(chr(0));
    Ristra=''
    
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'
    
def Cal_ACC_XY():
    
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(16));
    RS232.write(chr(0));
    Ristra=''
    
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'
        
def Cal_ACC_Z():
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(17));
    RS232.write(chr(0));
    Ristra=''
    
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'
def Reset_ACC():   
    
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(18));
    RS232.write(chr(0));
    Ristra=''
    
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'

def Set_Base():
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(15));
    RS232.write(chr(0));
    Ristra=''
    
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'   

def TransferFile(FileName,Device=''): #Transfiere el archivo de la ristra FileName (Necesita Halt System)

    
    RS232.flushInput();
    size = Get_Size(FileName);
    ORIG_SIZE = size;
    #digits = 14+len(str(FileName));
    #delete = "\b" * (digits);    
    #print  " Transfiriendo:",  FileName,
    #print FileName, end='\r'
    #print "-Size:",
    #print "%.2f kB" % (size/1024.0)
    #print "-ETA:", (size/164556.5), "a", (size/60000.0), "segundos"

    if (len(Device)>0):
        MyDir = os.path.join(Device,GetCurrentDir())
        #print "Directorio: ", MyDir
        try:
            os.stat(Device)
        except:
            os.mkdir(Device)
    else:
        MyDir = GetCurrentDir();
    try:
        os.stat(MyDir)
    except:
        os.mkdir(MyDir)

    
    file = open(os.path.join(MyDir,FileName), "wb")
    Burst_Size = 256;
    start = time.time()
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));   
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(5));
    RS232.write(FileName);
    RS232.write(chr(0));
    counter = int(0);

    Ristra=''
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                if (len(Ristra)>0):
                    print '***RESPUESTA:', Ristra,'***'
                break;
    except:
        print '***Error en transferencia***'
    
    if(RS232.closed==False):
        while (size > 0):
            if (size > Burst_Size):
                CHAR= RS232.read(Burst_Size)
                size = size - Burst_Size;
                #if (counter == 200):
                #    print "Transfer: ",100*(ORIG_SIZE-size)/ORIG_SIZE,'%'
                #    counter = 0;
                #else:
                #    counter = counter + 1;
                
                #progress = 100*(ORIG_SIZE-size)/ORIG_SIZE;
            else:
                CHAR= RS232.read(size)
                size = 0;
            file.write(bytearray(CHAR))
        file.close();
    end = time.time()
    Tiempo = (end-start);
    Speed = float(ORIG_SIZE/(Tiempo+0.01));
    #print "-Transferencia lista: %.2f kB/s\r\n" % (Speed/1024)
    #CONVERTIR DATOS
       
def Halt_System():
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(6));
    RS232.write(chr(0));
    Ristra=''
    time.sleep(1)
    #try:
    while(RS232.closed==False):
        CHAR= RS232.read(1)
        if (CHAR[0] != '$'):
            pass
        else:
            break
    while(RS232.closed==False):
        CHAR= RS232.read(1)
        if (ord(CHAR[0]) != 0):
            Ristra = Ristra + CHAR[0]
        else:
            print Ristra
            break;
    #except:
        #print 'Error'

def Reset_System(): #Resetea el sistema.
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(8));
    RS232.write(chr(0));
    Ristra=''
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'
    RS232.close()
        

def Query_Debug_Data():
    global LAT, LON, XPOS, YPOS, ZPOS,ACCX,ACCY,ACCZ, HORA, MINUTOS,SEGUNDOS, MILESIMAS, GYROX,GYROY,GYROZ,VELOCIDAD,TEMPERATURE
    RS232.flushInput();
    
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(7));
    RS232.write(chr(0));
    Ristra = ''
    while(RS232.closed==False):
        CHAR= RS232.read(1)
        if (CHAR[0] != '$'):
            pass
        else:
            break
    while(RS232.closed==False):
        CHAR= RS232.read(1)
        if (ord(CHAR[0]) != 0):
            Ristra = Ristra + CHAR[0]
        else:
            print Ristra
            break;
    try:
        buf = RS232.read(1) #Leer Hora.
        temp = unpack('>B', buf);

        HORA = float(temp[0])
        buf = RS232.read(1) #Leer Minutos.
        temp = unpack('>B', buf);

        MINUTOS = float(temp[0])
        buf = RS232.read(1) #Leer Segundos.
        temp = unpack('>B', buf);

        SEGUNDOS = float(temp[0])
        buf = RS232.read(1) #Leer milesimas
        temp = unpack('>B', buf);
        MILESIMAS = float(temp[0])*10

        #GYROSCOPIO
        buf = RS232.read(2) #Leer gyro.x
        temp = unpack('>h', buf)
        GYROX = temp[0] #Gyro X en grados por segundo.

        buf = RS232.read(2) #Leer gyro.y
        temp = unpack('>h', buf)
        GYROY = temp[0] #Gyro Y en grados por segundo.

        buf = RS232.read(2) #Leer gyro.z
        temp = unpack('>h', buf)
        GYROZ = temp[0] #Gyro Z en grados por segundo.

        #ACELERACION (Medidas en cuentas digitales ya que no fue necesario convertirlas internamente
        #pues las unidades se cancelaban)

        buf = RS232.read(2) #Leer ACC.x
        temp = unpack('>h', buf)
        ACCY = float(temp[0]) #ACC X.

        buf = RS232.read(2) #Leer ACC.y
        temp = unpack('>h', buf)
        ACCX = float(temp[0]) #ACC Y.

        buf = RS232.read(2) #Leer ACC.z
        temp = unpack('>h', buf)
        ACCZ = float(temp[0]) #ACC Z.

                                                
        #Leer Posicion X (Es posible tener que ajustar los signos y/o que YPOS sea XPOS o biceversa, no recuerdo como era)
        buf  = RS232.read(2)
        temp = unpack('>h', buf)
        XPOS = -float(temp[0])/100
        #Leer Posicion Y                 
        buf  = RS232.read(2)
        temp = unpack('>h', buf)
        YPOS = float(temp[0])/100
        #Leer Posicion Z (Dummy)        
        buf  = RS232.read(2)
        temp = unpack('>h', buf)
        ZPOS = float(temp[0])/100

        #leer GPS
        #Longitud
        buf  = RS232.read(4)
        temp = unpack('>f', buf)
        LON = float(temp[0])
        #Latitud
        buf = RS232.read(4)
        temp = unpack('>f', buf)
        LAT = float(temp[0])
        #Velocidad
        buf = RS232.read(2) #Leer velocidad
        temp = unpack('>h', buf)
        VELOCIDAD = float(temp[0]) #Velocidad.

        #TEMPERATURA
        buf  = RS232.read(2)
        temp = unpack('>h', buf)
        TEMPERATURE = temp[0]
    except:
        print "Error"

def GetCurrentDir():
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(13));
    RS232.write(chr(0));
    Ristra = '';
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1) 
            if (ord(CHAR[0]) != 0):
                if (CHAR[0] != '\\'):
                    Ristra = Ristra + CHAR[0]
            else:
                break;
    except:
        print 'Error en GetCWD'
        
    return Ristra
    
def CopyAll():
    #MyDevice = GetID();
    MyDevice = 'AABBCC'
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(2));
    RS232.write(chr(0));
    nn=0;
    Ristra = '';
    Lista_Archivos = list();
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                if (CHAR[0] != '\n'  and  CHAR[0] != '\r'):
                    Ristra = Ristra + CHAR[0]
                elif (CHAR[0] == '\r'):
                    Lista_Archivos.append(Ristra)
                    Ristra = '';
            else:
                Lista_Archivos.append(Ristra);
                break;
        for Archivo in Lista_Archivos:
            TransferFile(Archivo,MyDevice);
    except:
        print 'Error en CopyAll'
    print 'IMPORTANTE: RECUERDE REINICIAR EL SISTEMA ANTES DE SALIR!!!'

def SetInstall(Number):
    if (Number.__len__()    != 8):
        print 'Numero debe de ser de 8 caracteres'
    else:    
        RS232.flushInput();
        RS232.write(chr(16));
        RS232.write(chr(18));
        RS232.write(chr(255));
        RS232.write(chr(4));
        RS232.write(chr(14));
        RS232.write(Number);
        RS232.write(chr(0));
        Ristra = '';
        try:
            while(RS232.closed==False):
                CHAR= RS232.read(1)
                if (CHAR[0] != '$'):
                    pass
                else:
                    break
            while(RS232.closed==False):
                CHAR= RS232.read(1)
                if (ord(CHAR[0]) != 0):
                    Ristra = Ristra + CHAR[0]
                else:
                    print Ristra
                    break;
        except:
            print 'Error en SetInstall'
        RS232.close()
    
def TransferAll():

    MyDevice = GetID();
    
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(2));
    RS232.write(chr(0));
    nn=0;
    Ristra = '';
    Lista_Archivos = list();
    
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                if (CHAR[0] != '\n'  and  CHAR[0] != '\r'):
                    Ristra = Ristra + CHAR[0]
                elif (CHAR[0] == '\r'):
                    Lista_Archivos.append(Ristra)
                    Ristra = '';
            else:
                Lista_Archivos.append(Ristra);
                break;

        for Archivo in Lista_Archivos:
            TransferFile(Archivo,MyDevice);
        EraseFiles('*.*');
    except:
        print 'Error en TransferAll'
    print 'IMPORTANTE: RECUERDE REINICIAR EL SISTEMA ANTES DE SALIR!!!'
        
def PrintAll():
    counter =0;
    while (1):
        try:    
            CHAR= RS232.read(1)
            print CHAR[0],
        except:
            counter= counter+1;
            if (counter == 10):
                break;
            else:
                pass
    

def GetID():
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(20));
    RS232.write(chr(0));
    Ristra=''
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            #print CHAR
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            #print CHAR
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
                #print Ristra
            else:
                break;
    except:
        print 'Error'
    if (len(Ristra)==0):
        print 'No existe ID'        
    else:
        return Ristra

def SetID():
    
    var = raw_input("Ingrese ID del camion: ")
    if (len(var)>16):
        print "El ID no puede ser de mas de 16 caracteres"
        return 'NOID'
    else:
        print "El id sera: ", var
        print var
        RS232.flushInput();
        RS232.write(chr(16));
        RS232.write(chr(18));
        RS232.write(chr(255));
        RS232.write(chr(4));
        RS232.write(chr(19));
        RS232.write(var);
        RS232.write(chr(0));
        Ristra = '';
        print var, Ristra
        try:
            while(RS232.closed==False):
                CHAR= RS232.read(1)
                if (CHAR[0] != '$'):
                    pass
                else:
                    break
            while(RS232.closed==False):
                CHAR= RS232.read(1)
                if (ord(CHAR[0]) != 0):
                    print var, Ristra
                    if (CHAR[0] != '\\'):
                        Ristra = Ristra + CHAR[0]
                        print Ristra
                else:
                    break;
        except:
            print var
            print 'Error en SetID ', Ristra, var
        print 'Ristra', Ristra
        return var;



def FullSDTransfer():
    #Directorio origen
    Origen = GetCurrentDir()
    #deteniendo el sistema
    Halt_System()
    #Directorio Raiz
    Change_Dir('\\')

    #Obtener lista de Directorios
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(1));
    RS232.write(chr(0));
    Ristra = '';
    Lista_Directorios = list();
    
    try:
        while(RS232.closed==False):
            CHAR = RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR = RS232.read(1)
            if (ord(CHAR[0])!=0):
                if (CHAR[0]!='\n' and CHAR[0] !='\r' and CHAR[0] !='.'):
                    Ristra = Ristra + CHAR[0]
                elif (CHAR[0] == '\r'):
                    if ( len(Ristra) > 0):
                        Lista_Directorios.append(Ristra)
                        print Ristra
                    Ristra = '';
            else:
                if ( len(Ristra) > 0):
                    Lista_Directorios.append(Ristra)
                    print Ristra
                break;
        for Directorio in Lista_Directorios:
            print 'Cambiando a:', Directorio
            Change_Dir(Directorio)
            TransferAll()
            Change_Dir('\\')
        #print 'IMPORTANTE: RECUERDE REINICIAR EL SISTEMA ANTS DE SALIR!!!'
        Reset_System()
        
    except:
        print 'Error en FullSDTransfer'

def FullSDCopy():
    #Directorio origen
    Origen = GetCurrentDir()
    #deteniendo el sistema
    Halt_System()
    #Directorio Raiz
    Change_Dir('\\')

    #Obtener lista de Directorios
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(1));
    RS232.write(chr(0));
    Ristra = '';
    Lista_Directorios = list();
    
    try:
        while(RS232.closed==False):
            CHAR = RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR = RS232.read(1)
            if (ord(CHAR[0])!=0):
                if (CHAR[0]!='\n' and CHAR[0] !='\r' and CHAR[0] !='.'):
                    Ristra = Ristra + CHAR[0]
                elif (CHAR[0] == '\r'):
                    if ( len(Ristra) > 0):
                        Lista_Directorios.append(Ristra)
                        print Ristra
                    Ristra = '';
            else:
                if ( len(Ristra) > 0):
                    Lista_Directorios.append(Ristra)
                    print Ristra
                break;
        for Directorio in Lista_Directorios:
            print 'Cambiando a:', Directorio
            Change_Dir(Directorio)
            CopyAll()
            Change_Dir('\\')        
        
        Reset_System()
        
    except:
        print 'Error en FullSDTransfer'            


def Write_File(FileName):
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(21)); #Codigo para transferencia de arhivo a SD
    RS232.write(FileName)
    RS232.write(chr(0));
    FileSize = os.stat(FileName).st_size
    FileSize_str = str(FileSize)
    RS232.write(FileSize_str)
    RS232.write(chr(0));

    TotalSize = FileSize;
    LastSize = TotalSize;
    f = open(FileName,'rb')

    start = time.time()
    
    while FileSize>0:
        if (FileSize>64):
            Data = f.read(64)
            
            RS232.write(Data)
            FileSize = FileSize-64
        else:
            Data = f.read(FileSize)
            RS232.write(Data)
            FileSize = 0
            
        if (time.time()-start >= 0.2):
            start = time.time()
            print("Progreso %.0f. Velocidad %.0f kbps" % ((TotalSize-FileSize)/float(TotalSize)*100, 8*(LastSize-FileSize)/(0.2*1024)))
            
            
            LastSize = FileSize
            
    print("Progreso %.0f. Velocidad %.0f kbps" % ((TotalSize-FileSize)/TotalSize*100, 0))            

    
    Ristra=''
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]            
            else:
                print Ristra
                break;
    except:
        print 'Error'
        

def Set_ALARM():
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(23));
    RS232.write(chr(0));
    Ristra=''
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'
def Set_ALARM_Battery():
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(25));
    RS232.write(chr(0));
    Ristra=''
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'
def Set_ALARM_Enter_R():
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(26));
    RS232.write(chr(0));
    Ristra=''
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'
def Set_ALARM_Exit_R():
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(27));
    RS232.write(chr(0));
    Ristra=''
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'
def Send_Script():
    Halt_System()

 
        
    FileName = 'TelitScript.pyc'
    root = tk.Tk()
    root.withdraw()
       
    file_path = filedialog.askopenfilename()
    py_compile.compile(file_path,FileName)

    EraseFiles(FileName);
    
    Write_File(FileName)
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(22));
    RS232.write(FileName)
    RS232.write(chr(0));
    counter = 0;
    Ristra = ''
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            try:
                CHAR= RS232.read(1)
                if (ord(CHAR[0]) != 0):
                    Ristra = Ristra + CHAR[0]
                    if (CHAR[0]=='\n'):
                        sys.stdout.write( Ristra)
                        Ristra = ''                    
                else:
                    print Ristra
                    break;
            except:
                counter = counter + 1
                if (counter == 5):
                    print 'Error'
                    break;
                else:
                    pass
    except:
        print 'Error'

    EraseFiles(FileName)
    os.remove(FileName)
    
def EnterTransparentMode():
    RS232.flushInput();
    RS232.write(chr(16));
    RS232.write(chr(18));
    RS232.write(chr(255));
    RS232.write(chr(4));
    RS232.write(chr(35));
    RS232.write(chr(0));
    Ristra=''
    print 'En modo transparente el equipo no puede salir de este estado de forma automatica'
    print 'Debera desenergizar el equipo o presionar el boton de reset para salir de este modo'
    try:
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (CHAR[0] != '$'):
                pass
            else:
                break
        while(RS232.closed==False):
            CHAR= RS232.read(1)
            if (ord(CHAR[0]) != 0):
                Ristra = Ristra + CHAR[0]
            else:
                print Ristra
                break;
    except:
        print 'Error'

#COM = 'COM25'

#RS232 = serial.Serial(None, 921600, timeout=.5, stopbits=1)
#RS232.setPort(COM)
#try:
#    if (RS232.closed == False):
#        RS232.close()
#        RS232.open()
#except:
#    
#    RS232.close()
#    try:
#        RS232.open()
#    except:
#        print 'No se pudo abrir puerto COM'
#for x in range(0, 3):
#    Get_Mag()
#    time.sleep(0.1)

#print 'Directorio actual:', GetCurrentDir(),'>>'
#while(1):
#    PrintAll();




B = list(list_ports.comports())
i = 0
PUERTOS=[]
Candidatos = []

for Movismart in B:
    if (Movismart[2].find('USB VID:PID=04D8') != -1):
        Candidatos.append(Movismart)

if (len(Candidatos)>1):
    print 'Existe mas de un puerto COM disponible','(',len(B),').'    
elif (len(Candidatos)==0):
    print 'No se encontraron puertos COM. Adios!'
    text_pr = "sin pto com"
    sys.exit();
i=0;
for Tuple in Candidatos:
    PUERTOS.append(Tuple[0])
    if (len(Candidatos)>1):
        print 'Para utilizar el puerto ',Tuple[0],' ingrese' ,i
    i = i+1
if (len(PUERTOS)>1):
    PUERTO = raw_input('Ingrese numero: ')
    try:
        COM = PUERTOS[int(PUERTO)]
        print 'Ha seleccionado el puerto ', COM
    except:
        print 'Puerto no valido. Adios!'
        sys.exit();
else:
    COM = PUERTOS[0]

try:
    RS232 = serial.Serial(None, 115200, timeout=10, stopbits=1)
    RS232.setPort(COM)
except:
    print 'Algo raro ocurrio!. Probablemente error de sintaxis dentro del codigo'
    sys.exit();
try:
    RS232.open()
except:
    print 'Acceso denegado al puerto COM. Verifique que no este abierto por otra aplicacion'
    print 'Tratando de forzar el cierre del puerto'
    RS232.close()
    if (RS232.closed == True):
        print 'Se logro cerrar el puerto COM. Tratando de re-abrirlo'
        try:
            RS232.open()
        except:
            print 'No se pudo abrir el puerto COM despues de cerrarlo, Adios!' 
            sys.exit();
    else:
        print 'Imposible cerrar el puerto COM, una aplicacion con privilegios de administrador tiene tomado el puerto'        
        sys.exit();

if (RS232.isOpen()):
    print 'Puerto COM abierto satisfactoriamente'
else:
    print 'Error abriendo el puerto COM'
    sys.exit();
RS232.flushInput()

#try:
#    print 'Directorio actual:', GetCurrentDir(),'>>'
#except:
    #pass

EnterTransparentMode()
RS232.close()

