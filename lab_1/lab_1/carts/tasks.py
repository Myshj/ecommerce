from celery import shared_task,current_task
import yagmail

@shared_task(bind=True)
def send_mail(self):

    yag = yagmail.SMTP('alexedon57', 'DunkanKalahhan19')
    contents = ['Somewho added somewhat to cart.']
    yag.send('donmarin@mail.ru', 'TEST', contents)