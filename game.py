import pygame, sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber Rider: DyShinzou 2088 - DAY 5")
clock = pygame.time.Clock()

# LOAD BASE FORM - SCALE GIỮ TỶ LỆ
base_img = pygame.image.load("base.png")
base_height = 128  # Đổi số này để to/nhỏ
base_width = int(base_img.get_width() * (base_height / base_img.get_height()))
base_img = pygame.transform.scale(base_img, (base_width, base_height))

# LOAD RIDER FORM - SCALE GIỮ TỶ LỆ  
rider_img = pygame.image.load("rider.png")
rider_height = 128  # Cho bằng base_height
rider_width = int(rider_img.get_width() * (rider_height / rider_img.get_height()))
rider_img = pygame.transform.scale(rider_img, (rider_width, rider_height))
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
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h: # BẤM H = HENSHIN
                is_henshin = not is_henshin
                henshin_flash = 6 # Flash trắng 6 frame
                if is_henshin:
                    player_img = rider_img
                    print("HENSHIN! DZO DRIVER KÍCH HOẠT!")
                else:
                    player_img = base_img
                    print("Giải trừ henshin...")

    # Di chuyển A/D
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    # VẼ
    screen.fill((15, 10, 25)) # Nền Sài Gòn 2088
    pygame.draw.rect(screen, (50, 50, 50), (0, HEIGHT - 50, WIDTH, 50)) # Sàn
    
    # Hiệu ứng flash lúc biến hình
    if henshin_flash > 0:
        screen.fill((255, 255, 255))
        henshin_flash -= 1
    
    screen.blit(player_img, player_rect)
    
    # UI
    form_text = "RIDER FORM" if is_henshin else "BASE FORM"
    color = (255, 100, 0) if is_henshin else (0, 255, 255)
    text = font.render(f"{form_text} - Press H to Henshin", True, color)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)