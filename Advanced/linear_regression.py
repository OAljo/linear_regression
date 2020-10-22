#Linear Regression model from stratch 
'''ماهو الانحدار الخطي : 
هو طريقة تستخدم لتحديد العلاقة بين متغير تابع
 (Y) 
ومتغير مستقل 
(X). 
يتم تمثيل العلاقة بشكل المعادلة التالية : 
y=mx+b
Y المتغير التابع
m معامل القياس
x المتغير المستقل
b معامل التحيز : التحيز هو الفرق بين القيمة المتوقعة للمُقدِّر والقيمة الحقيقية التي يتم تقديرها
لمعرفة المزيد عن معامل التحيز اتبع الرابط التالي : 
https://stats.stackexchange.com/questions/13643/what-intuitively-is-bias

الهدف من الانحدار الخطي هو رسم خط يمثل العلاقة  ( المقدرة )بين المتغير التابع و المستقل 
للمزيد عن الانحدار الخطي و كيفية حساب المعاملات : 
https://www.statisticshowto.com/probability-and-statistics/regression-analysis/find-a-linear-regression-equation/

'''
''' هناك عدة طرق لحساب المعاملات و سنستخدم طريقة : 
تربيع أقل متوسط حسابي عادي 
Ordinary Least Mean Square Method 
الهدف هو رسم خط يحقق أفضل تناسب و يمر عبر معظم النقاط المبعثر ويقلل أيضا من الخطأ الذي هو المسافة من النقطة إلى الخط نفسه 
يمكن الاطلاع على الصورة رقم1 في مجلد الصور 
'''
''' 
مجموع الخطأ للنموذج الخطي هو مجموع  الخطأ عند كل نقطة 
ri =i المسافة بين الخط و النقطة رقم 
n =مجموع عدد النقاط 
ri **2 سنقوم بتربيع قيمة كل مسافة بين الخط و النقطة المحددة 
انظر لصورة رقم 2 

و المعادلة التي سوف نستخدمها لايجاد قيمة المعاملات يمكن ايجادها في الصورة رقم 3 
b0 ملخصها هو لايجاد قيمة 
Yنقوم بحساب متوسط المتغير التابع 
و نطرح منها قيمة المتغير المستقل مضروبة بمعامل التحيز للقيمة رقم 1

i المعادلةلحساب معامل التحيز للقيمة   : 
   في البسط : مجموع
   (مجموع قيم المتغير المستقل عند(i)  - متوسط القيم )

مضروب في 
( قيم المتغير التابع عند   (i) - المتوسط)
في المقام :
 مربع (مجموع قيم المتغير المستقل عند(i)  - متوسط القيم )

b0=b
b1=m 
'''
''' install numpay , matplot and pandas
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Advanced/dataset.csv')
print(dataset.shape)
print(dataset.head())
# العلاقة بين حجم الرأس بالسنتيميتر المكعب و وزن الرأس بالجرام 
#تخزين البيانات المطلوبة 
H = dataset['Head Size(cm^3)'].values #مدخلات 
B = dataset['Brain Weight(grams)'].values # مخرجات 
# متوسط المدخلات 
mean_H=np.mean(H)
# متوسط المخرجات 
mean_B=np.mean(B)
# n = هو عدد المدخلات = مجموع النقاط  H طول 
n = len(H)

numerator = 0
denominator = 0
#حساب المقام 
for i in range(n):
    numerator += (H[i] - mean_H) * (B[i] - mean_B)
    denominator += (H[i] - mean_H) ** 2

b1 = numerator / denominator
# b0 , b1 حساب قيم 
b1 = numerator / denominator
b0 = mean_B - (b1 * mean_H)
#طباعة المعاملات 
print("m = ")
print(b1)
print(" b =\n")
print(b0)
''' اذا حجم الدماغ أو المتغير التابع يساوي 
y=mx+b '''
#B = 0.26342933948939945*H + 325.57342104944223
# معلومات الرسوم البيانية 
H_max = np.max(H) + 100
H_min = np.min(H) - 100

h = np.linspace(H_min, H_max, 1000)
b = b0 + b1 * h


plt.plot(h, b, color='#008B8B', label='الانحدار الخطي')

plt.scatter(H, B, color='#8FBC8F', label='المدخلات')

# تسمية المحور السيني 
plt.xlabel('قياس الرأس (سم^3)')
#تسمية المحور الصادي
plt.ylabel('وزن الدماغ (جرام)')
plt.legend()
plt.show()

# حساب الخطأ 
rmse = 0
for i in range(n):
    b_pred=  b0 + b1* H[i]
    rmse += (B[i] - b_pred) ** 2
    
rmse = np.sqrt(rmse/n)
print(rmse)

# حساب الدقة 
sumofsquares = 0
sumofresiduals = 0
for i in range(n) :
    b_pred = b0 + b1 * H[i]
    sumofsquares += (B[i] - mean_B) ** 2
    sumofresiduals += (B[i] - b_pred) **2
    
score  = 1 - (sumofresiduals/sumofsquares)
print(score)


# الحقوق : 
# https://towardsdatascience.com/linear-regression-from-scratch-cd0dee067f72
