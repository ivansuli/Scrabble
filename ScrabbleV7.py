import random

#Funciones
def iniciartab(Tab):
    """Esta funcion se encarga de iniciar el tablero"""
    Multiplicador2L=[(3,0),(11,0),(14,3),(14,11),(11,14),(3,14),(0,11),(0,3),(6,2),(8,2),(12,6),(12,8),(8,12),(6,12),(2,6),(2,8),(7,3),(11,7),(7,11),(3,7),(6,6),(6,8),(8,6),(8,8)]
    Multiplicador3L=[(5,1),(9,1),(13,5),(13,9),(9,13),(5,13),(1,5),(1,9),(5,5),(5,9),(9,5),(9,9)]
    Multiplicador3P=[(0,0),(0,7),(0,14),(7,0),(14,0),(14,7),(14,14),(7,14)]
    for f in range(15):
        for c in range(15):
            pos=(f,c)
            if f==c:
                Tab[f][c]="2P"
            elif f+c==len(Tab)-1:
                Tab[f][c]="2P"
            if pos in Multiplicador2L:
                Tab[f][c]="2L"
            elif pos in Multiplicador3L:
                Tab[f][c]="3L"
            elif pos in Multiplicador3P:
                Tab[f][c]="3P"
    return Tab
                
def imprimirtab(Tab):
    Numeros=[]
    for i in range(1, 16):
        Numeros.append(i)
    print(r" F/C", end="")
    for i in range(0, 15):
        print("%4s" %Numeros[i],end="")
    print()
    for f in range(15):
        print("%4s" %Numeros[f],end="")
        for c in range(15):
            print("%4s" %Tab[f][c],end="")
        print()      

def DecisionJugador(listajug, Letr, Tab, jug, PuntL, puntos, conjpos, lispos, jug1):
    imprimirtab(Tab)
    print()
    print("Turno del jugador", jug)
    print("Fichas: ", end="")
    imprimirfichas(listajug)
    print()
    while True:
        try:
            print("¿Que accion desea tomar?(Elegir numero)\n1:Cambiar Fichas\n2:Usar Fichas\n3:Pasar Turno\n4:Rendirse\n5:Terminar Partida")
            Dec=int(input())
            assert 0<Dec<6
        except ValueError:
            print("Dato erroneo, Ingresar correctamente el numero")
        except AssertionError:
            print("Dato erroneo, Ingrese dentro del rango de decisiones")
        else:
            break
    if Dec==1:
        listajug, Letr=CambiarFichas(listajug, Letr)
        print("Fichas actualizadas: ", listajug)
        print()
    elif Dec==2:
        listajug, Tab, puntos, conjpos, lispos=FichasTablero(listajug, Tab, PuntL, puntos, conjpos, lispos)
        listajug, Letr=RepartirLetras(listajug, Letr)
        print("Tiene: ", puntos, "puntos en total")
    elif Dec==3:
        print("El jugador", jug, "decidio pasar el turno")
        print()
    elif Dec==4:
        jug=0
    elif Dec==5:
        while True:
            try:
                Dec=input("El jugador"+str(jug1)+" ¿Quiere tambien terminar la partida?(Si/No): ")
                Dec=Dec.capitalize()
                assert Dec=="Si" or Dec=="No"
                if Dec=="Si":
                    jug=0
                    jug1=0
            except AssertionError:
                print("La opcion que tomo es incorrecta, vuelva a intentarlo")
            else:
                break
    return listajug, Letr, Tab, jug, puntos, conjpos, lispos, jug1
        
def RepartirLetras(listajug, Letr):
    """Se encarga de dar fichas al jugador al principio y durante la partida"""
    valor=7-len(listajug)
    aux=1
    while aux<=valor:
        try:
            assert len(Letr)>0
            random.shuffle(Letr)
            let=random.choice(Letr)
            Letr.remove(let)
            listajug.append(let)
            aux=1+aux
        except AssertionError:
            print("La bolsa de letras se ha quedado sin fichas, el juego termino")
            break
    return listajug, Letr
    
def CambiarFichas(listajug, Letr):
    print("¿Cuantas fichas desea cambiar? (Ingrese 0 si no quiere intercambiar)")
    while True:
        try:
            Fichas=int(input())
            assert 0<=Fichas<8, "Dato Invalido, tiene que ser hasta maximo 7"
            assert len(Letr)>=Fichas, "La bolsa tiene menos fichas de las que quiere intercambiar, introduzca un numero menor"
            listajug, Letr=Intercambio(listajug, Letr, Fichas)
        except ValueError:
            print("Dato Invalido, tiene que escribirlo en numero")
            print("Vuelva a intentarlo")
        except AssertionError as mensaje:
            print(mensaje)
            print("Vuelva a intentarlo")
        else:
            break
    return listajug, Letras
        
