# Tinkoff introductory
В этом репозитории представлен генератор текста на основе gensim word2vec. <br/>
Вы можете обучить модель, используя:
```
python train.py --inputdir ./data/ --model w2v_model
```

Аргументы:
+ **--inputdir** Путь до дириктории с текстами, на которых будет обучаться модель. Default - ***./data/*** 
+ **--model** Название с которым сохраняется модель word2vec. Default - ***w2v_model***
<br/>
В папке может быть несколько текстов, при обучении они будут использоваться все.

---

Для генерации текста используйте:
```
python generate.py --model w2v_model --length 7 --prefix "мама"
```

Аргументы:
+ **--model** Название сохранённой модели word2vec. Default - ***w2v_model***
+ **--length** Колличество слов, которые будут сгенерированы. Default - ***7***
+ **--prefix** Начало предложения (одно или несколько слов).
  
При использовании нескольких слов, их необходимо обернуть в **""** или **''**

---

Автор обучал модель на текстах Ивана Алексеевича Бунина. Пример работы модели:
```
    python generate.py --length 9 --prefix "когда я"

    Output: когда я приказал коридорному отворить окна обрадовавшись возможности скрыть свое смущение
```
```
    python generate.py --length 9 --prefix мама

    Output: мама умерла давно я только нынешней весной кончила гимназию тут
```

---

Feel free to contact with me, if you have any questions: [vk click here](https://vk.com/otec_feodor) or Telegram - @Fedor_Lomakin

