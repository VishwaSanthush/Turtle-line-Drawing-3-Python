import turtle as t
t.tracer(200)
t.setup(1537,865)
t.bgcolor('black')
t.width(10)
color=('red','blue')
for i in range(2000):
   t.fillcolor(color[i%2])
   t.begin_fill()
   t.fd(i)
   t.rt(100)
   t.fd(i)
   t.circle(i,90)
   t.fd(i)
   t.rt(20)
   t.setpos(0,0)
   t.fd(i)
   t.end_fill()
   t.circle(i,200)
   t.fd(i)
   t.rt(300)
   t.fd(i)
   t.rt(210)
