from discord.ext import commands
import discord, datetime, time
from multilingual import *


class Information(commands.Cog):
    """色々な情報の設定をするよ!"""
    def __init__(self, bot):
        self.bot = bot  # type: commands.Bot

    async def cog_before_invoke(self, ctx):
        if str(ctx.author.id) in self.bot.BAN:
            await ctx.send(f"あなたのアカウントはBANされています(´;ω;｀)\nBANに対する異議申し立ては、公式サーバーの <#{self.bot.datas['appeal_channel']}> にてご対応させていただきます。")
            raise commands.CommandError("Your Account Banned")

    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"引数が不足しているよ!.\n使い方: `{self.bot.PREFIX}{ctx.command.usage}`\n詳しくは `{self.bot.PREFIX}help {ctx.command.qualified_name}`")
        else:
            await ctx.send(f"エラーが発生しました。管理者にお尋ねください。\n{error}")

    @commands.command(aliases=["inv"], usage="invite", description="BOTの招待リンクを表示するよ!是非いろんなサーバーに招待してね!。")
    async def invite(self, ctx):
        text = f"__**BOTの招待用URL**__:\n{self.bot.datas['invite']}\n" \
               f"__**サポート用サーバー(公式サーバー)**__:\n{self.bot.datas['server']}"
        await ctx.send(text)

    @commands.command(aliases=["about"], usage="info", description="BOTに関する情報を表示するよ!。")
    async def info(self, ctx):
        td = datetime.timedelta(seconds=int(time.time() - self.bot.uptime))
        m, s = divmod(td.seconds, 60); h, m = divmod(m, 60); d = td.days
        embed = discord.Embed(title="このBOTについて")
        embed.description = f"BOTをご使用いただき、ありがとうございます！\n" \
                            f"このBOTはMilkChocoをプレイする人達の、Discordサーバーのために `{self.bot.datas['author']}` によって作成されました。\n" \
                            f"詳しい使い方は `{ctx.prefix}help` で確認して下さい。\n" \
                            f"機能リクエストにもできる限り、ご対応させていただきます!"
        embed.add_field(name="ステータス", value=f"```導入サーバー数: {len(self.bot.guilds)}\nBOTが認識しているユーザー数:{len(self.bot.users)}```", inline=False)
        embed.add_field(name="稼働時間", value=f"{d}日 {h}時間 {m}分 {s}秒", inline=False)
        embed.add_field(name="各種URL", value=f"[BOT招待用URL]({self.bot.datas['invite']}) | [サポート用サーバー]({self.bot.datas['server']}) | [公式サイト]({self.bot.datas['web']})", inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=["pg"], usage="ping", description="BOTの反応速度を計測するよ!。")
    async def ping(self, ctx):
        await ctx.send(f"反応速度: `{int(self.bot.latency*1000)}`[ms]")

    @commands.command(usage="tos", description="BOTの利用規約を表示するよ!")
    async def tos(self, ctx):
        embed = discord.Embed(title="MilkCoffee 利用規約", color=0xcc66cc)
        embed.description = "この規約は,MafuWorldチーム(以下「当チーム」)が提供する,DiscordBOT「MilkCoffee」(以下「本サービス」)をユーザーの皆様(以下「利用者」)がご利用頂く際の取扱いにつき定めるものです。本規約に同意したうえで本サービスをご利用ください。"
        embed.add_field(name="第1条(定義)", value="""
    本規約上で使用する用語の定義は、次に掲げるとおりとします。
(1)当チーム
MilkCoffeeサービスを開発,提供するチーム
(2)本サービス
Discord内のMilkCoffeeBOT及び公式サイト,公式サーバーで提供される利用者へのサービス
(3)本コンテンツ
本サービス上で提供される文字、画像、ソフトウェアプログラム、コードコンテンツ等の総称
(4)本サイト
本サービスの説明が掲載されたウェブサイト
(5)知的財産
発明、考案、植物の新品種、意匠、著作物その他の人間の創造的活動により生み出されるもの(発見または解明がされた自然の法則または現象であって、産業上の利用可能性があるものを含む)、商標、商号その他事業活動に用いられる商品または役務を表示するもの及び営業秘密その他の事業活動に有用な技術上または営業上の情報
(6)知的財産権
特許権、実用新案権、育成者権、意匠権、著作権、商標権その他の知的財産に関して法令により定められた権利または法律上保護される利益に係る権利
        """, inline=False)
        embed.add_field(name="第2条(本規約への同意)", value="""
    1　利用者は、本利用規約に同意頂いた上で、本サービスを利用できるものします。
2　利用者が、本サービスの利用を開始した時点で、利用者と当チームとの間で、本規約の諸規定に従った利用契約が成立するものとします。
        """, inline=False)
        embed.add_field(name="第3条(規約の変更)", value="""
    1　当チームは、利用者の承諾を得ることなく、いつでも、本規約の内容を改定することができるものとし、利用者はこれを異議なく承諾するものとします。
2　当チームは、本規約を改定するときは、その内容について公式サーバーにより利用者に通知します。
3　前本規約の改定の効力は、当チームが前項により通知を行った時点から生じるものとします。
4　利用者は、本規約変更後、本サービスを利用した時点で、変更後の本利用規約に異議なく同意したものとみなされます。
        """, inline=False)
        embed.add_field(name="第4条(個人情報等の取り扱い)", value="本サービスが利用者の個人情報を求めることはなく、利用者間の個人情報に関する問題において一切の責任を負いません。", inline=False)
        embed.add_field(name="第5条(禁止行為)　", value="""
本サービスの利用に際し、当チームは、利用者に対し、次に掲げる行為を禁止します。当チームにおいて、利用者が禁止事項に違反したと認めた場合、利用者用の一時停止、退会処分その他当チームが必要と判断した措置を取ることができます。

(1)当チームまたは第三者の知的財産権を侵害する行為
(2)当チームまたは第三者の名誉・信用を毀損または不当に差別もしくは誹謗中傷する行為
(3)当チームまたは第三者の財産を侵害する行為、または侵害する恐れのある行為
(4)当チームまたは第三者に経済的損害を与える行為
(5)当チームまたは第三者に対する脅迫的な行為
(6)コンピューターウィルス、有害なプログラムを仕様またはそれを誘発する行為
(7)本サービス用インフラ設備に対して過度な負担となるストレスをかける行為
(8)当サイトのサーバーやシステム、セキュリティへの攻撃
(9)当チーム提供のインターフェース以外の方法で当チームサービスにアクセスを試みる行為
(10)Discord利用規約で禁止されている行為
(11)上記の他、当チームが不適切と判断する行為
        """, inline=False)
        embed.add_field(name="第6条(免責)", value="""
1　当チームは、本サービスの内容変更、中断、終了によって生じたいかなる損害についても、一切責任を負いません。
2　当チームは、利用者の本サービスの利用環境について一切関与せず、また一切の責任を負いません。
3　当チームは、本サービスが利用者の特定の目的に適合すること、期待する機能・商品的価値・正確性・有用性を有すること、利用者による本サービスの利用が利用者に適用のある法令または業界団体の内部規則等に適合すること、および不具合が生じないことについて、何ら保証するものではありません。
4　当チームは、本サービスが全ての端末に対応していることを保証するものではなく、本サービスの利用に供する端末の変更、アプリのバージョンアップ等に伴い、本サービスの動作に不具合が生じる可能性があることにつき、利用者はあらかじめ了承するものとします。当チームチーム、かかる不具合が生じた場合に当チームが行うプログラムの修正等により、当該不具合が解消されることを保証するものではありません。
5　利用者は、Discordの利用規約および運用方針の変更等に伴い、本サービスの一部又は全部の利用が制限される可能性があることをあらかじめ了承するものとします。
6　当チームは、本サービスを利用したことにより直接的または間接的に利用者に発生した損害について、一切賠償責任を負いません。
7　当チームは、利用者その他の第三者に発生した機会逸失、業務の中断その他いかなる損害(間接損害や逸失利益を含みます)に対して、当チームが係る損害の可能性を事前に通知されていたとしても、一切の責任を負いません。
8　第1項乃至前項の規定は、当チームに故意または重過失が存する場合又は契約書が消費者契約法上の消費者に該当する場合には適用しません。
9　前項が適用される場合であっても、当チームは、過失(重過失を除きます。)による行為によって利用者に生じた損害のうち、特別な事情から生じた損害については、一切賠償する責任を負わないものとします。　
10　利用者と他の利用者との間の紛争及びトラブルについて、当チームは一切責任を負わないものとします。利用者と他の利用者でトラブルになった場合でも、両者同士の責任で解決するものとし、当チームには一切の請求をしないものとします。
     """, inline=False)
        embed.add_field(name="第6条続き", value="""
11　利用者は、本サービスの利用に関連し、他の利用者に損害を与えた場合または第三者との間に紛争を生じた場合、自己の費用と責任において、かかる損害を賠償またはかかる紛争を解決するものとし、当チームには一切の迷惑や損害を与えないものとします。
12　利用者の行為により、第三者から当チームが損害賠償等の請求をされた場合には、利用者の費用(弁護士費用)と責任で、これを解決するものとします。当チームが、当該第三者に対して、損害賠償金を支払った場合には、利用者は、当チームに対して当該損害賠償金を含む一切の費用(弁護士費用及び逸失利益を含む)を支払うものとします。
13　利用者が本サービスの利用に関連して当チームに損害を与えた場合、利用者の費用と責任において当チームに対して損害を賠償(訴訟費用及び弁護士費用を含む)するものとします。
        """, inline=False)
        embed.add_field(name="第7条(権利譲渡の禁止)", value="""
1　利用者は、予め当チームの書面による承諾がない限り、本規約上の地位および本規約に基づく権利または義務の全部または一部を第三者に譲渡してはならないものとします。
2　当チームは、本サービスの全部または一部を当チームの裁量により第三者に譲渡することができ、その場合、譲渡された権利の範囲内で利用者のアカウントを含む、本サービスに係る利用者の一切の権利が譲渡先に移転するものとします。
        """, inline=False)
        embed.add_field(name="第8条(分離可能性)", value="""
本規約のいずれかの条項又はその一部が、消費者契約法その他の法令等により無効又は執行不能と判断された場合であっても、本規約の残りの規定及び一部が無効又は執行不能と判断された規定の残りの部分は、継続して完全に効力を有するものとします。
        """, inline=False)
        embed.add_field(name="第9条(当チームへの連絡方法)", value="""
本サービスに関する利用者の当チームへのご連絡・お問い合わせは、公式サーバーまたは当チームが指定する方法により行うものとします。
        """, inline=False)
        embed.add_field(name="第10条(準拠法)", value="""
本規約の有効性，解釈及び履行については，日本法に準拠し，日本法に従って解釈されるものとします。
        """, inline=False)
        embed.set_footer(text="施行日:2020年9月12日")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Information(bot))
