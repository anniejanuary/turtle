#grafika żółwia

import turtle

z=turtle.Turtle() #biblioteka.polecenie_Turtle #z, żeby nie pisać turtle.Turtle za każdym razem
z.shape('turtle') #polecenie .shape wyświetla grafikę 'turtle' z biblioteki

z.forward(100) #idz do przodu 100 kroków
z.right(90) #obroc się w prawo o 90st
z.forward(100)
z.right(90)
z.forward(100)
z.right(90)
z.forward(100)
z.right(90)
z.goto(-100,100) #idz 100 kroków na zachód i 100 na północ - układ współrzędy z 0,0 na środku
z.circle(100) # rysuj okrąg o promieniu 100

z.exitonclick() #zamyka grafikę przy kliknięciu iXem
