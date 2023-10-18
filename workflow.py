try:
    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime
    import pandas as pd

    

    print("All Dag modules are ok ......")
except Exception as e:
    print("Error  {} ".format(e))

def bot_reactivo(**context):
    import numpy as np
    import time as tm
    import random
    from os import system

    class nodo:
        
    
        def __init__(self,numero,estado):
            num=numero
            est=estado

        def __repr__  (self):
            return "<__main__ numero "+str(self.numero)+" estado: "+str(self.est)+">"
    
    
    class escoba:
        posx=random.randint(0,9)
        posy=random.randint(0,9)
        look=u"\U0001F9F9"
            
            
    celda=nodo
    mapa=np.empty((10,10),dtype=nodo)
    random.seed(version=2)
    for i in range (0,10):
        for j in range (0,10):
            r=random.randint(1,10)
            if r>=10:
                estado=u"\u2623"
            else:
                estado=u"\U0001F332"
            pos=i*10+j
            celda=(pos,estado)
            mapa[i][j]=celda
    
    salida=False
    limpia=escoba()
    total=0

    while salida==False:
        
        suciedad=0
        print("\n")
        tm.sleep(.5)
        for i in range(0,10):
            palabra=""
            for j in range(0,10):
                palabra+="["
                if i==limpia.posy and j==limpia.posx:
                    palabra+=limpia.look
                palabra+=mapa[i][j][1]+"]"
                if mapa[i][j][1]==u"\u2623":
                    suciedad+=1           
            
            if i==9:
                print ("basura restante: ",suciedad)
                mov=random.randint(1,4)
                limpia.posy
                moverse=False
                if (suciedad==0 or total==1000):
                    salida=True
                    moverse=True

                while(moverse!=True):

                    if mapa[limpia.posy][limpia.posx][1]==u"\u2623":
                        print ("limpiar en coordenadas :", limpia.posy," ",limpia.posx)
                        pos=limpia.posy*10+limpia.posx
                        estado=u"\U0001F332"
                        celda=(pos,estado)
                        mapa[limpia.posy][limpia.posx]=celda
                        print (mapa[limpia.posy][limpia.posx])
                        suciedad-=1
                        mov=5
                        moverse=True

                    if mov==1:
                        if limpia.posy<9:
                                limpia.posy+=1
                                moverse=True
                                total+=1
                        else:
                            mov=random.randint(1,4)
                    if mov==2:
                        if limpia.posy>0:
                                limpia.posy-=1
                                moverse=True
                                total+=1   
                        else:
                            mov=random.randint(1,4)
                    if mov==3:
                        if limpia.posx<9:
                                limpia.posx+=1
                                moverse=True
                                total+=1  
                        else:
                            mov=random.randint(1,4)
                    if mov==4:
                        if limpia.posx>0:
                                limpia.posx-=1
                                moverse=True
                                total+=1
                        else:
                            mov=random.randint(1,4)

    print ("Matriz limpia, total de movimientos requeridos: ",total)

def bot_obser(**context):
    import numpy as np
    import time as tm
    import random
    from os import system

    class nodo:
        
    
        def __init__(self,numero,estado):
            num=numero
            est=estado

        def __repr__  (self):
            return "<__main__ numero "+str(self.numero)+" estado: "+str(self.est)+">"
    
    
    class escoba:
        posx=random.randint(0,9)
        posy=random.randint(0,9)
        look=u"\U0001F9F9"
            
            
    celda=nodo
    mapa=np.empty((10,10),dtype=nodo)
    random.seed(version=2)
    for i in range (0,10):
        for j in range (0,10):
            r=random.randint(1,10)
            if r>=10:
                estado=u"\u2623"
            else:
                estado=u"\U0001F332"
            pos=i*10+j
            celda=(pos,estado)
            mapa[i][j]=celda
    
    salida=False
    limpia=escoba()
    total=0

    while salida==False:
        
        suciedad=0
        print("\n")
        tm.sleep(.5)
        for i in range(0,10):
            palabra=""
            for j in range(0,10):
                palabra+="["
                if i==limpia.posy and j==limpia.posx:
                    palabra+=limpia.look
                palabra+=mapa[i][j][1]+"]"
                if mapa[i][j][1]==u"\u2623":
                    suciedad+=1           
            
            if i==9:
                print ("basura restante: ",suciedad)
                mov=random.randint(1,4)
                limpia.posy
                moverse=False
                if (suciedad==0 or total==1000):
                    salida=True
                    moverse=True

                while(moverse!=True):

                    if(limpia.posy<9):
                        if mapa[limpia.posy+1][limpia.posx][1]==u"\u2623":
                            mov=1
                    if(limpia.posy>0):
                        if mapa[limpia.posy-1][limpia.posx][1]==u"\u2623":
                            mov=2
                    if(limpia.posx<9):
                        if mapa[limpia.posy][limpia.posx+1][1]==u"\u2623":
                            mov=3
                    if(limpia.posx>0):
                        if mapa[limpia.posy][limpia.posx-1][1]==u"\u2623":
                            mov=4

                    if mapa[limpia.posy][limpia.posx][1]==u"\u2623":
                        print ("limpiar en coordenadas :", limpia.posy," ",limpia.posx)
                        pos=limpia.posy*10+limpia.posx
                        estado=u"\U0001F332"
                        celda=(pos,estado)
                        mapa[limpia.posy][limpia.posx]=celda
                        print (mapa[limpia.posy][limpia.posx])
                        suciedad-=1
                        mov=5
                        moverse=True

                    if mov==1:
                        if limpia.posy<9:
                                limpia.posy+=1
                                moverse=True
                                total+=1
                        else:
                            mov=random.randint(1,4)
                    if mov==2:
                        if limpia.posy>0:
                                limpia.posy-=1
                                moverse=True
                                total+=1   
                        else:
                            mov=random.randint(1,4)
                    if mov==3:
                        if limpia.posx<9:
                                limpia.posx+=1
                                moverse=True
                                total+=1  
                        else:
                            mov=random.randint(1,4)
                    if mov==4:
                        if limpia.posx>0:
                                limpia.posx-=1
                                moverse=True
                                total+=1
                        else:
                            mov=random.randint(1,4)

    print ("Matriz limpia, total de movimientos requeridos: ",total)


with DAG(
        dag_id="workflow",
        schedule_interval="@hourly",
        default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2021, 1, 1),
        },
        catchup=False) as f:
     
    bot_reactivo = PythonOperator(
        task_id="bot_reactivo",
        python_callable=bot_reactivo,
        provide_context=True,
    )

    bot_obser = PythonOperator(
        task_id="bot_obser",
        python_callable=bot_obser,
        provide_context=True,
    )
