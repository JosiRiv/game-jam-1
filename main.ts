/**
 * Set Up Sprites And Positions
 */
// Set Up The Player Projectile
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    playerprojectile.setPosition(my_sprite.x, my_sprite.y)
    playerprojectile.setVelocity(100, 0)
})
// Set Up Collision
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
	
})
let playerprojectile: Sprite = null
let my_sprite: Sprite = null
scene.setBackgroundImage(img`
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
controller.moveSprite(my_sprite)
let rocket = sprites.create(img`
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
    `, SpriteKind.Enemy)
rocket.setPosition(146, 56)
playerprojectile = sprites.create(img`
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
    `, SpriteKind.Projectile)
let enemyprojectile = sprites.create(img`
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
    `, SpriteKind.Projectile)
