import tcod

from entity import Entity
from engine import Engine
from game_map import GameMap
from game_map import GameMap
from input_handlers import EventHandler
from procgen import generate_dungeon


def main() -> None:
    
    #screen resolution
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45


    #tileset
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    #define entities
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 0, 0))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "N", (255, 255, 0))
    bottom_left_text = Entity(int(1), int(screen_height-3), "Arrow Keys to move", (255, 255, 255))
    entities = {npc, player, bottom_left_text}


    #import map
    game_map = generate_dungeon(map_width, map_height)


    #import engine
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)
 

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
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()