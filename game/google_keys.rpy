init -5 :
    if renpy.android:
        define fullgame = iap.register(product = "fullgame",identifier = "com.ws.qc.productname", google = "productname") 
        python:
            build.google_play_key=""
            build.google_play_salt=""
