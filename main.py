
import pygame
import random
from settings import *
from sprites import *


# несколько видов людей: которые нападают только на игрока, которые иногда нападают на других людей, которые ни на кого не нападают

class Hero:
    hp = 100
    mana = 100
    width = 200
    height = 200
    X = 250 + width
    Y = 791 - height
    speed = 10
    bullets = []
    side = "RIGHT"
    action = "STAY"  # STAY, RUN, ATTACK1 - melee, ATTACK2 - range chaosball, blink (avoid enemies shots), blackhole (on a fickesed range),
    pict = {"STAYRIGHT": [pygame.image.load("pictures/DEATH/death_r1.png")],
            "STAYLEFT": [pygame.image.load("pictures/DEATH/death_l1.png")],
            "RUNRIGHT": [pygame.image.load("pictures/DEATH/death_r1.png"), pygame.image.load("pictures/DEATH/death_r2.png")],
            "RUNLEFT": [pygame.image.load("pictures/DEATH/death_l1.png"), pygame.image.load("pictures/DEATH/death_l2.png")],
            "ATTACK2RIGHT": [pygame.image.load("pictures/DEATH/death_attack1_r1.png"), pygame.image.load("pictures/DEATH/death_attack1_r2.png"), pygame.image.load("pictures/DEATH/death_attack1_r1.png")],
            "ATTACK2LEFT": [pygame.image.load("pictures/DEATH/death_attack1_l1.png"), pygame.image.load("pictures/DEATH/death_attack1_l2.png"), pygame.image.load("pictures/DEATH/death_attack1_l1.png")],
            "ATTACK1RIGHT": [pygame.image.load("pictures/DEATH/death_attack2_r1.png"), pygame.image.load("pictures/DEATH/death_attack2_r2.png"), pygame.image.load("pictures/DEATH/death_attack2_r3.png"), pygame.image.load("pictures/DEATH/death_attack2_r4.png"), pygame.image.load("pictures/DEATH/death_attack2_r5.png")],
            "ATTACK1LEFT": [pygame.image.load("pictures/DEATH/death_attack2_l1.png"), pygame.image.load("pictures/DEATH/death_attack2_l2.png"), pygame.image.load("pictures/DEATH/death_attack2_l3.png"), pygame.image.load("pictures/DEATH/death_attack2_l4.png"), pygame.image.load("pictures/DEATH/death_attack2_l5.png")],
            "ATTACK1INMOVERIGHT": [pygame.image.load("pictures/DEATH/death_attack2_r1.png"), pygame.image.load("pictures/DEATH/death_attack2_inmove_r2.png"), pygame.image.load("pictures/DEATH/death_attack2_r3.png"), pygame.image.load("pictures/DEATH/death_attack2_inmove_r4.png"), pygame.image.load("pictures/DEATH/death_attack2_r5.png"), pygame.image.load("pictures/DEATH/death_r2.png")],
            "ATTACK1INMOVELEFT": [pygame.image.load("pictures/DEATH/death_attack2_l1.png"), pygame.image.load("pictures/DEATH/death_attack2_inmove_l2.png"), pygame.image.load("pictures/DEATH/death_attack2_l3.png"), pygame.image.load("pictures/DEATH/death_attack2_inmove_l4.png"), pygame.image.load("pictures/DEATH/death_attack2_l5.png"), pygame.image.load("pictures/DEATH/death_l2.png")],
            "BLOCKRIGHT": [pygame.image.load("pictures/DEATH/death_block_r2.png")], "BLOCKLEFT": [pygame.image.load("pictures/DEATH/death_block_l2.png")],
            "ATTACK2INMOVERIGHT": [pygame.image.load("pictures/DEATH/death_attack1_r1.png"), pygame.image.load("pictures/DEATH/death_attack1_inmove_r2.png")],
            "ATTACK2INMOVELEFT": [pygame.image.load("pictures/DEATH/death_attack1_l1.png"), pygame.image.load("pictures/DEATH/death_attack1_inmove_l2.png")]}
    anim_count = 0

    def draw(self):
        if self.anim_count >= len(self.pict[self.action+self.side])-1:
            self.anim_count = 0
        else:
            self.anim_count += 1
        if self.action == "STAY":
            window.blit(self.pict[self.action+self.side][0], (self.X, self.Y))
        elif self.action == "BLOCK":
            window.blit(self.pict[self.action + self.side][0], (self.X, self.Y))
        else:
            window.blit(self.pict[self.action+self.side][self.anim_count], (self.X, self.Y))

    def attack1(self):
        global enemies
        self.mana -= 5
        for enemy in enemies:
            if (self.side == "RIGHT" and enemy.side == "LEFT" or self.side == "LEFT" and enemy.side == "RIGHT") and enemy.X + 56 <= self.X + self.width <= enemy.X + 96 or (self.side == "LEFT" and enemy.side == "LEFT" or self.side == "RIGHT" and enemy.side == "RIGHT") and enemy.X + 96 <= self.X + self.width <= enemy.X + 56:
                enemy.hp -= 10
                if enemy.hp <= 0:
                    enemies.pop(enemies.index(enemy))

    def block(self):
        global enemies
        for enemy in enemies:
            test = True
            if self.side == "RIGHT":
                for bullet in enemy.bullets:
                    if bullet.vel > 0:
                        test = False
            elif self.side == "LEFT":
                for bullet in enemy.bullets:
                    if bullet.vel < 0:
                        test = False
            if test:
                for enemy in enemies:
                    for bullet in enemy.bullets:
                        if bullet.X <= death.X + death.width - 22 and death.side == "RIGHT" or bullet.X <= death.X + 22 and death.side == "LEFT":
                            enemy.bullets.pop(enemy.bullets.index(bullet))


