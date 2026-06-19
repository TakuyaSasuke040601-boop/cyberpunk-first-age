import pygame, sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber Rider: DyShinzou 2088")
clock = pygame.time.Clock()

# --- LOAD NHÂN VẬT ---
base_img = pygame.image.load("base.png")
base_img = pygame.transform.scale(base_img, (64, 64))
player_img = base_img
player_rect = player_img.get_rect()
player_rect.midbottom = (100, HEIGHT - 50)

# --- BIẾN HENSHIN ---
is_henshin = False
font = pygame.font.Font(None, 24)
print("Game start. Bấm H để HENSHIN!")

# --- GAME LOOP ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                is_henshin = not is_henshin
                if is_henshin:
                    print("HENSHIN! DZO DRIVER KÍCH HOẠT!")
                else:
                    print("Giải trừ henshin...")

    # --- VẼ ---
    screen.fill((20, 10, 30)) # Nền tím cyber
    screen.blit(player_img, player_rect)

    # Hiện trạng thái Henshin
    status = "RIDER FORM" if is_henshin else "BASE FORM - Press H"
    text = font.render(status, True, (0, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)