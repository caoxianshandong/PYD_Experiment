实验二例题
b=float(input("请输入腹板宽 mm"))
bf=float(input("请输入翼缘宽 mm"))
h=float(input("请输入总高 mm"))
hf=float(input("请输入翼缘高 mm"))
y=(2*hf*h*bf-hf*hf*bf+h*h*b+hf*hf*b-2*h*hf*b)/(hf*bf+(h-hf)*b)/2
lx=float(input("请输入lx mm^4"))
Mx=float(input("请输入Mx KN*mm"))
σ=((Mx*y)/lx)*1000
print (σ) 