class Enemy:
    hp = 100
    mana = 100
    width = 200
    height = 200
    X = 700 + width
    Y = 791 - height
    speed = 10
    bullets = []
    side = "LEFT"
    action = "STAY"  # STAY, RUN, ATTACK1 - melee, ATTACK2 - range chaosball, blink (avoid enemies shots), blackhole (on a fickesed range),
    pict = {"STAYRIGHT": [pygame.image.load("pictures/DEATH/death_r1.png")],
            "STAYLEFT": [pygame.image.load("pictures/DEATH/death_l1.png")],
            "RUNRIGHT": [pygame.image.load("pictures/DEATH/death_r1.png"), pygame.image.load("pictures/DEATH/death_r2.png")],
            "RUNLEFT": [pygame.image.load("pictures/DEATH/death_l1.png"), pygame.image.load("pictures/DEATH/death_l2.png")],
            "ATTACK2RIGHT": [pygame.image.load("pictures/DEATH/death_attack1_r1.png"), pygame.image.load("pictures/DEATH/death_attack1_r2.png"), pygame.image.load("pictures/DEATH/death_attack1_r1.png")],
            "ATTACK2LEFT": [pygame.image.load("pictures/DEATH/death_attack1_l1.png"), pygame.image.load("pictures/DEATH/death_attack1_l2.png"), pygame.image.load("pictures/DEATH/death_attack1_l1.png")],
            "ATTACK1RIGHT": [pygame.image.load("pictures/DEATH/death_attack2_r1.png"), pygame.image.load("pictures/DEATH/death_attack2_r2.png"), pygame.image.load("pictures/DEATH/death_attack2_r3.png"), pygame.image.load("pictures/DEATH/death_attack2_r4.png"), pygame.image.load("pictures/DEATH/death_attack2_r5.png")],
            "ATTACK1LEFT": [pygame.image.load("pictures/DEATH/death_attack2_l1.png"), pygame.image.load("pictures/DEATH/death_attack2_l2.png"), pygame.image.load("pictures/DEATH/death_attack2_l3.png"), pygame.image.load("pictures/DEATH/death_attack2_l4.png"), pygame.image.load("pictures/DEATH/death_attack2_l5.png")],
            "ATTACK1INMOVERIGHT": [pygame.image.load("pictures/DEATH/death_attack2_r1.png"), pygame.image.load("pictures/DEATH/death_attack2_inmove_r2.png"), pygame.image.load("pictures/DEATH/death_attack2_r3.png"), pygame.image.load("pictures/DEATH/death_attack2_inmove_r4.png"), pygame.image.load("pictures/DEATH/death_attack2_r5.png"), pygame.image.load("pictures/DEATH/death_r2.png")],
            "ATTACK1INMOVELEFT": [pygame.image.load("pictures/DEATH/death_attack2_l1.png"), pygame.image.load("pictures/DEATH/death_attack2_inmove_l2.png"), pygame.image.load("pictures/DEATH/death_attack2_l3.png"), pygame.image.load("pictures/DEATH/death_attack2_inmove_l4.png"), pygame.image.load("pictures/DEATH/death_attack2_l5.png"), pygame.image.load("pictures/DEATH/death_l2.png")],
            "BLOCKRIGHT": [pygame.image.load("pictures/DEATH/death_block_r2.png")],
            "BLOCKLEFT": [pygame.image.load("pictures/DEATH/death_block_l2.png")],
            "ATTACK2INMOVERIGHT": [pygame.image.load("pictures/DEATH/death_attack1_r1.png"), pygame.image.load("pictures/DEATH/death_attack1_inmove_r2.png")],
            "ATTACK2INMOVELEFT": [pygame.image.load("pictures/DEATH/death_attack1_l1.png"), pygame.image.load("pictures/DEATH/death_attack1_inmove_l2.png")]}
    anim_count = 0

    def draw(self):
        if self.anim_count >= len(self.pict[self.action+self.side])-1:
            self.anim_count = 0
        else:
            self.anim_count += 1
        if self.action == "STAY":
            window.blit(self.pict[self.action+self.side][0], (self.X, self.Y))
        elif self.action == "BLOCK":
            window.blit(self.pict[self.action + self.side][0], (self.X, self.Y))
        else:
            window.blit(self.pict[self.action+self.side][self.anim_count], (self.X, self.Y))

    def attack1(self):
        global enemies
        self.mana -= 5
        for enemy in enemies:
            if (self.side == "RIGHT" and enemy.side == "LEFT" or self.side == "LEFT" and enemy.side == "RIGHT") and enemy.X + 56 <= self.X + self.width <= enemy.X + 96 or (self.side == "LEFT" and enemy.side == "LEFT" or self.side == "RIGHT" and enemy.side == "RIGHT") and enemy.X + 96 <= self.X + self.width <= enemy.X + 56:
                enemy.hp -= 10
                if enemy.hp <= 0:
                    enemies.pop(enemies.index(enemy))

    def block(self):
        global enemies
        for enemy in enemies:
            test = True
            if self.side == "RIGHT":
                for bullet in enemy.bullets:
                    if bullet.vel > 0:
                        test = False
            elif self.side == "LEFT":
                for bullet in enemy.bullets:
                    if bullet.vel < 0:
                        test = False
            if test:
                for enemy in enemies:
                    for bullet in enemy.bullets:
                        if bullet.X <= death.X + death.width - 22 and death.side == "RIGHT" or bullet.X <= death.X + 22 and death.side == "LEFT":
                            enemy.bullets.pop(enemy.bullets.index(bullet))


