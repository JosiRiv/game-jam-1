namespace SpriteKind {
    export const playerprojectile = SpriteKind.create()
    export const wall = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.wall, function (sprite, otherSprite) {
    enemy1.setPosition(153, randint(10, 105))
    enemyprojectile.setPosition(enemy1.x, enemy1.y)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    playerprojectile2.setPosition(my_sprite.x, my_sprite.y)
    playerprojectile2.setVelocity(150, 0)
    playerprojectile2.setFlag(SpriteFlag.Invisible, false)
})
sprites.onOverlap(SpriteKind.playerprojectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    pause(300)
    info.setScore(info.score() + 1)
    if (info.score() == 10) {
        game.splash("Level 2!")
        enemy2.setPosition(153, randint(10, 105))
        enemy2.setFlag(SpriteFlag.Invisible, false)
    }
    if (info.score() == 20) {
        game.over(true)
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Player, function (sprite, otherSprite) {
    game.over(false)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Enemy, function (sprite, otherSprite) {
    enemy2.setPosition(153, randint(10, 105))
})
/**
 * Set Up The Sprites And Score
 */
let enemy2: Sprite = null
let enemyprojectile: Sprite = null
let playerprojectile2: Sprite = null
let enemy1: Sprite = null
let my_sprite: Sprite = null
scene.setBackgroundImage(img`
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
    `)
my_sprite = sprites.create(img`
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
    `, SpriteKind.Player)
my_sprite.setPosition(9, 67)
game.splash("Reach a score of 10 to advance!")
controller.moveSprite(my_sprite)
enemy1 = sprites.create(img`
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
    `, SpriteKind.Enemy)
enemy1.setPosition(153, randint(10, 105))
playerprojectile2 = sprites.create(img`
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
    `, SpriteKind.playerprojectile)
enemyprojectile = sprites.create(img`
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
    `, SpriteKind.Projectile)
playerprojectile2.setFlag(SpriteFlag.Invisible, true)
enemyprojectile.setPosition(enemy1.x, enemy1.y)
let wall2 = sprites.create(img`
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    f . . . . . . . . . . . . . . . 
    `, SpriteKind.wall)
wall2.setPosition(0, 113)
enemyprojectile.setVelocity(-80, 0)
enemy2 = sprites.create(img`
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
    `, SpriteKind.Enemy)
enemy2.setFlag(SpriteFlag.Invisible, true)
enemy2.setPosition(0, 0)
let enemyprojectile2 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . f f . . . . 
    . . . . . . . . . . f f . . . . 
    . . . . . . . . f f f f f f . . 
    . . . . . . . f 7 7 7 f 5 f f . 
    . . . . . . f 7 7 7 7 f 5 5 f f 
    . . . . . . . f 7 7 7 f 5 f f . 
    . . . . . . . . f f f f f f . . 
    . . . . . . . . . . f f . . . . 
    . . . . . . . . . . f f . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
info.setScore(0)
info.setLife(3)
