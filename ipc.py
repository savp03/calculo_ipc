#Cambio de base ??????
def calcular_ipc(df,base):
    df=df/base
    print(df)


def run():
    import pandas as pd
    df=pd.read_excel("C:/Users/sergi/OneDrive/Escritorio/calculo_ipc/IPC_Indices2222.xlsx")


    print("""Este programa calcula el IPC en relacion a diferentes periodos de tiempo.
    Tenemos datos desde Enero de 2003 hasta Enero del 2022""")
    
    year=int(input("Escribe el año que quieres usar de base: "))    
    mes=input("Escribe el mes del "+str(year)+" que quiere usar: ")
    mes=mes.lower()
    mes=mes.strip()
    year=year-2002


    if mes=="enero":
        mes=0
    elif mes=="febrero":
        mes=1
    elif mes=="marzo":
        mes=2
    elif mes=="abril":
        mes=3
    elif mes=="mayo":
        mes=4
    elif mes=="junio":
        mes=5
    elif mes=="julio":
        mes=6
    elif mes=="agosto":
        mes=7
    elif mes=="septiembre":
        mes=8
    elif mes=="octubre":
        mes=9
    elif mes=="noviembre":
        mes=10
    elif mes=="diciembre":
        mes=11
    else:
        print("Escribe el mes correctamente")   


    base=df.iloc[mes,year]
    print("El ipc base es: "+str(base))


    df.drop(["Mes"], axis = 'columns', inplace=True)
    print(df)

    
    calcular_ipc(df,base)
    

if __name__=="__main__":
    run()


