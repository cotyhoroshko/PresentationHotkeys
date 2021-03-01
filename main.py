import pygame
import win32api
import win32con
import win32gui

from pch import hotkeys
from vsc import vsc_hotkeys

#itr = iter(vsc_hotkeys)
itr = iter(hotkeys)

pygame.init()
screen = pygame.display.set_mode((250, 100)) # For borderless, use pygame.NOFRAME
pygame.display.set_caption('')
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (139, 100, 0)

# Set window transparency color
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)


f1 = pygame.font.Font(None, 36)
text1 = f1.render('', 1, (180, 0, 0))
screen.blit(text1, (10, 50))

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            text1 = f1.render(next(itr), 1, (180, 200, 30))

    screen.fill(fuchsia)  # Transparent background
    pygame.draw.rect(screen, dark_red, pygame.Rect(30, 30, 60, 60))
    screen.blit(text1, (10, 50))
    pygame.display.update()
