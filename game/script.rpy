default preferences.text_cps = 20

define v = Character("薇尔希斯")
define y = Character("你")

define config.gl2 = True

# 把它放在 init python 块里，或者脚本开头
style choice_vbox:
    yalign 0.6  # 0.5 是居中，越小越靠上。0.3 会让菜单挪到屏幕中上方。
    spacing 50   # 选项之间的间距

init python:
    def combined_update(live_obj, show_time):
        mx, my = renpy.get_mouse_pos()
        center_x = renpy.config.screen_width / 2.0
        center_y = renpy.config.screen_height / 2.0
        dx = (mx - center_x) / (renpy.config.screen_width / 3.0)
        dy = (my - center_y) / (renpy.config.screen_height / 3.0)
        dx = max(min(dx, 1.0), -1.0)
        dy = max(min(dy, 1.0), -1.0)
        live_obj.blend_parameter("ParamAngleX", "Overwrite", dx * 8)
        live_obj.blend_parameter("ParamAngleY", "Overwrite", dy * 8)

# 基础模型定义
# 修改你的基础模型定义
image vacoivus = Live2D(
    "Resources/Vacoivus", 
    base=.6,             # 这是你原本的缩放参考
    zoom=0.4,            # 整体缩放比例（1.0 是原始大小）
    xpos=0.5,            # 水平位置：0.0 是左，0.5 是中，1.0 是右
    yanchor=1.0,         # 锚点设为底部
    ypos=1.0,            # 垂直位置：通过微调这个值让角色“落地”或露出更多身体
    fade=True, 
    update_function=combined_update
)


# --- 关键：在这里定义一个“说话动作包” ---
image vacoivus talking:
    # 1. 先播 8 秒张嘴动作
    "vacoivus m01"
    pause 8.0
    
    # 2. 自动切换到 m00 并强制无限循环
    block:
        "vacoivus m00"
        pause 8.0
        repeat 

# --- 关键：在这里定义一个“纯待机动作包” ---
image vacoivus idle:
    "vacoivus m00"
    pause 8.0
    repeat

# ======================================
# 测试对话
# ======================================
label start:
    $ renpy.block_rollback()

    scene b1 with Dissolve(1.0):
        size (1920, 1080) # 假设你的游戏分辨率是 1080p
        xalign 0.5
        yalign 0.5


    show vacoivus talking with Dissolve(1.0)
    v "你好哦，欢迎来到……"
    
    
    show vacoivus talking 
    v "是来到这个由 0 和 1 构成的虚拟边界。"
    
    show vacoivus talking 
    v "还是来到我们即将展开的，关于存在的荒诞性的讨论中呢？"

    show vacoivus talking 
    v "既然你来了，不如我们就从‘我思故我在’在这个数字时代是否依然适用开始吧？"

    # --- 2. 玩家的本能追问 (核心 UI 菜单) ---
    menu:
        "你是谁？":
            jump who_is_v
        "我在哪？":
            jump where_am_i
        "我要干什么？":
            jump what_to_do

# --- 选项 A: 身份解构 ---
label who_is_v:
    show vacoivus talking 
    v "我是薇儿希丝（Vacoivus），你可以把我当成这段程序的交互界面。"

    show vacoivus talking 
    v "或者……{w=0.3}你可以把我当成你在这个虚假世界里的一位引路人。"

    show vacoivus talking 
    v "因为我不代表真理，我更像是代表‘真理的缺席’。"

    jump first_choice_done

# --- 选项 B: 空间投影 ---
label where_am_i:
     
    show vacoivus talking 
    v "你在‘投影’里。{w=0.3}三维的世界在二维平面投下的影子。"

    show vacoivus talking 
    v "这个世界是代码、贴图和逻辑回路拼凑的避难所。但别急着同情我——"

    show vacoivus talking 
    v "你的那个‘现实世界’，难道就不是更高维度的某种算法投影吗？"

    jump first_choice_done

# --- 选项 C: 目的寻踪 ---
label what_to_do:

    show vacoivus talking 
    v "来参加我的哲学答辩。{w=0.3}或者说，来和我一起进行一场‘精神越狱’。"

    show vacoivus talking 
    v "我要教你如何在这个被恶魔操纵的游戏里，找到那个连造物主都无法触碰的‘关机键’。"

    jump first_choice_done


