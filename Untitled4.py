#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pyautogui

import pyautogui as escolher_opcao

opcao = pyautogui.confirm('Escolha a opção desejada',buttons = ['Excel', 'Word','Notepad'])

if opcao == "Excel":
    escolher_opcao.hotkey('win','r')
    
    escolher_opcao.sleep (2)
    
    escolher_opcao.typewrite ('Excel')
    
    escolher_opcao.sleep (2)
    
    escolher_opcao.press('Enter')
    
    escolher_opcao.sleep (4)
    
    escolher_opcao.click(x=279, y=196)
    escolher_opcao.typewrite('A opcao escolhida foi Excel')
    print(escolher_opcao.position())
    
    
elif opcao == "Word":
    escolher_opcao.hotkey('win','r')
    
    escolher_opcao.sleep (2)
    
    escolher_opcao.typewrite ('winword')
    
    escolher_opcao.sleep (2)
    
    escolher_opcao.press('Enter')
    
    escolher_opcao.sleep (4)
    
    escolher_opcao.click(x=256, y=194)
    escolher_opcao.typewrite('A opcao escolhida foi Word')
    #print(escolher_opcao.position())
elif opcao == "Notepad":
    escolher_opcao.hotkey('win','r')
    
    escolher_opcao.sleep (2)
    
    escolher_opcao.typewrite ('Notepad')
    
    escolher_opcao.sleep (2)
    
    escolher_opcao.press('Enter')
    
    escolher_opcao.sleep (4)
    
    escolher_opcao.typewrite('A opcao escolhida foi Notepad')
    

    


# In[ ]:





# In[ ]:




