init -100 python:
    class myRainbow(im.ImageBase):    
        def __init__(self, img, saturation, transparency, **properties):
            img = im.image(img)
            super(myRainbow, self).__init__(img, **properties)
            self.image = img
            self.saturation = saturation
            self.transparency = transparency

        def get_mtime(self):
            return self.image.get_mtime()
    
        def load(self):
            surf = im.cache.get(self.image)    
            size = surf.get_size()
            width, height = size
    
            rv = renpy.display.pgrender.surface(size, True)    
            rv.blit(surf,(0,0))    
            for x in range(0, width):
                dh = 1.0*x/width + 0.7
                for y in range(0, height):
                    (r,g,b,a) = rv.get_at((x, y))
                    h,s,v = count_hsv(r/255.0,g/255.0,b/255.0)
                    h += dh
                    while h > 1:
                        h -= 1
                    r,g,b = count_rgb(h,self.saturation/255.0,v)
                    a *= self.transparency/255.0
                    color = (int(r*255.0),int(g*255.0),int(b*255.0),a)
                    rv.set_at((x, y),color)
            return rv
    
        def predict_files(self):
            return self.image.predict_files()

    class mySaturation(im.ImageBase):    
        def __init__(self, img, hue, transparency, **properties):
            img = im.image(img)
            super(mySaturation, self).__init__(img, **properties)
            self.image = img
            self.hue = hue
            self.transparency = transparency

        def get_mtime(self):
            return self.image.get_mtime()
    
        def load(self):
            surf = im.cache.get(self.image)    
            size = surf.get_size()
            width, height = size
    
            rv = renpy.display.pgrender.surface(size, True)    
            rv.blit(surf,(0,0))    
            for x in range(0, width):
                sat = 1.0*x/width
                for y in range(0, height):
                    hue = 1.0*y/height
                    (r,g,b,a) = rv.get_at((x, y))
                    h,s,v = count_hsv(r/255.0,g/255.0,b/255.0)
                    r,g,b = count_rgb(self.hue,sat,v)
                    a *= self.transparency/255.0
                    color = (int(r*255.0),int(g*255.0),int(b*255.0),a)
                    rv.set_at((x, y),color)
            return rv
    
        def predict_files(self):
            return self.image.predict_files()

    class myBrightness(im.ImageBase):    
        def __init__(self, img, hue, transparency, **properties):
            img = im.image(img)
            super(myBrightness, self).__init__(img, **properties)
            self.image = img
            self.hue = hue
            self.transparency = transparency

        def get_mtime(self):
            return self.image.get_mtime()
    
        def load(self):
            surf = im.cache.get(self.image)    
            size = surf.get_size()
            width, height = size
    
            rv = renpy.display.pgrender.surface(size, True)    
            rv.blit(surf,(0,0))    
            for x in range(0, width):
                bright = 1.0*x/width
                for y in range(0, height):
                    (r,g,b,a) = rv.get_at((x, y))
                    h,s,v = count_hsv(r/255.0,g/255.0,b/255.0)
                    r,g,b = count_rgb(self.hue,0,bright)
                    a *= self.transparency/255.0
                    color = (int(r*255.0),int(g*255.0),int(b*255.0),a)
                    rv.set_at((x, y),color)
            return rv
    
        def predict_files(self):
            return self.image.predict_files()


    