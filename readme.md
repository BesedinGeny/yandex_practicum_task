<H1>Тестовое задание для компании "Яндекс Практикум"</H1>

<H2>Алгоритм решения</H2>
1) Получить синтаксическое дерево по заданному документу
2) Запустить проверку на правило "Вне класса" от всего модуля
3) 
   1) Если найден класс - запустить проверку имен "Внутри класса". Далее все проверки внутри 
      класса будут исключительно по правилу "Внутри класса"
   2) Если найден любой scope-образующий элемент - запустить проверку имен "Вне класса" от 
      текущего уровня
4) Проверить, если хотя бы одно имя не подходит по текущему правилу - завершить проверку с 
   результатом False
5) Если нигде не возникло False - вернуть True
   