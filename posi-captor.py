import pyautogui
import time

print("Você tem 5 segundos para posicionar o mouse na barra de digitação...")
time.sleep(5)

x, y = pyautogui.position()
print(f"Coordenadas capturadas: x={x}, y={y}")
