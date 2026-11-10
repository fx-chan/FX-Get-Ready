"""Interface languages. Slovak is the source language: a UI string is its own key.

Content has its own translations next to the Slovak files (theory.uk.md, description.uk.md,
strings.uk.json; see content.py).
"""
from flask import g, has_request_context, request

LANGS = {"sk": "Slovenčina", "uk": "Українська"}
DEFAULT = "sk"
COOKIE = "lang"

UK = {
    # layout
    "Príprava": "Підготовка",
    "písomky · skúšky": "контрольні · іспити",
    "Svetlý / tmavý režim": "Світла / темна тема",
    "Prepnúť tému": "Перемкнути тему",
    "Jazyk": "Мова",
    "Odhlásiť": "Вийти",
    "Prihlásiť": "Увійти",
    "Registrácia": "Реєстрація",
    "príprava na písomky a skúšky": "підготовка до контрольних та іспитів",
    # index
    "Príprava na písomky a skúšky": "Підготовка до контрольних та іспитів",
    "Priprav sa": "Готуйся",
    "krok za krokom": "крок за кроком",
    "Teória s interaktívnymi otázkami, mini úlohy priamo v lekcii a úlohy z cvičení a domácich úloh s automatickou kontrolou.":
        "Теорія з інтерактивними запитаннями, міні-завдання прямо в уроці та задачі з практичних і домашніх робіт з автоматичною перевіркою.",
    "Vytvoriť účet": "Створити акаунт",
    "Na kontrolu riešení je potrebné prihlásenie.": "Щоб перевіряти розв'язки, потрібно увійти.",
    "Predmety": "Предмети",
    "blokov": "блоків",
    "úloh": "задач",
    "Zatiaľ žiadne predmety.": "Поки що немає предметів.",
    # subject / block
    "mini úloh": "міні-завдань",
    "Otázka": "Запитання",
    "Mini úloha": "Міні-завдання",
    "Vyriešené": "Розв'язано",
    "A++ — úlohy vyššej úrovne": "A++ — задачі підвищеної складності",
    "Úlohy označené v domácej úlohe ako": "Задачі, позначені в домашньому завданні як",
    "dôkazy, konštrukcie a analýza všetkých prípadov.": "доведення, побудови та аналіз усіх випадків.",
    "Úlohy": "Задачі",
    "hotovo": "виконано",
    "vyššia úroveň": "підвищений рівень",
    "Mini úlohy v lekcii": "Міні-завдання в уроці",
    # task pages
    "časť": "частина",
    "časti": "частини",
    "Na spustenie a odoslanie kódu sa": "Щоб запускати й надсилати код,",
    "Na kontrolu odpovedí sa": "Щоб перевіряти відповіді,",
    "prihláste": "увійдіть",
    "Ďalšia úloha": "Наступна задача",
    # code widget
    "Vrátiť šablónu": "Повернути шаблон",
    "Šablóna": "Шаблон",
    "Spustiť": "Запустити",
    "Odoslať": "Надіслати",
    "Skontrolovať": "Перевірити",
    "Vlastný vstup (stdin)": "Власний ввід (stdin)",
    "napr. 10 8": "напр. 10 8",
    # answer widget
    "napr. -7/2, sqrt(2)/2, 3a+1": "напр. -7/2, sqrt(2)/2, 3a+1",
    "napr. 3x2": "напр. 3x2",
    "napr. 1, -3": "напр. 1, -3",
    "napr. 2, 2, 5": "напр. 2, 2, 5",
    "napr. 1+2t, t, 3   (parametre t, s, u)": "напр. 1+2t, t, 3   (параметри t, s, u)",
    "jeden vektor na riadok, napr.\n1, 0, 2": "один вектор у рядку, напр.\n1, 0, 2",
    "matica P (stĺpce = vlastné vektory)\n1 1\n1 -1": "матриця P (стовпці = власні вектори)\n1 1\n1 -1",
    "E1\n\nE2   (matice oddeľte prázdnym riadkom)": "E1\n\nE2   (матриці розділяйте порожнім рядком)",
    "matica C, napr.\n1 0 0\n0 1 0\n0 0 1": "матриця C, напр.\n1 0 0\n0 1 0\n0 0 1",
    "matica A\n\nmatica B   (oddeľte prázdnym riadkom)": "матриця A\n\nматриця B   (розділяйте порожнім рядком)",
    "postupnosť vrcholov, napr. A B C A": "послідовність вершин, напр. A B C A",
    "zoznam hrán, napr. AB, BC, CC (slučka)": "список ребер, напр. AB, BC, CC (петля)",
    "Označte všetky platné možnosti.": "Позначте всі правильні варіанти.",
    "Premenné": "Змінні",
    "Ako zapisovať odpovede?": "Як записувати відповіді?",
    "Zlomky a odmocniny:": "Дроби та корені:",
    "alebo": "або",
    "mocnina": "степінь",
    "komplexná jednotka": "уявна одиниця",
    "Matica: riadky na samostatné riadky (alebo oddelené": "Матриця: кожен рядок з нового рядка (або через",
    "), prvky medzerou alebo čiarkou.": "), елементи через пробіл або кому.",
    "Vektor:": "Вектор:",
    "Nekonečne veľa riešení: parametre": "Нескінченно багато розв'язків: параметри",
    "napr.": "напр.",
    "Desatinné čísla stačia na 2–3 miesta, presný tvar je vždy správny.":
        "Десяткових дробів досить із 2–3 знаками, точний вигляд завжди правильний.",
    "nedá sa vypočítať": "неможливо обчислити",
    "žiadna hodnota": "немає таких значень",
    "systém nemá riešenie": "система не має розв'язків",
    "nie je diagonalizovateľná": "не діагоналізовна",
    "taký ťah neexistuje": "такого ланцюга не існує",
    "taký graf neexistuje": "такого графа не існує",
    # auth
    "Prihlásenie": "Вхід",
    "Stačí meno a heslo, žiadny e-mail.": "Досить імені та пароля, без електронної пошти.",
    "Vitaj späť!": "З поверненням!",
    "Meno": "Ім'я",
    "Heslo": "Пароль",
    "Heslo znova": "Пароль ще раз",
    "Prihlásiť sa": "Увійти",
    "Máte účet?": "Маєте акаунт?",
    "Prihláste sa": "Увійдіть",
    "Nemáte účet?": "Немає акаунта?",
    "Stránka neexistuje.": "Сторінку не знайдено.",
    "Prihláste sa, prosím.": "Будь ласка, увійдіть.",
    "Meno: 3–32 znakov (písmená, čísla, _ . -).": "Ім'я: 3–32 символи (літери, цифри, _ . -).",
    "Heslo musí mať aspoň {n} znakov.": "Пароль має містити щонайменше {n} символів.",
    "Heslá sa nezhodujú.": "Паролі не збігаються.",
    "Toto meno je obsadené.": "Це ім'я вже зайняте.",
    "Nesprávne meno alebo heslo.": "Неправильне ім'я або пароль.",
    # API errors
    "Chýba zdrojový kód.": "Немає вихідного коду.",
    "Chýbajú odpovede.": "Немає відповідей.",
    "Príliš veľa spustení, počkajte minútu.": "Забагато запусків, зачекайте хвилину.",
    "Kompilátor je preťažený, skúste o chvíľu.": "Компілятор перевантажено, спробуйте за хвилину.",
    # answers.js / ide.js
    "Accepted — Správne": "Accepted — Правильно",
    "Wrong Answer — Nesprávny výstup": "Wrong Answer — Неправильний вивід",
    "Compilation Error — Chyba kompilácie": "Compilation Error — Помилка компіляції",
    "Time Limit — Prekročený čas": "Time Limit — Перевищено час",
    "Runtime Error — Chyba za behu": "Runtime Error — Помилка виконання",
    "Internal Error — Skúste neskôr": "Internal Error — Спробуйте пізніше",
    "(prázdne)": "(порожньо)",
    "Na spúšťanie kódu sa prihláste.": "Щоб запускати код, увійдіть.",
    "Prebieha…": "Виконується…",
    "Vrátiť pôvodnú šablónu?": "Повернути початковий шаблон?",
    "Program skončil": "Програма завершилась",
    "Kompilátor": "Компілятор",
    "Test": "Тест",
    "Verdikt": "Вердикт",
    "Čas": "Час",
    "Vstup": "Ввід",
    "Očakávané": "Очікувалось",
    "Váš výstup": "Ваш вивід",
    "Ďalšie testy sa nespúšťali.": "Інші тести не запускалися.",
    "Na kontrolu odpovedí sa prihláste.": "Щоб перевіряти відповіді, увійдіть.",
    "Kontrolujem…": "Перевіряю…",
    "Všetko správne!": "Усе правильно!",
    "Správne {a} z {b}. Opravte červené časti.": "Правильно {a} з {b}. Виправте червоні частини.",
    # exam
    "minút": "хвилин",
    "odpovede sa vyhodnotia až po odovzdaní": "відповіді перевіряються лише після здачі",
    "Otvoriť písomku": "Відкрити контрольну",
    "Odovzdať písomku": "Здати контрольну",
    "Naozaj odovzdať písomku?": "Справді здати контрольну?",
    "Spustiť písomku? Čas sa začne odpočítavať a nedá sa zastaviť.": "Почати контрольну? Час почне спливати, і зупинити його не можна.",
    "Písomka nebeží.": "Контрольна не триває.",
    "Písomka": "Контрольна",
    "Pravidlá": "Правила",
    "Na písomku máte {n} minút. Čas beží na serveri, obnovenie stránky ho nezastaví.":
        "На контрольну маєте {n} хвилин. Час рахує сервер, оновлення сторінки його не зупиняє.",
    "Zadanie uvidíte až po spustení.": "Умову побачите лише після старту.",
    "Výsledky ani správne odpovede sa počas písomky nezobrazujú.": "Результати й правильні відповіді під час контрольної не показуються.",
    "Keď čas vyprší, písomka sa odovzdá automaticky.": "Коли час вийде, контрольна здасться автоматично.",
    "Pripravte si papier a pero, kalkulačka nie je potrebná.": "Приготуйте папір і ручку, калькулятор не потрібен.",
    "Spustiť písomku": "Почати контрольну",
    "Na písomku sa": "Щоб писати контрольну,",
    "Výsledok": "Результат",
    "bodov": "балів",
    "Čas riešenia": "Час розв'язання",
    "min": "хв",
    "Odovzdané po čase, body berte s rezervou.": "Здано після завершення часу, бали орієнтовні.",
    "Príklad": "Приклад",
    "správne": "правильно",
    "Vaša odpoveď": "Ваша відповідь",
    "bez odpovede": "без відповіді",
    "Riešenie krok za krokom": "Розв'язання крок за кроком",
    "Skúsiť znova": "Спробувати знову",
    "Zostáva": "Залишилось",
    # mathcheck
    "Nerozumiem zápisu: {detail}.": "Не розумію запис: {detail}.",
    "Nerozumiem zápisu.": "Не розумію запис.",
    "prázdny výraz": "порожній вираз",
    "neúplný výraz": "неповний вираз",
    "nečakaný koniec výrazu": "неочікуваний кінець виразу",
    "chýba „{x}“": "бракує «{x}»",
    "neznámy symbol „{x}“": "невідомий символ «{x}»",
    "neznámy znak „{x}“": "невідомий знак «{x}»",
    "prázdny prvok": "порожній елемент",
    "prázdna odpoveď": "порожня відповідь",
    "riadky majú rôzny počet prvkov": "рядки мають різну кількість елементів",
    "očakáva sa vektor (jeden riadok alebo stĺpec)": "очікується вектор (один рядок або стовпець)",
    "chýba odpoveď": "немає відповіді",
    "príliš dlhá odpoveď": "задовга відповідь",
    "zapíšte rozmer v tvare 3x2": "запишіть розмір у вигляді 3x2",
    "neznámy vrchol „{x}“": "невідома вершина «{x}»",
    "zapíšte postupnosť vrcholov, napr. A B C A": "запишіть послідовність вершин, напр. A B C A",
    "hrana „{x}“ nemá dva konce": "ребро «{x}» не має двох кінців",
    # boolcheck (PPI)
    "Funkcia je správna, ale výraz nie je v tvare DNF (súčet súčinov).":
        "Функція правильна, але вираз не у формі DNF (сума добутків).",
    "Funkcia je správna, ale výraz nie je v tvare KNF (súčin súčtov).":
        "Функція правильна, але вираз не у формі KNF (добуток сум).",
    "Funkcia je správna, ale v UDNF musí byť každý súčin úplný (všetky premenné) a žiadny dvakrát.":
        "Функція правильна, але в UDNF кожен добуток має містити всі змінні й не повторюватися.",
    "Funkcia je správna, ale v UKNF musí byť každý súčet úplný (všetky premenné) a žiadny dvakrát.":
        "Функція правильна, але в UKNF кожна сума має містити всі змінні й не повторюватися.",
    "Funkcia je správna, ale použite iba členy NAND (↑) a premenné s negáciou alebo bez nej.":
        "Функція правильна, але використовуйте лише елементи NAND (↑) і змінні із запереченням або без нього.",
    "Funkcia je správna, ale použite iba členy NOR (↓) a premenné s negáciou alebo bez nej.":
        "Функція правильна, але використовуйте лише елементи NOR (↓) і змінні із запереченням або без нього.",
    "Funkcia je správna, ale dve susedné jednotky nepokrýva spoločný súčin (hazard).":
        "Функція правильна, але дві сусідні одиниці не покриває спільний добуток (газард).",
    "Funkcia je správna, ale dá sa zapísať s menším počtom členov ({n}).":
        "Функція правильна, але її можна записати з меншою кількістю членів ({n}).",
    "Funkcia je správna, ale výraz nie je minimálny (minimálny tvar má {n} písmen).":
        "Функція правильна, але вираз не мінімальний (мінімальна форма має {n} літер).",
    "Počet bitov má byť {n}.": "Кількість бітів має бути {n}.",
    "zapíšte iba 0 a 1": "пишіть лише 0 і 1",
    "neznáma premenná „{x}“": "невідома змінна «{x}»",
    "nadbytočný znak „{x}“": "зайвий знак «{x}»",
    "nečakaný znak „{x}“": "неочікуваний знак «{x}»",
    "chýba zatváracia zátvorka": "бракує закривальної дужки",
    "výraz je neúplný": "вираз неповний",
    "pri kombinácii {op} s inými operátormi použite zátvorky": "поєднуючи {op} з іншими операторами, ставте дужки",
    "neznáma inštrukcia „{x}“": "невідома інструкція «{x}»",
    "adresa musí byť 0 až 3: „{x}“": "адреса має бути від 0 до 3: «{x}»",
    "prázdny program": "порожня програма",
    "pamäť programu má len 4 slová": "пам'ять програми має лише 4 слова",
    "napr. a'b + c": "напр. a'b + c",
    "napr. 0110": "напр. 0110",
    "jedna inštrukcia na riadok, napr.\nLDA 0\nADD 1": "одна інструкція на рядок, напр.\nLDA 0\nADD 1",
    "Logický výraz: negácia": "Логічний вираз: заперечення",
    "súčin": "добуток",
    "súčet": "сума",
    "zátvorky": "дужки",
    "Bity píšte za sebou, medzery sa ignorujú:": "Біти пишіть підряд, пробіли ігноруються:",
    "Program: jedna inštrukcia na riadok,": "Програма: одна інструкція на рядок,",
    "alebo binárne": "або двійково",
}
CATALOG = {"uk": UK}


def current():
    return getattr(g, "lang", DEFAULT) if has_request_context() else DEFAULT


def pick_language():
    code = request.cookies.get(COOKIE)
    if code in LANGS:
        return code
    return request.accept_languages.best_match(list(LANGS), DEFAULT)


def t(text, lang=None, **args):
    """Translate a Slovak UI string; {name} placeholders are filled from args."""
    out = CATALOG.get(lang or current(), {}).get(text, text)
    return out.format(**args) if args else out


def js_strings():
    return CATALOG.get(current(), {})
