self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
self.rect = self.screen.get_rect()
pygame.display.set_caption(TITLE)
self.background = load_image('level.png')
self.back_rect = self.background.get_rect()
self.background = pygame.transform.scale(self.background,
                                     (int(self.back_rect.width * BACKGROUND_SIZE),
                                      int(self.back_rect.height * BACKGROUND_SIZE))).convert()
self.sheet = load_image('mario.png')
self.load_from_sheet()
self.rect = self.image.get_rect()
self.pos = vec(WIDTH * 0.5, GROUND_HEIGHT - 70)
self.vel = vec(0, 0)
self.acc = vec(0, 0)
self.acc = vec(0, GRAVITY)
if GROUND_HEIGHT < self.mario.pos.y:
    self.mario.acc.y = 0
    self.mario.vel.y = 0
    self.mario.pos.y = self.ground_collide.rect.top
 self.mario.landing = True
 keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        self.pos.x += 5 
    elif keys[pygame.K_LEFT]:
       if self.vel.x < 0:
            self.acc.x = -TURNAROUND
            if self.vel.x >= 0: 
                self.acc.x = -ACC
    if abs(self.vel.x) < MAX_SPEED:
        self.vel.x += self.acc.x
    elif keys[pygame.K_LEFT]:
        self.vel.x = -MAX_SPEED
    elif keys[pygame.K_RIGHT]:
        self.vel.x = MAX_SPEED
    self.acc.x += self.vel.x * FRICTION
    self.vel += self.acc
    self.pos += self.vel + 0.5 * self.acc
    self.rect.midbottom = self.pos
    if keys[pygame.K_SPACE]:
    if self.landing:
        self.vel.y = -JUMP
