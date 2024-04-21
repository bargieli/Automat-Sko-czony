#*****************#
#   24.11.2023    #
# IZABELA BARGIEŁ #
#*****************#

#-*- coding: utf-8 -*-
import pygame
import sys

pygame.init()
pygame.font.init()

print("------------------------------------------------------------")
print("Podaj ciąg wejściowy: ", end=' ')


#---------------------------------------------------------------ustalenie kolejności przejść
# tabela w uzytkowej formie
przejscia = [[2, 1], [3, 0], [0, 3], [1, 2]]

stan0 = 0
stan = stan0
wej = input()
do_ktorego = [0]

for i in wej:
    stan =  przejscia[stan][int(i)]
    do_ktorego.append(stan)
#---------------------------------------------------------------

#zmienne pomocnicze
t=-1
j = 0

#ustawienia okna
screen = pygame.display.set_mode((400, 400))

#tytul okna
pygame.display.set_caption("Automat skończony")



# funkcja rysująca teksty w roznych sytuacjach (nazwy strzalek, groty strzalek, nazwy wierzcholkow)
def tekst(text, x, y, font_size=20):
    font = pygame.font.Font(None, font_size)
    
    if(text[0]=='.'):
        text_render = font.render(text[1], True, 'purple')

    else:
        if(text == "q0" or text=="<" or text==">"):
            text_render = font.render(text, True, 'white')
        else:
            text_render = font.render(text, True, 'black')
            
        if(text=="0" or text=="1"):
            text_render = font.render(text, True, 'white')
    
    screen.blit(text_render, (x-7, y-7))
    

#funkcja rysująca obrocony tekst (do grotow strzalek)
def tekst_obr(text, x, y, font_size=20):
    font = pygame.font.Font(None, font_size)
    
    if(text[0]=='.'):
        text_render = pygame.transform.rotate(font.render(text[1], True, 'purple'), -90)
    else:
        text_render = pygame.transform.rotate(font.render(text, True, 'white'), -90)
    
    screen.blit(text_render, (x, y))


