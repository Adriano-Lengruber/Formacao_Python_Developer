import pyautogui
from time import sleep

# Para comentar várias linhas em python ,
# selecione as que deseja e depois dê o comando:
# Ctrl + KC

# Passo 1: Abrir o mouseInfo para mapear a Template
#     Abrir CMD e digitar: Python e depois ENTER
#     Depois digitar: from mouseinfo import mouseInfo
#     mouseInfo()


#Teste1 : Abrir App Xbox no Note
#Clicando no Ícone do windows:
pyautogui.click(40,1049, duration=1)
#Digitando Xbox:
pyautogui.write('xbox')
