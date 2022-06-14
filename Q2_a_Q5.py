import pandas as pd

# 2)
def fib(num):
    a=0
    b=1
    
    while True:
        if a+b == num or num == 0 or num == 1:
            print("pertence")
            return True
        elif a+b > num:
            print("não pertence")
            return False
        else:
            aux = a
            a = b
            b = aux+b

# 3)


def vec(fileName):
    df = pd.read_json(fileName)
    menor = df.min(axis=1)
    maior = df.max(axis=1)
    media = df.mean(axis = 0, skipna = True).mean()
    menorMedia = df[df < media].count().sum()

    return menor, maior, menorMedia

# 4)
def perce():
    df = pd.DataFrame({"SP":[67836.43],
                        "RJ":[36678.66], 
                        "MG":[29229.88],
                        "ES":[27165.48],
                        "Outros ":[19849.53]})
    return df/df.sum(axis=1)[0]

# 5)
def inverter(texto):
  return texto[::-1]