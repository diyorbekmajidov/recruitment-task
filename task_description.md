# Topshiriq

## Kirish
Bu topshiriq sizning REST APIlar bilan ishlay olishingizni sinash uchun tayyorlangan.
Biz sizning shunga oxshash loyihalarda qanday yondashingizni bilmoqchimiz.
Uning uchun siz quyidagi 4ta xususiyatlarni REST API ga qoshishingizni istaymiz.

## Talablar
Bu topshiriqni bajarish quyidagi bosqichlardan iborat:
* Repositoryni klon qilib oling,
* Quyidagi 4ta xususiyatlarni REST API ga qoshing,
* Barchasini topshirib bo'lganingizdan so'ng, bizda GitHub repositoryning linkini yuboring.

Bu loyihaga <a href="https://medium.com/@komilov_shamsiddin/unit-testing-ga-kirish-nega-unit-testing-yozishingiz-kerak-7bd0ef730f9" target="_blank">Unit testlar</a> ham qoshishingiz kerak.


## Loyiha haqida ma'lumot:
Turli hil loyihalarga invistitsiya kirituvchi REST API servisi yozishingiz kerak.

Database models:

```
1. User (foydalanuvchi): # Authentication uchun shu modeldan foydalaning
    - first_name     # ismi
    - last_name      # familiyasi
    - email          # elektron pochta


2. Investor:
    - user: foreign key -> User model # User modeliga bog'lang
    - budget                          # Investorning byudjeti
    - project_deadline                # Loyihani bitirish muddati


3. Project (Loyiha modeli):
    - owner: foreign key -> User model # User modeliga bog'lang
    - name                             # Loyiha nomi
    - min_investment_amount            # minimum invistisiya summasi
    - deadline                         # Loyihani bitish sanasi
    - invested                         # Loyihaga invistitsiya kirtilgan yoki hali invistitsiya kiritilmaganligi haqida  
    - investor                         # Investor modeliga bog'lang agar inivistitsiya qilinga bo'lsa, bo'lmasa null qiymatga ega holda qoldiriladi.
```

# Qoshishingiz kerak bo'lgan xususiyatlar:

## 1. Quyidagi API endpoint larni qoshing:
- `/investors/<investor_id>/matches` - bu API endpoint, tanlangan investor byudjetiga mos keladigan barcha loyihalarni chiqarish kerak
- `/projects/<project_id>/<matches>` - bu API endpoint, tanlangan loyiha uchun mos barcha investorlarni chiqarish kerak

## Loyihalar Investorlarga yoki Investorlar Loyihalarga moslash algoritimi:

Loyihalar va Investorlar quyidagi barcha talablar tog'ri kelsagina bir biriga mos kelishi kerak:

1. Agar loyiha investorning loyihani bitirish muddatigacha bitirilsa
2. Agar Investorda Loyiha ucuhn yetarlicha byudjet bo'lsa
3. Loyihaga invistitsiya kiritilmagan bo'lishi kerak



## Eslatmalar
* Investor bir necha loyihaga invistitsiya kirta oladi, lekin barcha kiritilgan invistitsiya summalari investorning umumiy byudjetidan oshib ketamasligi kerak


## Topshiriqni boshlashdan oldin:
1. Repositroyni fork qilib oling
2. Repositoryni o'z github profilingizdan klon qiling:
```bash
$ git clone <repository_link>
```
3. Loyihani klon qilib bo'lganingizdan so'ng python environment yarating and environmentni aktivatsiya qiling
4. Barcha kerakli dependencylarni environmentingiza yuklab olish ucuhn quyidagi buyruqni kiriting terminal/cmd/powershell da:
```bash
$ pip install -r requirements.txt
```


Loyihani bajarib bo'lganingizdan so'ng, Recruiterni telegram accountiga ismingiz va familiyangizni yozgan holda topshiriq github repositorysi uchun link bilan jo'nating.

Email subject: Abdumalikov Jamshid - Backend topshiriq

Email body: Github repository uchun link