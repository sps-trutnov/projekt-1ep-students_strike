# pouzite knihovny 
import sys  
import random
import time
# pouzity framework  
import pygame  
# spusteni frameworku  
pygame.init()  
  
# pocatecni nastaveni hodnot  
ROZLISENI_X = 1280 
ROZLISENI_Y = 720
FPS = 60
CERNA_BARVA = (0, 0, 0)  
BILA_BARVA = (255, 255, 255)  
barva_hl = (128,0,128) 
barva_foloweri = (255,0,0) 
pocet_foloweri = 10
pozadavek = random.randint(15, 25)
povoleni = 0
velikost = 50 
x = 10 
y = 10 
pozice_x = (ROZLISENI_X - velikost) / 2  
pozice_y = (ROZLISENI_Y - velikost) / 2  
rychlost = 3 # pixely / frame

pozadí_prizemi = pygame.image.load("chodba.png")
pozadí_prizemi = pygame.transform.scale(pozadí_prizemi, (ROZLISENI_X , ROZLISENI_Y))
pozadi_nadprizemi = pygame.image.load("chodba 1.png")
pozadi_nadprizemi = pygame.transform.scale(pozadi_nadprizemi, (ROZLISENI_X , ROZLISENI_Y))
reditelna = pygame.image.load("obrázky/reditelna.png")
reditelna = pygame.transform.scale(reditelna, (ROZLISENI_X , ROZLISENI_Y))
venek = pygame.image.load("obrázky/před-školou.png")
cislo_patra = 1
cislo_patra_font = pygame.font.Font(None, 72) # Font pro vykresení čísla patra

navstiveny_třídy = []
# pomocny objekt pro omezeni FPS  
hodiny = pygame.time.Clock()

okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))  
pygame.display.set_caption('Strike')  
  
# vykreslovaci smycka  
while True:  
    # jake nastaly udalosti?  
    for udalost in pygame.event.get():  
        # byla nektera z nich typu QUIT?  
        if udalost.type == pygame.QUIT:  
            # vypnuti frameworku  
            pygame.quit()  
            # vypnuti aplikace  
            sys.exit()
            
    okno.blit(reditelna, (0, 0))
    # prekresleni obsahu okna  
    pygame.display.update()  
    # zastropovani FPS  
    hodiny.tick(FPS)  
 