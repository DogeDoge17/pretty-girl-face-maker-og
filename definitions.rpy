...
# Characters
# This is where the characters bodies and faces are defined in the mod.
# They are defined by a left half, a right half and their head.
# To define a new image, declare a new image statement like in this example:
#     image sayori 1ca = Composite((960, 960), (0, 0), "mod_assets/sayori/1cl.png", (0, 0), "mod_assets/sayori/1cr.png", (0, 0), "sayori/a.png")



default sFit = 0
default sFace = "happy"
default sLeft = 0
default sRight = 0

init python:
    def changeSayori(**kwargs):
        global sFace
        global sLeft
        global sRight
        global sFit


        sFace = kwargs.get("face", sFace).lower()
        sLeft = kwargs.get("left", sLeft)
        sRight = kwargs.get("right", sRight)
        sFit = kwargs.get("fit", sFit)

    def s_pt(st, at, **kwargs):
        global sFace
        global sLeft
        global sRight
        global sFit
        #image_path = f"images/{outfit}_{emotion}.png"

        left = sLeft
        right = sRight
        fit = sFit
        face = sFace

        armTex = [" ", " "]

        for i in range(len(armTex)):   
            #print(i)      
            armPos = left if (i == 0) else left #0 for down, 1 for arms up

            if fit == 0:
                if(armPos == 0):
                    armTex[i] = "1"
                    #print("chose 1")
                else: #if (armPos == 1)
                    armTex[i] = "2"
                    #print("chose 2")
            else:
                if(armPos == 0):
                    armTex[i] = "1b"
                    #print("chose 1b")
                else: #if (armPos == 1)
                    armTex[i] = "2b"
                    #print("chose 2b")


        if face in ["happy", "smile", "hpy"]:
            faceText = "a"
        elif face == "concerned":
            faceText = "b"
        elif face == "open":
            faceText = "c"
        elif face == "sincere":
            faceText = "d"
        elif face == "blusho":
            faceText = "e"
        elif face in ["sad", "frown", "worried"]:
            faceText = "f"
        elif face in ["wsopen", "slight open", "mworried", "sow"]:
            faceText = "g"
        elif face in ["wtalk", "wopen", "wwide"]:
            faceText = "h"
        elif face in ["serious", "srs" ,"srsclosed"]:
            faceText = "i"
        elif face in ["srsopen", "serious slight open", "serious talk", "srsTalk"]:
            faceText = "j"
        elif face in ["longing", "melancholy", "zone out", "zoneout"]:
            faceText = "k"
        elif face in ["nervous", "nside", "nsweat", "longing happy"]:
            faceText = "l"
        elif face in ["whoops", "wah"]:
            faceText = "m"
        elif face in ["oop", "melancholy", "surprised"]:
            faceText = "n"
        elif face in ["oop", "retard", "fuuka"]:
            faceText = "o"
        elif face in [">.<", "uah", "><"]:
            faceText = "p"
        elif face in ["sthappy", "shut happy", "innocent"]:
            faceText = "q"
        elif face in ["osthappy", "open shut happy", "shut talk" ,"crashout", "808", "ts"]:
            faceText = "r"
        elif face in ["bosthappy", "blush open shut happy", "blush shut talk" ,"bcrashout", "b808", "bts"]:
            faceText = "s"
        elif face in ["chappy", "cry happy", "tears happy" ,"happy tears", "crying happy"]:
            faceText = "t"
        elif face in ["csad", "cry", "crying"]:
            faceText = "u"
        elif face in ["bcsad", "bcry", "bcrying", "blush cry", "blush crying"]:
            faceText = "v"
        elif face in ["cspaz", "noo", "cotalk", "spaz"]:
            faceText = "w"
        elif face in ["innocent happy", "happy talk", ":d", "htalk", "talk","ohappy"]:
            faceText = "x"
        elif face in ["blush", "bside", "bhappy", "happy blush", "blush happy"]:
            faceText = "y"
        elif len(face) > 1:
            faceText = "a"
            print("could not find face: ", face)
        else:
            faceText = face
            print("defaulting to letter ", face)

        #print(st, " at ", at, " face ", face, " left ", left, " right ", right, " kwargs ", kwargs, " faceText ", faceText, " armText ", armTex, " fit ", fit)    

        #s_last = im.Composite((960, 960), (0, 0), "sayori/" + armTex[0] + "l.png", (0, 0), "sayori/" + armTex[1] + "r.png", (0, 0), "sayori/" + faceText + ".png")

        return im.Composite((960, 960), (0, 0), "sayori/" + armTex[0] + "l.png", (0, 0), "sayori/" + armTex[1] + "r.png", (0, 0), "sayori/" + faceText + ".png"), 0

