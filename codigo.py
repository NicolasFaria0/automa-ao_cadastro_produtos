import pyautogui
import time
import pandas as pd
#open the navagator
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=1003, y=615)
pyautogui.click(x=927, y=77)

#enter the url
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#log in
time.sleep(1)
pyautogui.click(x=812, y=476)
pyautogui.write("aluno")
pyautogui.press("tab")
pyautogui.write("aluno")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=1159, y=458)
#pick data infos

tabela = pd.read_csv("produtos.csv")

#insert data infos on the url
for produto in tabela.index:
    pyautogui.click(x=881, y=329)

    #codigo
    codigo = tabela.loc[produto, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[produto, "marca"]    
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[produto, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[produto, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco unitario
    preco_unitario = tabela.loc[produto, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[produto, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[produto, "obs"]
    if pd.notna(obs):
        pyautogui.write(str(obs))

    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)