while True:

    #wypisanie przejsc
    if(j<len(wej)):
        print("q%d -> " % (do_ktorego[j]), end=' ')
    if(j==len(wej)):
        print("q%d" % (do_ktorego[j]))


    #warunki wyjscia z petli
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if(t==0):
                print("Ciąg został zaakceptowany.")
            else:
                print("Ciąg nie został zaakceptowany.")
            print("------------------------------------------------------------")
            pygame.quit()
            sys.exit()

    #wyswietlanie tla
    screen.fill('black')
    
    #srodek okna
    srodek = (200, 200)
    
    #wspolrzedne srodkow wierzcholkow
    lg = (srodek[0]-120, srodek[1]-120)
    pg = (srodek[0]+120, srodek[1]-120)
    ld = (srodek[0]-120, srodek[1]+120)
    pd = (srodek[0]+120, srodek[1]+120)
    
    
    #wierzcholki
    pygame.draw.circle(screen, 'blue', (lg[0], lg[1]), 20)
    pygame.draw.circle(screen, 'white', (pg[0], pg[1]), 20)
    pygame.draw.circle(screen, 'white', (ld[0], ld[1]), 20)
    pygame.draw.circle(screen, 'white', (pd[0], pd[1]), 20)
    pygame.draw.circle(screen, 'blue', (lg[0], lg[1]), 25, 1)
    
    #nazwy wierzcholkow
    tekst("q0", lg[0], lg[1])
    tekst("q1", pg[0], pg[1])
    tekst("q2", ld[0], ld[1])
    tekst("q3", pd[0], pd[1])
    

    #strzalki (linie)
    pygame.draw.lines(screen, 'white', False, [(lg[0]-10, lg[1]+30), (ld[0]-10, ld[1]-30)], width=2)
    pygame.draw.lines(screen, 'white', False, [(lg[0]+30, lg[1]-10), (pg[0]-30, pg[1]-10)], width=2)
    pygame.draw.lines(screen, 'white', False, [(ld[0]+30, ld[1]+10), (pd[0]-30, pd[1]+10)], width=2)
    pygame.draw.lines(screen, 'white', False, [(pg[0]+10, pg[1]+30), (pd[0]+10, pd[1]-30)], width=2)
    
    pygame.draw.lines(screen, 'white', False, [(lg[0]+10, lg[1]+30), (ld[0]+10, ld[1]-30)], width=2)
    pygame.draw.lines(screen, 'white', False, [(lg[0]+30, lg[1]+10), (pg[0]-30, pg[1]+10)], width=2)
    pygame.draw.lines(screen, 'white', False, [(ld[0]+30, ld[1]-10), (pd[0]-30, pd[1]-10)], width=2)
    pygame.draw.lines(screen, 'white', False, [(pg[0]-10, pg[1]+30), (pd[0]-10, pd[1]-30)], width=2)
    
    
    
    #kolorowanie aktualnego stanu
    if(j<len(wej)+1):
            if(j!=len(wej)):
                if(do_ktorego[j]==0):
                        pygame.draw.circle(screen, 'orange', (lg[0], lg[1]), 20)
                        pygame.draw.circle(screen, 'orange', (lg[0], lg[1]), 25, 1)
                            
                if(do_ktorego[j]==1):
                        pygame.draw.circle(screen, 'orange', (pg[0], pg[1]), 20)
                            
                if(do_ktorego[j]==2):
                        pygame.draw.circle(screen, 'orange', (ld[0], ld[1]), 20)
                            
                if(do_ktorego[j]==3):
                        pygame.draw.circle(screen, 'orange', (pd[0], pd[1]), 20)
                    
            
    j+=1

    #nazwy strzalek
    tekst("1", srodek[0], lg[1]-20)
    tekst("1", srodek[0], pg[1]+20)
    tekst("1", srodek[0], ld[1]-20)
    tekst("1", srodek[0], pd[1]+20)
    tekst("0", lg[0]-20, srodek[1])
    tekst("0", lg[0]+25, srodek[1])
    tekst("0", pg[0]-20, srodek[1])
    tekst("0", pg[0]+25, srodek[1])
    
    
    #groty strzalek
    tekst(">", pg[0]-30, pg[1]-10)
    tekst("<", lg[0]+35, lg[1]+10)
    tekst(">", pd[0]-30, pd[1]-10)
    tekst("<", ld[0]+35, ld[1]+10)
    tekst_obr("<", lg[0]-10-4, lg[1]+30-3)
    tekst_obr("<", pg[0]-10-4, pg[1]+30-3)
    tekst_obr(">", ld[0]+10-4, ld[1]-30-3)
    tekst_obr(">", pd[0]+10-4, pd[1]-30-3)

    
    #kolorowanie strzalek i grotow
    if(j>0 and j<len(wej)+1):
        if(do_ktorego[j-1]==0 and do_ktorego[j]==1):
                pygame.draw.lines(screen, 'purple', False, [(lg[0]+30, lg[1]-10), (pg[0]-30, pg[1]-10)], width=2)
                tekst(".>", pg[0]-30, pg[1]-10)
                
        if(do_ktorego[j-1]==0 and do_ktorego[j]==2):
                pygame.draw.lines(screen, 'purple', False, [(lg[0]+10, lg[1]+30), (ld[0]+10, ld[1]-30)], width=2)
                tekst_obr(".>", ld[0]+10-4, ld[1]-30-3)
                
        if(do_ktorego[j-1]==1 and do_ktorego[j]==3):
                pygame.draw.lines(screen, 'purple', False, [(pg[0]+10, pg[1]+30), (pd[0]+10, pd[1]-30)], width=2)
                tekst_obr(".>", pd[0]+10-4, pd[1]-30-3)
                
        if(do_ktorego[j-1]==1 and do_ktorego[j]==0):
                pygame.draw.lines(screen, 'purple', False, [(lg[0]+30, lg[1]+10), (pg[0]-30, pg[1]+10)], width=2)
                tekst(".<", lg[0]+35, lg[1]+10)
           
        if(do_ktorego[j-1]==2 and do_ktorego[j]==3):
                pygame.draw.lines(screen, 'purple', False, [(ld[0]+30, ld[1]-10), (pd[0]-30, pd[1]-10)], width=2)
                tekst(".>", pd[0]-30, pd[1]-10)
                
        if(do_ktorego[j-1]==2 and do_ktorego[j]==0):
                pygame.draw.lines(screen, 'purple', False, [(lg[0]-10, lg[1]+30), (ld[0]-10, ld[1]-30)], width=2)
                tekst_obr(".<", lg[0]-10-4, lg[1]+30-3)
                
        if(do_ktorego[j-1]==3 and do_ktorego[j]==1):
                pygame.draw.lines(screen, 'purple', False, [(pg[0]-10, pg[1]+30), (pd[0]-10, pd[1]-30)], width=2)
                tekst_obr(".<", pg[0]-10-4, pg[1]+30-3)
                
        if(do_ktorego[j-1]==3 and do_ktorego[j]==2):
                pygame.draw.lines(screen, 'purple', False, [(ld[0]+30, ld[1]+10), (pd[0]-30, pd[1]+10)], width=2)
                tekst(".<", ld[0]+35, ld[1]+10)
                
                
             
    #wyswietlanie stanu koncowego
    if(t==0):
        pygame.draw.circle(screen, 'green', (lg[0], lg[1]), 20)
        pygame.draw.circle(screen, 'green', (lg[0], lg[1]), 25, 1)
    if(t==1):
        pygame.draw.circle(screen, 'red', (pg[0], pg[1]), 20)
    if(t==2):
        pygame.draw.circle(screen, 'red', (ld[0], ld[1]), 20)
    if(t==3):
        pygame.draw.circle(screen, 'red', (pd[0], pd[1]), 20)
                
                
    #wyswietlanie stanu koncowego
    if(j-1==len(wej) and t==-1):
        if(do_ktorego[j-1]==0):
            pygame.draw.circle(screen, 'green', (lg[0], lg[1]), 20)
            pygame.draw.circle(screen, 'green', (lg[0], lg[1]), 25, 1)
            pygame.draw.circle(screen, 'white', (pg[0], pg[1]), 20)
            pygame.draw.circle(screen, 'white', (ld[0], ld[1]), 20)
            pygame.draw.circle(screen, 'white', (pd[0], pd[1]), 20)
            t=0
                    
        if(do_ktorego[j-1]==1):
            pygame.draw.circle(screen, 'red', (pg[0], pg[1]), 20)
            pygame.draw.circle(screen, 'blue', (lg[0], lg[1]), 20)
            pygame.draw.circle(screen, 'white', (ld[0], ld[1]), 20)
            pygame.draw.circle(screen, 'white', (pd[0], pd[1]), 20)
            t=1
                            
        if(do_ktorego[j-1]==2):
            pygame.draw.circle(screen, 'red', (ld[0], ld[1]), 20)
            pygame.draw.circle(screen, 'blue', (lg[0], lg[1]), 20)
            pygame.draw.circle(screen, 'white', (pg[0], pg[1]), 20)
            pygame.draw.circle(screen, 'white', (pd[0], pd[1]), 20)
            t=2
                
        if(do_ktorego[j-1]==3):
            pygame.draw.circle(screen, 'red', (pd[0], pd[1]), 20)
            pygame.draw.circle(screen, 'blue', (lg[0], lg[1]), 20)
            pygame.draw.circle(screen, 'white', (pg[0], pg[1]), 20)
            pygame.draw.circle(screen, 'white', (ld[0], ld[1]), 20)
            t=3

        
    #nazwy wierzcholkow
    tekst("q0", lg[0], lg[1])
    tekst("q1", pg[0], pg[1])
    tekst("q2", ld[0], ld[1])
    tekst("q3", pd[0], pd[1])
    
    #uaktualnienie ekranu
    pygame.display.flip()
    pygame.time.wait(2000)
    
    #warunek wyjscia z petli
    if(j>len(wej)+3):
        if(t==0):
            print("Ciąg został zaakceptowany.")
        else:
            print("Ciąg nie został zaakceptowany.")
        print("------------------------------------------------------------")
    
        pygame.quit()
        sys.exit()
    


