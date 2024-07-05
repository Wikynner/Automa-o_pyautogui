
#importa biblioteca pyautogui



import pyautogui as bot

bot.PAUSE = 3

bot.press('win') # Pressionamento tecla Windos
bot.PAUSE = 2 # tempo de espera para execução 
bot.write('texto1') # Escrever Texto1 ao executar os comandos anteriores 

bot.press('enter')# preciona a tecla enter 

#abre o arquivo que criei em excel salvo com o nome  texto1


# Point(x=179, y=65)
#bot.click(179, y=65)# opção insert 
bot.click(x=70, y=287) # Point(x=70, y=287) #click na celula A1

bot.write('Shazan')
bot.press('tab')
bot.write('Acabou o teste')
bot.click(x=1754, y=290)
#Point(x=1754, y=290)AA1
bot.write('Este teste deu certo')




