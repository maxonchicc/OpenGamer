define max = Character("Макс", color="#c8ffc8")
define alex = Character("Саня", color="#FFFF00")
define teacher = Character("Борис Петрович", color="#FF1493")
define rask = Character("Рассказчик", color="#808080")

image room = "bg/bg_room.jpg"
image toilet = "bg/bg_toilet.jpg"
image max = "pers/max.png"
image alex = "pers/alex.png"
image teacher = "pers/teacher.png"

label splashscreen:
    scene black
    with Pause(1)

    show text "Команда 'OpenGamer' представляет..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    show toilet
    show max at right
    with dissolve
    max "Я так больше не могу... мама говорит, надо в Вуз, батёк вообще.. МГИМО! МГИМО!.. Какое нахер МГИМО, я школу то заканчиваю с трудом!"

    show alex at left
    with dissolve
    alex "Почему с трудом? Котелок-то у тебя варит, просто предметы не все интересные. Да и система образования полная шляпа."

    show max
    max "И не говори. Почему, если я шарю в инфе и мне нравится кодить, я должен знать, как писать сочинение на 200 страниц."

    show alex
    alex "Не спорю, не спорю. Нууу... скоро ЕГЭ... Покажешь на что способен. Инфой как раз вытянешь. Мне-то вообще дай бог сдать."

    show max
    max "Хахахах ну да"

    hide max with dissolve
    hide alex with dissolve

    show teacher
    with dissolve
    teacher "Вы чё, мужики, со всем берега попутали! Быстро вышли и отраву эту мне сдайте, потом заберете."

    pause(2)

    scene black
    with Pause(1)

    "ЗАТЕМНЕНИЕ."

    with Pause(1)

    "Сцена 2"
    "Локация: комната Макса."

    show room
    show max

    max "Сидеть в туалете и курить парилку — это что-то. Надо бы подготовиться к ЕГЭ."

    max "По всюду бардак, но мне как-то все равно."

    max "Пойду за компьютер, пора закодить чего-нибудь."
