import skittle

class GameScene(skittle.scene.Scene):
    def __init__(self, scene_manager: skittle.scene.SceneManager, ctx: skittle.Context) -> None:
        super().__init__(scene_manager, ctx)

    def draw(self, ctx: skittle.Context):
        return super().draw(ctx)

    def update(self, dt: float, ctx: skittle.Context):
        return super().update(dt, ctx)