def Intercambio(lisj, Letr, Fi):
    aux=1
    while aux<=Fi:
        let=input("Ingrese la letra de la ficha que quiere cambiar: ")
        if let in lisj:
            aux=aux+1
            lisj.remove(let)
            let2=random.choice(Letr)
            lisj.append(let2)
            Letr.append(let)
        else:
            print("No se ha encontrado la ficha, vuelva a intentarlo")
    return lisj, Letr

def FichasTablero(listajug, Tab, PuntL, puntos, conjpos, lispos):
    pot=1
    dup=set()
    listapalabras=[]
    listafilas=[]
    listacolumnas=[]
    Si=True
    while Si:
        if len(listajug)>5:
            listajug, Tab, pot, conjpos, lispos, listacolumnas, listafilas, dup=ColocacionEnTablero(listajug, Tab, pot, conjpos, lispos, listacolumnas, listafilas, dup)
        else:
            while True:
                try:
                    Dec=input("¿Desea Seguir poniendo fichas? (Si/No): ")
                    Dec=Dec.capitalize()
                    assert Dec=="Si" or Dec=="No"
                except AssertionError:
                    print("No eligio las opciones correctas. Vuelva a intentarlo")
                else:
                    break
            if Dec=="Si" and len(listajug)>0:
                listajug, Tab, pot, conjpos, lispos, listacolumnas, listafilas, dup=ColocacionEnTablero(listajug, Tab, pot, conjpos, lispos, listacolumnas, listafilas, dup)
            else:
                Si=False
            if len(listajug)==0:
                print("Ha ganado 50 puntos por usar todas sus fichas")
                puntos=puntos+50
    listafilas=quitarbasura(listafilas)
    listacolumnas=quitarbasura(listacolumnas)
    listapalabras=listafilas+listacolumnas
    print("Palabras que ha formado:")
    for i in range(0, len(listapalabras)):
        punpal=0
        palabr=list(listapalabras[i])
        if Validar_Palabra(listapalabras[i]):
            for f in range(len(palabr)):
                if palabr[f] in dup:
                    punpal=punpal+PuntL.get(palabr[f])*dup.get(palabr[f])
                else:
                    punpal=punpal+PuntL.get(palabr[f])
            print(listapalabras[i]+". Obtuvo "+str(punpal)+" puntos")
        else:
            print("La palabra "+listapalabras[i]+" es invalida. No obtuvo puntos")
        puntos=puntos+punpal*pot
    listapalabras.clear()
    listacolumnas.clear()
    listafilas.clear()
    dup.clear()
    return listajug, Tab, puntos, conjpos, lispos       

def ColocacionEnTablero(listajug, Tab, potenciador, conjpos, lispos, lispalcolumn, lispalfil, duplicador):
    print("Fichas:", end="")
    imprimirfichas(listajug)
    print()
    let=input("Escriba la ficha que quiere usar: ")
    let=let.upper()
    if let in listajug:
        f, c, conjpos, lispos=posicionFicha(conjpos, lispos)
        while Tab[f-1][c-1]!=".":
            if Tab[f-1][c-1]=="3P":
                potenciador=3
                break
            elif Tab[f-1][c-1]=="2P":
                potenciador=2
                break
            elif Tab[f-1][c-1]=="2L":
                duplicador={let:2}
                break
            elif Tab[f-1][c-1]=="3L":
                duplicador={let:3}
                break
            conjpos.discard(str(f)+","+str(c))
            print("Posicion ya tomada, vuelva a ingresar otra posicion")
            f, c, conjpos, lispos=posicionFicha(conjpos, lispos)
        Tab[f-1][c-1]=let
        try:
            lispalcolumn=palabracolumna(f, c, Tab, lispos, let, lispalcolumn)
            lispalcolumn.remove(let)
            lispalfil=palabrafila(f, c, Tab, lispos, let, lispalfil)
            lispalfil.remove(let)
        except ValueError:
            pass
        listajug.remove(let)
    else:
        print("No tiene esa ficha, vuelva a intentarlo")
    return listajug, Tab, potenciador, conjpos, lispos, lispalcolumn, lispalfil, duplicador            

