import pygame
import sys
import os

FPS = 60


def load_image(name):
    try:
        fullname = os.path.join('datagame', name)
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    return image


def load_pers(name, data):
    fullname = os.path.join(data, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    color_key = image.get_at((0, 0))
    image.set_colorkey(color_key)
    image = image.convert_alpha()
    return image


def terminate():
    if lvl:
        lvlsave = []
        x, y = board.get_cell((player.rect.x, player.rect.y))
        for j in range(len(board.board[0])):
            line = ''
            for i in range(len(board.board)):
                if board.board[i][j]:
                    line += board.board[i][j].code
                else:
                    if i == x and j == y:
                        line += '@'
                    else:
                        line += 'q'
            lvlsave.append(line)
        file = open('datalvl/lvl1reserve.txt', 'w')
        file.write('\n'.join(lvlsave))
        file.close()
    pygame.quit()
    sys.exit()


def start_screen():
    muza2.play()
    intro_text = ["Heroes of sword", "",
                  "Start",
                  "Continue",
                  "Exit"]

    fon = pygame.transform.scale(load_image('back2.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 150
    rects = []
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        rects.append(pygame.Rect(intro_rect).move(180, text_coord))
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 180
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rects[2].collidepoint(event.pos):
                    muza2.stop()
                    return 'lvl1.txt'
                elif rects[3].collidepoint(event.pos):
                    muza2.stop()
                    return 'lvl1reserve.txt'
                elif rects[4].collidepoint(event.pos):
                    terminate()

        screen.blit(fon, (0, 0))
        if rects[2].collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (155, 155, 155), ((rects[2].x, rects[2].y + 10), rects[2].size))

        if rects[3].collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (155, 155, 155), ((rects[3].x, rects[3].y + 10), rects[3].size))

        if rects[4].collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (155, 155, 155), ((rects[4].x, rects[4].y + 8), rects[4].size))

        text_coord = 150
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'), ())
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 180
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        mose_group.draw(screen)
        pygame.display.flip()
        mose_group.update()
        clock.tick(FPS)


def pause():
    muza2.play()
    intro_text = ["Heroes of sword", "",
                  "Continue",
                  "Save and exit"]

    fon = pygame.transform.scale(load_image('back2.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 150
    rects = []
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        rects.append(pygame.Rect(intro_rect).move(180, text_coord))
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 180
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rects[2].collidepoint(event.pos):
                    muza2.stop()
                    return  # начинаем игру
                elif rects[3].collidepoint(event.pos):
                    terminate()

        screen.blit(fon, (0, 0))
        if rects[2].collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (155, 155, 155), ((rects[2].x, rects[2].y + 10), rects[2].size))

        if rects[4].collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (155, 155, 155), ((rects[4].x, rects[4].y + 8), rects[4].size))

        text_coord = 150
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'), ())
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 180
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        mose_group.draw(screen)
        pygame.display.flip()
        mose_group.update()
        clock.tick(FPS)


def bag():
    intro_text = ['blocks', 'tools',
                  'fon blocks',
                  "go back"]

    fon = pygame.transform.scale(load_image('back2.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 150
    rects = []
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        rects.append(pygame.Rect(intro_rect).move(180, text_coord))
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 180
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rects[2].collidepoint(event.pos):
                    muza2.stop()
                    return  # начинаем игру
                elif rects[3].collidepoint(event.pos):
                    terminate()

        screen.blit(fon, (0, 0))
        if rects[2].collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (155, 155, 155), ((rects[2].x, rects[2].y + 10), rects[2].size))

        if rects[4].collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (155, 155, 155), ((rects[4].x, rects[4].y + 8), rects[4].size))

        text_coord = 150
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'), ())
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 180
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        mose_group.draw(screen)
        pygame.display.flip()
        mose_group.update()
        clock.tick(FPS)


def load_level(filename):
    filename = "datalvl/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, ' '), level_map))


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(mose_group, all_sprites)
        self.image = load_image("pickaxe.jpg")
        self.rect = self.image.get_rect()

    def update(self):
        a, s = pygame.mouse.get_pos()
        self.rect.x = a
        self.rect.y = s


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, cod):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.type = tile_type
        self.code = cod
        if tile_type == 'lawa':
            self.add(lawagrup)
        self.rect = self.image.get_rect().move(
            totx + tile_width * pos_x, toty + tile_height * pos_y)
        self.x = pos_x
        self.y = pos_y

    def new(self, x, y):
        if self.type == 'lawa':
            self.add(lawagrup)
        self.rect.x = totx + tile_width * x
        self.rect.y = toty + tile_height * y
        self.x = x
        self.y = y


