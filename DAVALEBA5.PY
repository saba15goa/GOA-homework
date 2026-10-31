 # 2) მომხმარებელს შემოაყვანინე სამი რიცხვი, ხოლო პროგრამამ დაბეჭდოს მათი საშუალო არითმეტიკული.
num_1= int(input("first number:"))
num_2= int(input("second number:"))
num_3= int(input("third  number:"))
print(int(num_1+num_2+num_3)//3)
# 3) მომხმარებელს შემოატანინე ორი რიცხვი და დაბეჭდე მათი ჯამი.
ricx_1 = int(input("chose first number for add:"))
ricx_2 = int(input("second number :"))
print(ricx_1+ricx_2)
# 4) input ფუნქციის საშუალებით შემოიყვანეთ თქვენი და თქვენი ოჯახის წევრების სახელები და დაპრინტეთ ერთი დიდი წინადადება კონკატენაციის სახით.
s_n= (input("your name :"))
n_1= (input("moms name :"))
n_2=(input("dads name :"))
n_3=(input("brothers name:"))
n_4=(input("sisters name :"))
print("my name is "+  s_n  +  " my moms name is "+ n_1 + " my dads name is "+  n_2+  " my bros name is "+ n_3 + " and  my sisters name is " + n_4)
# 5) მომხმარებელს შემოატანინეთ მისი ქალაქის, უბნის, კორპუსის და სართულის შესახებ ინფორმაცია (რომლებიც უნდა შეინახოთ ცალ-ცალკე ცვლადებში). მაგ. city = "Tbilisi", District = "{თქვენი უბანი}" და ა.შ. საბოლოოდ print() ბრძანების საშუალებით ტერმინალში გამოიტანეთ მომხმარებლის სრული მისამართი.
p =(input("witch planet are you on: "))
co =(input("witch continent are you on: "))
c =(input("witch country are you in: "))
st =(input("witch region are you in: "))
dist=(input("witch district are you in : "))
ste=(input("witch street are you in : "))
sten=(input("what street number is your home : "))
print( "your planet is:"+ p +"     your continet is:"+ co +"      your country is:" + c +"      your region is: " + st + "       your district is: " + dist + "    your street is: "+ ste + "     your street number is: " + sten )



# 6) მომხმარებელს შემოატანინეთ ასაკი და ამოყენებითმსგავსი ფორმატის წინადადება: 
# "You are ასაკი years old".

age =input("your age :")
print("You are "+ age + " years old")