import skittle
from pyglm import glm

from src.scn import game

class TitleScene(skittle.scene.Scene):
    def __init__(self, scene_manager: skittle.scene.SceneManager, ctx: skittle.Context) -> None:
        super().__init__(scene_manager, ctx)

    def draw(self, ctx: skittle.Context):
        ctx.clear(1,0,1)

    def update(self, dt: float, ctx: skittle.Context):
        skittle.log("SKIPPING TITLE SCENE COS I HAVENT DONE IT YET")
        self.switch_scene(game.GameScene)