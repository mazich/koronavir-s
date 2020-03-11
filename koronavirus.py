#Birkaç soru ile COVID-19 enfeksiyonu tehlikeni ölç.
print('İsmini ve yaşını belirt.')
isim = input('isim: ')
yas = int(input('yaş: '))

print('\nBu semptomlardan hangilerini kendinde gözlemliyorsun?')
ates = int(input('Ateşin var mı? (0= yok, 1= var): '))
oksur = int(input('Öksürük var mı? (0= yok, 1= var): '))
nd = int(input('Nefes darlığı var mı? (0= yok, 1= var): '))
bog = int(input('Boğaz ağrısı veya burun akıntısı var mı? (0= yok, 1= var): '))
kus = int(input('Kusma durumu var mı? (0= yok, 1= var): '))
hastalik = int(input('Diyabet, böbrek veya kalp hastalığı var mı? (0= yok, 1= var): '))
bolge = int(input('Son 14 günde salgın bölgesinde veya bu bölgeden biriyle temas halinde bulundun mu?(0= hayır, 1= evet): '))

tehlike = ates*2 + oksur*2 + nd*2 + bog + kus + hastalik

print(isim,',')
if bolge ==0:
    if tehlike > 4: print("Belirttiğin semptomlar COVID-19 için ciddi risk teşkil etmiyor,muhtemelen gripsin.")
    else: print("Enfekte olma ihtimalin var,kendine dikkat et dostum.")
if bolge ==1:
    if tehlike > 4: print('Enfekte olma ihtimalin hayli yüksek,teyit edilene kadar maske kullanıp ve kendine dikkat etmelisin.')
    else: print("Enfeksiyon belirtileri düşük,ama yine de bölgeden dolayı enfekte olma tehliken var. ")

if -1<yas<41: oran = "0.2 %"
if 40<yas<51: oran = "0.4 %"
if 50<yas<61: oran = '1.3 %'
if 60<yas<71: oran = "3.6 %"
if 70<yas<81: oran = '8 %'
if 80<yas: oran = '14.8 %'
print('Eğer enfekte isen yaşına göre ölüm oranın:', oran)