# Set Up The Controls, Collision, And Wall

@namespace
class SpriteKind:
    playerprojectile = SpriteKind.create()
    wall = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    rocket.set_position(153, randint(10, 105))
    enemyprojectile.set_position(rocket.x, rocket.y)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.wall, on_on_overlap)

def on_a_pressed():
    playerprojectile2.set_position(my_sprite.x, my_sprite.y)
    playerprojectile2.set_velocity(100, 0)
    playerprojectile2.set_flag(SpriteFlag.INVISIBLE, False)
    playerprojectile2.set_flag(SpriteFlag.INVISIBLE, False)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap2(sprite, otherSprite):
    pause(300)
    info.set_score(info.score() + 1)
    if info.score() == 10:
        game.over(True)
sprites.on_overlap(SpriteKind.playerprojectile,
    SpriteKind.enemy,
    on_on_overlap2)

def on_on_overlap3(sprite, otherSprite):
    game.over(False)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap3)

# Set Up The Sprites And Score

enemyprojectile: Sprite = None
playerprojectile2: Sprite = None
rocket: Sprite = None
my_sprite: Sprite = None
scene.set_background_image(img("""
    b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c f f f f f f f f f f f f f f f c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b f f f f f f f b b b b b b b b b b b b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f f f f f f f f f f f f f f f f f c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b f b b b b b b b b b b b f 5 5 5 f f f f f f f f b b b b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f a a a a a f f f f f f a a a a a a a a a a a a a a a a a a a f f f f f a a a a a a a a a 
            b b b b b b f f f f f f f f f f f f f f b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f f f f f f 5 5 5 5 5 5 f a a a a a a a a a a a a f f f f f f 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b c c c c c c c c f f f f f f f f f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b c c c c c c c c c c c c c c c c c f f f f f f f f f f f f f f f 5 5 5 5 5 5 5 f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c f f f f f f f f c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c f c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b f 5 5 5 5 5 5 5 f f f f f f f b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b b f f f f f f f b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b f 5 5 5 5 5 5 f f f f f b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b f f f f f f b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b f f f f f f f b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b f f f f f f f f f f 5 5 5 5 5 f b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a 
            b b b b b b b b b b b b b f f f f f f f f f f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a 
            b b b b b b b f f f f f f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c f f f f f f f f f f f f f f f c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f f f f f f f f f f f f f f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f f f a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 f f f f a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 f f f a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 f f f f f a a a a a a a a a a a a a a a a a a f 5 5 5 5 f f f f f f f a a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a f f f f a a a a a a a a a a a a a a a a a a a a a a a a f f f f a a a a a a a a a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f f f a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a f f f f f 5 5 f a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a f f f f f f f f f a a a a a a a a a a a f f f f f 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a f f f f f f 5 5 5 5 5 5 5 5 5 f a a a a a a a f f f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f f f f f f f b b b b b b b b c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b f f 5 5 5 5 5 5 5 5 f f f f f f f f f f f f f f b b b b b b b b b b b b b b b c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b f f f f f f f f f f f b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f f f c f c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f f f f c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7 f f f f f c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 f f f f c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c f 5 5 5 5 5 5 f f f f f c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c f 5 5 f f f f c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c f f f c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b f b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b f f f f f f f b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f f f f f f f f f b b b b b b b b b b f f f f f 5 5 5 5 5 5 f b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c f f f f f f f f f f c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c f f f f f f f f f f f f f 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a a f f f f f f f f f f f f f f f a a a a a a f 5 5 5 5 5 5 5 5 5 5 5 5 f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a a a f a a a a a a a a a a a a a a a a a a a a f f f f f f f f f f f f f a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b c c c c c c c c c c c c c c c c c c c c c f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b c c c c c c c c c c c c c c c c c c c c c f f f f f f f f f f f 5 5 5 5 5 5 5 5 5 5 f c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b f 5 5 5 5 5 5 5 f b b b b b b b b b f 5 5 5 5 5 5 5 5 5 5 5 5 5 f b b b b b b b c c c c c c c c c c c c c c c c c c c c f c c c c c c c c c c c f f f f f f f f f f f c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b f f f f f f f f f f b b b b b b b b f 5 5 5 5 5 5 5 f f f f f f f f b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b f f f f f f f f f b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
            b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
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
game.splash("Reach a score of 10 to win!")
controller.move_sprite(my_sprite)
rocket = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . f f f f f 
                    . . . . f f f f f f f f 5 5 7 7 
                    . . . f 4 4 4 4 4 a a a a 5 5 7 
                    . . f 4 4 f 4 4 a a a a a a 5 5 
                    . . . f 4 4 4 4 4 a a a a 5 5 7 
                    . . . . f f f f f f f f 5 5 7 7 
                    . . . . . . . . . . . f f f f f 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
rocket.set_position(146, 56)
playerprojectile2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 4 4 4 4 4 . . . . . . . 
                    . . . 4 3 3 3 3 3 4 . . . . . . 
                    . . 4 3 3 8 8 8 3 3 4 . . . . . 
                    . 4 8 7 8 8 8 8 f 7 7 4 . 2 2 2 
                    . 4 7 7 8 8 8 8 8 7 4 2 2 2 2 2 
                    . 4 7 7 8 8 8 8 8 7 4 2 2 2 2 2 
                    . 4 8 7 8 8 8 8 8 7 7 4 . 2 2 2 
                    . . 4 3 3 8 8 8 3 3 4 . . . . . 
                    . . . 4 3 3 3 3 3 4 . . . . . . 
                    . . . . 4 4 4 4 4 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
    """),
    SpriteKind.playerprojectile)
enemyprojectile = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . 4 4 
                    . . . . e e e e e e e . . 4 4 2 
                    . . . e e 3 3 6 3 3 e e 4 4 2 2 
                    . . e e 3 3 3 6 3 3 3 e 4 2 2 2 
                    . . e 7 7 7 7 6 7 7 7 e 4 2 2 2 
                    . . e e 3 3 3 6 3 3 3 e 4 2 2 2 
                    . . . e e 3 3 6 3 3 e e 4 4 2 2 
                    . . . . e e e e e e e . . 4 4 2 
                    . . . . . . . . . . . . . . 4 4 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
    """),
    SpriteKind.projectile)
playerprojectile2.set_flag(SpriteFlag.INVISIBLE, True)
enemyprojectile.set_position(rocket.x, rocket.y)
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
    """),
    SpriteKind.wall)
wall2.set_position(0, 113)
enemyprojectile.set_velocity(-80, 0)
info.set_score(0)