class Fonblock(pygame.sprite.Sprite):
    def __init__(self, fon_type, pos_x, pos_y):
        super().__init__(fonblock_group, all_sprites)
        self.image = tile_images[fon_type]
        self.type = fon_type
        self.rect = self.image.get_rect().move(
            totx + tile_width * pos_x, toty + tile_height * pos_y)
        self.x = pos_x
        self.y = pos_y

    def new(self, x, y):
        self.rect.x = totx + tile_width * x
        self.rect.y = toty + tile_height * y
        self.x = x
        self.y = y


class Healf(pygame.sprite.Sprite):
    def __init__(self, man):
        super().__init__(hert_group)
        self.man = man
        self.image = pygame.Surface((self.man.rect.width, 8),
                                    pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color("red"),
                         ((0, 0), ((self.man.heart / self.man.max) * self.man.rect.width, 8)))
        pygame.draw.rect(self.image, pygame.Color(185 , 0, 0),
                         ((self.man.rect.width, 0),
                          (-((self.man.max - self.man.heart) / self.man.max) * self.man.rect.width, 8)))
        self.rect = self.image.get_rect().move(self.man.rect.x, self.man.rect.y - 5)

    def update(self):
        if self.man.heart <= 0:
            self.kill()
        pygame.draw.rect(self.image, pygame.Color("red"),
                         ((0, 0), ((self.man.heart / self.man.max) * self.man.rect.width, 8)))
        pygame.draw.rect(self.image, pygame.Color(185, 0, 0),
                         ((self.man.rect.width, 0),
                          (-((self.man.max - self.man.heart) / self.man.max) * self.man.rect.width, 8)))
        self.rect = self.image.get_rect().move(self.man.rect.x, self.man.rect.y - 5)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites, alife_group)
        self.sheet = npc_image['elf']
        self.frames = []
        self.cut_sheet(self.sheet)
        self.cur_frame = 0
        self.maxframe = 9
        self.r = 1
        self.image = self.frames[10][0]
        self.rect = self.image.get_rect().move(pos_x * 50, pos_y * 50)
        self.radius = 150
        self.xvel = 0
        self.yvel = 0
        self.t = 0
        self.onGround = False
        self.max = self.heart = 2000
        self.bag = []
        Healf(self)

    def cut_sheet(self, sheet):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // 13, sheet.get_height() // 21)
        for j in range(21):
            row = []
            for i in range(13):
                frame_location = (self.rect.w * i, self.rect.h * j)
                row.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))
            self.frames.append(row)

    def update(self):
        if self.heart < self.max and self.t % 7 == 0:
            self.heart += 2

        if left:
            if self.r == 1:
                self.cur_frame = 0
                self.maxframe = 9
            self.r = 0
            self.xvel = -9
        if right:
            if self.r == 0:
                self.cur_frame = 0
                self.maxframe = 9
            self.r = 1
            self.xvel = 9
        if not (left or right):
            self.xvel = 0

        if up:
            if self.onGround:
                self.maxframe = 7
                self.yvel = -10

        if click1 or click2:
            self.maxframe = 6

        if not self.onGround:
            self.yvel += 0.25

        if self.t % 3 == 0:
            self.cur_frame = (self.cur_frame + 1) % self.maxframe
            if click1 or click2:
                if self.r:
                    self.image = self.frames[15][self.cur_frame]
                else:
                    self.image = self.frames[13][self.cur_frame]
                for mon in npc_group:
                    if pygame.sprite.collide_rect(self, mon):
                        mon.heart -= 50
                stook.play()

            elif up:
                if self.r:
                    self.image = self.frames[3][self.cur_frame]
                else:
                    self.image = self.frames[1][self.cur_frame]

            elif right:
                self.image = self.frames[11][self.cur_frame]

            elif left:
                self.image = self.frames[9][self.cur_frame]

            else:
                self.image = self.frames[10][0]

        if (left or right) and self.yvel == 0:
            if self.t % 15:
                walk.play(0, 60)
                walk.set_volume(8)
        else:
            walk.stop()

        if self.t % 1500 == 0:
            pos = board.get_cell((self.rect.x - 800, self.rect.y))
            if pos:
                Goplit(pos[0], pos[1])


        self.t += 1
        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0)
        self.rect.y += self.yvel
        self.collide(0, self.yvel)
        self.die()

    def die(self):
        if self.heart <= 0:
            self.kill()
            start_screen()
            terminate()

    def collide(self, xvel, yvel):
        for tile in tiles_group:
            if pygame.sprite.collide_rect(self, tile):
                if xvel > 0:
                    self.rect.right = tile.rect.left
                if xvel < 0:
                    self.rect.left = tile.rect.right
                if yvel > 0:
                    if not self.onGround and yvel > 3:
                        jump.play()
                    self.rect.bottom = tile.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = tile.rect.bottom
                    self.yvel = 0
                if tile.type == 'lawa':
                    self.heart -= 60


