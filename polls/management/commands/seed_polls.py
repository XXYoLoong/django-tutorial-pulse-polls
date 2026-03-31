import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from polls.models import Choice, Question


POLL_FIXTURES = [
    {
        "question_text": "你理想的周末打开方式是？",
        "question_text_en": "What is your ideal weekend mode?",
        "description": "轻松一点，看看大家更偏爱休息、社交、出门还是自我充电。",
        "description_en": "A light poll about whether people recharge through rest, friends, going out, or solo time.",
        "choices": [
            ("睡到自然醒，再慢慢吃早午餐", "Sleep in and ease into brunch"),
            ("约朋友见面，边聊边走", "Meet friends and wander around together"),
            ("找个新地方逛逛，顺便拍照", "Explore somewhere new and snap photos"),
            ("在家看书看片，安静回血", "Stay in with books or shows and recharge"),
        ],
    },
    {
        "question_text": "点饮品之前，你最先考虑什么？",
        "question_text_en": "What matters most before you order a drink?",
        "description": "咖啡、奶茶和果饮爱好者大集合，不聊配方，只聊选择时的第一反应。",
        "description_en": "For coffee, tea, and fruit-drink fans: what drives your first decision?",
        "choices": [
            ("今天到底想提神还是放松", "Whether I need energy or something calming"),
            ("甜度和冰量要不要改", "The sugar and ice level"),
            ("有没有新口味值得尝鲜", "Whether there is a new flavor to try"),
            ("价格是否对今天的钱包友好", "Whether it fits today's budget"),
        ],
    },
    {
        "question_text": "如果一天突然多出一小时，你最想怎么用？",
        "question_text_en": "If you suddenly gained one extra hour today, how would you use it?",
        "description": "这不是效率挑战，而是看看大家最想把时间花在哪里。",
        "description_en": "Not a productivity test, just a peek at where people most want to spend extra time.",
        "choices": [
            ("把一直想学的技能继续推进", "Make progress on a skill I want to learn"),
            ("出门散步，认真看看城市", "Take a walk and notice the city around me"),
            ("彻底发呆，不安排任何任务", "Do absolutely nothing and enjoy the pause"),
            ("把拖延的小事一口气清掉", "Clear out the little tasks I keep postponing"),
        ],
    },
    {
        "question_text": "出发旅行前，你最先确认哪一件事？",
        "question_text_en": "What do you double-check first before a trip?",
        "description": "轻装出发派和准备充分派，通常在这一题会非常有代表性。",
        "description_en": "Minimal packers and meticulous planners often reveal themselves here.",
        "choices": [
            ("证件、车票和充电器", "Documents, tickets, and chargers"),
            ("天气和当天穿什么", "The weather and what I should wear"),
            ("攻略收藏夹和路线安排", "My saved spots and travel plan"),
            ("零食和路上听的歌单", "Snacks and the playlist for the road"),
        ],
    },
    {
        "question_text": "学习或写东西时，你最喜欢什么陪伴？",
        "question_text_en": "What is your favorite companion while studying or writing?",
        "description": "安静派和氛围派都很常见，看看你的专注条件是哪一种。",
        "description_en": "Some people need silence, others need atmosphere. Which one sounds like you?",
        "choices": [
            ("完全安静，最好没有任何提醒", "Total silence with no interruptions"),
            ("白噪音或轻音乐", "White noise or soft background music"),
            ("咖啡馆的人声和环境感", "Cafe chatter and ambient energy"),
            ("桌边放一杯热饮就足够", "Just having a warm drink nearby"),
        ],
    },
    {
        "question_text": "哪种小确幸最容易瞬间点亮你的一天？",
        "question_text_en": "Which tiny delight can brighten your day instantly?",
        "description": "选项都不大，却很像日常里真正有用的快乐开关。",
        "description_en": "These are all small moments, but they often work like instant mood boosters.",
        "choices": [
            ("收到一句真诚的夸奖", "Receiving a sincere compliment"),
            ("吃到今天状态特别好的那一口", "Taking that one perfect bite today"),
            ("通勤路上刚好赶上绿灯和空位", "Catching green lights and an empty seat on the way"),
            ("回家后发现还有完整的独处时间", "Realizing I still have some peaceful solo time"),
        ],
    },
]


class Command(BaseCommand):
    help = "Seed the project with curated bilingual demo polls."

    def handle(self, *args, **options):
        Question.objects.all().delete()

        now = timezone.now()
        for index, item in enumerate(POLL_FIXTURES):
            question = Question.objects.create(
                question_text=item["question_text"],
                question_text_en=item["question_text_en"],
                description=item["description"],
                description_en=item["description_en"],
                pub_date=now - datetime.timedelta(hours=index + 1),
            )
            for choice_zh, choice_en in item["choices"]:
                Choice.objects.create(
                    question=question,
                    choice_text=choice_zh,
                    choice_text_en=choice_en,
                )

        self.stdout.write(
            self.style.SUCCESS(f"Seeded {len(POLL_FIXTURES)} bilingual demo polls.")
        )
