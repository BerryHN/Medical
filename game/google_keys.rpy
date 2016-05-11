init -53:
    python:
        build.google_play_key="MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzFv70bouKVbF6IdFxCTmSc1RSNUgJkUU2xN0ek0Toi3DGhxYuo3S+9ggI6EXJYWrCbeOaQSWmVUHokmysLKV/GjfzoM6Hdl6n/J+xPJzM2jX61kTAPCtCVjv1QphQLP7iRmPi/D/GAN5nVEFcBmXtkPjuiOBi0/tYLkaDRdREWl5HnVuhmmdO5N/hW0lXqcWwh67+r2nVXyBiAeon1GmQZ5NYEyeM+x75vw+cbFaDIWghVGxENvdfknlE97vzhyUCD4XvdylwmwUH8VGzuvFD4SfF9Vr16tU7+2bdBI6fWdfabY680ig3uiEYEPQe9EUxzed73MdOV6mXh8Nt/2CtQIDAQAB"
        build.google_play_salt=(1,3,4,5,-1, -5, 12, -122, 100, 12,112,13,41,15,-11, -51, 122, -122, 110, 125)
    if renpy.android:
        define fullgame = iap.register(product = "fullgame",identifier = "com.hedley", google = "productname") 
        
