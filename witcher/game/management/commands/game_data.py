rpg_data = [
    {
        'name': '1',
        'message': '''Шёл холодный осенний дождь. Геральт, уставший, пребывавший уже около трёх дней в
пути, нуждался в ночлеге и тепле. Около недели он не мог найти новых заказов на чудовищ, а
припасы заканчивались. Он понимает, что если не найдёт какой-нибудь заказ, то не сможет
доехать до Новиграда, где работы всегда хватает.
-Три дня в пути, кроме курганов и выжженных полей - ничего. - пробурчал Геральт.
Но вдруг, за небольшим холмом, послышались звуки, походившие на звуки рабочего села.
- Хм, неужели?...''',
        'actions': {'Отправиться в сторону деревни.': (35, None)},
        'image': 'AgACAgIAAxkBAAMPYJmUy4uzQEJYC0SVFmWYMdXR_O0AAqqzMRvr2dFI_gLnUHgshkRu21OiLgADAQADAgADbQADAw4CAAEfBA',
    },
    {
        'name': '2',
        'message': '''На старой, прогнившей от влаги доске, висели несколько потёртых объявлений.
В одном говорилось о необходимости передать серебряные предметы в Новиград.
В другом, агитационные плакаты, призывающие вступить в ряды партизан против
Нильфгаардских оккупантов.
Но Геральт, естественно, искал не это.
Просмотрев около 5 бумаг, он всё-таки нашёл то, что могло его заинтересовать.
"Тролль под мостом совсем учудился. Смельчаку, что его зарубить сумеет - будет
полагаться награда. Коли вопросы будут - обращаться к [000010010111100001100]."
- Опять какой-то тролль разошёлся. Предчувствие, что такая деревня на отшибе не
сможет заплатить за убийство тролля. Но к кому идти то? - Сам себя спросил Геральт.
-Не уж то только ведьмакам тут рады?
Он применил ведьмачье чутьё и увидел на краю объявления обозначения:
А - 00 Е - 100 О - 111 П - 10 Р - 101 С - 000 Т - 01
''',
        'actions': {'Отправиться к дому старосты': (21, None)},
        'answer': {'answ': 'старосте', 'before': 'Отгадайте слово', 'after': 'Дом старосты я уже видел, можно наведаться.',
                   'reward': 50}
    },
    {
        'name': '3',
        'message': '''- Возьмак прав. Возьми только вот это от меня. Я так спасибо сказать тебе. Недавно оленя
задушить. Не знать зачем, у меня тут суп из нильфов, будешь!? А, возьмак ж не ест людя, тогда
возьми ещё и это( помимо правого бедра оленя, действительно свежего, тролль притащил
целый рюкзак, наполненный различным барахлом, вроде кошелька с монетами, какими-то
ценными чашами и ещё чем-то)
- Это я у нильфов взять. Обычно, богатый мужик всё забирать, да это я забыл отдать.
Теперь твоё это.
''',
        'actions': {'Принять дар от тролля. Пожарить оленину и уйти.': (29, None)},
        'image': 'AgACAgIAAxkBAAMRYJmU7FsaSaO3rqpa17FaE8s1m0MAAquzMRvr2dFIZOT7YoQR_6HMhcOaLgADAQADAgADbQADb4IAAh8E',
    },
    {
        'name': '4',
        'message': '''Геральт неспешно подошёл к троллю. Было заметно, что тот не в восторге от того, что по
его логову бродит мутант, который создан, чтобы подобных убивать. Тролль не напал только
потому, что был под действием алкоголя. Сколько и как нужно пить, чтобы такая здоровенная
детина была в таком состоянии...
- Я нашёл записку в остатках тех несчастных, что напали на вас. В ней прямым текстом
даётся понять, что вы были им заказаны. Старостой, на которого ты работаешь - сказал Геральт.
- Что?! - прокричал на всю местность тролль. - Эта птичье дерьмо сказать нас убить этим
железякам?! Возьмак, пойдём в деревня, я с ним такое проверну!
- Успокойся, то, что ты справился с пятью наёмниками-пьяницами, не значит, что
справишься и целой деревней, тебя закидают вилами, а из бошки сделают прекрасное чучело -
ответил осторожно Геральт, чтобы тролль не впал в бешенство. - Я сам поговорю с этим
Борисом.
- Возьмак. Если он убить мою троллиху, надо чтоб он сдох. - с очень грустным тоном
произнёс трёхметровый каменный тролль.
- Я что-нибудь придумаю.
''',
        'actions': {'Отправиться в деревню.': (19, None)},
    },
    {
        'name': '5',
        'message': '''Геральт продолжил свой путь по Большаку.
Кто знает, может, ещё что-нибудь подвернётся, только более простое.
В сотый раз за свою жизнь в голову приходил вопрос: "Кто всё-таки настоящее чудовище.
Тролль-алкоголик? Староста, что пользовался услугами убитого горем тролля и наживался на
горе других людей? А может, сам ведьмак?"...
''',
        'actions': {},
        'image': 'AgACAgIAAxkBAAMTYJmVB520g3IpgZdtyvjbdsQ8GgQAAqyzMRvr2dFI-5gBo1ZI4hXa6TKbLgADAQADAgADbQADKVkGAAEfBA',
        'ending': 'Вопросы мироздания'
    },
    {
        'name': '6',
        'message': '''Времени для раздумий особо не было. Тролль вот-вот ринется напролом. Чтобы выстоять
перед ударом такого здоровяка физическая форма обычного человека не подходойдёт. А силы, чтобы пробить полукаменную кожу, нужно немерено, благо, у Геральта
в маленьком подсумке на поясе среди эликсиров Ласточка и Иволга, был небольшой флакон с
эликсиром Грач, который увеличивал мышечную массу на короткое время, силы удара вполне
хватит, чтобы пробить такую кожу каменного тролля, лишь бы меч не сломался.
Выпив флакончик, Геральт успевает сделает пару резких шагов в сторону, чтобы тролль
не вмял его в землю. Развернувшись, ведьмак с максимально возможной силой сделал замах,
чтобы сделать рассечение от шеи до левого бока тролля. Удалось лишь слегка ранить гиганта.
Тот взвыл, резко развернувшись, снёс правой рукой Геральта метра на три. Тот бы
потерял сознание, но Грач увеличивал болевой порог. Тролль резко
приблизился, наклонился, чтобы всей тушей навалиться на ведьмака.
Всего секунда, чтобы подняться и приготовиться к удару, но
Геральт успел. Ударив по руке, что тянулась, дабы схватить его, он отсекает её.
Воспользовавшись шоком чудовища, Геральт в пируэте делает максимально точный удар
по шее чудовище. Огромная двухсоткилограммовая туша рухнула на землю.
Оставалось только взять трофей, голову тролля, и отправиться в деревню за наградой.
''',
        'actions': {' Взять трофей. Отправиться в деревню за наградой.': (26, None, 'troll_dead', -10)},
        'image': 'AgACAgIAAxkBAAMVYJmVRtEM8dnIPUhTYAm3zQiXY3oAAjG0MRtK9chIAx10lrVQ9zcPUQukLgADAQADAgADbQADbuMAAh8E',
    },
    {
        'name': '7',
        'message': '''Геральт аккуратно спустился вниз, стараясь не выдать себя. Придерживая мечи за
спиной, он скользил по сырой глине, еле удерживаясь за уступы, что поросли травой. Больше
рыков чудовища не последовало, но Геральт знал, что тролль в состоянии застать врасплох
даже самого опытного ведьмака.
Спустившись, Белый Волк, тихими шагами пытался понять, откуда шёл звук, но снова
наступила мёртвая тишина. Правда, всего на секунд десять. И вот чудовище показалось. Это был
каменный тролль - наиболее агрессивный среди своих собратьев, только непонятно, что он
здесь делает, ведь они живут преимущественно в заброшенных шахтах или пещерах. Рост
около трёх метров, практически всё тело покрыто каменным панцирем, а морда была вся в
шрамах, ужесточая и без того небезобидный облик клыкастого монстра.
Он заметил Геральта, когда тот неосторожно наступил на сухую ветку ели.
Тролль моментально приблизился к ведьмаку.
- ААА! Стоять, людь должен плату. Нет плата - нет прохода. Будешь ругаться - сожру. Давай
плата. Водка лучше. - быстро и доходчиво объяснил тролль.
''',
        'actions': {'-"Ты будешь брать плату меня за невыполненную работу?"': (25, None),
                    '-"Оплаты не будет, тролль, хватит с тебя проблем для умирающей деревни" [напасть на тролля]': (9, None, None, -5)},
        'image': 'AgACAgIAAxkBAAMXYJmVWlr0l5ZQTkYsC0RkCYZMObMAAjK0MRtK9chIE2KjkJG65oXqyYqiLgADAQADAgADbQADQhwCAAEfBA',
    },
    {
        'name': '8',
        'message': '''- Хм, вижу, ты слишком много узнал, белоголовый. Ты не поймешь, что выжить в этом мире
сможет только тот, у кого хватает мозгов повелевать тупоголовыми, вроде этого тролля. - 
цинично произнёс Борис. - Разве его жизнь стоит того, чтобы умереть самому?! Я не смогу
просто так тебя отпустить, если об этом узнают, меня будет ждать суд, а нильфгаардские палачи
не славятся своей милостью...
Вдруг, буквально из ниоткуда, две мощные руки крепко схватили Геральта за плечи, и
вышвырнули с порога прямо на улицу. Он не успел даже понять, что произошло, ведь к
ведьмаку так легко не подобраться, значит, двое уже стояли за дверями дома, ждали, пока
Геральт даст повод, чтобы поиграть с ними.
Его окружили шесть человек. Та самая охрана возле дома. Вооружены топорами, мечами.
Двое с большими полукруглыми щитами. По снаряжению можно было понять, что это не
обычная солдатня.
Поэтому, хоть Геральт и ожидал атаки, он всё же был слегка сбит с толку.
Нужно было быстро привести себя в чувства.
"Ничего не бодрит лучше, чем порция математики" - сказал он себе.

((X + 44) * 2) ** 0.5 = 12
''',
        'actions': {'Встать в боевую стойку, дожидаясь возможности контратаковать': (23, None),
                    'Пустить знак Аард в землю, чтобы раскидать окружающих наёмников': (22, None)},
        'answer': {'answ': 28, 'before': 'Найдите X', 'after': 'Отлично, кажется Белый Волк пришёл в себя, можно и подраться',
                   'reward': 50}

    },
    {
        'name': '9',
        'message': '''-Нет, я просто брать монета. Так мужик богатый сказать. Ты отдавать мне монета, я
отдавать мужику монета, а он мне выпить дать.
''',
        'actions': {'-"Ты собираешь дань с прохожих, зарабатывая от старосты водку?!"': (32, None)}
    },
    {
        'name': '10',
        'message': '''Геральт быстро достал из ножен серебряный меч. Тролль хоть и был пьян в дребезги, но
это только усугубляло ситуацию. В таком случае, тролль становился более агрессивным.
Кожа такого чудовища слишком тверда, чтобы пробить её в обычном состоянии с мечом.
Нужно было спешно что-то придумать, но для этого перед сражением стоило сосредоточиться.
Геральту с этим помогала математика.
x ** 2 + x - 6 = 0    "Хммм, больший корень равен..."
''',
        'actions': {'Применять ведьмачьи знаки.': (31, None),
                    'Применить эликсир "Грач".': (5, None),
                    'Применить масло против тролля.': (33, None)},
        'answer': {'answ': 2, 'before': 'Найдите больший корень', 'after': 'Отлично, кажется Белый Волк пришёл в себя, можно и подраться',
                   'reward': 50},
        'image': 'AgACAgIAAxkBAAMVYJmVRtEM8dnIPUhTYAm3zQiXY3oAAjG0MRtK9chIAx10lrVQ9zcPUQukLgADAQADAgADbQADbuMAAh8E',
    },
    {
        'name': '11',
        'message': '''Геральт схватил за шкирку Бориса и вывел на улицу перед толпой.
- Все ваши беды с мостом из-за жадности этого человека. - сказал ведьмак. - он вытащил
записку из кармана и дал зачитать мужику с вилами.
- Прочитав в слух приказ, люди начали рассуждать, мол почему троллей не убили, ведь
староста говорил, что солдаты обманули его и сбежали.
Самые злые и крепкие мужики скрутили старосту, увели, чтобы его связали.
- Мы расскажем нильфам о том, что эта скотина специально наживалась на горе людей.
Спасибо Вам, мастер ведьмак. Я полагаю, это Ваше - пухленький мужичек протянул мешочек с
золотом к Геральту. - Вы совершили абсолютно правильный поступок.
''',
        'actions': {'-"Спасибо"[взять награду]': (16, 'troll_dead'),
                    'Я не могу взять. Тролль все ещё жив." [отправиться к троллю]': (28, 'troll_side')}
    },
    {
        'name': '12',
        'message': '''-О, спасибо большое, возьмак, я не знаю, как бы дальше тута был, если бы тот гад не сдох. Я
думаю, тебе не дать монета, я ведь живой"
''',
        'actions': {'-"Да, остался я из-за тебя без награды, но оно того стоило."': (15, None)},
        'image': 'AgACAgIAAxkBAAMZYJmVsFCWl-44EPoZOIayLhjC8KYAAs6zMRvr2dFIrDeS1zU9VbZf91miLgADAQADAgADbQAD4voBAAEfBA',
    },
    {
        'name': '13',
        'message': '''
''',
        'actions': {}
    },
    {
        'name': '14',
        'message': '''- "Впервые вижу в Новой Темерии такой контраст между домом старосты и
остальными халупами. Вижу, хорошо вы устроились"
- Хе-хе, война всех поставила перед выбором. Помирать за наплевавших на нас королей
или жить, но под сапогом врага, но врага щедрого, если его слушаться. Вот так Темерия только
и выстояла, пусть и под властью этих нильфов. Вот и я, когда войска пришли, стоял перед таким
выбором, да выбрал жизнь. Нашу деревню не тронули, а меня за помощь наградили командиры
нильфов. Не вам меня судить, мастер ведьмак. Поступи я по-другому, что тогда? Помахал бы
вилами дня два, а потом меня, семью мою, да всю деревню утопили бы в реке. - в глазах
старосты мелькнуло презрение. Видно было, что он не хотел бы снова возвращаться к этой
теме. - меня Борисом звать, скажите, как имя-то ваше?
''',
        'actions': {'-"Я Геральт из Ривии. Ближе к делу." ': (17, None)}
    },
    {
        'name': '15',
        'message': '''Когда Геральт зашёл в дом, Борис так и сидел на лавке за своей тарелкой с супом. Увидев
ведьмака, староста вскрикнул, упал со скамьи, максимально быстро встал к стене и стал молить
о пощаде. Видимо, он переоценил способности своих вояк.
- Прошу, без меня деревня не справится! Эта деревенщина не сможет ничего сделать! -
выл староста. 
''',
        'actions': {'Вывести старосту на улицу и рассказать о том, что староста пользовался спившимся троллем, а все убийства и грабежи прохожих лежат насовести Бориса]( Геральт останется без денег) ': (10, 'note', None, 5),
                    'Обезглавить Бориса': (24, None, None, -8),
                    '-"Хмм, тролль мёртв". Спокойно забрать деньги': (16, 'troll_dead')}
    },
    {
        'name': '16',
        'message': '''- Как дальше то быть? Жить здеся - нельзя, убьють.
''',
        'actions': {'-"Я думаю, бросай пить и иди отсюда подальше. Драться я с тобой не буду, а вот в деревне хоте ли бы, чтобы ты умер" ': (2, None)},
        'image': 'AgACAgIAAxkBAAMZYJmVsFCWl-44EPoZOIayLhjC8KYAAs6zMRvr2dFIrDeS1zU9VbZf91miLgADAQADAgADbQAD4voBAAEfBA',
    },
    {
        'name': '17',
        'message': '''Геральт взял мешочек, наполненный золотом. Перепроверять сумму награды не было
смысла. Любой человек знает, что не стоит обманывать ведьмаков с наградой.
800 оренов вполне хватит, чтобы добраться до Новиграда, купить необходимые для
эликсиров травы, набить желудок, снять маленькую комнату хотя бы на пару
дней и отмыться.
Собраться с мыслями, наконец-то расслабиться. Таков ритм жизни
ведьмака. Постоянный поиск работы ради выживания. Благо, после войны,
различных трупоедов и других бестий на большаке хватает.
Это был всего лишь очередной заказ на очередное чудовище.
''',
        'actions': {},
        'image': 'AgACAgIAAxkBAAMbYJmVy2QK7cH5Y2EWlrQiKMp3XYQAAs-zMRvr2dFImXwhKTFYfGdzp1qkLgADAQADAgADbQADIdkAAh8E',
        'ending': 'Всего лишь очередной заказ',
        'reward': 80,
    },
    {
        'name': '18',
        'message': '''- Что ж, будем знакомы. Понимаете, мастер ведьмак, тут такое дело. Около пяти лет
назад, как только война-то кончилась с нильфами, мост наш сильно пострадал, а через него и
в город, и на большак торговцы выезжали. И никак нам без него. Вот и пришёл к нам как-то
этот тролль, чтоб его... Он не буйным казался, поселился он под этим мостом, людей жрал, что
отказывались плату давать, да повозки грабил. Но когда мы деревней-то собрались, пришли к
нему, думали, что серьёзная драка будет, детина-то вон какая здоровая, но он сказал, мол,
драться не хочет. Я там прикинул, да договорились мы. Он мост достраивает, но никого не
трогает, а мы ему то оленину протухшую, то водки бросим. Но, как говорится, план накрылся.
Примерно год назад, он мост забросил, да давай людей проходящих грабить, да так, что
ничего потом не оставалось! Ну, и подумал я, к чему нам такой работяга, который жрёт всё, что
видит. Деревня у нас небольшая, но денег мы давно уж собирали, 
всё надеялись, что хоть кто-то с ним справится, но он, зараза, всех, кто к нему приходил сожрал! 
Платим 800 оренов. Да, они уже здесь весу не имеют, все ведь на нильфские кроны перешли, 
но в Новиграде-то обменяете на них. По рукам?
''',
        'actions': {'По рукам. Покажите мне, где этот мост. Я посмотрю, что можно сделать.': (34, None)}
    },
    {
        'name': '19',
        'message': '''- Что за беда у вас с троллем? - произнёс Геральт, давая понять, что не желает возиться с
любезностями. - Я ведьмак, нашёл и разгадал объявление на площади.
- Прошу меня извинять, не сразу заметил, что вы ведьмак, а если честно, то
вообще первый раз вживую вижу кого-то, кто вашим ремеслом занимается. - Сказал староста. - Меня Борисом звать.
''',
        'actions': {'Я Геральт из Ривии. Приятно. Ближе к делу.': (17, None)}
    },
    {
        'name': '20',
        'message': '''Геральт знал, что, если староста узнает о том, что тролль ещё жив, то сразу поймёт, в чём
дело.
Ведьмак заметил возле дома старосты пару человек в лёгких доспехах. Шесть человек,
вооруженных топориками и короткими мечами. Кто-то из них пил что-то из стеклянных
бутылок, кто-то о чём-то спорил между собой. Никто внимания на ведьмака особо и не обратил,
зато Геральт обратил.
Он вошёл в хату, староста сидел за столом на скамье, доедая свой суп.
- Мастер ведьмак? В чём дело? Вас не было довольно долго, а головы тролля я с Вами не
наблюдаю чего-то? Возникли проблемы? - насторожился Борис
''',
        'actions': {'Обвинить Бориса в том, что он изначально нанимал людей, чтобы убить двух троллей, но выжил только один. Староста решил намеренно споить того, чтобы получать с него деньги за разграбление прохожих.': (7, 'note')}
    },
    {
        'name': '21',
        'message': '''''',
        'actions': {'Рассказать троллю о записке': (3, None, 'troll_side', 5),
                    'Напасть на тролля.': (9, None)},
    },
    {
        'name': '22',
        'message': '''Геральт постучал в старую деревянную дверь. Но стоит сказать, что сам дом
отличался от других халуп в деревне. Разукрашенные ставни, аккуратно сложенная крыша и
видный дымоход сразу говорили о том, что здесь живёт сравнительно богатый человек. Кроме
того, замечательный высокий забор, сделанный из серого камня, выдавал статус этого
человека. Это вообще для удалённой от большого города деревни - редкость.
Староста вышел на крыльцо своей усадьбы.
- О, добрый путешественник, что привело вас в наши края? - спрашивал староста, пытаясь
быть вежливым.
''',
        'actions': {'-"Что за беда у вас с троллем?"': (18, None),
                    '-"Впервые вижу в Новой Темерии, чтобы был такой контраст между домом старосты и остальными халупами. Вижу, хорошо вы устроились': (13, None, None, 3)},
        'image': 'AgACAgIAAxkBAANEYJqs98842q4U_V5203NNT77-BaMAAtCzMRvr2dFIyQ4yC5Wl3okvXg6kLgADAQADAgADbQADa9sAAh8E',
    },
    {
        'name': '23',
        'message': '''Геральт моментально пустил знак Аард в наёмников. Трое не выдержали ударную войну и
повалились на спины, это был удобный момент, чтобы в кувырке покончить хотя бы с двумя.
Осталось четверо. Того, что лежал, ведьмак спалил знаком Игней. Сил для сотворения знаков
больше не оставалось, да и не нужно было. Отразив удар здоровяка с топором, Геральт кольнул
сзади стоящего прямо в грудь, ударил рукояткой меча здоровяка так, чтобы сломать ему нос, и,
развернувшись, контратаковать удар меча наёмника справа. Того, кому ведьмак сломал нос, оставалось лишь добить.
Вокруг шума уже собралась толпа из жителей деревни, но простой мужик с вилами не
кинется на только что убившего шесть человек ведьмака. Геральт решительным шагом
отправился в хату к старосте...
''',
        'actions': {'Войти в хату к старосте.': (14, None)},
        'image': 'AgACAgIAAxkBAAMfYJmWCrJ1g7PQnJYwG9JYDXXdh0wAAtGzMRvr2dFIDHhFkVCFfztOm1ekLgADAQADAgADbQADwOoAAh8E',
    },
    {
        'name': '24',
        'message': '''Геральт встал в боевую стойку, обнажив меч. Руки крепко сжали рукоять клинка. Тишина.
Около тридцати секунд. Никто не рисковал первым ударить ведьмака, и не зря.
Один смельчак решился нанести удар сзади, но сейчас Геральт уже не терял
концентрацию. Парирование. Резкие удар снизу-вверх, рассекающий бандита от пояса до
мочки уха. Геральт тут же встал обратно в стойку, он прекрасно знал, как нужно драться в
окружении. Тут же последовал топора, Геральт аккуратным движением меча
сломал древко топора, а заодно и срезал голову наёмника.
Тут же ещё два удара, оба парированы, оба бандита уже на земле.
Осталось всего двое, но убегать они не решались. Один попытался обойти ведьмака с
боку, другой, со щитом, ринулся напролом. Геральт, сделав два шага в сторону и нагнувшись,
поделил первого надвое, а в высоком пируэте нанёс удар по всей спине здоровяка со щитом.
Всего шесть ударов - шесть трупов.
Вокруг шума уже собралась толпа из жителей деревни, но простой мужик с вилами не
кинется на только что убившего шесть человек ведьмака. Геральт решительным шагом
отправился в хату к старосте...
''',
        'actions': {'Войти в хату к старосте.': (14, None)},
        'image': 'AgACAgIAAxkBAAMhYJmWG_1L5wbH2p8SIa_JO2YljjEAAtOzMRvr2dFIPmgWOPxSilgORYmiLgADAQADAgADbQADEPsBAAEfBA',
    },
    {
        'name': '25',
        'message': '''Геральт быстро и решительно нанёс удар по шее мерзавца.
Выдохнув, Геральт выходит на улицу.
Деревенщина, понимая, что ведьмак сделал, расходится в страхе. Но в ушах Белого Волка
всё-таки слышны своеобразные выкрики: "убийца", "выродок".
Он слышал это слишком часто.
Ведьмак сел на Плотву и отправился в путь.
Денег он не мог брать. Хоть дело и было выполнено, как сказано в заказе, но убит
работодатель, так что, следуя кодексу ведьмаков, платы у трупа он не имеет права брать.
''',
        'actions': {'Отправиться в путь': (4, None),
                    'Отправиться к троллю.': (28, 'troll_side')}
    },
    {
        'name': '26',
        'message': '''-Я свою работу делать. Я просить монеты, ты мне их отдавать, а если нет, то по башке бум!
Было понятно, что тролль говорит вовсе не о строительстве моста.
''',
        'actions': {'-"Ты должен был достроить мост, не лукавь"': (8, None)}
    },
    {
        'name': '27',
        'message': '''Вернувшись в деревню, Геральт заметил возле дома старосты пару человек в лёгких
доспехах. Шесть человек, вооруженных топориками и короткими мечами. Кто-то из них пил что-то из стеклянных бутылок, кто-то о чём-то спорил между собой. Никто внимания на ведьмака
особо и не обратил.
Зайдя в дом к Борису, Геральт демонстративно кинул голову тролля на стол перед
старостой. Тот даже не шелохнулся, лишь с улыбкой посмотрел в глаза ведьмаку.
- Спасибо за проделанную работу, ведьмак Геральт, вся деревня у тебя в долгу!
''',
        'actions': {'Обвинить Бориса в том, что он изначально нанимал людей, чтобы убить двух троллей, но выжил только один. Староста решил намеренно споить того, чтобы получать с него деньги за разграбление прохожих': (7, 'note', None, 2),
                    'Поблагодарить старосту, взять деньги и уйти восвояси': (16, None),
                    'Шантажировать старосту тем фактом, что знаешь о намеренном спаивании тролля с целью грабежа прохожих людей. Рассказать деревне о том, что все бедства деревни связаны с этим': (7, 'note')},
        'image': 'AgACAgIAAxkBAAMdYJmV8TQ2vjDJoL2BNl-wcr4CgG8AAtCzMRvr2dFIyQ4yC5Wl3okvXg6kLgADAQADAgADbQADa9sAAh8E',
    },
    {
        'name': '28',
        'message': '''-Угу.
Подойдя к доспехам, а вернее, к тому, что от них осталось, Геральт начал лазать
по карманам, чтобы найти хоть что-то. Не из побуждений помародёрствовать, а для
того, чтобы найти что-то важное, за что можно зацепиться. Потому что он чувствовал 
неладное.
Его предчувствие оправдалось. В кармане левой штанины, сшитой из клёпанной кожи, он
обнаружил записку.
"Тому, кто двух троллей убиет под мостом, будет полагаться награда в размере 2000
оренов. По вопросам всяческим - обращаться к старосте Борису".
''',
        'actions': {'Получается, Борис изначально нанимал кого-то, чтобы убить троллей. Видно, не очень у них это получилось. Но зачем староста стал платить троллю за грабёж прохожих, но говорит, что тот должен был достроить мост? Ерунда какая-то': (20, None, 'note')},
        'image': 'AgACAgIAAxkBAAMjYJmWROaJux2OkMU7Fh1Sc9-EEoAAAtWzMRvr2dFIoigMecumkCzElJuiLgADAQADAgADbQADWe0BAAEfBA',
    },
    {
        'name': '29',
        'message': '''Снова пройдя четыре километра от деревни. Геральт вновь спустился к логову тролля,
откуда уже доносился ещё более противный запах мертвечины, видимо, тролль готовил себе
что-то из остатков несчастных, что здесь проходили когда-то.
Увидев Геральта, тролль с большим интересом спросил: "НУ ЧТО, ТЫ СДЕЛАЛ БАМ-БАМ
ТОЙ СКОТИНА?!"
''',
        'actions': {'Да, я отомстил за твою супругу.': (11, None)},
        'image': 'AgACAgIAAxkBAAMZYJmVsFCWl-44EPoZOIayLhjC8KYAAs6zMRvr2dFIrDeS1zU9VbZf91miLgADAQADAgADbQAD4voBAAEfBA',
    },
    {
        'name': '30',
        'message': '''Хорошо поев, Геральт собрался, сложил всё барахло на лошадь, что ждала выше. Тролль
тоже собирался уходить: паковал свой драгоценный котёл, остатки мяса
неизвестного происхождения.
Попрощавшись друг с другом, оба ушли в разные стороны.
Как оказалось, барахло было ценным, Геральт выручил за него неплохие деньги.
Их вполне хватит, чтобы добраться до Новиграда, купить необходимые для эликсиров
недостающие травы, набить желудок, снять маленькую комнату хотя бы на пару дней, отмыться.
Сделать всё это, собраться с мыслями, наконец-то расслабиться. Таков ритм жизни
ведьмака. Постоянный поиск хоть какой-нибудь работы, чтобы выжить, благо, после войны,
различных трупоедов и других бестий на большаке хватает.
Очередной заказ на очередное чудовище обернулся тем, что ведьмак вновь помог миру,
оставив его без большего зла.
''',
        'actions': {},
        'ending': 'Месть свершилась',
        'image': 'AgACAgIAAxkBAAMlYJmWdvBOj_uNNY3XtiSCpJQBj2gAAjO0MRtK9chIaDznDOsNukTH5pCiLgADAQADAgADbQAD1S8CAAEfBA',
    },
    {
        'name': '31',
        'message': '''Лошадь медленно шла по середине дороги, ведущей к большому дому, который являлся,
скорее всего, домом старосты. Некоторые жители с презрением смотрели на проезжающего
мимо ведьмака, но он ловил эти взгляды так часто за свою жизнь, что они никак его не
тревожили. Дети, пробегающие мимо, с удивлением смотрели на ранее невиданного
пришельца с кошачьими глазами и двумя мечами за спиной.
- А зачем ему два меча?! - прошептал один из мальчишек рядом.
- Глупый ты, Олешка! Запасной это! - ответил рядом стоящий паренёк.
Геральт знал, что если тут не будет работы, то он незамедлительно отправится дальше,
чтобы не терять времени.
На небольшой центральной площади, Геральт всё-таки нашёл доску объявлений."
''',
        'actions': {'Рассмотреть доску объявлений.': (1, None)},
    },
    {
        'name': '32',
        'message': '''Тролль зарычал и сразу ринулся на Геральта.
После применения знака Ирден тролля парализовало в кругу из жёлтого энергетического
поля, бьющего током.
Это ненадолго задержало чудовище, но ведьмак не успел сделать смертельный удар, а
лишь ранил его в области живота, в вместе, что хоть как-то не  было покрыто каменной коркой.
Как только тролль пришёл в себя, последовала серия мощных замахов, но Геральту хватило
ловкости увернуться. Таким ударом он спокойно мог бы разорвать пополам корову.
Как только Геральт почувствовал подходящий момент для удара, он применил Аард и
отбросил здоровяка на полметра. Тролль потерял ориентацию, а вместе с ней и руку, а затем и
голову. Работа была сделана.
''',
        'actions': {'Взять трофей и отправиться в деревню.': (26, None, 'troll_dead')},
        'image': 'AgACAgIAAxkBAAMVYJmVRtEM8dnIPUhTYAm3zQiXY3oAAjG0MRtK9chIAx10lrVQ9zcPUQukLgADAQADAgADbQADbuMAAh8E',
    },
    {
        'name': '33',
        'message': '''-Да, как мою жену...убили. Пришли людя в железе. Я спал. Моя начала кричать. Когда я
встал, она двух пришибла, да попало ей сильно. Я остальных сожрал. Одно железо оставил.
Горя мне было много. Да уходить я уже не хотеть. Нашёл водка в сумках. Понравилась. Думать
не даёт. Староста пришёл и сказал, что ещё давать будет, если буду собирать монета. Жена
раньше запрещала говорить с людями, говорила:"Людя жестокий".
Геральт решил осмотреть местность в поисках зацепок, но ведьмачье чутьё начало его подводить.
Перед глазами мелькали лишь наборы цифр.
С трудом удалось собрать всё в цельную картину: 10011101000101011
Д - 100 Е - 101 О - 111 П - 000 С - 01 Х - 011
''',
        'actions': {'-"Если ты не трогал доспехи тех наёмников, можно я их осмотрю?"': (27, None)},
        'answer': {'answ': 'доспех', 'before': 'Отгадайте слово', 'after': 'Вдруг, Геральт заметил недалеко от котла разбросанные железные доспехи, которые почти не заржавели.',
                   'reward': 50}
    },
    {
        'name': '34',
        'message': '''Времени на раздумья особо не было. Тролль уже ринулся на Геральта, чтобы снести и
ошеломить ведьмака. Кожа каменного тролля, как не странно, окаменелая, пробить её мечом,
пусть даже серебряным. Самым верным вариантом, было бы обработать меч специальным
маслом, которое дало бы возможность пробить кожу чудовища, только вот, делают это обычно
заранее…
Достав из кармана на поясе флакон с маслом, Геральту пришлось уворачиваться от
многочисленных попыток тролля размозжить ему голову.
Выбрав наиболее подходящий момент, ведьмак выливает масло на меч так, чтобы
полностью покрыть лезвие, чтобы ускорить процесс реакции, пришлось кинуть меч как
можно ближе к огню, что грел котёл тролля с непонятным содержимым.
Нужно было лишь остаться на ногах, пока пьяный тролль, размахивая руками, пытался
схватить беловолосого убийцу чудовищ.
Сначала аккуратный кувырок прямо из под мощного удара, затем, аккуратный разворот с
целью оставить тролля спиной к себе. Чудовище зарычало с такой громкостью, что по
периметру не осталось ни одной птицы, белки или зайца. Пока тролль орал что-то на матерном
языке, ведьмак приготовился к мощному разбегу тролля. Костёр и меч оставались за спиной
гиганта. Обегать его вокруг - дело бессмысленное. Подпустив тролля как можно ближе,
ведьмак сделал ювелирно точный кувырок за спину. Он схватил меч, и, развернувшись, нанёс
два точно таких же точных удара, отсекая троллю сначала руку, а затем и голову. Меч
прошёл по плоти тролля так мягко, будто его кожа не была покрыта сантиметровым слоем из
камня. Схватка оказалась довольно быстрой, но очень напряженной. Работа была
сделана. Оставалась взять трофей, голову, и отправиться в деревню за наградой от
старосты Бориса...
''',
        'actions': {'Взять трофей и отправиться в деревню за наградой.': (26, None, 'troll_dead')},
        'image': 'AgACAgIAAxkBAAMVYJmVRtEM8dnIPUhTYAm3zQiXY3oAAjG0MRtK9chIAx10lrVQ9zcPUQukLgADAQADAgADbQADbuMAAh8E',
    },
    {
        'name': '35',
        'message': '''Отойдя от деревни километра на четыре, Геральт увидел старый каменный мост,
разрушенный по самой его середине. Мост был украшен старинными барельефами с
изображением эльфийских женщин. Река, что под ним, звалась Ялуткой. Она являлась
притоком реки Понтар, пусть и не большим, чтобы по ней ходили торговые суда, но достаточно
глубокой и широкой, чтобы принести сложности с неё переходом.
Подойдя к началу моста, Геральт вдохнул мерзкий запах трупа. Пахло
серой, гнилью. Не больше минуты царила полная тишина, если бы ведьмак не знал, что где-то
здесь поселился тролль-алкоголик-инженер, то он бы считал, что вокруг нет ни одной живой
души.
Но вдруг, внезапный рык, калечивший уши, который доносился откуда-то снизу, из-под
моста.
''',
        'actions': {'Спуститься по уступам вниз.': (6, None)}
    },
    {
        'name': '36',
        'message': '''Выдвинувшись по намеченному пути, Ведьмак замечает мужчину в тёмном балахоне,
который копошится в зарослях травы. Он не слабо походил на люд, обычно встречавшийся в деревнях.
Мужчина, обернувшись на звук приближающейся лошади, разглядел пепельно-белые волосы ведьмака и, видимо,
сразу понял, кто он такой.
-Эй, путник, не поможешь?\n
Геральт остановился. - Ты это мне?\n
-Тебе, тебе. Мужчина положил травы в сумку. Моё имя - продолжил он - Гаспар. Я алхимик.
Ты, наверное, в эликсирах разбираешься, не этому ли тебя учили в Каэр Морхане?
Так вот, случилось так, что мою лабораторию ограбили,
но я знаю, кто это сделал - мой давний знакомый, Прометиций, посягнул на мои наработки.
Он заплатил какому-то упырю, чтобы тот пробрался в лабораторию пока меня там не было.
Вернёшь мои дневники и зелья - заплачу чеканными. У нас с ним давняя вражда, ещё со времён
учёбы в Оксенфурте, но всё-таки, постарайся ему не навредить, не хочу проблем в профессорском обществе.
Его пристанище в часе езды отсюда вот по этой дороги, но там повсюду руны, которые лишь алхимику под силу разбить.
''',
        'actions': {'-Не, я в алхимии не смыслю [Отправиться в деревню]': (30, None),
                    '-Почему бы и нет, если платят [Помочь учёному]': (36, None, None, 2)}
    },
    {
        'name': '37',
        'message': '''Отлично, тогда ищи меня за тем холмом, когда вернёшься, я там разбил палатку.
Геральт выдвинулся по указанному Гаспаром пути, через час на горизонте показался дом с садом.
Ведьмак слез с лошади и продолжил путь пешком. Подобравшись к дому, он заглянул в окно и увидел мужчину
за письменным столом, сгорбившегося над листом бумаги, это, по-видимому, и был Прометиций. 
В доме явно не было место для склада зелий, да и рун Геральт не чувствовал поблизости. 
''',
        'actions': {'Обойти дом': (37, None)}
    },
    {
        'name': '38',
        'message': '''Обойдя дом, Ведьмак увидел ещё одно строение похожее на амбар. 
Тут ты добро спрятал? - Подумал он.
Геральт подошёл к дверям амбара и обнаружил, что на них лежит руна, не дающая проходу.\n
Руна гласила: C3H4 + O2 → CO2 + H2O\n
Чёртова алхимия, может просто припугнуть Прометиция... - Подумал он.
''',
        'actions': {'Попытаться разгадать руну': (38, None),
                    'Угрожать Прометицию': (41, None, None, -7)}
    },
    {
        'name': '39',
        'message': '''Руна гласила: C3H4 + O2 → CO2 + H2O
Уравняйте химическую реакцию и введите сумму всех коэффициентов в правой части реакции.
Бестиарий вам в помощь:
https://ru.wikihow.com/%D0%B1%D0%B0%D0%BB%D0%B0%D0%BD%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D1%85%D0%B8%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5-%D1%83%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F
''',
        'actions': {'Войти внутрь': (39, None)},
        'answer': {'answ': 5, 'before': 'Сбалансируйте уравнение', 'after': 'Отлично, двери открылись',
                   'reward': 70}
    },
    {
        'name': '40',
        'message': '''Внутри выло множество стеллажей с книгами, травами и зельями, но Геральта они не интересовали.
Применив ведьмачье чутьё, он нашёл мешок, из которого доносился запах похожий на тот, что шёл от Гаспара. 
Внутри и правда были дневники и зелья.
''',
        'actions': {'Взять мешок и вернуться к Гаспару': (40, None)},
        'image': 'AgACAgIAAxkBAANwYJrfZRLuNdN8oCU73DL5chKili8AAj-0MRuttthIhU56AqRPJifYDQifLgADAQADAgADbQADzyECAAEfBA',
    },
    {
        'name': '41',
        'message': '''Геральт прибыл на место встречи, застав Гаспара сидящим у костра
и раскладывающим недавно собранные травы просушиться.
- Заказ выполнен. - С этими славами Геральт слез с лошади и поставил на землю мешок.\n
- Отлично мой друг. - С довольством сказал Гаспар и передал Ведьмаку мешок монет.
''',
        'actions': {'Взять деньги и отправиться в деревню': (30, None)},
        'reward': 50,
    },
    {
        'name': '42',
        'message': '''Ведьмак ворвался в дом к Прометицию. Тот вскочил от неожиданности.
-Тебя Гаспар прислал?!\n
-Не играет роли! - Геральт накинулся на учёного и прижал его к стене.\n
Прометиций пытался сопротивляться, но был слишком слаб, чтобы вырваться из хватки
белого волка.
-Отвечай, в амбаре спрятал его барахло? - Геральт замахнулся, готовясь нанести удар.\n
-Д-да - заикаясь, ответил Прометиций.\n
-Ну тогда сними руну!\n
Геральт взял за шкирку алхимика и вывел к амбару. Тот снял руну и открыл двери.
''',
        'actions': {'Войти внутрь': (39, None)}
    },
]