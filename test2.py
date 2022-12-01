import math
from colorsys import rgb_to_hls
from colorsys import hls_to_rgb

def perceived_brightness(r,g,b):
    #https://alienryderflex.com/hsp.html
    #rgb = hex_to_rgb(value)
    return math.sqrt( (0.299 * r * r) + (0.587 * g * g) + (0.114 * b * b) )

def pb_r(g, b, pb):
    try:
        return math.sqrt( ( (pb*pb) - (0.587 * g * g) - (0.114 * b * b) ) / 0.299 )
    except:
        return -1

def pb_g(r, b, pb):
    try:
        return math.sqrt( ( (pb*pb) - (0.299 * r * r) - (0.114 * b * b) ) / 0.587 )
    except:
        return -1

def pb_b(r, g, pb):
    try:
        return math.sqrt( ( (pb*pb) - (0.299 * r * r) - (0.587 * g * g) ) / 0.114 )
    except:
        return -1

def rgb_to_hex(value):
    return '#%02x%02x%02x' % (int(value[0]*255.0), int(value[1]*255.0), int(value[2]*255.0))

def hex_to_rgb(value):
    h = value.lstrip('#')
    if len(h) == 6:
        return tuple(int(h[i:i+2], 16)/255.0 for i in (0, 2, 4))
    else:
        return tuple(int(h[i], 16)/15.0 for i in (0, 1, 2))

def find_r(pb):
    for g in range(0,255):
        for b in range(0,255):
            r = pb_r(g/255, b/255, pb)
            if r > 0 and r < 1:
                hls = rgb_to_hls(r,g/255,b/255)
                hue = hls[0]
                light = hls[1]
                sat = hls[2]
                if light == 0.5 and (abs(sat-0.47) < 0.01 or abs(sat-0.57) < 0.01 or abs(sat-0.67) < 0.01 or abs(sat-0.77) < 0.01 or abs(sat-0.87) < 0.01):
                    rgb = rgb_to_hex(hls_to_rgb(hue,light,sat))
                    colors.add(rgb)

def find_g(pb):
    for r in range(0,255):
        for b in range(0,255):
            g = pb_g(r/255, b/255, pb)
            if g > 0 and g < 1:
                hls = rgb_to_hls(r/255,g,b/255)
                hue = hls[0]
                light = hls[1]
                sat = hls[2]
                if light == 0.5 and (abs(sat-0.47) < 0.01 or abs(sat-0.57) < 0.01 or abs(sat-0.67) < 0.01 or abs(sat-0.77) < 0.01 or abs(sat-0.87) < 0.01):
                    rgb = rgb_to_hex(hls_to_rgb(hue,light,sat))
                    colors.add(rgb)


def find_b(pb):
    for r in range(0,255):
        for g in range(0,255):
            b = pb_b(r/255, g/255, pb)
            if b > 0 and b < 1:
                hls = rgb_to_hls(r/255,g/255,b)
                hue = hls[0]
                light = hls[1]
                sat = hls[2]
                if light == 0.5 and (abs(sat-0.47) < 0.01 or abs(sat-0.57) < 0.01 or abs(sat-0.67) < 0.01 or abs(sat-0.77) < 0.01 or abs(sat-0.87) < 0.01):
                    rgb = rgb_to_hex(hls_to_rgb(hue,light,sat))
                    colors.add(rgb)

colors = set()

find_r(0.41)
find_r(0.42)
find_r(0.43)
find_r(0.44)
find_r(0.45)
find_r(0.46)
find_r(0.47)
find_r(0.48)
find_r(0.49)
find_r(0.5)
find_r(0.51)
find_r(0.52)
find_r(0.53)
find_r(0.54)
find_r(0.55)
find_r(0.56)
find_r(0.57)
find_r(0.58)
find_r(0.59)

find_g(0.41)
find_g(0.42)
find_g(0.43)
find_g(0.44)
find_g(0.45)
find_g(0.46)
find_g(0.47)
find_g(0.48)
find_g(0.49)
find_g(0.5)
find_g(0.51)
find_g(0.52)
find_g(0.53)
find_g(0.54)
find_g(0.55)
find_g(0.56)
find_g(0.57)
find_g(0.58)
find_g(0.59)

find_b(0.41)
find_b(0.42)
find_b(0.43)
find_b(0.44)
find_b(0.45)
find_b(0.46)
find_b(0.47)
find_b(0.48)
find_b(0.49)
find_b(0.5)
find_b(0.51)
find_b(0.52)
find_b(0.53)
find_b(0.54)
find_b(0.55)
find_b(0.56)
find_b(0.57)
find_b(0.58)
find_b(0.59)


scolors = {}
for color in sorted(colors):
    rgb = hex_to_rgb(color)
    hls = rgb_to_hls(rgb[0],rgb[1],rgb[2])
    scolors[color] = round(hls[0]*50,0) + hls[2]

head="""
<!DOCTYPE html>
<html>
<title>colors</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>
<div class="w3-row-padding" style="color:#fff">
"""
print(head)

cnt = 2
for color in sorted(scolors, key=scolors.get):
    if cnt == 0:
        print('<div class="w3-center w3-padding w3-col l1 m2 s3" style="background-color:'+color+';cursor: copy;" onclick="copyColor(this.textContent);">'+color+'</div>')
        cnt = 2
    else:
        cnt -= 1

foot="""
</div>
<script>
function copyColor(color) {
  navigator.clipboard.writeText(color);
}
</script>
</body>
</html>"""
print(foot)