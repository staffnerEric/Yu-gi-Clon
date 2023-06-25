import pygame
import random
import os
from enum import Enum

#bilder
karte = pygame.image.load(os.path.join("E:\Informatik mit Luca","Testcard.png"))
Hintergrund = pygame.image.load(os.path.join("E:\Informatik mit Luca","image.jpg"))
kartenslots = pygame.image.load(os.path.join("E:\Informatik mit Luca","kartslo.jpg"))
kartenslotsgeg = pygame.image.load(os.path.join("E:\Informatik mit Luca","kardgeg.jpg"))

pygame.init()
#höhe und breite des bildschirms
info = pygame.display.Info()
H = info.current_h
W = info.current_w
pos=1400
pos2=750
kardclick = False
CARD_WIDTH = 100
CARD_HEIGHT = 150
Hand = []
#kart=Testkarte
kart = pygame.transform.scale(karte, (100, 150))
Hinterbild = pygame.transform.scale(Hintergrund, (W, H))
kartslot = pygame.transform.scale(kartenslots, (100, 150))
kartslotgeg = pygame.transform.scale(kartenslotsgeg, (100, 150))
yuuuu = True
Testdeck=[kart, kart, kart, kart, kart, kart ,kart, kart]
win=pygame.display.set_mode((W, H-50), pygame.RESIZABLE)
win.blit(Hinterbild, (0,0))
class Slots(float, Enum):
    a ,b ,c ,d =750, 550, 350, 150
    Slot1y = a
    Slot2y = a
    Slot3y = a
    Slot4y = a
    Slot5y = a
    Slot6y = a
    Slot7y = b
    Slot8y = b
    Slot9y = b
    Slot10y = b
    Slot11y = b
    Slot12y = b

    gegSlot1y = d
    gegSlot2y = d
    gegSlot3y = d
    gegSlot4y = d
    gegSlot5y = d
    gegSlot6y = d
    gegSlot7y = c
    gegSlot8y = c
    gegSlot9y = c
    gegSlot10y = c
    gegSlot11y = c
    gegSlot12y = c

    Slot1x = 500
    Slot2x = 650
    Slot3x = 800
    Slot4x = 950
    Slot5x = 1100
    Slot6x = 1250
    Slot7x = 500
    Slot8x = 650
    Slot9x = 800
    Slot10x = 950
    Slot11x = 1100
    Slot12x = 1250

    gegSlot1x = 500
    gegSlot2x = 650
    gegSlot3x = 800
    gegSlot4x = 950
    gegSlot5x = 1100
    gegSlot6x = 1250
    gegSlot7x = 500
    gegSlot8x = 650
    gegSlot9x = 800
    gegSlot10x = 950
    gegSlot11x = 1100
    gegSlot12x = 1250

#Kartenslots
S1=win.blit(kartslot, (Slots.Slot1x, Slots.Slot1y))
S2=win.blit(kartslot, (Slots.Slot2x, Slots.Slot2y))
S3=win.blit(kartslot, (Slots.Slot3x, Slots.Slot3y))
S4=win.blit(kartslot, (Slots.Slot4x, Slots.Slot4y))
S5=win.blit(kartslot, (Slots.Slot5x, Slots.Slot5y))
S6=win.blit(kartslot, (Slots.Slot6x, Slots.Slot6y))
S7=win.blit(kartslot, (Slots.Slot7x, Slots.Slot7y))
S8=win.blit(kartslot, (Slots.Slot8x, Slots.Slot8y))
S9=win.blit(kartslot, (Slots.Slot9x, Slots.Slot9y))
S10=win.blit(kartslot, (Slots.Slot10x, Slots.Slot10y))
S11=win.blit(kartslot, (Slots.Slot11x, Slots.Slot11y))
S12=win.blit(kartslot, (Slots.Slot12x, Slots.Slot12y))
Sg1=win.blit(kartslotgeg, (Slots.Slot1x, Slots.gegSlot1y))
Sg2=win.blit(kartslotgeg, (Slots.Slot2x, Slots.gegSlot2y))
Sg3=win.blit(kartslotgeg, (Slots.Slot3x, Slots.gegSlot3y))
Sg4=win.blit(kartslotgeg, (Slots.Slot4x, Slots.gegSlot4y))
Sg5=win.blit(kartslotgeg, (Slots.Slot5x, Slots.gegSlot5y))
Sg6=win.blit(kartslotgeg, (Slots.Slot6x, Slots.gegSlot6y))
Sg7=win.blit(kartslotgeg, (Slots.Slot7x, Slots.gegSlot7y))
Sg8=win.blit(kartslotgeg, (Slots.Slot8x, Slots.gegSlot8y))
Sg9=win.blit(kartslotgeg, (Slots.Slot9x, Slots.gegSlot9y))
Sg10=win.blit(kartslotgeg, (Slots.Slot10x, Slots.gegSlot10y))
Sg11=win.blit(kartslotgeg, (Slots.Slot11x, Slots.gegSlot11y))
Sg12=win.blit(kartslotgeg, (Slots.Slot12x, Slots.gegSlot12y))

for i in range(6):
    e = random.randint(0, len(Testdeck)-1)
    card_pos = (pos, pos2)  # Store card position as a tuple
    win.blit(Testdeck[e], card_pos)
    Hand.append(card_pos)
    del Testdeck[e]
    pos2 -= 200
    if pos2 == 350:
        pos += 150
        pos2 = 750

