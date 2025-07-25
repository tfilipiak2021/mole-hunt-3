scene.setBackgroundImage(assets.image`
    grid
    `)
let myMole = sprites.create(img`
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . e e e e e e e e e e e e . .
        . e e e e e e e e e e e e e e .
        e e e e e e f e e f e e e e e e
        e e e e e e f e e f e e e e e e
        e e e e e e e e e e e e e e e e
        e e e e f e e e e e e f e e e e
        e e e e e f 3 3 3 3 f e e e e e
        e e e e e e f 3 3 f e e e e e e
        e e e e e f e e e e f e e e e e
        e e e e e e e e e e e e e e e e
        e e e f e e e e e e e e f e e e
        e e e e f f f f f f f f e e e e
        e e e e e e e e e e e e e e e e
        e e e e e e e e e e e e e e e e
        `, SpriteKind.Enemy)
game.onUpdateInterval(1000, function on_update_interval() {
    simplified.moveToRandomHoleOnGrid(myMole)
})
