import pygame
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT=500,500
display_surface=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Adding images")
background_images=pygame.transform.scale(pygame.image.load("C:/Users/symbi/Pictures/Screenshots/Screenshot 2024-11-29 175918.png").convert(),(500,500))
ballon_image=pygame.transform.scale(pygame.image.load("C:/Users/symbi/Pictures/Screenshots/Screenshot (156).png").convert_alpha(),(200,300))
text=pygame.font.Font(None,36).rander('Hello world',True,pygame.Color("black"))
text_rect=text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2 +110))
def gameloop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event .type==pygame.QUIT:
                pygame.quit()
        display_surface.blit(background_images,(0,0))
        display_surface.blit(ballon_image,(SCREEN_WIDTH//2,SCREEN_HEIGHT//2 -30))
        display_surface.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
gameloop()