class Snaryad:

    def __init__(self, x, y, radius, color, facing, damage):
        self.X = x
        self.Y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 12 * facing
        self.damage = damage

    def draw(self):
        pygame.draw.circle(window, self.color, (self.X, self.Y), self.radius)


def draw_all():
    global bushes, flowers
    count_trees = move_forest
    window.fill((33, 81, 101))  # x с 192  по 1728,  y с 108 по 972
    pygame.draw.rect(window, (28, 52, 88), (192, 791, 1536, 181))
    window.blit(bg["moon"], (210, 130))
    for i in range(0, len(forest)):
        if str(type(forest[i])) != "<class 'int'>":
            if forest[i] == bg["blue"]["windmill_1"]:
                forest[i] = bg["blue"]["windmill_2"]
            elif forest[i] == bg["blue"]["windmill_2"]:
                forest[i] = bg["blue"]["windmill_1"]
            window.blit(forest[i], (count_trees, 791 - 500))
        else:
            count_trees += forest[i]
    death.draw()
    for bullet in death.bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
        for bullet in enemy.bullets:
            bullet.draw()
    for i in range(0, len(bushes)):
        if str(type(bushes[i])) != "<class 'int'>":
            window.blit(bg["green"][bushes[i]], (bushes[i+1] + move_forest, 791 - 100))
    for j in range(0, len(flowers)):
        if str(type(flowers[j])) != "<class 'int'>":
            window.blit(bg["purple"][flowers[j]], (flowers[j+1] + move_forest, 791 - 100))
    window.blit(hp_mana_line, (650, 922))
    if death.mana < 100:
        pygame.draw.rect(window, (33, 81, 101), (900, 932, 2.3*(100 - death.mana), 30))
    if death.hp < 100:
        pygame.draw.rect(window, (33, 81, 101), (890, 932, -2.3*(100 - death.hp), 30))
    pygame.display.update()


