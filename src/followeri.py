# pouzite knihovny 
import sys  
import random  
# pouzity framework  
import pygame  
# spusteni frameworku  
pygame.init()  
  
# pocatecni nastaveni hodnot  
ROZLISENI_X = 1920 
ROZLISENI_Y = 1080 
FPS = 120 
CERNA_BARVA = (0, 0, 0)  
BILA_BARVA = (255, 255, 255)  
barva_hl = (128,0,128) 
barva_foloweri = (255,0,0) 
pocet_foloweri = 10
velikost = 50 
x = 10 
y = 10 
pozice_x = (ROZLISENI_X - velikost) / 2  
pozice_y = (ROZLISENI_Y - velikost) / 2  
rychlost = 3 # pixely / frame  
  
# pomocny objekt pro omezeni FPS  
hodiny = pygame.time.Clock()  
 
class foloweri_class: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
 
 
 
 
 
foloweri = [] 
for i in range(pocet_foloweri): 
    foloweri.append(foloweri_class(random.randint(velikost, ROZLISENI_X - velikost), random.randint(velikost, ROZLISENI_Y - velikost))) 
 
 
# vytvoreni okna  
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
  
#ovladani pomoci klavesnice  
    klavesy = pygame.key.get_pressed()  
      
    if klavesy[pygame.K_ESCAPE]:  
        pygame.quit()  
        sys.exit()  
#ovládání hráće
    if klavesy[pygame.K_RIGHT]:  
        pozice_x += rychlost  
    if klavesy[pygame.K_LEFT]:  
        pozice_x -= rychlost  
    if klavesy[pygame.K_DOWN]:  
        pozice_y += rychlost  
    if klavesy[pygame.K_UP]:  
        pozice_y -= rychlost  
      
#kolize hráče
    if pozice_x > ROZLISENI_X:  
        pozice_x = ROZLISENI_X 
    if pozice_y > ROZLISENI_Y:  
        pozice_y = ROZLISENI_Y 
    if pozice_x < 0:  
        pozice_x = 0  
    if pozice_y < 0:  
        pozice_y = 0 
     
     
 
     
    # stanoveni barvy pozadi  
    okno.fill(BILA_BARVA)  
     
#kolize foloweru na hrace
    for i in range(pocet_foloweri): 
        distance = ((pozice_x - foloweri[i].x) ** 2 + (pozice_y - foloweri[i].y) ** 2) ** 0.5 
        if distance > velikost + 10: 
            if foloweri[i].x > pozice_x: 
                foloweri[i].x -= rychlost 
            elif foloweri[i].x < pozice_x: 
                foloweri[i].x += rychlost 
            if foloweri[i].y > pozice_y: 
                foloweri[i].y -= rychlost 
            elif foloweri[i].y < pozice_y: 
                foloweri[i].y += rychlost
#kolize hráće na foloweri
    for i in range(pocet_foloweri):
        distance = ((pozice_x - foloweri[i].x) ** 2 + (pozice_y - foloweri[i].y) ** 2) ** 0.5 
        if distance < velikost + 10: 
            if foloweri[i].x > pozice_x: 
                foloweri[i].x += rychlost 
            elif foloweri[i].x < pozice_x: 
                foloweri[i].x -= rychlost 
            if foloweri[i].y > pozice_y: 
                foloweri[i].y += rychlost 
            elif foloweri[i].y < pozice_y: 
                foloweri[i].y -= rychlost
#kolize foloweru stěn 
    for i in range(pocet_foloweri):
        if foloweri[i].x > ROZLISENI_X:
            foloweri[i].x = ROZLISENI_X
        elif foloweri[i].x < 0: 
            foloweri[i].x = 0
        if foloweri[i].y > ROZLISENI_Y: 
            foloweri[i].y = ROZLISENI_Y 
        elif foloweri[i].y < 0: 
            foloweri[i].y = 0
#kolize folowerů na folowera
    for i in range(pocet_foloweri): 
        for y in range(pocet_foloweri): 
            if y != i: 
                distance_1 = ((foloweri[i].x - foloweri[y].x) ** 2 + (foloweri[i].y - foloweri[y].y ) ** 2) ** 0.5 
                if distance_1 < velikost + 10: 
                    if foloweri[i].x > foloweri[y].x: 
                        foloweri[i].x += rychlost 
                    elif foloweri[i].x < foloweri[y].x: 
                        foloweri[i].x -= rychlost 
                    if foloweri[i].y > foloweri[y].y: 
                        foloweri[i].y += rychlost 
                    elif foloweri[i].y < foloweri[y].y: 
                        foloweri[i].y -= rychlost
                        

             
#vykreslení folowerů
    for i in range(pocet_foloweri): 
        pygame.draw.circle(okno, barva_foloweri, (foloweri[i].x, foloweri[i].y), velikost / 2) 
         
    pygame.draw.circle(okno,barva_hl,(pozice_x, pozice_y),velikost / 2) 
  #  pygame.draw.circle(okno,barva_foloweri,(x, y),velikost / 2) 
 
    # prekresleni obsahu okna  
    pygame.display.update()  
    # zastropovani FPS  
    hodiny.tick(FPS)  
 