class Warior(pygame.sprite.Sprite):
    def cut_sheet(self, sheet):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // 13, sheet.get_height() // 21)
        for j in range(21):
            row = []
            for i in range(13):
                frame_location = (self.rect.w * i, self.rect.h * j)
                row.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))
            self.frames.append(row)

    def die(self):
        if self.heart <= 0:
            self.kill()

    def collide(self, xvel, yvel):
        for tile in tiles_group:
            if pygame.sprite.collide_rect(self, tile):

                if xvel > 0:
                    self.rect.right = tile.rect.left
                if xvel < 0:
                    self.rect.left = tile.rect.right
                if yvel > 0:
                    self.rect.bottom = tile.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = tile.rect.bottom
                    self.yvel = 0
                if tile.type == 'lawa':
                    self.heart -= 40


class Assasin(Warior):
    def __init__(self, pos_x, pos_y):
        super().__init__(npc_group, all_sprites, alife_group)
        self.sheet = npc_image['elf']
        self.frames = []
        self.cut_sheet(self.sheet)
        self.cur_frame = 0
        self.maxframe = 9
        self.r = 1
        self.image = self.frames[10][0]
        self.rect = self.image.get_rect().move(pos_x * 50, pos_y * 50)
        self.xvel = 0
        self.yvel = 0
        self.t = 0
        self.bit = False
        self.onGround = False
        self.max = self.heart = 800
        Healf(self)

    def update(self):
        if self.heart < self.max and self.t % 4 == 0:
            self.heart += 2

        if player.rect.x - self.rect.x > -500 and player.rect.x - self.rect.x < -50:
            if self.r == 1:
                self.cur_frame = 0
                self.maxframe = 9
            self.r = 0
            self.xvel = -7

        if player.rect.x - self.rect.x < 500 and player.rect.x - self.rect.x > 50:
            if self.r == 0:
                self.cur_frame = 0
                self.maxframe = 9
            self.r = 1
            self.xvel = 7

        if player.rect.x - self.rect.x < 40 and player.rect.x - self.rect.x > -40:
            self.xvel = 0
            self.maxframe = 6
            self.bit = True
        else:
            self.bit = False

        if player.rect.x - self.rect.x > 500 or player.rect.x - self.rect.x < -500:
            self.xvel = 0

        if up:
            if self.onGround:
                self.maxframe = 7
                self.yvel = -9

        if not self.onGround:
            self.yvel += 0.25

        if self.t % 3 == 0:
            self.cur_frame = (self.cur_frame + 1) % 7
            if self.bit:
                if self.r:
                    self.image = self.frames[15][self.cur_frame]
                else:
                    self.image = self.frames[13][self.cur_frame]
                if pygame.sprite.collide_rect(self, player):
                    player.heart -= 10
                    stook.play()

            elif up:
                if self.r:
                    self.image = self.frames[3][self.cur_frame]
                else:
                    self.image = self.frames[1][self.cur_frame]

            elif self.xvel == 7:
                self.image = self.frames[11][self.cur_frame]

            elif self.xvel == -7:
                self.image = self.frames[9][self.cur_frame]

            else:
                self.image = self.frames[10][0]

        if (left or right) and self.yvel != 0:
            if self.t % 15:
                walk.play(0, 60)
        else:
            walk.stop()

        self.t += 1
        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0)
        self.rect.y += self.yvel
        self.collide(0, self.yvel)
        self.die()


