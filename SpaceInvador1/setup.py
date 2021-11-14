import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name = 'Space Invaders',
    options={"build.exe":{"packages":["pygame"],
                          "include_files":["a415up.jpeg", "laser.png", "space-invaders.png", "space-invaders-enemy.png", "spaceship.png"]}},
executables = executables
)