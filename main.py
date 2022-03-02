#CAITLIN PESTANA
#all done
#runs per usual



import arcade
import random

def main():

#create window
    arcade.open_window(800, 800, "drawing horizontal rectangles")
    arcade.set_background_color(arcade.color.WHITE)
#define our_colors
    our_colors = [arcade.color.EGYPTIAN_BLUE, arcade.color.ELECTRIC_PURPLE, arcade.color.PSYCHEDELIC_PURPLE,
                  arcade.color.MAGENTA, arcade.color.PURPLE_HEART,
                  arcade.color.BLACK, arcade.color.BRIGHT_TURQUOISE]
#open a data file
    data_file = open('data.txt')
#define all_lines
    all_lines = data_file.readlines()
#open arcade
    arcade.start_render()
#draw text
    arcade.draw_text(all_lines[0], 300, 750, arcade.color.DARK_MAGENTA, 20)
    arcade.draw_text(all_lines[1], 300, 50, arcade.color.BLACK, 15)
    arcade.draw_text(all_lines[2], 50, 400, arcade.color.BLACK, 20, rotation=90.0)
#define rest_of_lines
    rest_of_the_lines = all_lines[3:]
    x_loc = 400
    y_loc = 200
#for function
#"line" can be called anything
    for line in rest_of_the_lines:
#split line after the colon
        split_line = line.split (':')
#define size as an integer!!
        size = int(split_line[1])
#define this_color
        this_color = random.choice(our_colors)
#define rectangle
        rectangle = arcade.create_rectangle(x_loc, y_loc, size * 2, 50, this_color)


#draw rectangle
        rectangle.draw()
        arcade.draw_text(split_line[0], 70, y_loc-10, arcade.color.BLACK, 20)
#define y_loc of each rectangle
        y_loc = y_loc+50

    arcade.finish_render()
    arcade.run()
main()