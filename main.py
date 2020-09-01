# Set Up Overlaps

@namespace
class SpriteKind:
    playerprojectile = SpriteKind.create()
    wall = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    enemy1.set_position(153, randint(10, 105))
    enemyprojectile.set_position(enemy1.x, enemy1.y)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.wall, on_on_overlap)

def on_a_pressed():
    playerprojectile2.set_position(my_sprite.x, my_sprite.y)
    playerprojectile2.set_velocity(150, 0)
    playerprojectile2.set_flag(SpriteFlag.INVISIBLE, False)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap2(sprite, otherSprite):
    pause(300)
    info.set_score(info.score() + 1)
    if info.score() == 10:
        game.splash("Level 2!")
        enemy2.set_position(153, randint(10, 105))
        enemy2.set_flag(SpriteFlag.INVISIBLE, False)
    if info.score() == 20:
        game.over(True)
sprites.on_overlap(SpriteKind.playerprojectile,
    SpriteKind.enemy,
    on_on_overlap2)

def on_on_overlap3(sprite, otherSprite):
    game.over(False)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap3)

def on_on_overlap4(sprite, otherSprite):
    enemy2.set_position(153, randint(10, 105))
sprites.on_overlap(SpriteKind.enemy, SpriteKind.enemy, on_on_overlap4)

# Set Up The Sprites And Score

