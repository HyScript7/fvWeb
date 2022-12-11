#  ______   __   __   __     __     ______     ______
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/
#
# fvWeb
# License: MIT LICENSE
# For more information on copyright and licensing view the README.md file.
#
from flask import render_template, request, url_for
from routes.web import getCards, navBarLinks
from routes.web.wiki import web


@web.route("/")
async def index():
    cards = await getCards()
    return render_template(
        "wiki/index.html", thisPage="Wiki", cards=cards, navBarLinks=navBarLinks
    )


@web.route("/article/<id>")
async def article(id):
    cards = await getCards()
    content = []
    lorem = [
        "Dolorem sed ut ipsum neque quisquam quiquia. Est sit sed modi non labore. Magnam quisquam consectetur neque. Ut modi amet adipisci est. Porro eius velit sit. Numquam dolore adipisci aliquam velit. Numquam dolorem tempora magnam sed. Adipisci neque numquam amet quisquam non magnam. Consectetur sit ut tempora sit. Quaerat tempora amet quisquam.",
        "Modi labore dolorem dolor consectetur non. Modi etincidunt dolor quaerat. Magnam quaerat quisquam non quiquia magnam aliquam velit. Numquam quiquia tempora adipisci consectetur. Non amet quisquam est consectetur tempora. Sit sed dolore ipsum. Labore voluptatem quaerat quiquia sed sed.",
        "Aliquam eius quaerat consectetur dolore dolor sed. Magnam numquam est neque dolorem numquam dolore. Etincidunt amet ipsum etincidunt voluptatem. Eius dolore voluptatem modi amet. Amet tempora ut dolor neque eius. Quiquia consectetur dolore labore sed labore quaerat.",
        "Labore etincidunt dolore numquam labore dolorem quisquam aliquam. Amet etincidunt porro non. Sed labore consectetur numquam dolorem labore eius numquam. Quiquia sit quisquam magnam sit ipsum tempora. Quaerat quaerat quaerat sit. Dolorem adipisci adipisci quiquia magnam. Dolor voluptatem consectetur neque dolore. Porro labore adipisci sit ut neque dolore.",
        "Sit quaerat adipisci tempora quaerat sit modi sed. Ut neque tempora magnam dolore aliquam quisquam sit. Magnam est neque velit ipsum eius aliquam quaerat. Etincidunt ipsum sed est amet est. Etincidunt labore quisquam adipisci voluptatem porro. Dolor tempora quaerat dolorem quaerat ipsum modi modi. Ipsum consectetur etincidunt labore adipisci neque quiquia tempora. Labore quisquam velit sed amet aliquam dolore sit. Quaerat dolor eius eius velit neque voluptatem tempora.",
        "Dolore quiquia quisquam aliquam quaerat quisquam eius. Ipsum velit non numquam ipsum adipisci. Numquam quiquia dolore adipisci. Dolor est dolorem sed porro tempora dolorem aliquam. Magnam quaerat aliquam dolore voluptatem. Velit non dolore quaerat sed. Aliquam etincidunt numquam adipisci tempora quisquam amet dolorem. Est quaerat quisquam eius neque neque magnam consectetur. Ut voluptatem dolore tempora dolor. Consectetur neque non dolore consectetur neque.",
    ]
    return render_template(
        "wiki/article.html",
        id=id,
        thisPage="Wiki",
        cards=cards,
        navBarLinks=navBarLinks,
        content=content,
        lorem=lorem,
    )
