import stellarlib
from src.game import Game
from src.settings import *


if __name__ == '__main__':

    scene_registry = stellarlib.SceneRegistry(
                                    'main',
                                    {
                                        'main': Game,
                                    }
                                )

    app = stellarlib.build_app(# main_scene=Game,
                                scene_registry = scene_registry,
                                SCREEN_W=SCREEN_W,
                                SCREEN_H=SCREEN_H)
    app.main()
