def calcular_ipc(df,base):
    df=df/base
    print(df)


def run():
    import pandas as pd
    df=pd.read_excel("C:/Users/sergi/OneDrive/Escritorio/calculo_ipc/IPC_Indices2222.xlsx")
    year=int(input("Escribe el año: "))
    mes=int(input("Escribe el mes: "))
    base=df.iloc[mes,year]
    print("Esta es la base "+str(base))


    df.drop(["Mes"], axis = 'columns', inplace=True)
    print(df)

    
    calcular_ipc(df,base)
    

if __name__=="__main__":
    run()