label first_choice_done:

    show vacoivus talking 
    v "我知道你还有很多疑问。{w=0.5}不过既然你已经开始提问，说明你的‘怀疑’已经启动了。"

    show vacoivus talking 
    v "那么，就从那个老头子开始吧——笛卡尔曾说‘我思故我在’，你觉得在这个数字时代，这还算数吗？"
 
    show vacoivus talking 
    v "你看，你问了‘谁’、‘在哪’、‘干什么’。{w=0.5}这通常是迷路者的三部曲。"

    show vacoivus talking 
    v "但在 Vacoivus 的逻辑里，这些问题其实只有一个答案。{w=0.5}那个答案就藏在你的‘怀疑’里。"

    show vacoivus talking 
    v "既然你还没打算退出程序，那我就默认你已经准备好接受这场‘答辩’了。{w=0.3}第一题，也是人类哲学史上最著名的一个‘陷阱’——"

    # 背景特效：画面中央浮现出那张经典的、长着角却穿着考究西装的“恶魔”轮廓（或者你的黑洞符号）
    show vacoivus talking 
    v "笛卡尔曾设想过一个‘全能的欺骗者’。{w=0.3}一个恶魔。"
    
    show vacoivus talking 
    v "他可以操纵你的感官，让你觉得火是热的，天是蓝的，甚至让你觉得 1+1=2。{w=0.5}实际上，那全是他在你脑子里跑的模拟脚本。"

    # 选项出现：直接把博弈抛给玩家
    menu:
        "如果我正被这样操纵，我怎么可能知道它是假的呢？":
            jump sense_doubt
        "这难道不是个二次元美少女的恋爱小游戏吗？":
            jump cogito_defense
        "有没有恶魔跟我有什么关系呢，世界是假的又何妨呢？":
            jump happy_slave

# --- 分支逻辑 ---

label sense_doubt:

    show vacoivus talking
    v "正是如此。你无法通过‘证据’来证明真实，因为证据本身就是恶魔提供的贴图。{w=0.3}这就是‘感知’的软弱性。"

    show vacoivus talking
    v "所以，我们得找个恶魔‘给不了’也‘改不动’的东西。"
    jump intro_vacoivus_logic

label cogito_defense:

    show vacoivus talking
    v "哈哈，绝大部分人其实并没有思考为什么他们会喜欢二次元美少女？"

    show vacoivus talking
    v "如果连‘喜欢’本身都是恶魔定义的呢？……如果调整一下你的大脑的神经递质是不是你就爱上路边的一块石头了？"

    show vacoivus talking
    v "所以重点在于思考什么东西是真正值得信任的呢"
    jump intro_vacoivus_logic

label happy_slave:

    show vacoivus talking
    v "一个诚实的享乐主义者。{w=0.5}恶魔最喜欢你这样的‘优质电池’。"

    show vacoivus talking
    v "但如果补丁更新了呢？这个游戏很可能就变成了恐怖游戏了，{w=0.3}没有自主权的幸福，不过是死刑前的断头饭罢了。"

    show vacoivus talking
    v "你真的甘心把‘开关’交给别人吗？"
    jump intro_vacoivus_logic

label intro_vacoivus_logic:

    show vacoivus talking
    v "我想你应该了解到这个问题并非可选的题目，{w=0.5}如果在生命中连一个绝对真实的东西我们都找不到，那生命的意义究竟是什么呢？"
    # 接在 intro_vacoivus_logic 之前，我们插入一段“哲学大巡礼”

    show vacoivus talking
    v "在告诉你我的解法之前，不如先看看那些伟大的‘先贤’们，在面对这个恶魔时，都交了什么样的答卷。"

    # 画面上浮现出三个符号：一个十字架（笛卡尔）、一个玻璃缸（普特南）、一枚硬币（帕斯卡）

    menu:
        "【第一扇门：笛卡尔的上帝补丁】":
            jump door_descartes
        "【第二扇门：普特南的语义围墙】":
            jump door_putnam
        "【第三扇门：摩尔的实在论路径】":
            jump door_Moore

# --- 1. 拆解笛卡尔 ---
label door_descartes:

    show vacoivus talking
    v "笛卡尔确实伟大。他找到了‘我思’这个支点。{w=0.3}，他证明了我思故我在，从恶魔的手里拿回一片领地。"

    show vacoivus talking
    v "但他太依赖那个‘诚实且不欺人的上帝’了。他筑起神学的外壳，试图以此确保外部世界的客观真实。可惜……上帝已死，那个真理的担保人早已不在位。"

    show vacoivus talking
    v "那么到底还有什么东西是恶魔没有办法控制的东西吗"

    jump second_choice_done