class Goplit(Warior):
    def __init__(self, pos_x, pos_y):
        super().__init__(npc_group, all_sprites, alife_group)
        self.sheet = npc_image['goplit']
        self.frames = []
        self.cut_sheet(self.sheet)
        self.cur_frame = 0
        self.maxframe = 9
        self.r = 1
        self.image = self.frames[10][0]
        self.rect = self.image.get_rect().move(pos_x * 50 + totx, pos_y * 50 + toty)
        self.xvel = 0
        self.yvel = 0
        self.t = 0
        self.bit = False
        self.onGround = False
        self.max = self.heart = 2800
        Healf(self)

    def update(self):
        if self.heart < self.max and self.t % 4 == 0:
            self.heart += 2

        if player.rect.x - self.rect.x > -500 and player.rect.x - self.rect.x < -50:
            if self.r == 1:
                self.cur_frame = 0
                self.maxframe = 9
            self.r = 0
            self.xvel = -4

        if player.rect.x - self.rect.x < 500 and player.rect.x - self.rect.x > 50:
            if self.r == 0:
                self.cur_frame = 0
                self.maxframe = 9
            self.r = 1
            self.xvel = 4

        if player.rect.x - self.rect.x < 45 and player.rect.x - self.rect.x > -45:
            self.xvel = 0
            self.maxframe = 6
            self.bit = True
        else:
            self.bit = False

        if player.rect.x - self.rect.x > 500 or player.rect.x - self.rect.x < -500:
            self.xvel = 0

        if up:
            if self.onGround:
                self.maxframe = 7
                self.yvel = -9

        if not self.onGround:
            self.yvel += 0.25

        if self.t % 3 == 0:
            self.cur_frame = (self.cur_frame + 1) % 7
            if self.bit:
                if self.r:
                    self.image = self.frames[7][self.cur_frame]
                else:
                    self.image = self.frames[5][self.cur_frame]
                if pygame.sprite.collide_rect(self, player):
                    player.heart -= 10
                    stook.play()

            elif up:
                if self.r:
                    self.image = self.frames[3][self.cur_frame]
                else:
                    self.image = self.frames[1][self.cur_frame]

            elif self.xvel == 4:
                self.image = self.frames[11][self.cur_frame]

            elif self.xvel == -4:
                self.image = self.frames[9][self.cur_frame]

            else:
                self.image = self.frames[10][0]

        if self.xvel and (self.yvel < 2 or self.yvel > -2):
            if self.t % 15:
                walk.play(0, 60)
        else:
            walk.stop()

        self.t += 1
        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0)
        self.rect.y += self.yvel
        self.collide(0, self.yvel)
        self.die()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * height for _ in range(width)]

        self.left = 0
        self.top = 0
        self.cell_size = tile_width

    def set_view(self, left, top):
        self.left += left
        self.top += top

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mpos):
        x, y = mpos
        if x in range(self.left, self.left + self.width * self.cell_size) and \
                y in range(self.top, self.top + self.height * self.cell_size):
            x1 = (x - self.left) // self.cell_size
            y1 = (y - self.top) // self.cell_size
            return x1, y1
        else:
            return None

    def on_click(self, cell):
        if cell:
            x, y = cell
            if self.board[x][y] and click1:
                player.bag.append(self.board[x][y])
                pick.play()
                self.board[x][y].kill()
                self.board[x][y] = 0

            if self.board[x][y] == 0 and click2:
                self.board[x][y] = Tile('wood', x, y, '#')
                if pygame.sprite.spritecollideany(self.board[x][y], alife_group):
                    self.board[x][y].kill()
                    self.board[x][y] = 0
                else:
                    self.board[x][y].kill()
                    if player.bag:
                        block.play()
                        neu = player.bag.pop()
                        neu.new(x, y)
                        all_sprites.add(neu)
                        tiles_group.add(neu)
                        self.board[x][y] = neu
                    else:
                        self.board[x][y] = 0

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, (0, 0, 0),\
                                 (self.left + i * self.cell_size, self.top + j * self.cell_size,\
                                  self.cell_size, self.cell_size), 1)


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def boardapply(self):
        board.set_view(self.dx, self.dy)

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('dirt', x, y, '.')
            elif level[y][x] == '#':
                Tile('wood', x, y, '#')
            elif level[y][x] == '@':
                 man = Player(x, y)
            elif level[y][x] == '5':
                Tile('lawa', x, y, '5')
            elif level[y][x] == '6':
                Tile('stone', x, y, '6')
            elif level[y][x] == 'g':
                Tile('gas', x, y, 'g')
            elif level[y][x] == '$':
                Assasin(x, y)
            elif level[y][x] == '&':
                Goplit(x, y)
    return man, x + 1, y + 1


