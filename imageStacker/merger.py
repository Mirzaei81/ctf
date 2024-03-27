from PIL import Image
import numpy as np
img1 = Image.open("./scrambled1.png").convert("RGBA")
img2 = Image.open("./scrambled2.png").convert("RGBA")
res = np.array(img1)+np.array(img2)
Image.fromarray(res).save("encryptrd.png")


        