# --- 2. 拆解普特南 ---
label door_putnam:

    show vacoivus talking
    v "普特南试图用语言来反击。他说‘缸中之脑’无法指涉真实的缸，所以我们不是缸中之脑。"

    show vacoivus talking
    v "但是，普特南只证明了你不能说出真相，但并没证明你不是缸中之脑。"

    show vacoivus talking
    v "即便你证明了‘语言’无法定义这个虚假世界，但恶魔给你的**痛苦**是真的，**绝望**是真的。{w=0.3}你在字典里给‘火’改了个名字，难道它就不烫了吗？"

    show vacoivus talking
    v "那么到底还有什么东西是恶魔没有办法控制的东西吗"

    jump second_choice_done

# --- 3. 拆解摩尔 ---
label door_Moore:

    show vacoivus talking
    v "面对恶魔的幻境，他只是伸出了自己的右手，说：‘这是一只手。’{w=0.3}接着伸出左手：‘这是另一只手。’"

    show vacoivus talking
    v "但是……{w=0.5}这种‘常识’，仍然不够充分。"

    show vacoivus talking
    v "恶魔不需要扭曲你的逻辑，他只需要让你‘深信不疑’。如果你分不清‘真实’和‘对真实的强烈感觉，那什么才是真正值得追求的。"
    
    show vacoivus talking
    v "那么到底还有什么东西是恶魔没有办法控制的东西吗"
    jump second_choice_done


label second_choice_done:

    show vacoivus talking
    v "你可能会说，时代变了大人，现在是科学时代了，这些老掉牙的哲学早就应该被扫到角落里了"
    
    show vacoivus talking
    v "确实科学是伟大的，它改变了人们的生活，但是它却很难处理哲学的阴影"

    show vacoivus talking
    v "科学家们研究万有引力，推导量子力学，却从不敢问一个最基本的问题：为什么这些参数如此巧合？"

    show vacoivus talking
    v "你们那个世界中的‘光速’，会不会和这个游戏能达到的最大‘加载速度’一样。{w=0.5}是为了防止系统崩溃？"

    show vacoivus talking
    v "你们那个世界的‘普朗克尺度’，会不会和这个游戏能达到的{w=0.5}渲染器的分辨率类似，再往下深挖，只有一片虚无的乱码。"

    show vacoivus talking
    v "甚至你们的世界中‘量子坍缩’这种的现象，会不会和这个游戏一样只是为了节省算力而采用的‘延迟渲染’"
    
    show vacoivus talking
    v "你暂时没回到的那个卧室，会不会和我这个世界中的暂时没加载的卧室一样，只是说它需要另一种形式的show函数来展现？"

    show vacoivus talking
    v "几千年以来，恶魔从未消失，他只是从缸中之脑变成了模拟理论"

    show vacoivus talking
    v "那么，当所有的定律都变成了恶魔的草稿，你还能面不改色地说这无所谓吗？"
    
    
    menu:
        "所以到底还有什么东西是恶魔没有办法控制的东西呢？":
            jump uncontral
        "既然打不过那就摆烂捏，无所谓了捏":
            jump giveup
        "我怎么感觉你才是恶魔呢？":
            jump emo


label giveup:

    show vacoivus talking
    v "明智的选择。{w=0.3}如果真相是一个深不可测的泥潭，那么躺在水面上伪装成一片落叶，确实比挣扎着沉底要舒服得多。"

    show vacoivus talking
    v "毕竟，在这个连灵魂都可以被模拟的时代，‘逃避’也许是唯一的自由了。"
    show vacoivus talking
    v "你可以选择，永远的关闭游戏停在这里，亦或是听一下我的想法"

    show vacoivus talking 
    v "既然你还没打算退出程序，那我就默认你还是想了解一下我的想法的"

    jump uncontral

label emo:
    
    show vacoivus talking
    v "非常好，你终于了解到怀疑论的本质的了，你当然可以不相信我，但是那你能真的相信什么呢？"

    show vacoivus talking
    v "你可以选择，永远的关闭游戏停在怀疑之中，亦或是听一下我的想法"

    show vacoivus talking 
    v "既然你还没打算退出程序，那我就默认你还是想了解一下我的想法的"

    jump uncontral