def forest_filling():
    counter = 0
    mas_trees = []
    mas_bushes = []
    mas_flowers = []
    for i in range(0, 5):
        rand_loc = random.choice(["blue", "brown", "purple", "green", "red"])
        a = 0
        for j in range(0, 15):
            if rand_loc == "blue" and a == 0:
                rand_tree = random.choice(["tree_1", "tree_2", "tree_3", "windmill_1"])
                if rand_tree == "windmill_1":
                    a += 1
            elif rand_loc == "brown" and a == 0:
                rand_tree = random.choice(["tree_1", "tree_2", "tree_3", "cross"])
                if rand_tree == "cross":
                    a += 1
            else:
                rand_tree = random.choice(["tree_1", "tree_2", "tree_3"])
            if rand_loc == "green":
                rand_bash = random.choice(["bush_1", "bush_2", "bush_3", "bush_4"])
                mas_bushes.append(rand_bash)
                mas_bushes.append(counter)
            elif rand_loc == "purple":
                rand_flower = random.choice(["flowers"])
                mas_flowers.append(rand_flower)
                mas_flowers.append(counter)
            x = random.randint(150, 300)
            mas_trees += [bg[rand_loc][rand_tree]] + [x]  # 200 - 400 чтобы деревья не касались
            counter += x
    return [mas_trees, mas_bushes, mas_flowers]


