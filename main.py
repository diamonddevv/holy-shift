import skittle

from src.scn import title

if __name__ == "__main__":
    skittle.init()

    window = skittle.window.Window(
        title.TitleScene,
        title="HOLY SHIFT",
        width=1000,
        height=1000,
        fps_in_title=True
    )
    
    window.run()