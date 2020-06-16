from stellarlib.scene_node import SceneNode
from src.animations.arc_animation import ArcAnimation
from src.settings import PIXEL_SCALE
from .components.arrow_component import ArrowComponent
from .components.javelin_component import JavelinComponent


class ProjectileNode(SceneNode):

    ARROW_SPEED = PIXEL_SCALE * 2.0
    JAVELIN_SPEED = PIXEL_SCALE * 1.6

    @classmethod
    def arrow(cls, actor, target_pos, on_hit):
        node = cls(actor, target_pos, cls.ARROW_SPEED, on_hit)
        node.add_component(ArrowComponent(node))

    @classmethod
    def javelin(cls, actor, target_pos, on_hit):
        node = cls(actor, target_pos, cls.JAVELIN_SPEED, on_hit)
        node.add_component(JavelinComponent(node))

    def __init__(self, actor, target_pos, speed, on_hit):

        origin = actor._get_screen_pos()

        SceneNode.__init__(self, actor.game.game_objects, origin)
        ArcAnimation(actor, self, target_pos, self.get_peak(origin, target_pos), speed, self.get_hit_func(on_hit))

    def get_hit_func(self, on_hit):

        def resolve():
            on_hit()
            self.orphan()

        return resolve

    def get_peak(self, origin, dest):

        return PIXEL_SCALE * 5
