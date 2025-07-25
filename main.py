scene.set_background_image(assets.image("""
    grid
    """))
myMole = sprites.create(img("""
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
        """),
    SpriteKind.enemy)

def on_update_interval():
    simplified.move_to_random_hole_on_grid(myMole)
game.on_update_interval(1000, on_update_interval)
