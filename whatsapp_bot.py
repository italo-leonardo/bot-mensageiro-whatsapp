import pywhatkit as kit
import pyautogui
import time

# Lista dos números de destino
numeros = [
    "+5588999009596"
]

mensagem = """
Olá, tudo bem?! Sou um Bot
"""

# Coordenadas do campo de digitação do WhatsApp Web (ajuste conforme necessário)
valor_x = 3639
valor_y = 1220

erros = []
for i, numero in enumerate(numeros):
    try:
        kit.sendwhatmsg_instantly(numero, mensagem, wait_time=10, tab_close=False)
        time.sleep(6)

        pyautogui.click(x=valor_x, y=valor_y)
        pyautogui.press('space')
        pyautogui.press('backspace')
        time.sleep(1)
        pyautogui.press('enter')

        print(f"✅ Mensagem enviada para {numero}")
        time.sleep(4)

        if (i + 1) % 20 == 0:
            print("⏸️ Pausa de 30 segundos para evitar travamentos...")
            time.sleep(30)

    except Exception as e:
        print(f"❌ Erro ao enviar para {numero}: {e}")
        erros.append(numero)

if erros:
    with open("log_erros.txt", "w") as f:
        for num in erros:
            f.write(num + "\n")
    print("📄 Log de erros salvo em 'log_erros.txt'")
else:
    print("✅ Todas as mensagens foram enviadas com sucesso!")
