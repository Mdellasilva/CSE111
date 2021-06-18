import tkinter as tk
import random

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")
    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    """
    tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    """
    draw_ground(canvas, 0, 0, 799, 600)
    
    draw_sky(canvas, 0, 0, 799, 350)

    draw_stars(canvas, 3, 3, 2, 1)
    
    draw_cloud(canvas, 500, 50, 750, 100)
    draw_cloud(canvas, 50, 100, 250, 150)
    draw_cloud(canvas, 400, 150, 500, 100)
    draw_cloud(canvas, 600, 200, 775, 100)
    draw_cloud(canvas, 150, 40, 350, 125)

    draw_water(canvas, 0, 300, 799, 400)

    draw_rocks(canvas, 0, 390, 15, 405)

    draw_lighthouse_base(canvas, 210, 415, 340, 440)

    draw_lighthouse_top(canvas, 220, 100, 230, 195)
    draw_lighthouse_top(canvas, 220, 100, 325, 110)
    draw_lighthouse_top(canvas, 320, 100, 330, 195)

    draw_lighthouse_light(canvas, 262, 170, 287, 195)

    draw_lighthouse_roof(canvas, 200, 95, 350, 110)

    draw_light(canvas, 275, 170, 400, 175)

    
    '''
    draw_lighthouse(canvas, 211, 395, 339, 420)
    draw_lighthouse(canvas, 212, 375, 338, 400)
    draw_lighthouse(canvas, 213, 355, 337, 380)
    draw_lighthouse(canvas, 214, 335, 336, 360)
    draw_lighthouse(canvas, 215, 315, 335, 340)
    draw_lighthouse(canvas, 216, 295, 334, 320)
    draw_lighthouse(canvas, 217, 275, 333, 300)
    draw_lighthouse(canvas, 218, 255, 332, 280)
    draw_lighthouse(canvas, 219, 235, 331, 260)
    draw_lighthouse(canvas, 220, 215, 330, 240)
    '''
    

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_ground(canvas, sl, st, sr, sb):
    canvas.create_rectangle(sl, st, sr, sb, width=1, fill="blanched almond")
    return

def draw_sky(canvas, sl, st, sr, sb):
    canvas.create_rectangle(sl, st, sr, sb, width=1, fill="midnight blue")
    return

def draw_cloud(canvas, sl, st, sr, sb):
    canvas.create_oval(sl, st, sr, sb, width=0, fill="royal blue4")
    return

def draw_water(canvas, sl, st, sr, sb):
    canvas.create_rectangle(sl, st, sr, sb, width=0, fill="dodger blue4")

def draw_lighthouse_base(canvas, sl, st, sr, sb):
    for i in range(0,12):
        canvas.create_rectangle(sl, st, sr, sb, width=0, fill="light steel blue")
        sl += 1
        st -= 20
        sr -= 1
        sb -= 20

def draw_lighthouse_top(canvas, sl, st, sr, sb):   
    canvas.create_rectangle(sl, st, sr, sb, width=0, fill="black")

def draw_lighthouse_light(canvas, sl, st, sr, sb):
    canvas.create_rectangle(sl, st, sr, sb, width=0, fill="yellow")

def draw_lighthouse_roof(canvas, sl, st, sr, sb):
    canvas.create_oval(sl, st, sr, sb, width=0, fill="black")

def draw_rocks(canvas, sl, st, sr, sb):
    left = sl
    right = sr
    for i in range(0,12):
        for i in range(0,100):
            rock_color = random.randint(0,5)
            if rock_color == 0:
                canvas.create_oval(sl, st, sr, sb, width=1, fill="gray40")
            elif rock_color == 1:
                canvas.create_oval(sl, st, sr, sb, width=1, fill="gray20")
            elif rock_color == 2:
                canvas.create_oval(sl, st, sr, sb, width=1, fill="slate gray")
            elif rock_color == 3:
                canvas.create_oval(sl, st, sr, sb, width=1, fill="light grey")
            elif rock_color == 4:
                canvas.create_oval(sl, st, sr, sb, width=1, fill="gray30")
            elif rock_color == 5:
                canvas.create_oval(sl, st, sr, sb, width=1, fill="gray50")           
            sl += 8
            sr += 8
        sb += 10
        st += 10
        sl = left
        sr = right

def draw_stars(canvas, sl, st, sr, sb):
    left = sl
    right = sr
    for i in range(0,15):
        for i in range(0,100):
            star_color = random.randint(0,1)
            if star_color == 0:
                canvas.create_oval(sl, st, sr, sb, width=1, fill="yellow")
            elif star_color == 1:
                canvas.create_oval(sl, st, sr, sb, width=0, fill="light goldenrod")         
            sl += random.randint(18,75)
            sr = sl
        sb += random.randint(27,29)
        st = sb
        sl = left
        sr = right

def draw_light(canvas, sl, st, sr, sb): 
    for i in range(0,10):
        canvas.create_oval(sl, st, sr, sb, width=0, fill="light yellow")
        sl += 50
        st -= 2
        sr += 50
        sb += 2


"""
def draw_pine_tree(canvas, peak_x, peak_y, height):
    Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")
"""

# Call the main function so that
# this program will start executing.
main()