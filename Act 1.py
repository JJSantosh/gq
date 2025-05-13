import pygame
import random 
pygame.init()
surf_colors="pink"
color="blue"

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,h,w):
        super().__init__()
        self.image=pygame.Surface([w,h])
        self.image.fill(surf_colors)
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,w,h))
        self.rect=self.image.get_rect() 

pygame.init()
screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("ADD SPRITE")
all_sprites_list=pygame.sprite.Group()

sp1=Sprite(color,20,30)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,380)
all_sprites_list.add(sp1)

sp2=Sprite(color,20,30)
sp2.rect.x=random.randint(0,480)
sp2.rect.y=random.randint(0,380)
all_sprites_list.add(sp2)

exit=True
clock=pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=False

    all_sprites_list.update()
    screen.fill(surf_colors)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()