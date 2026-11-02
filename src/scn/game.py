import skittle
from pyglm import glm

from src import car

class GameScene(skittle.scene.Scene):
    def __init__(self, scene_manager: skittle.scene.SceneManager, ctx: skittle.Context) -> None:
        super().__init__(scene_manager, ctx)

        self.font = skittle.resource.sysfont(ctx, "comicsans", 48)


        self.player = car.Car()

    def draw(self, ctx: skittle.Context):
        self.font.render(ctx, "fuck comic sans", glm.vec2(100, 100), color=skittle.color.RED, overlay=True, center=True)



    def update(self, dt: float, ctx: skittle.Context):
       pass