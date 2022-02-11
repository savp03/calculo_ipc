def run():
    import pandas as pd
    df=pd.read_excel("C:/Users/sergi/OneDrive/Escritorio/calculo_ipc/IPC_Indices2222.xlsx")


    contador=0
    print("""Este programa grafica 10 IPC""")

    ipc=list()
    year_list=list()
    mes_list=list()
    while contador<10:
        year=int(input("Escribe el año que quieres usar de base: ")) 
        year_list.append(year)     
        mes=input("Escribe el mes del "+str(year)+" que quiere usar: ")
        mes=mes.lower()
        mes=mes.strip()
        mes_list.append(mes)
        year=year-2002
        contador=contador+1             


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
        ipc.append(base)

    #meter ipc, años y meses en matrices y graficar con los 3 vectores

    print(ipc)
    print(year_list)
    print(mes_list)

if __name__=="__main__":
    run()


# https://python-para-impacientes.blogspot.com/2019/11/convertir-copiar-ordenar-unir-y-dividir.html

