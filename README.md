bliPy
=====

#A Python wrapper for thingM's blink(1) USB RGB LED

Example code

    import bliPy
    interval = 1.75
    bl1 = bliPy.Blink1()
    bl1.breath(interval)
    bl1.breathrand(interval)
    bl1.fade(interval)
    bl1.fadeseq(interval)
    bl1.fadetorand(interval)
    bl1.rand(interval)
    bl1.blink(interval)
    
Using colors from the dictionnary
    bl1.breath(interval, bl1.colors['RED'])

Available colors: Red, Orange, Yellow, Spring_Green, Green, Turquoise, Cyan, Ocean, Blue, Violet, Magenta, Raspberry, White and Grey.

You will see blink(1) 'breathing' like the Macbook presence LED