def bot():
    if len(enemies[0].bullets) < 1:
        enemies[0].action = "ATTACK2"
        if enemies[0].side == "RIGHT":
            facing = temp = 1  # temp - коэффициент для вылета снаряда именно из руки
        else:
            facing = -1
            temp = 0
        enemies[0].bullets.append(Snaryad(enemies[0].X + temp*enemies[0].width - 16*facing, enemies[0].Y + enemies[0].height//2 + 25, 8, (92, 15, 95), facing, 10))
    else:
        enemies[0].action = "STAY"


move_forest = 0
death = Hero()
enemies = [Enemy()]
bg = {"moon": pygame.image.load("pictures/Background/moon3.png"),
      "blue": {"tree_1": pygame.image.load("pictures/Background/tree_blue_1.png"), "tree_2": pygame.image.load("pictures/Background/tree_blue_2.png"), "tree_3": pygame.image.load("pictures/Background/tree_blue_3.png"), "windmill_1": pygame.image.load("pictures/Background/windmill_blue_1.png"), "windmill_2": pygame.image.load("pictures/Background/windmill_blue_2.png")},
      "brown": {"tree_1": pygame.image.load("pictures/Background/tree_brown_1.png"), "tree_2": pygame.image.load("pictures/Background/tree_brown_2.png"), "tree_3": pygame.image.load("pictures/Background/tree_blue_3.png"), "cross": pygame.image.load("pictures/Background/cross_brown.png")},
      "purple": {"tree_1":pygame.image.load("pictures/Background/tree_purple_1.png"), "tree_2": pygame.image.load("pictures/Background/tree_purple_2.png"), "tree_3": pygame.image.load("pictures/Background/tree_blue_3.png"), "flowers": pygame.image.load("pictures/Background/flowers_purple.png")},
      "green": {"tree_1": pygame.image.load("pictures/Background/tree_green_1.png"), "tree_2": pygame.image.load("pictures/Background/tree_green_2.png"), "tree_3": pygame.image.load("pictures/Background/tree_blue_3.png"), "bush_1": pygame.image.load("pictures/Background/bush_green_1.png"), "bush_2": pygame.image.load("pictures/Background/bush_green_2.png"), "bush_3": pygame.image.load("pictures/Background/bush_green_3.png"), "bush_4": pygame.image.load("pictures/Background/bush_green_4.png")},
      "red": {"tree_1": pygame.image.load("pictures/Background/tree_red_1.png"), "tree_2": pygame.image.load("pictures/Background/tree_red_2.png"), "tree_3": pygame.image.load("pictures/Background/tree_blue_3.png")}}
hp_mana_line = pygame.image.load("pictures/DEATH/hp_mana_line.png")
forest = forest_filling()[0]
bushes = forest_filling()[1]
flowers = forest_filling()[2]
pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Target of the death")
clock = pygame.time.Clock()

work = True

while work:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            work = False
            pygame.quit()
            quit
    for bullet in death.bullets:
            if 192 + bullet.radius < bullet.X < 1728 - bullet.radius:
                for enemy in enemies:
                    if (enemy.X + 56 <= bullet.X <= enemy.X + enemy.width - 96 and enemy.side == "LEFT") or (enemy.X + 96 <= bullet.X <= enemy.X + enemy.width - 56 and enemy.side == "RIGHT"):
                        enemy.hp -= bullet.damage
                        if enemy.hp <= 0:
                            enemies.pop(enemies.index(enemy))
                        death.bullets.pop(death.bullets.index(bullet))
                        break
                if bullet != None:
                    bullet.X += bullet.vel
            else:
                death.bullets.pop(death.bullets.index(bullet))
    for enemy in enemies:
        for bullet in enemy.bullets:
            if 192 + bullet.radius < bullet.X < 1728 - bullet.radius:
                if (death.X + 56 <= bullet.X <= death.X + death.width - 96 and death.side == "LEFT") or (death.X + 96 <= bullet.X <= death.X + death.width - 56 and death.side == "RIGHT"):
                    death.hp -= bullet.damage
                    if death.hp <= 0:
                        del death
                    enemy.bullets.pop(enemy.bullets.index(bullet))
                    break
                if bullet != None:
                    bullet.X += bullet.vel
            #else:
                #enemy.bullets.pop(death.bullets.index(bullet))
    bot()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and 1728 > death.X + death.width:
        death.side = "RIGHT"
        if keys[pygame.K_q]:
            if death.mana >= 5:
                death.action = "ATTACK1INMOVE"
                death.attack1()
            else:
                death.action = "RUN"
        elif keys[pygame.K_w]:
            if death.mana >= 10:
                if len(death.bullets) < 1:
                    death.mana -= 10
                    death.action = "ATTACK2INMOVE"
                    death.bullets.append(Snaryad(death.X + death.width - 16, death.Y + death.height // 2 + 39, 8, (92, 15, 95), 1, 10))
                else:
                    death.action = "RUN"
            else:
                death.action = "RUN"
        else:
            death.action = "RUN"
        move_forest -= death.speed
        for enemy in enemies:
            enemy.X -= death.speed
            for bullet in enemy.bullets:
                bullet.X -= death.speed
    elif keys[pygame.K_LEFT] and death.X > 192:
        death.side = "LEFT"
        if keys[pygame.K_q]:
            if death.mana >= 5:
                death.action = "ATTACK1INMOVE"
                death.attack1()
            else:
                death.action = "RUN"
        elif keys[pygame.K_w]:
            if death.mana >= 10:
                if len(death.bullets) < 1:
                    death.mana -= 10
                    death.action = "ATTACK2INMOVE"
                    death.bullets.append(Snaryad(death.X + 16, death.Y + death.height // 2 + 39, 8, (92, 15, 95), -1, 10))
                else:
                    death.action = "RUN"
            else:
                death.action = "RUN"
        else:
            death.action = "RUN"
        move_forest += death.speed
        for enemy in enemies:
            enemy.X += death.speed
            for bullet in enemy.bullets:
                bullet.X += death.speed
    elif keys[pygame.K_q]:
        if death.mana >= 5:
            death.action = "ATTACK1"
            death.attack1()
        else:
            death.action = "STAY"
    elif keys[pygame.K_w]:
        if death.mana >= 10:
            if len(death.bullets) < 1:
                death.mana -= 10
                death.action = "ATTACK2"
                if death.side == "RIGHT":
                    facing = temp = 1  # temp - коэффициент для вылета снаряда именно из руки
                else:
                    facing = -1
                    temp = 0
                death.bullets.append(Snaryad(death.X + temp*death.width - 16*facing, death.Y + death.height//2 + 25, 8, (92, 15, 95), facing, 10))
            else:
                death.action = "STAY"
        else:
            death.action = "STAY"
    elif keys[pygame.K_e]:
        if death.mana >= 1:
            death.mana -= 1
            death.action = "BLOCK"
            death.block()
        else:
            death. action = "STAY"
    elif keys[pygame.K_ESCAPE]:
        work = False
        pygame.quit()
        quit
    else:
        death.action = "STAY"
    draw_all()