import tcod

from entity import Entity
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    
    #screen resolution
    screen_width = 80
    screen_height = 50

    #tileset
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 0, 0))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "N", (255, 255, 0))
    entities = {npc, player}
 
    #creating terminal
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        

        #game loop
        while True:
            root_console.print(x=player.x, y=player.y, string=player.char, fg=player.color)
            root_console.print(x=npc.x, y=npc.y, string=npc.char, fg=npc.color)

            #updates the screen to actually show the player
            context.present(root_console)

            #removes the last instance of whare the entity was to not leave a trail
            root_console.clear()

            
            #input detection
            for event in tcod.event.wait():
                
                action = event_handler.dispatch(event)
                
                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player.move(dx=action.dx, dy=action.dy)

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()