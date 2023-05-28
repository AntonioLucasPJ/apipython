from fastapi import FastAPI
import pandas as pd 
import json
lista = []
tabela = pd.read_excel('teste.xlsx')
for i in tabela.index:
    nome = tabela.loc[i,"Nome"]
    telefone = tabela.loc[i,"Telefone"]
    email = tabela.loc[i,"Email"]
    lista.append(nome)
    jsonstring = json.dumps(nome)
print(jsonstring)
app = FastAPI()

@app.get("/home")
def home():
    return f"{jsonstring}"