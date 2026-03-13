from django.core.mail import send_mail
from django.conf import settings

def send_order_email(to_email, order):
    subject = f"Ваш заказ #{order.id} принят!"
    message = (
        f"Привет, {order.user.username}!\n\n"
        f"Спасибо за покупку в AsiaMall!\n"
        f"Продукт: {order.product_name}\n"
        f"Количество: {order.quantity}\n"
        f"Дата заказа: {order.created_at.strftime('%d-%m-%Y %H:%M')}\n\n"
        f"Ваш заказ обрабатывается."
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [to_email], fail_silently=False)