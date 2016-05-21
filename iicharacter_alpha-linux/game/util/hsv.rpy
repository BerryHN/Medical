init -100 python:
    def count_hsv(r,g,b):
        max = r
        max = g if g>max else max
        max = b if b>max else max
        min = r
        min = g if g<min else min
        min = b if b<min else min

        if  max == min:
            return 0,0,max

        if  max == r:
            if  g>=b:
                h = (g-b)/(max-min)/6.0
            else:
                h = (g-b)/(max-min)/6.0 + 1.0
        elif max== g:
            h = (b-r)/(max-min)/6.0 + 1.0/3.0
        else:
            h = (r-g)/(max-min)/6.0 + 2.0/3.0

        s = 1 - min/max if max!=0 else 0
        v = max

        return h,s,v   

    def count_rgb(h,s,v):
        hi = int(h*6.0) % 6
        f = h*6.0 - int(h*6.0)
        p = v * (1-s)
        q = v * (1-f*s)
        t = v * (1-(1-f)*s)
        if  hi == 0:
            return v,t,p
        elif  hi == 1:
            return q,v,p
        elif  hi == 2:
            return p,v,t
        elif  hi == 3:
            return p,q,v
        elif  hi == 4:
            return t,p,v
        elif  hi == 5:
            return v,p,q
        else:
            return v,t,p