image sayori pt = DynamicDisplayable(s_pt)


# Sayori's Character Definitions
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
...
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

# This image shows a glitched Sayori sprite during Act 2.
image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

default nFit = 0
default nFace = "happy"
default nLeft = 0 #2 for arms crossed
default nRight = 0

default nLayers = ["layer1.png", "layer2.png", "layer3.png"]
default nOffsets = [(0, 0), (0, 0), (0, 0)] 

init python:
    def changeNatsukiEMR(**kwargs):
        global nLayers 
        global nOffsets

        if kwargs.get("crossed", None) != None:
            faceOff = (18, 22)
        else:
            faceOff = (0,0)

        nLayers = ((faceOff), "mod_assets/natsuki/face.png")

        if kwargs.get("nose", None) != None:
            nLayers = nLayers + ((faceOff), "/mod_assets/natsuki/" + kwargs.get("nose", "/natsuki_ff_nose_n1.png"))
            #nLayers.append(((faceOff), "/mod_assets/natsuki/" + kwargs.get("nose", "/natsuki_ff_nose_n1.png")))
            #nOffsets.append(faceOff)
        if kwargs.get("eyes", None) != None:
            nLayers = nLayers + ((faceOff), "/mod_assets/natsuki/" + kwargs.get("eyes", "/natsuki_ff_eyebrows_b1a.png"))
            #nLayers.append(((faceOff), "/mod_assets/natsuki/" + kwargs.get("eyes", "/natsuki_ff_eyebrows_b1a.png")))
            #nOffsets.append(faceOff)
        if kwargs.get("brows", None) != None:
            nLayers = nLayers + ((faceOff), "/mod_assets/natsuki/" + kwargs.get("brows", "/natsuki_ff_nose_n1.png"))
            #nLayers.append(((faceOff), "/mod_assets/natsuki/" + kwargs.get("brows", "/natsuki_ff_nose_n1.png")))
           # nOffsets.append(faceOff)
        if kwargs.get("mouth", None) != None:
            nLayers = nLayers + ((faceOff), "/mod_assets/natsuki/" + kwargs.get("mouth", "/natsuki_ff_nose_n1.png"))
            #nLayers.append(((faceOff), "/mod_assets/natsuki/" + kwargs.get("mouth", "/natsuki_ff_nose_n1.png")))
            #nOffsets.append(faceOff)
        if kwargs.get("beat", None) != None:
            nLayers = nLayers + ((faceOff), "/mod_assets/natsuki/" + kwargs.get("beat", "/natsuki_ff_nose_n1.png"))
            #nLayers.append(((faceOff), "/mod_assets/natsuki/" + kwargs.get("beat", "/natsuki_ff_nose_n1.png")))
            #nOffsets.append(faceOff)

        if (kwargs.get("left", None) != None and kwargs.get("right", None) != None):
            nLayers = nLayers + ((0,0), "/mod_assets/natsuki/" + kwargs.get("left", "/natsuki_ff_nose_n1.png"))
            #nLayers.append(((0,0), "/mod_assets/natsuki/" + kwargs.get("left", "/natsuki_ff_nose_n1.png")))
            #nOffsets.append()
            nLayers = nLayers + ((0,0), "/mod_assets/natsuki/" + kwargs.get("right", "/natsuki_ff_nose_n1.png"))
            #nLayers.append(((0,0), "/mod_assets/natsuki/" + kwargs.get("right", "/natsuki_ff_nose_n1.png")))
            #nOffsets.append()

        elif kwargs.get("crossed", None) != None:
            nLayers = nLayers + ((0,0), "/mod_assets/natsuki/" + kwargs.get("crossed", "/natsuki_ff_nose_n1.png"))
            #nLayers.append(((0,0), "/mod_assets/natsuki/" + kwargs.get("crossed", "/natsuki_ff_nose_n1.png")))
            #nOffsets.append()
        else:
            nLayers = nLayers + ((0,0), "/mod_assets/natsuki/natsuki_turned_uniform_left_down.png")
            #nLayers.append(((0,0), "/mod_assets/natsuki/natsuki_turned_uniform_left_down.png"))
            #nOffsets.append((0,0))
            nLayers = nLayers + ((0,0), "/mod_assets/natsuki/natsuki_turned_uniform_right_down.png")
            #nLayers.append(((0,0), "/mod_assets/natsuki/natsuki_turned_uniform_right_down.png"))
            #nOffsets.append((0,0))
        # print(nOffsets)
        # print(nLayers)


    def changeNatsuki(**kwargs):
        global nFace
        global nLeft
        global nRight
        global nFit
        #global nCrossed

        #if "crossed" in kwargs
        #    nCrossed = kwargs.get("crossed", nCrossed)
        #    nLeft = -1
        #    nRight = -1
        #else
        #    kwargs.get("crossed", False):

        nFace = kwargs.get("face", nFace)
        nLeft = kwargs.get("left", nLeft)
        nRight = kwargs.get("right", nRight)
        nFit = kwargs.get("fit", nFit)

    def n_pt(st, at, **kwargs):
        global nLayers # = ["layer1.png", "layer2.png", "layer3.png"]
        global nOffsets

        return im.Composite((960, 960), *nLayers),0

        global nFace
        global nLeft
        global nRight
        global nFit

        left = nLeft
        right = nRight
        fit = nFit
        face = nFace

        armTex = ["", ""]

        crossed = False

        for i in range(len(armTex)):   
            armPos = left if (i == 0) else left #0 for down, 1 for arms up

            if fit == 0:
                if(armPos == 0):
                    armTex[i] = "1"
                elif (armPos == 1):
                    armTex[i] = "2"
                else:
                    armTex[i] = "3"
                    crossed = True
                    break
            else: #fit == 1:
                if(armPos == 0):
                    armTex[i] = "1b"
                elif (armPos == 1):
                    armTex[i] = "2b"
                else:
                    armTex[i] = "3b"
                    crossed = True
                    break
    
    
        if face in ["happy", "smile", "hpy"]:
            faceText = "a"
        elif face == "concerned":
            faceText = "b"
        elif face == "open":
            faceText = "c"
        elif face == "sincere":
            faceText = "d"
        elif face == "blusho":
            faceText = "e"
        elif face in ["sad", "frown", "worried"]:
            faceText = "f"
        elif face in ["wsopen", "slight open", "mworried", "sow"]:
            faceText = "g"
        elif face in ["wtalk", "wopen", "wwide"]:
            faceText = "h"
        elif face in ["serious", "srs" ,"srsclosed"]:
            faceText = "i"
        elif face in ["srsopen", "serious slight open", "serious talk", "srsTalk"]:
            faceText = "j"
        elif face in ["longing", "melancholy", "zone out", "zoneout"]:
            faceText = "k"
        elif face in ["nervous", "nside", "nsweat", "longing happy"]:
            faceText = "l"
        elif face in ["whoops", "wah"]:
            faceText = "m"
        elif face in ["oop", "melancholy", "surprised"]:
            faceText = "n"
        elif face in ["oop", "retard", "fuuka"]:
            faceText = "o"
        elif face in ["bcsad", "bcry", "bcrying", "blush cry", "blush crying"]:
            faceText = "p"
        elif face in ["sthappy", "shut happy", "innocent"]:
            faceText = "q"
        elif face in ["osthappy", "open shut happy", "shut talk" ,"crashout", "808", "ts"]:
            faceText = "r"
        elif face in ["bosthappy", "blush open shut happy", "blush shut talk" ,"bcrashout", "b808", "bts"]:
            faceText = "s"
        elif face in ["chappy", "cry happy", "tears happy" ,"happy tears", "crying happy"]:
            faceText = "t"
        elif face in ["csad", "cry", "crying"]:
            faceText = "u"
        elif face in [">.<", "uah", "><"]:
            faceText = "v"
        elif face in ["cspaz", "noo", "cotalk", "spaz"]:
            faceText = "w"
        elif face in ["innocent happy", "happy talk", ":d", "htalk", "talk","ohappy"]:
            faceText = "x"
        elif face in ["blush", "bside", "bhappy", "happy blush", "blush happy"]:
            faceText = "y"
        elif face == "scream":
            faceText = "scream"
        elif len(face) > 4:
            faceText = "a"
            print("could not find face: ", face)
        else:
            faceText = face
            print("defaulting to letter ", face)
    
        print(st, " at ", at, " face ", face, " left ", left, " right ", right, " kwargs ", kwargs, " faceText ", faceText, " armText ", armTex, " fit ", fit, " crossed ", crossed)            
        if not crossed:
            return im.Composite((960, 960), (0, 0), "natsuki/" + armTex[0] + "l.png", (0, 0), "natsuki/" + armTex[1] + "r.png", (0, 0), "natsuki/" + faceText + ".png"), 0
        else:
            return im.Composite((960, 960), (0, 0), "natsuki/" + max(armTex) + ".png", (18, 22), "natsuki/" + faceText + ".png"), 0

image natsuki pt = DynamicDisplayable(n_pt)


# Natsuki's Character Definitions
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
...
# I didnt do monika or yuri
