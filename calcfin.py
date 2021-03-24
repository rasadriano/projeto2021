print("\n","Calculadora financeira")
print("______________________________________")
print(" Escolhas as seguintes opções: ",'\n', "1. valor futuro",'\n', "2. valor presente",'\n', "3. taxa",'\n', "4. tempo",'\n', "5. pagamento",  end='\n')
print("______________________________________")

pergunta = input("O que você quer calcular ? \n ")

if pergunta == "1":
    print("Opte por valor futuro com valor presente ou pagamento")
    print("Se valor presente, pagamento = 0")
    print("Se pagamento, valo presente = 0")
    valor_presente = input("Digite o valor presente: ")
    taxa = input("Digite a taxa de juros: ")
    tempo = input("Digite o periodo: ")
    pagamento = input("Digite o valor da parcela: ")
    vp = eval(valor_presente)
    i = eval(taxa)
    t = eval(tempo)
    pmt = eval(pagamento)
    if pmt == 0 and vp !=0 :   
        import math
        def fator(i,t):
            return (math.pow(1+i/100,t))
        def valorfuturo(vp, i, t):
            return vp * fator(i,t)

        vf = round(valorfuturo(vp, i, t),3)

        print()
        print("O valor do valor futuro é",'\n', "R$",vf)
        #print("Parcelas de: ",'\n', "R$",pmt_acumulado)
        
    elif vp == 0 and pmt !=0:
        import math
        def fator(i,t):
            return (math.pow(1+i/100,t))
        def amortizacao_pmt(i, t):
            return (fator(i,t)*i/100)/(fator(i,t)-1)
        def pv_pmt(pmt, i, t):
            return pmt/amortizacao_pmt(pmt,i,t)
        def fv_pmt(pmt,i,t):
            return pv_pmt(pmt, i, t)*fator(i,t)
        fv_pmt = round(fv_pmt(pmt,i,t),3)
        pv_pmt = round(pv_pmt(pmt, i, t),3)
        #pmt_fixo = pmt*t
        print()
        print("O montante pago será de:",'\n', 'R$',fv_pmt)
        #print("Caso parcela for fixa:",'\n', 'R$',pmt_fixo)
        print("O valor inicial foi de:",'\n', 'R$', pv_pmt)
    
elif pergunta == "2":
    valor_futuro = input("Digite o valor futuro:  ")
    taxa = input("Digite a taxa de juros: ")
    tempo = input("Digite o periodo: ")
    pagamento = input("Digite o valor da parcela: ")
    vf = eval(valor_futuro)
    i = eval(taxa)
    t = eval(tempo)
    pmt = eval(pagamento)
    
    if pmt == 0 and vf != 0:
        import math
        def fator(i,t):
        	return (math.pow(1+i/100,t))
        def valorpresente(vf, i, t):
            return vf / fator(i,t)
        vp = round(valorpresente(vf, i, t),3)
        print()
        print("O valor presente é: ",'\n', "R$", vp)
    
    elif vf == 0 and pmt!= 0:
        import math
        def fator(i,t):
            return (math.pow(1+i/100,t))
        def pagamento(vp, i, t):
            return (vp*fator(i,t)*i/100)/(fator(i,t)-1)
        def amortizacao_pmt(pmt, i, t):
            return (fator(i,t)*i/100)/(fator(i,t)-1)
        def pv_pmt(pmt, i, t):
            return pmt/amortizacao_pmt(pmt,i,t)
        pv_pmt = round(pv_pmt(pmt, i, t),3)
        print()
        print("O valor presente é: ",'\n', "R$", pv_pmt)
    
elif pergunta == "3":
    valor_futuro = input("Digite o valor futuro: ")
    valor_presente = input("Digite o valor presente: ")
    tempo = input("Digite o periodo: ")
    vf = eval(valor_futuro)
    vp = eval(valor_presente)
    t = eval(tempo)
    
    import math 
    def taxa(vf, vp, t):
        return (math.pow((vf/vp),1/t)) -1 
    i = round(taxa(vf, vp, t)*100,3)
    print("A taxa é de:  ",'\n', i,"%")

elif pergunta == "4":
    valor_futuro = input("Digite o valor futuro: ")
    valor_presente = input("Digite o valor presente: ")
    taxa = input("Digite a taxa: ")
    vf = eval(valor_futuro)
    vp = eval(valor_presente)
    i = eval(taxa)

    import math
    def tempo(vf, vp, i):
        return (math.log((vf/vp),10))/(math.log((1+i/100),10))
    t = round(tempo(vf, vp, i),3)
    print("A periodo foi de:  ",'\n', t, "meses")

elif pergunta == "5":
    valor_presente = input("Digite o valor do bem: ")
    taxa = input("Digite a taxa ")
    tempo = input("Digite o periodo: ")
    vp = eval(valor_presente)
    i = eval(taxa)
    t = eval(tempo)

    import math
    def fator(i,t):
        return (math.pow(1+i/100,t))
    def pagamento(vp, i, t):
        return (vp*fator(i,t)*i/100)/(fator(i,t)-1)
    pag = round(pagamento(vp, i, t),3)
    print("O valor da parcela é de:  ",'\n', "R$", pag)
    
else:
    print("Desculpe o transtorno, não temos essa função ")
   
print("______________________________________")

#def juros(vp, i, t):
    #return vf - vp
#j = juros(vp, i, t)
#def fator(i,t):
    #return (math.pow(1+i/100,t))
#def fatoracumulacao(i,t):
    #return (i/100)/(fator(i,t) -1)
#pmt_acumulado = vf*fatoracumulacao(i,t)


