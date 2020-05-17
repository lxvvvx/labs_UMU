import reportlab
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.platypus import Paragraph, Table, TableStyle, SimpleDocTemplate
from reportlab.lib.pagesizes import  letter, A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

#данные для формирования счета
telephony = 36.23
sms = 15
traffic = 176.66
traffic_sum = 77.46
telephony_sum = 72.46
sms_sum = 5
tax = round((traffic + telephony + sms) / 100 * 20, 2)
bill = round(traffic + telephony + sms + tax, 2)

data1 = [['ПАО \'БанкРОТ\', Г. САНКТ-ПЕТЕРБУРГ', '', 'БИК', '056384259'],
       ['', '', 'Счёт №', '50326499000003732479'],
       ['Банк получателя', '', '', ''],
       ['ИНН 1647582648', 'КПП 636295847', 'Счёт №', '60386500000002496582'],
       ['ООО "РИНГ"\n', '', '', ''],
       ['Получатель', '', '', '']
       ]

data2 = [['Поставщик\n(Исполнитель):\n\n', 'ООО"РИНГ", ИНН 1647582648, КПП 636295847, 113859,\nг.Санкт-Петербург, ЛИСИЧАНСКАЯ ул., дом №26, строение 1,\n тел.: +79235757648\n'],
        ['Покупатель\n(Заказчик):\n', 'Богачёв В.В., ИНН 2379371846, КПП 258368957, 132345,\nг.Санкт-Петербург, ДНЕПРОПЕТРОВСКАЯ ул., дом №77, корпус 13\n'],
        ['Основание:', '№ 74228483 от 12.01.2020']]

service_cost = [['№', 'Услуги', 'Условия', 'Цена', 'Количество', 'Сумма, руб'], 
                ['1', 'Телефония', 'Плата за исходящие звонки', '2 руб/мин', telephony, telephony_sum],
                ['2', 'SMS', '10 бесплатных сообщений','1 руб/шт',  sms, sms_sum],
                ['3', 'Интернет', 'Входящий трафик', '0.5 руб/мб', traffic, traffic_sum]]
final = [['Итого:', bill],
        ['В том числе НДС:', tax],
        ['Всего к оплате:', bill]]

registerFont(TTFont('times','times.ttf'))
registerFont(TTFont('times-bold','timesbd.ttf'),)
registerFontFamily('times', normal='times', bold='times-bold')
canvas = canvas.Canvas("bill.pdf", pagesize=letter)
canvas.setLineWidth(.3)

#работа с таблицей, содержащей информацию о реквизитах получателя и его банка
d1 = Table(data1, style = [('FONT', (0, 0), (3, 5), 'times'),
                        ('FONTSIZE', (0, 0), (3, 5), 12),
                        ('FONTSIZE', (0, 3), (1, 3), 11),
                        ('FONTSIZE', (0, 5), (1, 5), 11),
                        ('ALIGN', (0, 0), (3, 5), 'LEFT'),
                        ('BOX', (0, 0), (3, 5), 1, colors.black),
                        ('GRID', (0, 3), (3, 3), 1, colors.black),
                        ('LINEBEFORE', (2, 0), (-1, -1), 1, colors.black),
                        ('LINEABOVE', (2, 1), (3, 1), 1, colors.black),
                        ('SPAN', (2, 4), (2, 5)),
                        ('SPAN', (3, 4), (3, 5)),
                        ('VALIGN',(2, 3),(3, 5),'TOP'),
                        ])
d1.wrapOn(canvas, 0, 0)
d1.drawOn(canvas, 60, 600)

canvas.setFont('times-bold', 16)
canvas.drawString(60,560,'Счёт на оплату № 50 от 10 мая 2020 г.')
canvas.line(60,540,555,540)
canvas.setFont('times', 12)

#работа с таблицей, содержащей информацию о реквизитах поставщика и покупателя
d2 = Table(data2, style = [('FONT', (0, 0), (0, 2), 'times', 12),
                           ('FONT', (1, 0), (1, 2), 'times-bold', 12),
                          ])
d2.wrapOn(canvas, 0, 0)
d2.drawOn(canvas, 55, 400)

#работа с таблицами, содержащими информацию об итоговой стоимости услуг
s = Table(service_cost, style = [('FONT', (0, 0), (5, 3), 'times'),
                                 ('FONTSIZE', (0, 0), (5,3), 11),
                                 ('FONT', (0, 0), (5, 0), 'times-bold'),
                                 ('ALIGN',(1, 0),(3, 3),'LEFT'),
                                 ('ALIGN',(4, 0),(5, 3),'RIGHT'),
                                 ('INNERGRID', (0,0), (5, 3), 0.5, colors.black),
                                 ('BOX', (0,0), (5, 3), 1.5, colors.black),
                                ])
s._argW[3]=1.8*inch
s.wrapOn(canvas, 0, 0)
s.drawOn(canvas, 60, 320)

f = Table(final, style = [('FONT', (0, 0), (1, 2), 'times-bold', 12),
                         ('ALIGN', (0, 0), (1, 2), 'RIGHT')])
f.wrapOn(canvas, 0, 0)
f.drawOn(canvas, 405, 250)

#работа с текстом, содержащим итоговую информацию
canvas.drawString(60,240,'Всего наименований 3, на сумму ' + str(bill))
canvas.setFont('times-bold', 12)
canvas.drawString(60,220, 'Двести семьдесят рублей сорок семь копеек')
canvas.setFont('times', 12)
canvas.drawString(60, 190, 'Внимание!')
canvas.drawString(60, 170, 'Оплата данного счета означает согласие с условиями предоставления услуг.')
canvas.drawString(60, 150, 'Услуги предоставляются по факту прихода денег на р\с Поставщика.')
canvas.line(60,130,555,130)
canvas.setFont('times-bold', 12)
canvas.drawString(60, 80, 'Руководитель')
canvas.drawString(350, 80, 'Бухгалтер')
canvas.setFont('times', 11)
canvas.line(140,80,340,80)
canvas.drawString(285,81, 'Грачёв В.А.')
canvas.line(410,80,555,80)
canvas.drawString(485,81, 'Грошевич А.Л.')

canvas.save()