def posicionFicha(conjpos, lispos):
    while True:
        try:
            print("Estas son sus posiciones disponibles:", conjpos)
            pos=input("Ingrese la posicion que quiere agregarlo(Fila, Columna): ")
            x, y=pos.split(",")
            y=y.strip()
            assert x.isdigit() and y.isdigit(), "Ingrese numeros enteros, no letras ni numeros con coma. Vuelva a intentarlo"
            f=int(x)
            c=int(y)
            assert 0<f<16, "La fila esta fuera del rango del tablero. Vuelva a intentarlo"
            assert 0<c<16, "La columna esta fuera del rango del tablero. Vuelva a intentarlo"
            pos=str(f)+","+str(c)
            assert pos in conjpos, "La posicion que trato de poner esta fuera de su alcance. Vuelva a intentarlo"
            conjpos=lugaresposibles(conjpos, f, c)
            lispos.append(pos)
            for i in range(len(lispos)):
                           conjpos.discard(lispos[i])
        except AssertionError as mensaje:
            print(mensaje)
        else:
            break
    return f, c, conjpos, lispos

def lugaresposibles(conjpos, x, y):
    if x==1 and y==1:
        pos=str(x)+","+str(y+1)
        conjpos.add(pos)
        pos=str(x+1)+","+str(y)
        conjpos.add(pos)
    elif y==1:
        pos=str(x)+","+str(y+1)
        conjpos.add(pos)
        pos=str(x+1)+","+str(y)
        conjpos.add(pos)
        pos=str(x-1)+","+str(y)
        conjpos.add(pos)
    elif x==1:
        pos=str(x)+","+str(y+1)
        conjpos.add(pos)
        pos=str(x+1)+","+str(y)
        conjpos.add(pos)
        pos=str(x)+","+str(y-1)
        conjpos.add(pos)
    elif x==15 and y==15:
        pos=str(x)+","+str(y-1)
        conjpos.add(pos)
        pos=str(x-1)+","+str(y)
        conjpos.add(pos)
    elif y==15:
        pos=str(x)+","+str(y-1)
        conjpos.add(pos)
        pos=str(x+1)+","+str(y)
        conjpos.add(pos)
        pos=str(x-1)+","+str(y)
        conjpos.add(pos)
    elif x==15:
        pos=str(x)+","+str(y+1)
        conjpos.add(pos)
        pos=str(x-1)+","+str(y)
        conjpos.add(pos)
        pos=str(x)+","+str(y-1)
        conjpos.add(pos)
    else:
        pos=str(x)+","+str(y+1)
        conjpos.add(pos)
        pos=str(x-1)+","+str(y)
        conjpos.add(pos)
        pos=str(x)+","+str(y-1)
        conjpos.add(pos)
        pos=str(x+1)+","+str(y)
        conjpos.add(pos)
    return conjpos

def palabracolumna(f, c, Tab, lispos, let, lispal):
    y=c
    pala=let
    x=f
    while str(x-1)+","+str(y) in lispos:
        pala=Tab[x-2][y-1]+pala
        x=x-1
    x=f
    while str(x+1)+","+str(y) in lispos:
            pala=pala+Tab[x][y-1]
            x=x+1
    lispal.append(pala)
    return lispal

def palabrafila(f, c, Tab, lispos, let, lispal):
    x=f
    y=c
    pala=let
    while str(x)+","+str(y-1) in lispos:
            pala=Tab[x-1][y-2]+pala
            y=y-1
    y=c
    while str(x)+","+str(y+1) in lispos:
            pala=pala+Tab[x-1][y]
            y=y+1
    lispal.append(pala)
    return lispal

def quitarbasura(lispal):
    j=0
    lispal.sort(key=len)
    while j<len(lispal):
        aux1=lispal[j]
        while lispal.count(aux1)>1:
           lispal.remove(aux1)
        k=0
        while k<len(lispal):
            if lispal[j]!=lispal[k]:
                aux2=lispal[k]
                if aux1[0]==aux2[0] and aux1[0]==aux2[0]:
                    lispal.remove(aux1)
            k=k+1
        j=j+1
    return lispal

def Validar_Palabra(word):
    try:
        palabras = open("Palabras.txt", "rt")
        linea=palabras.readline()
        linea=linea.rstrip("\n")
        while linea:
            if word==linea:
                correcto = True
                break
            else:
                correcto = False
            linea=palabras.readline()
            linea=linea.rstrip("\n")
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            palabras.close()
        except NameError:
            pass
    return correcto

