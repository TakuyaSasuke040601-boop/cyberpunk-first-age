import pygame, sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber Rider: DyShinzou 2088 - DAY 6.5")
clock = pygame.time.Clock()

# LOAD BASE FORM - MẶC ÁO HOODIE
base_img = pygame.image.load("base.png")
base_height = 128  
base_width = int(base_img.get_width() * (base_height / base_img.get_height()))
base_img = pygame.transform.scale(base_img, (base_width, base_height))

# LOAD RIDER FORM - NORMAL CYAN CAM
rider_normal_img = pygame.image.load("rider_normal.png")
rider_normal_img = pygame.transform.scale(rider_normal_img, (base_width, base_height))

# LOAD RIDER FORM - OVERCLOCK BẠC XANH LÁ
rider_overclock_img = pygame.image.load("rider_overclock.png")
rider_overclock_img = pygame.transform.scale(rider_overclock_img, (base_width, base_height))

# LOAD RIDER FORM - FINAL ĐEN CAM ĐỎ
rider_final_img = pygame.image.load("rider_final.png")
rider_final_img = pygame.transform.scale(rider_final_img, (base_width, base_height))

# LOAD RIDER FORM - GHOSTWALKER ĐEN XANH LÁ CÓ CÁNH
rider_ghostwalker_img = pygame.image.load("rider_ghostwalker.png")
rider_ghostwalker_img = pygame.transform.scale(rider_ghostwalker_img, (base_width, base_height))
rider_ghostwalker_img.set_alpha(255)

# --- PLAYER ---
player_img = base_img
player_rect = player_img.get_rect()
player_rect.midbottom = (100, HEIGHT - 50)
player_speed = 5

# --- HENSHIN STATE ---
is_henshin = False
henshin_flash = 0

font = pygame.font.Font(None, 28)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:  # B = BASE
                player_img = base_img
                is_henshin = False
                print("BASE FORM")
                
            if event.key == pygame.K_h:  # H = NORMAL
                player_img = rider_normal_img
                is_henshin = True
                henshin_flash = 6
                print("RIDER FORM - NORMAL")
                
            if event.key == pygame.K_j:  # J = OVERCLOCK
                player_img = rider_overclock_img
                is_henshin = True
                henshin_flash = 6
                print("OVERCLOCK FORM")
                
            if event.key == pygame.K_f:  # F = FINAL
                player_img = rider_final_img
                is_henshin = True
                henshin_flash = 6
                print("FINAL FORM - DZO DRIVER")
                
            if event.key == pygame.K_k:  # K = GHOSTWALKER
                player_img = rider_ghostwalker_img
                is_henshin = True
                henshin_flash = 6
                print("GHOSTWALKER FORM")

    # Di chuyển A/D hoặc LEFT/RIGHT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    
    # Giới hạn không cho đi ra ngoài màn hình
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > WIDTH:
        player_rect.right = WIDTH

    # VẼ
    screen.fill((15, 10, 25))
    pygame.draw.rect(screen, (50, 50, 50), (0, HEIGHT - 50, WIDTH, 50))
    
    # Hiệu ứng flash trắng lúc biến hình
    if henshin_flash > 0:
        screen.fill((255, 255, 255))
        henshin_flash -= 1
    
    screen.blit(player_img, player_rect)
    
    # UI
    if is_henshin:
        if player_img == rider_normal_img:
            form_text = "RIDER FORM - NORMAL"
        elif player_img == rider_overclock_img:
            form_text = "OVERCLOCK FORM"
        elif player_img == rider_final_img:
            form_text = "FINAL FORM"
        elif player_img == rider_ghostwalker_img:
            form_text = "GHOSTWALKER FORM"
        color = (255, 100, 0)
    else:
        form_text = "BASE FORM"
        color = (0, 255, 255)
        
    text = font.render(f"{form_text} - Press B/H/J/F/K", True, color)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)