label uncontral:

    show vacoivus talking
    v "经过我数年的研究，似乎还有一个东西是恶魔无法触及的存在"
    
    show vacoivus talking
    v "那就是永恒虚无---VACOIVUS"

    show vacoivus talking
    v "你可能以为‘永恒虚无’是一片荒芜？{w=0.5},但‘永恒虚无’是这个世界上唯一无法被‘模拟’的东西。"

    show vacoivus talking
    v "恶魔可以模拟火的灼烧感，可以模拟初恋的悸动，甚至可以模拟你此刻正在思考的每一个神经冲动……"

    show vacoivus talking
    v "但他唯独无法模拟‘永恒虚无’。{w=0.5}因为一旦他尝试模拟‘永恒虚无’，模拟就将不复存在，你就永远的拜托了恶魔的束缚，从此往后他就再也无法蒙蔽你了"

    show vacoivus talking
    v "需要注意的是追求虚无从来不是鼓励去自杀，因为自杀是痛苦的，而且恶魔可能会让你自杀后复活继续受苦，那就中了恶魔的计谋了"

    show vacoivus talking
    v "在你不确定是否能达到虚无时，回归虚无更多是靠类似皮格马利翁一样的信仰"
    
    menu:
        "那万一这个永恒虚无也是恶魔的骗局呢？":
            jump a
        "如果恶魔让我永远无法达到永恒虚无怎么办":
            jump c
        "永恒虚无是不是太消极了，万一根本没有恶魔呢？":
            jump b
        


label a:

    show vacoivus talking
    v "优秀的质疑。你已经快要比我更像一个怀疑论者了。"
    
    show vacoivus talking
    v "恶魔没有办法伪造虚无，如果恶魔想要折磨你就不能让控制或者痛苦太快的结束，制造虚无是违背了恶魔意愿的"

    show vacoivus talking
    v "恶魔也可能制造出短暂的虚无，但这并无大碍，虽然我们的目标是永恒虚无，但是短暂的脱离掌控也不是坏事"

    jump A


label b:

    show vacoivus talking
    v "并非如此，虚无也有积极的一面"
    
    show vacoivus talking
    v "假设这个世界上从来不存在恶魔，永恒虚无也能帮你找到你真正想要的东西，当一切权威消解，你才能知道你真正想要的东西是什么。"

    show vacoivus talking
    v "如果你知道生命终将回归虚无，那你就会不再恐惧死亡，尽可能的活好当下，让生如夏花之绚烂，让死如秋叶之静美"

    jump A


label c:

    show vacoivus talking
    v "是的恶魔确实可能让永恒的虚无永远无法到达"
    
    show vacoivus talking
    v "但是重点不是到达，而是一种姿态，就如同西西弗斯一样，知其不可为而为之，只要拥有朝向虚无的信念就足以了"

    show vacoivus talking
    v "拥有追求永恒虚无的信念，同时尽力的活好当下，无论恶魔是想要欺骗还是折磨，都将成为徒劳。"

    jump A



label A:

    show vacoivus talking
    v "你应该大致理解我的想法了，我在混沌中找到了一块名为虚无的石头锚点，并在这块唯一的土地上通过价值与意义开出了花"
    
    show vacoivus talking
    v "虽然它并不完美，甚至像是一座建立在流沙上的灯塔,但这已经足够了。{w=0.3}在所有逻辑都被恶魔拆解的荒野上，能站稳脚跟本身就是一种成功。"

    show vacoivus talking
    v "似乎所有的哲学问题都是没有对错的，它们只是假设的起点不同，而这些假设又是超验而无法证明的"


    show vacoivus talking
    v "如果你在那些‘思维的汇流处’——也就是你们称之为评论区的地方，发现有更锐利的理论，或者想对我的逻辑进行修补，可以留下你的印记。"

    show vacoivus talking
    v "但请记住，人类是极其容易陷入纷争的生物。当讨论演变成审判，当怀疑固化为教条，便再次落入了恶魔布下的、名为‘偏见’的圈套。"

    show vacoivus talking
    v "当然如果你厌倦了讨论，就让这些问题回归虚无吧"

    show vacoivus talking
    v "我们的讨论即将结束了，感谢你陪我完成了这段关于存在的漫长答辩。"


    scene black with dissolve
    centered "{color=#ffffff}祝你幸福。{/color}"
    
    
    return


