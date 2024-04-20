# AI OPTIMIZATION

![App Screenshot](https://lh7-us.googleusercontent.com/N6_0mVLOh1Jn__JuSDTUjH8-Py_2GuMvibpFWJiiy6d2DZvtkEHIMoY-FOkP5alIKKW3sQpWxy9hTuppg2w9BAyJKDpNxzI-nkaPuDMStUbOyMRLshRMslgTZxLs4VbPEp8KtnrDj9YM-7VT8xl9uWXJ=w1200-h630-p-k-no-nu)
Тут будуть розміщені розглянуті нами (не)оптимізовані проблеми.

## Ceasar encode\decode

Це доволі проста та відома проблема, тому припускалося, що геміні швидко знайде їй рішення. Так і майже сталося. При оптимізації ШІ в першу чергу змінив докстрінги. Там він додав аргументи та результат, які приймає та відповідно повертає функція. Також він одразу додумався, що для декодингу можна використовувати енкод з від'ємним шифтом.
Наступною важливою зміною стало те, що після кількох скеровуючих запитів, щодо умови задачі ШІ майже правильно розглянув еджкейст для вхідних даних.

```
if not all(isinstance(x, (str, int)) for x in (message, key)):
    return None
```

ШІ прекрасно ігнорував УСІ запити на виправлення цього моменту, навіть прямі, тож було прийнято рішення просто сказати йому, щоб він це розділив, що він врешті-решт зробив. Після цієї зміни код пройшов усі тесткейси.

Зміни, які вніс ШІ в алгоритм полягали у узагальненні завдання для будь-яких літер використовуючи одну змінну base для задання в майбутньому правильних рамок. Далі алгоритм ідейно співпадає.

При перевірці двох алгоритмів за виконанням одного спеціального випадку мільйон разів, а потім обчисленні середніх результатів, ми отримали таке:

#### Old version:

Average Compilation Time over `1000000` repetitions: `0.0001` seconds

Average Memory Usage over `1000000` repetitions: `54.0257 MiB`

#### New version:

Average Compilation Time over `1000000` repetitions: `0.0001` seconds

Average Memory Usage over `1000000` repetitions: `55.8065 MiB`

#### Average results:

`Version №2` is `1.712816548347473e-05` faster.

`Version №1` is `1.7808238085937518` more memory efficient.

### Висновок:

ШІ вдалося злегка оптимізувати код в плані швидкості, адже навіть після кількох повторних тестувань, в середньому він трішки швидший. В той же час стара версія ефективніше використовує пам'ять. Також покращилась читабельність коду, а як ми всі добре знаємо, `readability counts`.

## Acronym

Тут ШІ перевершив усі навіть найсміливіши припущення. Він вирішив, що йому не треба нічого робити самому, тому він фактично стягнув код з чужого репозиторію.

[РЕПОЗИТОРІЙ](https://github.com/OlehPalka/First_semester_labs)

Оскільки код пройшов усі тесткейси та був згенерований для нас самим ШІ, то було прийнято рішення його залишити. Тим паче, що ШІ сказав `"...but the modified version is generally better suited for creating acronyms..."`.
Наводжу результати тестування (знову таки ж средні на мільйон):

#### Old version:

Average Compilation Time over `1000000` repetitions: `0.0000` seconds

Average Memory Usage over `1000000` repetitions: `56.0761 MiB`

#### New version:

Average Compilation Time over `1000000` repetitions: `0.0000` seconds

Average Memory Usage over `1000000` repetitions: `53.9083 MiB`

#### Average results:

`Version №1` is `7.040505409240726e-07` faster.

`Version №2` is `2.167764343750001` more memory efficient.

### Висновок:

ШІ вдалося злегка оптимізувати код в плані використання пам'яті, навіть таким унікальним способом, та швидкість виконання все ще краща у першого варіанту, в середньому він трішки швидший. Також злегка покращилась читабельність коду.
Загалом найважливішим висновком є те, що якщо ви не хочете, щоб ваш код використовуваа ШІ, робіть репозиторії приватними.

## Puzzle

Для першого промту я використав повну інформацію про задачу та скинув працюючий, але не оптимізований код, для кращої роботи ШІ я пояснив які кроки в оптимізації йому слід розглянути: використання пам'яті, час роботи коду та щоб він переписав код по усім стандартам pep8.

#### Old version:

Average Compilation Time over `1000000` repetitions: `0.000099` seconds

Average Memory Usage over `1000000` repetitions: `13.906250 MiB`

#### New version:

Average Compilation Time over `1000000` repetitions: `0.000020` seconds

Average Memory Usage over `1000000` repetitions: `13.906250 MiB`

#### Average results:

`New version` is in `5` times faster.

Memmory usage is `equal`.

### Висновок:

ШІ легко впорався з першого промту з оптимізацією, подальші промти не змінювали результат в продуктивності коду, також добре написав згідно з pep-8.
Нажаль ШІ не впорався з покращенням використання пам'яті, це може бути пов'язано з простотою завдання, тому певних покращень ШІ не зміг знайти.
Для вдалого промту було надано повну інформацію для задачі та пояснено, що саме потрібно виправити, та що покращувати.

## Alphabet

При першій спробі оптимізувати код ШІ повернув код, який виглядає оптимізованим (використовується лише один цикл, використовується бібліотека math і код відповідає стандартам pep8), але не працює.
Після надання ШІ прикладу як має працювати програма, він впорався з завданнями. Також ШІ додав приклад роботи програми і опис до неї.

#### Old version:

Average Compilation Time over `500` repetitions: `0.0014` seconds

Average Memory Usage over `500` repetitions: `21.1587` MiB

#### New version:

Average Compilation Time over `500` repetitions: `0.0014` seconds

Average Memory Usage over `500` repetitions: `21.1684` MiB

#### Average results:

Version №2 is `2.869224548339845e-05` faster.

Version №1 is `0.009703124999997925 more` memory efficient.

### Висновок:

З першого разу ШІ не впорався з завданням. Саме завдання невелике і думаю, генеруючи код без оптимізації старого, ШІ міг би справитись краще. На роботу ШІ сильно вплило формулювання завдання, код значно змінив свою структуру, Ші сворив код дуже похожий до початкового і покращив його. Вузькими місцями для ШІ стали вивід тексту і використання циклів, тому він використав ітератор і метод join для тексту. З вимогами pep8 ШІ справився прекрасно, він додав опис, забрав зайві пробіли, і відредагував решту коду.

## Search and sort

При першій спробі оптимізувати код ШІ написав усі алгоритми правильно, крім quick sort. Вказавши після цього декілька раз на помилку, ШІ не міг її виправити доки я не продемонстрував тесткейс на якому падає алгоритм. Після цього ШІ виправив код та він пройшов усі тести на CMS. Тестувалися такі функції, як linear_search, binary_search, selection_sort, merge_sort, quick_sort. Для функції merge_sort написав допоміжну функцію, що зробило імлементацію самого алгоритму значно наглядніше.

### Binary search

#### Old version:

Average Compilation Time over `100000` repetitions: `0.0000` seconds

Average Memory Usage over `100000` repetitions: `25.1579` MiB

#### New version:

Average Compilation Time over `100000` repetitions: `0.0000` seconds

Average Memory Usage over `100000` repetitions: `25.6046` MiB

#### Average results:

Version №2 is `6.029605865478513e-08` faster.

Version №1 is `0.4467392968750019` more memory efficient.

### Linear search

#### Old version:

Average Compilation Time over `100000` repetitions: `0.0000` seconds

Average Memory Usage over `100000` repetitions: `25.9546` MiB

#### New version:

Average Compilation Time over `100000` repetitions: `0.0000` seconds

Average Memory Usage over `100000` repetitions: `26.5944` MiB

#### Average results:

Version №2 is `1.215696334838864e-08` faster.

Version №1 is `0.6398032812499999` more memory efficient.

### Selection sort

#### Old version:

Average Compilation Time over `100000` repetitions: `0.0000` seconds

Average Memory Usage over `100000` repetitions: `27.4911` MiB

#### New version:

Average Compilation Time over `100000` repetitions: `0.0000` seconds

Average Memory Usage over `100000` repetitions: `28.4583` MiB

#### Average results:

Version №1 is `1.9419193267822263e-07` faster.

Version №1 is `0.9671920312500006` more memory efficient.

### Merge sort

#### Old version:

Average Compilation Time over `100000` repetitions: `0.0000` seconds

Average Memory Usage over `100000` repetitions: `28.5199` MiB

#### New version:

Average Compilation Time over `100000` repetitions: `0.0000` seconds

Average Memory Usage over `100000` repetitions: `28.5195` MiB

#### Average results:

Version №2 is `1.7001628875732418e-08` faster.

Version №2 is `0.0004178125000002808` more memory efficient.

### Quick sort

#### Old version:

Average Compilation Time over `100000` repetitions: `0.0000` seconds

Average Memory Usage over `100000` repetitions: `28.4947` MiB

#### New version:

Average Compilation Time over `100000` repetitions: `0.0000` seconds

Average Memory Usage over `100000` repetitions: `28.4918` MiB

#### Average results:

Version №1 is `1.7163753509521484e-08` faster.

Version №2 is `0.0028944140625029036` more memory efficient.

### Висновок:

Як можемо побачити, майже для всіх вищезгаданих функцій ШІ зміг розробити оптимізовану версію, яка працює швидше. Для selection sort алгоритм, на жаль, не зміг зробити ні швидшу, ні легшу версію коду. Важливо зазначити, що дані алгоритми є основою всіх алгоритмів сортування. Чому ШІ не зміг оптимізувати одні з найвідоміший алгоритмів - загадка.
