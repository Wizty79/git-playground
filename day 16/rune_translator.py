from riimut import younger_futhark, elder_futhark, medieval_futhork, futhorc

# From Old Groms runestone.
content1 = "auk tani karþi kristna"
result1 = younger_futhark.letters_to_runes(content1)
print result1 # ᛅᚢᚴ:ᛏᛅᚾᛁ:ᚴᛅᚱᚦᛁ:ᚴᚱᛁᛋᛏᚾᛅ

# From 4th century axe in Jutland
content2 = "wagagastiz alu wihgu sikijaz aiþalataz"
result2 = elder_futhark.letters_to_runes(content2)
print result2 # ᚹᚨᚷᚨᚷᚨᛋᛏᛁᛉ:ᚨᛚᚢ:ᚹᛁᚻᚷᚢ:ᛋᛁᚲᛁᛃᚨᛉ:ᚨᛁᚦᚨᛚᚨᛏᚨᛉ

# From Lord's Prayer, in Old Norse.
content3 = "Faðer uor som ast i himlüm, halgað warðe þit nama"
result3 = medieval_futhork.letters_to_runes(content3)
print result3 # ᚠᛆᚦᚽᚱ:ᚢᚮᚱ:ᛋᚮᛘ:ᛆᛋᛏ:ᛁ:ᚼᛁᛘᛚᚢᛘ,:ᚼᛆᛚᚵᛆᚦ:ᚠᛆᚱᚦᚽ:ᚦᛁᛏ:ᚿᛆᛘᛆ

# From 8th century Franks Casket, in late West Saxon.
content4 = "fisc.flodu.ahofonferg | enberig |"
result4 = futhorc.letters_to_runes(content4)
print result4 # ᚠᛁᛋᚳ.ᚠᛚᚩᛞᚢ.ᚪᚻᚩᚠᚩᚾᚠᛖᚱᚷ:|:ᛖᚾᛒᛖᚱᛁᚷ:|

# All four dialects contain runes_to_letters function.
from riimut import younger_futhark

runic = "ᛅᚢᚴ:ᛏᛅᚾᛁ:ᚴᛅᚱᚦᛁ:ᚴᚱᛁᛋᛏᚾᛅ"
latin = younger_futhark.runes_to_letters(runic)

print latin # "auk tani karþi kristna"

#remember to run pip install riimut
