init python:
    lang = "ru"

    if  not lang in localization:
        localization[lang] = {}

    localization[lang][u"Image export"] = u"Экспорт изображения:"
    localization[lang][u"Save as PNG"] = u"Сохранить как PNG"
    localization[lang][u"Save as PNG and copy to clipboard"] = u"Сохранить как PNG, скопировать в буфер обмена"
    localization[lang][u"Exported files are put to /export/ folder on your harddrive."] = u"Файлы кладутся в каталог /export/ на жёстком диске."
    localization[lang][u"See exported pictures in OS browser"] = u"Посмотреть экспортированные изображения в системном проводнике"

    localization[lang][u"Export %s"] = u"Экспорт %s"
    localization[lang][u"Moved export directory"] = u"Изменён каталог для экспорта"
    localization[lang][u"Added export to clipboard"] = u"Добавлен экспорт в буфер обмена"