pygame.display.update()
while yuuuu:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            yuuuu = False
        elif e.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            for i, card_pos in enumerate(Hand):
                card_rect = pygame.Rect(card_pos[0], card_pos[1], CARD_WIDTH, CARD_HEIGHT)
                if card_rect.collidepoint(click_pos):
                    kardclick = True
                if S1.collidepoint(click_pos) and kardclick:
                    Hand.remove(card_pos)
                    card_pos = (Slots.Slot1x, Slots.Slot1y)
                    Hand.append(card_pos)
                elif S2.collidepoint(click_pos) and kardclick:
                    Hand.remove(card_pos)
                    card_pos = (Slots.Slot2x, Slots.Slot2y)
                    Hand.append(card_pos)
                elif S3.collidepoint(click_pos) and kardclick:
                    Hand.remove(card_pos)
                    card_pos = (Slots.Slot3x, Slots.Slot3y)
                    Hand.append(card_pos)
                elif S4.collidepoint(click_pos) and kardclick:
                    Hand.remove(card_pos)
                    card_pos = (Slots.Slot4x, Slots.Slot4y)
                    Hand.append(card_pos)
                elif S5.collidepoint(click_pos) and kardclick:
                    Hand.remove(card_pos)
                    card_pos = (Slots.Slot5x, Slots.Slot5y)
                    Hand.append(card_pos)
                elif S6.collidepoint(click_pos) and kardclick:
                    Hand.remove(card_pos)
                    card_pos = (Slots.Slot6x, Slots.Slot6y)
                    Hand.append(card_pos)
                elif S7.collidepoint(click_pos) and kardclick:
                    Hand.remove(card_pos)
                    card_pos = (Slots.Slot7x, Slots.Slot7y)
                    Hand.append(card_pos)
                elif S8.collidepoint(click_pos) and kardclick:
                    Hand.remove(card_pos)
                    card_pos = (Slots.Slot8x, Slots.Slot8y)
                    Hand.append(card_pos)
                elif S9.collidepoint(click_pos) and kardclick:
                    Hand.remove(card_pos)
                    card_pos = (Slots.Slot9x, Slots.Slot9y)
                    Hand.append(card_pos)
                elif S10.collidepoint(click_pos) and kardclick:
                    Hand.remove(card_pos)
                    card_pos = (Slots.Slot10x, Slots.Slot10y)
                    Hand.append(card_pos)
                elif S11.collidepoint(click_pos) and kardclick:
                    Hand.remove(card_pos)
                    card_pos = (Slots.Slot11x, Slots.Slot11y)
                    Hand.append(card_pos)
                elif S12.collidepoint(click_pos) and kardclick:
                    Hand.remove(card_pos)
                    card_pos = (Slots.Slot12x, Slots.Slot12y)
                    Hand.append(card_pos)

    win.blit(Hinterbild, (0,0))
    for card_pos in Hand:
        win.blit(kart, card_pos)
    win.blit(kartslot, (Slots.Slot1x, Slots.Slot1y))
    win.blit(kartslot, (Slots.Slot2x, Slots.Slot2y))
    win.blit(kartslot, (Slots.Slot3x, Slots.Slot3y))
    win.blit(kartslot, (Slots.Slot4x, Slots.Slot4y))
    win.blit(kartslot, (Slots.Slot5x, Slots.Slot5y))
    win.blit(kartslot, (Slots.Slot6x, Slots.Slot6y))
    win.blit(kartslot, (Slots.Slot7x, Slots.Slot7y))
    win.blit(kartslot, (Slots.Slot8x, Slots.Slot8y))
    win.blit(kartslot, (Slots.Slot9x, Slots.Slot9y))
    win.blit(kartslot, (Slots.Slot10x, Slots.Slot10y))
    win.blit(kartslot, (Slots.Slot11x, Slots.Slot11y))
    win.blit(kartslot, (Slots.Slot12x, Slots.Slot12y))

    win.blit(kartslotgeg, (Slots.Slot1x, Slots.gegSlot1y))
    win.blit(kartslotgeg, (Slots.Slot2x, Slots.gegSlot2y))
    win.blit(kartslotgeg, (Slots.Slot3x, Slots.gegSlot3y))
    win.blit(kartslotgeg, (Slots.Slot4x, Slots.gegSlot4y))
    win.blit(kartslotgeg, (Slots.Slot5x, Slots.gegSlot5y))
    win.blit(kartslotgeg, (Slots.Slot6x, Slots.gegSlot6y))
    win.blit(kartslotgeg, (Slots.Slot7x, Slots.gegSlot7y))
    win.blit(kartslotgeg, (Slots.Slot8x, Slots.gegSlot8y))
    win.blit(kartslotgeg, (Slots.Slot9x, Slots.gegSlot9y))
    win.blit(kartslotgeg, (Slots.Slot10x, Slots.gegSlot10y))
    win.blit(kartslotgeg, (Slots.Slot11x, Slots.gegSlot11y))
    win.blit(kartslotgeg, (Slots.Slot12x, Slots.gegSlot12y))

    pygame.display.update()
        #nun will ich versuchen karten zu platzieren
        #und die karten designen
        #und ideen fur die decks sammeln