def tiles():
    for tile in tiles_group:
        x, y = tile.x, tile.y
        board.board[x][y] = tile


pygame.init()
pygame.mixer.init()
left = right = up = click1 = click2 = False
totx = toty = 0
setka = -1
camera = Camera()
pygame.mouse.set_visible(False)

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
fonblock_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
lawagrup = pygame.sprite.Group()
npc_group = pygame.sprite.Group()
alife_group = pygame.sprite.Group()
hert_group = pygame.sprite.Group()
mose_group = pygame.sprite.Group()

width, height = 500, 500

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
clock2 = pygame.time.Clock()
muza2 = pygame.mixer.Sound(os.path.join('music', 'run.ogg'))
Mouse()

lvl = None
lvl = start_screen()

tile_images = {
    'wood': load_image('wood.png'),
    'dirt': load_image('dirt.png'),
    'lawa': load_image('lawa.jpg'),
    'gas': load_image('gas.jpg'),
    #'water': load_image('water.png'),
    'stone': load_image('stone.jpg')
    }

npc_image = {
    'goplit': load_pers('goplit1.png', 'gym'),
    'elf': load_pers('elf4.png', 'gym')
}

tile_width = tile_height = 50

player, x1, y1 = generate_level(load_level(lvl))

board = Board(x1, y1)
tiles()
width, height = 800, 640
fon = pygame.transform.scale(load_image('back2.jpg'), (width, height))
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font(None, 30)
running = True

muza = pygame.mixer.Sound(os.path.join('music', 'day.ogg'))
walk = pygame.mixer.Sound(os.path.join('music', 'walk.ogg'))
jump = pygame.mixer.Sound(os.path.join('music', 'jump.ogg'))
pick = pygame.mixer.Sound(os.path.join('music', 'pick.ogg'))
stook = pygame.mixer.Sound(os.path.join('music', 'stook.ogg'))
block = pygame.mixer.Sound(os.path.join('music', 'block.ogg'))

muza.play(-1)
muza.set_volume(0.2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == pygame.KEYDOWN:
            f = pygame.key.get_pressed()
            if f[pygame.K_w]:
                up = True
            if f[pygame.K_a]:
                left = True
            if f[pygame.K_d]:
                right = True
            if f[pygame.K_q]:
                terminate()
            if f[pygame.K_LSHIFT]:
                setka *= -1
            if f[pygame.K_p]:
                muza.stop()
                left = right = up = click1 = click2 = False
                pause()
                muza.play(-1)
            if f[pygame.K_h]:
                player.heart = 2000


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up = False
            elif event.key == pygame.K_a:
                left = False
            elif event.key == pygame.K_d:
                right = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click1 = True
                board.get_click(event.pos)
            elif event.button == 3:
                click2 = True
                board.get_click(event.pos)

        if event.type == pygame.MOUSEMOTION:
            if click1 or click2:
                board.get_click(event.pos)

        if event.type == pygame.MOUSEBUTTONUP:
            click1 = False
            click2 = False

    screen.blit(fon, (0, 0))
    tiles_group.draw(screen)
    npc_group.draw(screen)
    player_group.draw(screen)
    camera.boardapply()
    hert_group.draw(screen)
    mose_group.draw(screen)
    if setka > 0:
        board.render()

    camera.update(player)
    totx += camera.dx
    toty += camera.dy
    npc_group.update()
    player.update()
    hert_group.update()
    mose_group.update()
    for sprite in all_sprites:
        camera.apply(sprite)
    c = 'fps  ' + str(round(clock.get_fps()))
    screen.blit(font.render(c, 1, (0, 0, 0)), (0, 0))
    m = '{}/{} HP'.format(player.heart, player.max)
    screen.blit(font.render(m, 1, (255, 155, 155)), (width - 200, height - 50))
    clock.tick(FPS)
    pygame.display.flip()
