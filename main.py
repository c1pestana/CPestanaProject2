#CAITLIN PESTANA
#Y AXIS NOT YET LABELLED
#PROGRAM RUNS AS NORMAL


import random

import arcade

def main():
    arcade.open_window(700, 700, "drawing horizontal rectangles")

    our_colors = [arcade.color.EGYPTIAN_BLUE, arcade.color.ELECTRIC_PURPLE, arcade.color.PSYCHEDELIC_PURPLE,
                  arcade.color.MAGENTA, arcade.color.PURPLE_HEART,
                  arcade.color.BLACK, arcade.color.BRIGHT_TURQUOISE]


    arcade.set_background_color(arcade.color.WHITE)
    data_file = open('data.txt', 'r')
    all_lines = data_file.readlines()

    arcade.start_render()

    arcade.draw_text(all_lines[0], 250, 650, arcade.color.DARK_MAGENTA, 20)
    arcade.draw_text(all_lines[1], 265, 100, arcade.color.BLACK, 15)
#WRITE SPECIFIC LINES BY SLICING
    rest_of_the_lines = all_lines[3:]
    x_loc = 350
    y_loc = 600
#"line" can be called anything
    for line in rest_of_the_lines:
#write everything AFTER COLON ONLY
        split_line = line.split (':')
#make sure number is an integer and not a string
#the size of the rectangle will be based on the integer- "size"
        size = int(split_line[1])
        this_color = random.choice(our_colors)
        rectangle = arcade.create_rectangle(x_loc, y_loc, size*2, 50, this_color)
        rectangle.draw()

        y_loc = y_loc-50






    arcade.finish_render()
    arcade.run()
main()