def ReglasJuego():
    try:
        re=open("ReglasScrabble.txt", "rt")
        linea=re.readline()
        while linea:
            print(linea)
            linea=re.readline()
        while True:
            try:
                print()
                opcion=input("Escriba 'Regresar' para volver al menu: ")
                opcion=opcion.capitalize()
                assert opcion=="Regresar"
            except AssertionError:
                    print("No eligio las opciones correctas. Vuelva a intentarlo")
            else:
                break
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            re.close( )
        except NameError:
            pass

def imprimirfichas(lista, inicio=0):
    if inicio<len(lista):
        print(lista[inicio], end=" ")
        imprimirfichas(lista, inicio+1)

#Programa princial
while True:
    try:
        print("Scrabble".center(15,"-"))
        print("Reglas".center(10,"-"))
        print("Jugar".center(10,"-"))
        Decision=input("Escriba la opcion que quiere tomar: ")
        Decision=Decision.capitalize()
        assert Decision.isalpha(), "No escriba numeros, sino la palabra de la opcion. Vuelva a intentarlo"
        assert Decision=="Reglas" or Decision=="Jugar", "No tomo las opciones correctas, Vuelva a intentarlo"
        if Decision=="Reglas":
            print()
            ReglasJuego()
        else:
            print()
            break
    except AssertionError as mensaje:
        print(mensaje)
print()
Tablero=[["."]*15 for i in range(15)]
Tablero=iniciartab(Tablero)
Letras=["A"]*11+["E"]*11+["O"]*8+["S"]*7+["I"]*6+["U"]*6+["N"]*5+["L"]*4+["R"]*4+["T"]*4+["C"]*4+["D"]*4+["G"]*2+["M"]*3+["B"]*3+["P"]*2+["F"]*2+["H"]*2+["V"]*2+["J"]*2+["Y","K","LL","Ñ","Q","RR","W","X","Z"]
PuntajeL={"A":1,"E":1,"I":1,"O":1,"U":1,"S":1,"N":1,"L":1,"R":1,"T":1,"C":2,"D":2,"G":2,"M":3,"B":3,"P":3,"F":4,"H":4,"V":4,"Y":4,"J":6,"K":8,"LL":8,"Ñ":8,"Q":8,"RR":8,"W":8,"X":8,"Z":10}
FichasJugador1=[]
FichasJugador2=[]
FichasJugador1, Letras=RepartirLetras(FichasJugador1, Letras)
FichasJugador2, Letras=RepartirLetras(FichasJugador2, Letras)
jug1=1
jug2=2
puntosjug1=0
ConjuntoPosi=set()
ConjuntoPosi={"8,8"}
puntosjug2=0
ListaPosi=[]
while len(Letras)>0 and jug1!=0 and jug2!=0:
    if jug1==1 and jug2==2:
        FichasJugador1, Letras, Tablero, jug1, puntosjug1, ConjuntoPosi, ListaPosi, jug2=DecisionJugador(FichasJugador1, Letras, Tablero, jug1, PuntajeL, puntosjug1, ConjuntoPosi, ListaPosi, jug2)
    if jug2==2 and jug1==1:
        FichasJugador2, Letras, Tablero, jug2, puntosjug2, ConjuntoPosi, ListaPosi, jug1=DecisionJugador(FichasJugador2, Letras, Tablero, jug2, PuntajeL, puntosjug2, ConjuntoPosi, ListaPosi, jug1)
if jug1==0 and jug2==0:
    print("La partida ha terminado")
    print("Puntos obtenidos por el jugador 1 fueron", puntosjug1)
    print("Puntos obtenidos por el jugador 2 fueron", puntosjug2)
    if puntosjug1>puntosjug2:
        print("El jugador 1 ha ganado por tener mayor cantidad de puntos")
    elif puntosjug1==puntosjug2:
        print("Ambos jugadores tienen la misma cantidad de puntos. Es un empate")
    else:
        print("El jugador 2 ha ganado por tener mayor cantidad de puntos")
elif jug1==0:
    print("El jugador 1 se ha rendido\nGana el Jugador 2")
elif jug2==0:
    print("El jugador 2 se ha rendido\nGana el Jugador 1")
else:
    if puntosjug1>puntosjug2:
        print("El jugador 1 ha ganado por tener mayor cantidad de puntos")
    elif puntosjug1==puntosjug2:
        print("Ambos jugadores tienen la misma cantidad de puntos. Es un empate")
    else:
        print("El jugador 2 ha ganado por tener mayor cantidad de puntos")
    