import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    
    #screen resolution
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    #tileset
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    #creating terminal
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        
        while True:
            root_console.print(x=player_x, y=player_y, string="@")

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
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()