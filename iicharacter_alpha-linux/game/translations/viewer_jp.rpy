init python:
    lang = "jp"

    if  not lang in localization:
        localization[lang] = {}

    localization_prefix[lang] = u"{font=FOT-BudoStd-L.otf}"
    localization_suffix[lang] = u"{/font}"

    localization[lang][u"Load configuration:"] = u"設定を読み込む:"
    localization[lang][u"Save configuration:"] = u"設定を保存:"
    localization[lang][u"Rewrite configuration:"] = u"設定を書き換える:"
    localization[lang][u"Cancel"] = u"キャンセル"
    localization[lang][u"Input a name"] = u"ファイル名を入力"
