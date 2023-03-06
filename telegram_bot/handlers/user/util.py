from telegram_bot.utils import TgConfig
from misc.html_tags import b, i


def _user_agreement_text(name: str) -> str:
    data = (
        b(f"🎉Уважаемый {name}! Вы запустили установку юзербота с анимациями на ваш аккаунт!\n"),
        i(
            f'{b("Юзербот")} - это бот, привязанный к аккаунту "вашего" пользователя. '
            'Он напрямую подключаются к вашему аккаунту. '
            f'Наш {b("БОТ")} имеет доступ только к тем сообщениям, которые вызываются командами.\n'
          ),
        b('Продолжив установку данного бота к себе на аккаунт, вы соглашаетесь с пользовательским соглашением❗')
    )
    return '\n'.join(data)


def _buy_vip_text() -> str:
    data = (
        b("⭐️ Хочешь преобрести полный доступ???"),
        i("- Тогда тебе нужен VIP\n"),
        b(f"💰 Стоимость - {TgConfig.PRICE}р / навсегда\n"),
        b("😯 Чем VIP отличается от бесплатного бота?\n"),
        i("・ Отсутствие рекламного текста после анимаций"),
        i("・ Доступ к VIP командам\n"),
        b("Для покупки нажмите на кнопку Оплатить."),
        b("После оплаты не забудьте ее проверить!")
    )
    return "\n".join(data)