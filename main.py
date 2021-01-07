import pyautogui as pg

for x in range(3600):
    pg.moveTo(4398,178,0.8)
    pg.click()
    pg.moveTo(4734,644,0.8)
    pg.click()
    print(x)