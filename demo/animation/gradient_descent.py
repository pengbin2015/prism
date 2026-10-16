"""A 180-second original geometric explanation of gradient descent.
Render from this directory: .venv/bin/manim -qh gradient_descent.py GradientDescent
"""
from manim import *
import numpy as np

config.background_color = '#101820'
BG='#101820'; INK='#F3EEE3'; MUTED='#A9B9C3'; BLUE='#60C9F1'; GOLD='#FFB86B'; GREEN='#9ADDB4'; RED='#F98080'

def text(s,size=26,color=INK):
    return Text(s,font='Avenir',font_size=size,color=color)
def math(s,size=36,color=INK):
    return MathTypst(s,font_size=size,color=color)

class GradientDescent(Scene):
    def at(self,t):
        if self.time > t+.04: raise ValueError(f'Timeline overrun: {self.time:.3f} > {t}')
        if t-self.time>.001: self.wait(t-self.time)
    def header(self,n,title):
        new=VGroup(text(f'PRISM  /  {n:02}   GRADIENT DESCENT',15,GREEN).move_to([-3.7,3.55,0]),text(title,34).move_to([0,2.9,0]))
        if hasattr(self,'heading'): self.play(ReplacementTransform(self.heading,new),run_time=.6)
        else: self.play(FadeIn(new),run_time=.8)
        self.heading=new
    def caption(self,s):
        new=text(s,22,MUTED).move_to([0,-3.45,0])
        if new.width>12.8: new.scale_to_fit_width(12.8)
        if hasattr(self,'cap'): self.play(ReplacementTransform(self.cap,new),run_time=.5)
        else: self.play(FadeIn(new),run_time=.5)
        self.cap=new
    def label_ticks(self,ax):
        # Text labels keep rendering independent of LaTeX.
        return VGroup(*[text(str(x),17,MUTED).next_to(ax.c2p(x,0),DOWN,buff=.13) for x in [-1,1,3,5,7]],
                      *[text(str(y),16,MUTED).next_to(ax.c2p(-2,y),LEFT,buff=.13) for y in [0,8,16,24]])
    def construct(self):
        self.header(1,'How does a model find better parameters?')
        self.caption('One adjustable number. One rule for improving it.')
        parameter=math('w',64,BLUE).move_to([-4,0.8,0])
        model=RoundedRectangle(width=3,height=1.35,corner_radius=.14,color=MUTED).move_to([0,.8,0])
        model_label=text('MODEL',28).move_to(model)
        loss=math('L(w)',55,GOLD).move_to([4,.8,0])
        a1=Arrow([-3,.8,0],[-1.65,.8,0],color=BLUE,buff=.12)
        a2=Arrow([1.65,.8,0],[2.9,.8,0],color=GOLD,buff=.12)
        self.at(2);self.play(FadeIn(parameter),Create(model),FadeIn(model_label),run_time=1.5)
        self.at(5);self.play(GrowArrow(a1),GrowArrow(a2),FadeIn(loss),run_time=1.5)
        paramlabel=text('parameter',22,BLUE).next_to(parameter,DOWN,buff=.35)
        losslabel=text('prediction error',22,GOLD).next_to(loss,DOWN,buff=.35)
        self.play(FadeIn(paramlabel),FadeIn(losslabel),run_time=1)
        self.at(11);self.play(Indicate(parameter,color=BLUE),run_time=1)
        self.at(14);self.play(FadeOut(VGroup(parameter,model,model_label,loss,a1,a2,paramlabel,losslabel)),run_time=1)
        ax=Axes(x_range=[-2,8,1],y_range=[0,25,8],x_length=8.2,y_length=4.4,tips=False,axis_config={'color':'#536D7C','include_ticks':False}).move_to([-1.65,-.3,0])
        ticks=self.label_ticks(ax)
        xl=text('parameter w',20,BLUE).next_to(ax.x_axis,DOWN,buff=.55)
        yl=text('loss',20,GOLD).next_to(ax.y_axis,UP,buff=.18)
        self.play(Create(ax),FadeIn(ticks),FadeIn(xl),FadeIn(yl),run_time=1.5)
        points=VGroup(*[Dot(ax.c2p(x,(x-3)**2),radius=.055,color=GOLD) for x in np.linspace(-1.5,7.5,13)])
        self.at(18);self.play(LaggedStart(*[FadeIn(p,shift=UP*.15) for p in points],lag_ratio=.08),run_time=2)
        curve=ax.plot(lambda x:(x-3)**2,x_range=[-1.8,7.8],color=BLUE,stroke_width=3)
        self.at(21);self.play(Create(curve),points.animate.set_opacity(.35),run_time=2)
        formula=math('L(w) = (w - 3)^2',34).move_to([4,1.6,0])
        self.at(25);self.header(2,'Find a rule you can use from here.')
        self.play(Write(formula),run_time=1.4)
        minimum=Dot(ax.c2p(3,0),color=GREEN,radius=.085)
        minlabel=text('minimum at w = 3',22,GREEN).next_to(minimum,UP,buff=.35)
        self.at(31);self.play(FadeIn(minimum),FadeIn(minlabel),run_time=1)
        self.at(34);self.play(Indicate(minimum,color=GREEN),run_time=1)
        w=ValueTracker(-1)
        bead=always_redraw(lambda:Dot(ax.c2p(w.get_value(),(w.get_value()-3)**2),color=GOLD,radius=.09))
        projection=always_redraw(lambda:DashedLine(ax.c2p(w.get_value(),0),ax.c2p(w.get_value(),(w.get_value()-3)**2),color=GOLD,stroke_opacity=.45))
        self.at(38);self.play(FadeIn(bead),FadeIn(projection),FadeOut(minlabel),run_time=1)
        question=text('Which direction\nreduces the loss?',27).move_to([4,.2,0])
        self.at(42);self.play(FadeIn(question),run_time=1)
        self.caption('Use local information: the slope at the current position.')
        self.at(50);self.header(3,'The slope tells us which way to move.')
        self.play(FadeOut(question),run_time=.5)
        tangent=always_redraw(lambda:Line(ax.c2p(w.get_value()-.6,(w.get_value()-3)**2-2*(w.get_value()-3)*.6),ax.c2p(w.get_value()+.6,(w.get_value()-3)**2+2*(w.get_value()-3)*.6),color=GOLD,stroke_width=4))
        slope=math('(d L)/(d w) = 2(w - 3)',32,GOLD).move_to([4,.3,0])
        self.play(Create(tangent),run_time=1)
        tri=VGroup(Line(ax.c2p(-1,16),ax.c2p(-.4,16),color=MUTED),Line(ax.c2p(-.4,16),ax.c2p(-.4,11.2),color=MUTED))
        self.play(Create(tri),run_time=1)
        neg=text('negative slope\nmove right',25,GREEN).move_to([4,-1,0])
        self.at(55);self.play(FadeIn(neg),run_time=.7)
        self.at(58);self.play(FadeOut(tri),w.animate.set_value(.6),run_time=2)
        pos=text('positive slope\nmove left',25,GREEN).move_to([4,-1,0])
        self.at(62);self.play(w.animate.set_value(6.5),ReplacementTransform(neg,pos),run_time=2)
        zero=text('zero slope\nat the minimum',25,GREEN).move_to([4,-1,0])
        self.at(65);self.play(w.animate.set_value(3),ReplacementTransform(pos,zero),run_time=1.5)
        self.at(68);self.play(Write(slope),run_time=1)
        self.at(71);self.caption('One parameter: derivative. Many parameters: gradient.')
        self.at(77);self.play(FadeOut(zero),w.animate.set_value(-1),run_time=1)
        self.at(80);self.header(4,'Take a step opposite the gradient.')
        self.play(FadeOut(formula),FadeOut(slope),FadeOut(tangent),run_time=.6)
        update=math('w_"next" = w - eta (d L)/(d w)',35).move_to([3.8,1.7,0])
        if update.width>4.3:update.scale_to_fit_width(4.3)
        self.play(Write(update),run_time=1.2)
        rate=text('η = learning rate',25,GREEN).move_to([3.8,.75,0])
        self.at(86);self.play(FadeIn(rate),run_time=.8)
        self.caption('New parameter = current parameter − learning rate × slope.')
        grad=Arrow(ax.c2p(-1,1),ax.c2p(-2,1),color=RED,buff=0)
        step=Arrow(ax.c2p(-1,3),ax.c2p(.6,3),color=GREEN,buff=0)
        gl=text('gradient',17,RED).next_to(grad,UP,buff=.12)
        sl=text('−η × gradient',17,GREEN).next_to(step,UP,buff=.12)
        self.at(90);self.play(GrowArrow(grad),FadeIn(gl),run_time=.8)
        self.at(93);self.play(GrowArrow(step),FadeIn(sl),run_time=.8)
        numbers=VGroup(math('w = -1',30,BLUE),math('"slope" = -8',30,GOLD),math('eta = 0.2',30,GREEN)).arrange(DOWN,buff=.24).move_to([3.8,-.65,0])
        self.at(94);self.play(FadeIn(numbers),run_time=1)
        calc=math('-1 - 0.2(-8) = 0.6',32,GREEN).move_to([3.8,-2.15,0])
        self.at(98);self.play(Write(calc),run_time=1)
        self.at(100);self.play(w.animate.set_value(.6),run_time=2)
        self.caption('The minus sign turns a negative slope into a step to the right.')
        self.at(110);self.header(5,'Direction is not enough. Step size matters.')
        self.caption('Repeat the same update to approach the minimum.')
        self.play(FadeOut(VGroup(update,rate,numbers,calc,grad,step,gl,sl)),run_time=.8)
        for target in [1.56,2.136,2.4816,2.68896]:
            self.play(w.animate.set_value(target),run_time=.65)
        self.at(116);self.play(FadeOut(VGroup(ax,ticks,xl,yl,curve,points,minimum,bead,projection)),run_time=.8)
        # Equal iteration counts, identical scales and initial conditions.
        rates=[.04,.2,1.05];cols=[BLUE,GREEN,RED]
        names=['SMALL · η = 0.04','SUITABLE · η = 0.2','TOO LARGE · η = 1.05']
        smallaxes=[];runners=[];trackers=[];readouts=[]
        for i,(eta,col) in enumerate(zip(rates,cols)):
            center=-4.65+i*4.65
            a=Axes(x_range=[-6,12,3],y_range=[0,81,20],x_length=3.9,y_length=3.5,tips=False,axis_config={'color':'#536D7C','include_ticks':False}).move_to([center,-.1,0])
            c=a.plot(lambda x:(x-3)**2,x_range=[-6,12],color=col,stroke_width=2)
            title=text(names[i],19,col).move_to([center,2.05,0])
            v=ValueTracker(-1);trackers.append(v)
            dot=always_redraw(lambda a=a,v=v,col=col:Dot(a.c2p(v.get_value(),(v.get_value()-3)**2),color=col,radius=.075))
            minimumdot=Dot(a.c2p(3,0),radius=.04,color=INK)
            # Text updater avoids LaTeX-dependent DecimalNumber.
            readout=always_redraw(lambda v=v,center=center:text(f'loss = {(v.get_value()-3)**2:.3f}',19).move_to([center,-2.35,0]))
            smallaxes += [a,c,title,minimumdot];runners.append(dot);readouts.append(readout)
        self.at(118);self.play(*[FadeIn(m) for m in smallaxes+runners+readouts],run_time=1)
        self.caption('Same starting point. Same axes. Six updates for every learning rate.')
        counter=text('update 0 / 6',22).move_to([0,-2.9,0]);self.add(counter)
        self.at(122)
        for k in range(6):
            nxt=[v.get_value()-eta*2*(v.get_value()-3) for v,eta in zip(trackers,rates)]
            trails=VGroup(*[Line(smallaxes[i*4].c2p(v.get_value(),(v.get_value()-3)**2),smallaxes[i*4].c2p(x,(x-3)**2),color=cols[i],stroke_width=1.2,stroke_opacity=.45) for i,(v,x) in enumerate(zip(trackers,nxt))])
            self.add(trails)
            self.play(*[v.animate.set_value(x) for v,x in zip(trackers,nxt)],Transform(counter,text(f'update {k+1} / 6',22).move_to(counter)),run_time=1.6)
            self.wait(.8)
        self.at(137);self.caption('For this curve: 0 < η < 1 converges; η = 1 oscillates; η > 1 diverges.')
        self.at(142);self.play(*[FadeOut(m) for m in list(self.mobjects) if m not in [self.heading,self.cap]],run_time=1)
        self.at(145);self.header(6,'Many parameters. The same local rule.')
        self.caption('Each contour joins parameter values with equal loss.')
        # Contours of L(w1,w2)=w1²+2w2²; arrows use its exact gradient.
        center=np.array([-2.0,-.25,0]);scale=1.05
        plane=Axes(x_range=[-3,3,1],y_range=[-2.2,2.2,1],x_length=6.3,y_length=4.62,tips=False,axis_config={'color':'#405966','include_ticks':False}).move_to(center)
        contours=VGroup(*[Ellipse(width=2*r*scale,height=2*r/np.sqrt(2)*scale,color=BLUE,stroke_width=1.8,stroke_opacity=.35+.1*i).move_to(center) for i,r in enumerate([.5,1,1.5,2,2.5])])
        lab1=math('w_1',26,BLUE).next_to(plane.x_axis,RIGHT,buff=.1);lab2=math('w_2',26,BLUE).next_to(plane.y_axis,UP,buff=.1)
        cf=math('L(w_1,w_2) = w_1^2 + 2w_2^2',29).move_to([3.5,1.75,0])
        self.play(Create(plane),Create(contours),FadeIn(lab1),FadeIn(lab2),Write(cf),run_time=2)
        xy=np.array([-1.8,1.05]);pt=lambda p:center+np.array([p[0]*scale,p[1]*scale,0])
        current=Dot(pt(xy),color=GOLD,radius=.09);self.play(FadeIn(current),run_time=.6)
        uphill=np.array([2*xy[0],4*xy[1]]);uphill=uphill/np.linalg.norm(uphill)*.8
        ga=Arrow(pt(xy),pt(xy+uphill),color=RED,buff=0)
        da=Arrow(pt(xy),pt(xy-uphill),color=GREEN,buff=0)
        key=VGroup(text('gradient: steepest increase',21,RED),text('negative gradient: decrease',21,GREEN)).arrange(DOWN,buff=.3).move_to([3.5,.3,0])
        self.at(155);self.play(GrowArrow(ga),FadeIn(key[0]),run_time=1)
        self.at(159);self.play(GrowArrow(da),FadeIn(key[1]),run_time=1)
        self.at(162);self.play(FadeOut(ga),FadeOut(da),run_time=.5)
        for _ in range(5):
            new=xy-.18*np.array([2*xy[0],4*xy[1]])
            self.play(Create(Line(pt(xy),pt(new),color=GREEN,stroke_width=3)),current.animate.move_to(pt(new)),run_time=.65)
            xy=new
        caveat=text('Local improvement does not\nguarantee a global minimum.',22,MUTED).move_to([3.5,-1.2,0])
        self.at(167);self.play(FadeIn(caveat),run_time=.8)
        self.at(171);self.caption('Measure the slope. Take a controlled step. Repeat.')
        final=math('bold(w)_"next" = bold(w) - eta nabla L',32,GREEN).move_to([3.4,-2.45,0])
        self.play(Write(final),run_time=1)
        self.at(178.5);self.play(*[FadeOut(m) for m in list(self.mobjects)],run_time=1)
        self.at(180)
