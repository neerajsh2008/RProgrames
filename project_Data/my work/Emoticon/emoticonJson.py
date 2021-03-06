# -*- coding: utf-8 -*-

import simplejson as json
z={
"😄":" Smiling Face With Open Mouth And Smiling Eyes",
"😃":" Smiling Face With Open Mouth",
"😀":" Grinning Face",
"😊":" Smiling Face With Smiling Eyes",
"☺ ":"White Smiling Face",
"😉":" Winking Face",
"😍":" Smiling Face With Heart-Shaped Eyes",
"😘":" Face Throwing A Kiss",
"😚":" Kissing Face With Closed Eyes",
"😗":" Kissing Face",
"😙":" Kissing Face With Smiling Eyes",
"😜":" Face With Stuck-Out Tongue And Winking Eye",
"😝":" Face With Stuck-Out Tongue And Tightly-Closed Eyes",
"😛":" Face With Stuck-Out Tongue",
"😳":" Flushed Face",
"😁":" Grinning Face With Smiling Eyes",
"😔":" Pensive Face",
"😌":" Relieved Face",
"😒":" Unamused Face",
"😞":" Disappointed Face",
"😣":" Persevering Face",
"😢":" Crying Face",
"😂":" Face With Tears Of Joy",
"😭":" Loudly Crying Face",
"😪":" Sleepy Face",
"😥":" Disappointed But Relieved Face",
"😰":" Face With Open Mouth And Cold Sweat",
"😅":" Smiling Face With Open Mouth And Cold Sweat",
"😓":" Face With Cold Sweat",
"😩":" Weary Face",
"😫":" Tired Face",
"😨":" Fearful Face",
"😱":" Face Screaming In Fear",
"😠":" Angry Face",
"😡":" Pouting Face",
"😤":" Face With Look Of Triumph",
"😖":" Confounded Face",
"😆":" Smiling Face With Open Mouth And Tightly-Closed Eyes",
"😋":" Face Savouring Delicious Food",
"😷":" Face With Medical Mask",
"😎":" Smiling Face With Sunglasses",
"😴":" Sleeping Face",
"😵":" Dizzy Face",
"😲":" Astonished Face",
"😟":" Worried Face",
"😦":" Frowning Face With Open Mouth",
"😧":" Anguished Face",
"😈":" Smiling Face With Horns",
"👿":" Imp",
"😮":" Face With Open Mouth",
"😬":" Grimacing Face",
"😐":" Neutral Face",
"😕":" Confused Face",
"😯":" Hushed Face",
"😶":" Face Without Mouth",
"😇":" Smiling Face With Halo",
"😏":" Smirking Face",
"😑":" Expressionless Face",
"👲":" Man With Gua Pi Mao",
"👳":" Man With Turban",
"👮":" Police Officer",
"👷":" Construction Worker",
"💂":" Guardsman",
"👶":" Baby",
"👦":" Boy",
"👧":" Girl",
"👨":" Man",
"👩":" Woman",
"👴":" Older Man",
"👵":" Older Woman",
"👱":" Person With Blond Hair",
"👼":" Baby Angel",
"👸":" Princess",
"😺":" Smiling Cat Face With Open Mouth",
"😸":" Grinning Cat Face With Smiling Eyes",
"😻":" Smiling Cat Face With Heart-Shaped Eyes",
"😽":" Kissing Cat Face With Closed Eyes",
"😼":" Cat Face With Wry Smile",
"🙀":" Weary Cat Face",
"😿":" Crying Cat Face",
"😹":" Cat Face With Tears Of Joy",
"😾":" Pouting Cat Face",
"👹":" Japanese Ogre",
"👺":" Japanese Goblin",
"🙈":" See-No-Evil Monkey",
"🙉":" Hear-No-Evil Monkey",
"🙊":" Speak-No-Evil Monkey",
"💀":" Skull",
"👽":" Extraterrestrial Alien",
"💩":" Pile Of Poo",
"🔥":" Fire",
"✨ ":"Sparkles",
"🌟":" Glowing Star",
"💫":" Dizzy Symbol",
"💥":" Collision Symbol",
"💢":" Anger Symbol",
"💦":" Splashing Sweat Symbol",
"💧":" Droplet",
"💤":" Sleeping Symbol",
"💨":" Dash Symbol",
"👂":" Ear",
"👀":" Eyes",
"👃":" Nose",
"👅":" Tongue",
"👄":" Mouth",
"👍":" Thumbs Up Sign",
"👎":" Thumbs Down Sign",
"👌":" Ok Hand Sign",
"👊":" Fisted Hand Sign",
"✊ ":"Raised Fist",
"👋":" Waving Hand Sign",
"✋ ":"Raised Hand",
"👐":" Open Hands Sign",
"👆":" White Up Pointing Backhand Index",
"👇":" White Down Pointing Backhand Index",
"👉":" White Right Pointing Backhand Index",
"👈":" White Left Pointing Backhand Index",
"🙌":" Person Raising Both Hands In Celebration",
"🙏":" Person With Folded Hands",
"☝ ":"White Up Pointing Index",
"👏":" Clapping Hands Sign",
"💪":" Flexed Biceps",
"🚶":" Pedestrian",
"🏃":" Runner",
"💃":" Dancer",
"👫":" Man And Woman Holding Hands",
"👪":" Family",
"👬":" Two Men Holding Hands",
"👭":" Two Women Holding Hands",
"💏":" Kiss",
"💑":" Couple With Heart",
"👯":" Woman With Bunny Ears",
"🙆":" Face With Ok Gesture",
"🙅":" Face With No Good Gesture",
"💁":" Information Desk Person",
"🙋":" Happy Person Raising One Hand",
"💆":" Face Massage",
"💇":" Haircut",
"💅":" Nail Polish",
"👰":" Bride With Veil",
"🙎":" Person With Pouting Face",
"🙍":" Person Frowning",
"🙇":" Person Bowing Deeply",
"🎩":" Top Hat",
"👑":" Crown",
"👒":" Womans Hat",
"👟":" Athletic Shoe",
"👞":" Mans Shoe",
"👡":" Womans Sandal",
"👠":" High-Heeled Shoe",
"👢":" Womans Boots",
"👕":" T-Shirt",
"👔":" Necktie",
"👚":" Womans Clothes",
"👗":" Dress",
"🎽":" Running Shirt With Sash",
"👖":" Jeans",
"👘":" Kimono",
"👙":" Bikini",
"💼":" Briefcase",
"👜":" Handbag",
"👝":" Pouch",
"👛":" Purse",
"👓":" Eyeglasses",
"🎀":" Ribbon",
"🌂":" Closed Umbrella",
"💄":" Lipstick",
"💛":" Yellow Heart",
"💙":" Blue Heart",
"💜":" Purple Heart",
"💚":" Green Heart",
"❤":"Heavy Black Heart",
"💔":" Broken Heart",
"💗":" Growing Heart",
"💓":" Beating Heart",
"💕":" Two Hearts",
"💖":" Sparkling Heart",
"💞":" Revolving Hearts",
"💘":" Heart With Arrow",
"💌":" Love Letter",
"💋":" Kiss Mark",
"💍":" Ring",
"💎":"Gem Stone",
"👤":"Bust In Silhouette",
"👥":"Busts In Silhouette",
"💬":"Speech Balloon",
"👣":"Footprints",
"💭":"Thought Balloon",
":-)":"Smiley or happy",
":)":"Smiley or happy",
":D":"Smiley or happy",
":o)":"Smiley or happy",
":]":"Smiley or happy" ,
":3":"Smiley or happy",
":c)":"Smiley or happy",
":>":"Smiley or happy" ,
"=]":"Smiley or happy",
"8)":"Smiley or happy",
"=)":"Smiley or happy" ,
":}":"Smiley or happy",
":^)":"Smiley or happy",
":っ)":"Smiley or happy" ,
":-D":"Laughing or big grin or laugh with glasses",
"8-D":"Laughing or big grin or laugh with glasses",
"8D":"Laughing or big grin or laugh with glasses",
"x-D":"Laughing or big grin or laugh with glasses",
"xD":"Laughing or big grin or laugh with glasses",
"X-D":"Laughing or big grin or laugh with glasses",
"XD":"Laughing or big grin or laugh with glasses",
"=-D":"Laughing or big grin or laugh with glasses",
"=D":"Laughing or big grin or laugh with glasses",
":-))":"Very happy or double chinn",
">:[":"Frown or sad",
":-(":"Frown or sad",
":(":"Frown or sad",
":-c":"Frown or sad",
":c":"Frown or sad",
":-<":"Frown or sad",
":っC":"Frown or sad",
":<":"Frown or sad",
":-[":"Frown or sad",
":[":"Frown or sad",
":{":"Frown or sad",
";(":"Winky frowny or used to signify sadness or with a bit of sarcasm or It is easily misunderstood",
":-||":"Angrry",
":@":"Angry",
">:(":"Angry",
":'-(":"Crying",
":'(":"Crying",
":'-)":"Tears of happiness",
":')":"Tears of happiness",
"D:<":"Horror or disgust or sadness or great dismay",
">:O":"Surprise or shock or yawn",
":-O":"Surprise or shock or yawn",
":*":"Kiss",
":^*":"Kiss",
"( '}{' )":"Kiss",
";-)":"Wink or smirk",
";)":"Wink or smirk",
"*-)":"Wink or smirk",
"*)":"Wink or smirk",
";-]":"Wink or smirk",
";]":"Wink or smirk",
";D":"Wink or smirk",
";^)":"Wink or smirk",
":-,":"Wink or smirk",
" >:/":"Skeptical or annoyed or undecided or uneasy or hesitant",
":-/":"Skeptical or annoyed or undecided or uneasy or hesitant",
":-.":"Skeptical or annoyed or undecided or uneasy or hesitant",
 ":/":"Skeptical or annoyed or undecided or uneasy or hesitant",
"=/":"Skeptical or annoyed or undecided or uneasy or hesitant",
":L":"Skeptical or annoyed or undecided or uneasy or hesitant",
"=L":"Skeptical or annoyed or undecided or uneasy or hesitant",
":S":"Skeptical or annoyed or undecided or uneasy or hesitant",
">.<":"Skeptical or annoyed or undecided or uneasy or hesitant",
":|":"Straight face or no expression or indecision",
":-|":"Straight face or no expression or indecision",
":$":"Embarrassed or blushing",
":-X":"Sealed lips or wearing braces",
":X":"Sealed lips or wearing braces",
":-#":"Sealed lips or wearing braces",
":#":"Sealed lips or wearing braces",
"O:-)":"Angel or saint or innocent",
"0:-3":"Angel or saint or innocent",
"0:3":"Angel or saint or innocent",
"0:-)":"Angel or saint or innocent",
"0:)":"Angel or saint or innocent",
"0;^)":"Angel or saint or innocent",
">:)":"Evil",
">;)":"Evil",
">:-)":"Evil",
"}:-)":"Devilish",
"}:)":"Devilish",
"3:-)":"Devilish",
"3:)":"Devilish",
"|;-)":"Cool or bored or yawning",
"|-O":"Cool or bored or yawning",
":-J":"Tongue-in-cheek",
":-&":"Tongue-tied",
":&":"Tongue-tied",
"#-)":"Partied all night",
"%-)":"Drunk",
"%)":"confused",
":-###..":"Being sick",
":###..":"Being sick",
"<:-|":"Dumb or dunce-like",
"ಠ_ಠ":"Look of disapproval",
"<*)))-{":"Fish",
"><(((*>":"something's fishy",
"><>":"Christian fish",
"o/":"Cheer or Yay yay",
"*0/*":"Cheerleader",
"@}-;-'---":"Rose",
"@>-->--":"Rose",
"*<|:-)":"Santa Claus",
"=:o]":"Bill Clinton",
"<3":"Heart",
"</3":"broken-heart",
"(>_<)":"Troubled",
"(>_<)>":"Troubled",
"(';')":"Baby",
"<コ:彡":"Squid",
"(^。^)y-.。o○":"Smoking",
"(-。-)y-゜゜゜":"Smoking",
"(-_-)zzz":"Sleeping",
"(^_-)":"Wink",
"(^_-)-☆":"Wink",
"((+_+))　(+o+)":"Confused",
"(゜゜) (゜-゜)":"Confused",
"(゜.゜)":"Confused",
"(゜_゜)":"Confused",
"(゜_゜>)":"Confused",
"(゜レ゜)":"Confused",
"☆彡":"Shooting star",
"(ー_ー)!!　(-.-)　(-_-)":"Shame",
"( 一一)　(；一_一)":"Shame",
"(=_=)":"Tired",
"~>゜)～～～　":"Snake",
"～゜・_・゜～　":"Bat",
"(=^・^=)　(=^・・^=)　=^_^=":"Cat",
"(..)":"looking down",
"(._.)":"Looking down",
"(・・?":"Confusion",
"(?_?)":"Confusion",
"●～*":"Bomb",
"＼(~o~)／":"Excited",
"＼(^o^)／":"Excited",
"＼(-o-)／":"Excited",
"ヽ(^。^)ノ":"Excited",
"ヽ(^o^)丿":"Excited",
"(*^0^*)":"Excited",
"(*_*)":"Amazed",
"(*_*;":"Amazed",
"(+_+)":"Amazed",
"(@_@)":"Amazed",
"(@_@。":"Amazed",
"(＠_＠;)　＼(◎o◎)／！":"Amazed",
"(*^^)v":"Laughing or cheerful",
"(^^)v":"Laughing or cheerful",
"(^_^)v":"Laughing or cheerful",
"(＾▽＾)":"Laughing or cheerful",
"（・∀・）":"Laughing or cheerful",
"（　´∀｀）":"Laughing or cheerful",
"（⌒▽⌒）":"Laughing or cheerful",
"（＾ｖ＾）":"Laughing or cheerful",
"（’-’*)":"Laughing or cheerful", 	
"((d[-_-]b))":"Headphones or listening to drum and bass music",
"(^0_0^)":"Eyeglasses",
"（●＾o＾●）":"Happy",
"（＾ｖ＾）":"Happy",
"（＾ｕ＾）":"Happy",
"（＾◇＾）":"Happy",
"( ^)o(^ )":"Happy",
"(^O^)":"Happy",
"(^o^)":"Happy",
"(^○^)":"Happy",
")^o^(":"Happy",
"(*^▽^*)":"Happy",
"(✿◠‿◠)":"Happy",
"（￣ー￣）":"Grinning",
"（￣□￣；）":"Surprised",
"(*^3^)/~☆":"Blowing a kiss",
}

fout=open('emoticon_words_Json.json','w')
content=json.dumps(z)
fout.write(content)
fout.close()

#open file for reading Data
fin=open("emoticon_words_Json.json","r")
data=fin.read()
fin.close()
x=json.loads(data)

print len(x.keys())