enemy2: Sprite = None
enemyprojectile: Sprite = None
playerprojectile2: Sprite = None
enemy1: Sprite = None
my_sprite: Sprite = None
scene.set_background_image(img("""
    f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
        c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f f f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 f f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
        c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f f f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 f f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 
        c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f f 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 f f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c 
        c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c f 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 f f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c 
        c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c f 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 f c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c 
        c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c f 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 f c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c 
        c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c f 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 f c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c 
        c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c f 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 f c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c 
        c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c f 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 f c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c 
        c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c f 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 f c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c 
        c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c f 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 f c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c 
        c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c f 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 f c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c 
        c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c f 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 f c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c 
        c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c f 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 f c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c 
        c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c f 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 f c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c 
        c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c f 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c 
        c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c f 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c 
        c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c 
        c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c 
        c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c 
        c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c 
        c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c 
        c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c 
        c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c 
        c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c 
        c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c 
        c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c 
        c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c 
        c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c 
        c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c 
        c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c 
        c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c 
        c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c 
        c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c 
        c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c 
        c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c 
        c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c 
        c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c 
        c c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c f 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c f 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c f 2 2 2 2 2 2 2 f c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c f 2 2 2 2 2 2 f c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c f 2 2 2 2 2 2 f c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c f 2 2 2 2 2 2 f c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c f 2 2 2 2 2 f c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c f 2 2 2 2 2 2 2 f c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c f 2 2 2 2 f c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c f 2 2 2 2 2 f c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c f 2 2 2 2 f c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c f 2 2 2 2 2 f c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c f 2 2 2 f c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c f 2 2 2 2 2 f c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c f 2 2 2 f c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c c f 2 2 2 f c c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c f 2 2 f c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c c f 2 2 2 f c c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c f 2 2 f c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c c c f 2 f c c c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c c f 2 f c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c c c f 2 f c c c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 4 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c c f f c c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c c c f 2 f c c c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c c f f c c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c c c c f c c c c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c c f f c c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c c c c f c c c c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c c c f c c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c c c f 4 f c c c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c c f f c c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c c c f 4 f c c c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c c f f c c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c c c f 4 f c c c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c c f 4 f c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c c f 4 4 4 f c c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c c f 4 f c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c c f 4 4 4 f c c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c f 4 4 f c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c f 4 4 4 4 4 f c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c f 4 4 f c c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c f 4 4 4 4 4 f c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c c f 4 4 4 f c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c c f 4 4 4 4 4 f c c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c f 4 4 4 4 f c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c f 4 4 4 4 f c c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c f 4 4 4 4 4 f c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c c f 4 4 4 4 4 f c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c f 4 4 4 4 4 4 f c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c f 4 4 4 4 4 4 f c c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c c f 4 4 4 4 4 4 4 f c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c f 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c f 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c f 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c 
        c c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c 
        c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c 
        c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c 
        c c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c 
        c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c 
        c c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c 
        c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c 
        c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c 
        c c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c 
        c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c 
        c c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c 
        c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c 
        c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c 
        c c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c 
        c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c 
        c c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c 
        c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c 
        c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c 
        c c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c 
        c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c 
        c c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c c f 6 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 6 f c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c 
        c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c f 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 f c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c 
        c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c f 6 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 6 f c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c 
        c c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c c f 6 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 f c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c 
        c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c f 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 6 f c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c 
        c c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c c f 6 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 6 f c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c 
        c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c f 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 f c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c 
        c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c f 6 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 6 f c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c 
        c c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c c f 6 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 6 f c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c 
        c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c f 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 f c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c 
        c c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c f 6 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 6 f c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c c 
        c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c f 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 6 f c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c 
        c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c f 6 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 f c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c 
        c c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c f 6 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 6 f c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c c 
        c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c f 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 6 f c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c 
        c c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c f 6 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 f f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c 
        c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f f 6 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 6 f f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c 
        c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f f f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f 6 f f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f c 
        c f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f f f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f f f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 
        f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
"""))
my_sprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 9 9 f f f . . . . 
            . . . f f f 9 9 9 9 f f f . . . 
            . . f f f 9 9 9 9 9 9 f f f . . 
            . . f f 9 9 9 9 9 9 9 9 9 f . . 
            . . f 9 9 f 9 9 9 f 9 9 9 f . . 
            . . f 9 9 f 9 9 9 f 9 9 9 f . . 
            . f f 9 9 9 9 9 9 9 9 9 9 f f . 
            . f 9 9 9 f f f f f 9 9 9 9 f . 
            . f 9 9 9 9 9 9 9 9 9 9 9 9 f . 
            . f 9 9 9 9 9 9 9 9 9 9 9 9 f . 
            . f 9 9 9 9 9 9 9 9 9 9 9 9 f . 
            . f 9 9 9 9 9 9 9 9 9 9 9 9 f . 
            . f 8 8 9 9 8 8 8 9 9 8 8 9 f . 
            f f 8 8 8 9 8 8 8 8 9 8 8 8 f f 
            f 8 8 8 8 8 8 8 8 8 8 8 8 8 8 f
    """),
    SpriteKind.player)
my_sprite.set_position(9, 67)
game.splash("Reach a score of 10 to advance!")
controller.move_sprite(my_sprite)
enemy1 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . f f f f f f f 
            . . . . . . . . . . f 2 2 f 4 4 
            . . . . . . . . . f f f f f 4 4 
            . . . . . . f f f f b b b f 4 4 
            . . . . . . f b b b b b b f 4 4 
            . . . . . . f f f f b b b f 4 4 
            . . . . . . . . . f f f f f 4 4 
            . . . . . . . . . . . . . f 4 4 
            . . . . . . . . . . . . . f f f 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
enemy1.set_position(153, randint(10, 105))
playerprojectile2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . f f . . . . . . . . . . . . 
            . f 9 9 f f f . . . . . . . . . 
            f 9 f 9 9 9 9 f . f . . . . . . 
            f 9 9 f f f 9 9 f 9 f . . . . . 
            . f 9 9 9 9 9 9 9 9 9 f . . . . 
            . f 9 9 9 9 9 9 9 9 9 f . . . . 
            . . f f f f 9 9 9 9 9 f . . . . 
            . . . . . f 9 9 9 9 f . . . . . 
            . . . f f 9 9 9 f f . . . . . . 
            . . f 9 9 9 f f . . . . . . . . 
            . . . f f f . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.playerprojectile)
enemyprojectile = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . f f f f . 4 . 4 . 
            . . f f f f f 9 7 7 f 4 . . . 4 
            . f 7 7 9 9 9 9 f f 4 4 . 4 . . 
            . f 7 7 9 9 9 9 f f 4 4 . . . 4 
            . . f f f f f 9 7 7 f 4 . 4 . . 
            . . . . . . . f f f f . 4 . . 4 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.projectile)
playerprojectile2.set_flag(SpriteFlag.INVISIBLE, True)
enemyprojectile.set_position(enemy1.x, enemy1.y)
wall2 = sprites.create(img("""
        f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . . 
            f . . . . . . . . . . . . . . .
    """),
    SpriteKind.wall)
wall2.set_position(0, 113)
enemyprojectile.set_velocity(-80, 0)
enemy2 = sprites.create(img("""
        . . . . . . . . . . . . . . f f 
            . . . . . . . . . . . . . f f 2 
            . . . . . . . . . . . . f f 2 2 
            . . . . . . . . . . . f f 2 2 2 
            . . . . . . . . f f f f 2 2 2 2 
            . . . . . . . f 7 f f 9 2 5 5 2 
            . . . . . . f 7 7 7 f 9 2 5 5 2 
            . . . . f f f f f f f 9 2 5 5 2 
            . . . . f f f f f f f 9 2 5 5 2 
            . . . . . . f 7 7 7 f 9 2 5 5 2 
            . . . . . . . f 7 f f 9 2 5 5 2 
            . . . . . . . . f f f f 2 2 2 2 
            . . . . . . . . . . . f f 2 2 2 
            . . . . . . . . . . . . f f 2 2 
            . . . . . . . . . . . . . f f 2 
            . . . . . . . . . . . . . . f f
    """),
    SpriteKind.enemy)
enemy2.set_flag(SpriteFlag.INVISIBLE, True)
enemy2.set_position(0, 0)
enemyprojectile2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
info.set_score(0)