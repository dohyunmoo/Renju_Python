import pygame

def numberType(a):
    if a%2 == 1:
        return True # true if odd
    elif a%2 == 0:
        return False # false if even

def winType(a):
    if numberType(a) == True:
        pygame.quit()
        print("Black Win") # odd = black
    elif numberType(a) == False:
        pygame.quit()
        print("White Win") # even = white
