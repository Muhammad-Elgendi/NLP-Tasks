#  علامات الإسم
# قبلة حرف جر
# قبلها حرف نذاء زي يا

# التنوين
# قبلها الألف واللام
# التاء المربوطة

# الفعل الماضي يقبل التاء في اخرة
# الفعل المضارع يقبل قبله س او سوف
# الفعل الأمر يقبل الياء في اخرة ويدل علي الطلب

# علامات الفعل
# قد
# س
# سوف
# تاء التأنيث الساكنه تدخل علي الفعل الماض


# إن الفعل إذا كان مضارعا فلا بد أن يبتدئ بحرف من حروف المضارعة فلا يلزم من ذلك أن كل فعل ابتدأ بأحد هذه الحروف يكون فعلا مضارعا.

# وحروف المضارعة هي: الألف والنون والياء والتاء.
# يفعل
# يفاعل
# ينفعل
# يتفاعل
# يستفعل
# يفعلل
# يتفعلل
# 

# الحرف
# حروف الجر 
# حروف العطف

# الجملة الفعلية
# فعل فاعل مفعول بة
# الجملة الاسمية 
# مبتدا و خبر
# شبة جملة

# يقسم الكلام في اللغة العربية إلى اسم، وفعل، وحرف، ويتم استخدام أقسام الكلام في تكوين جمل مختلفة المعاني والدلالات،
#  بحيث تحوي هذه الجمل معنىً تامًا، وتقسم الجمل في اللغة العربية إلى جمل اسميه، وجمل فعلية،
#  أما الجملة الاسمية فهي التي تبدأ باسم وتتكون من المبتدأ والخبر الذي يخبر عنه،
#  والجملة الفعلية هي التي تبدأ بفعل، والتي تتكون من الفعل، والفاعل، والمفعول به، وهناك ما يسمى بأشباه الجمل
#  والتي لها استخدامات محددة وتعطي معنى إضافيًا إلى الجملة الأصلية يفيد في أعطاء معلومات حول الحدث في الجملة
# أنواع شبه الجملة في اللغة العربية تقسم شبه الجملة 
# إلى نوعين هما: شبه الجملة الظرفية: وهي تقسم إلى نوعين هما: الظرف الزماني:
#  ومن أمثلة ذلك ما يلي: رأيتك بعد الصلاة. سافرت أمس. زرتُك يوم الثلاثاء.
#  كلمتك قبل ساعة. الظرف المكاني: ومن أمثلة ذلك ما يلي: لعبنا قرب الشاطئ. وقفتُ عند الشجرة.
#  سقطتُ قرب الدرج. شبه الجملة من الجار والمجرور:
#   وهي تلك التي تتكون من حرف جر واسم مجرور مثل: سافرتُ إلى الشامِ كتبتُ بالقلم. رسمتُ بالفرشاة. دخلتُ من الباب.


# ألأفعال
# الأسماء ولو تشابة حاجة من الأفعال نشيلها من الأفعال
#  أسماء المكان والزمان و اسماء موصولة 


import re
from tkinter import *
elGr =['من','إلي','عن','علي','في','ب','ك','ل']
elAtf = ['و','ف','أو','ثم','أم','بل','لا','لكن','حتي']
elNasb = ['لن','أن','كي','حتي','ل','إذا','ف']
elGazm = ['لم','لما','إن','من','مهما','ما','أين','حيثما','متي']
elNedaa = ['يا','أيا','هيا','آ','أي','وا']
elTanween = ['ً','ٍ','ٌ']
zroofElzaman = ['حين','صباح','ظُهر','ساعة','سنة','أمس','متى','أيّانَ','أمسِ','الآنَ','مذْ','منذُ','بينما','ريثما','حيث']
zroofElmakan = ['فوق','تحت','أمام','وراء','حيث','دون','هنا','أيْنَ']
elmusool = ['الذي','التي','اللذين','اللذان','اللتان','اللتين','اللاتي','اللواتي','اللائي','الأُلى']
awazanElmodare = ['فعل','فاعل','نفعل','تفاعل','ستفعل','فعلل','تفعلل']
def statementTokenize(statement):
    return re.split(r'[\.]+',statement)

def tokenizeArabic(text):
    return re.split(r'[-,،!\s\_]+',text)

def getNouns(statement):
    nouns =[]
    for index ,token in enumerate(statement):
        if token.endswith('ة') or token.startswith('ال') or token.startswith('ل') or token.startswith('ك')  or token.startswith('ب')  or token.startswith('وا') or token.startswith('آ'):
            nouns.append(token)
        for elTan in elTanween:
            if token.__contains__(elTan):
                nouns.append(token)
        if statement[index-1] in elNedaa:
            nouns.append(statement[index])
        if statement[index-1] in elGr:
            nouns.append(statement[index])
    return nouns

def getElgr(statement):
    hroofElgr =[]
    for token in statement:
        if token in elGr:
            hroofElgr.append(token)
    return hroofElgr

def getElAtf(statement):
    hroofElAtf =[]
    for token in statement:
        if token in elAtf:
            hroofElAtf.append(token)
    return hroofElAtf

def getElnedaa(statement):
    hroofElnedaa =[]
    for token in statement:
        if token in elNedaa:
            hroofElnedaa.append(token)
    return hroofElnedaa

def getNasb(statement):
    hroofNasb =[]
    for token in statement:
        if token in elNasb:
            hroofNasb.append(token)
    return hroofNasb

def getGazm(statement):
    hroofGazm =[]
    for token in statement:
        if token in elGazm:
            hroofGazm.append(token)
    return hroofGazm
    
def getElzaman(statement):
    zroofElzamans =[]
    for token in statement:
        if token in zroofElzaman:
            zroofElzamans.append(token)
    return zroofElzamans

def getElmakkan(statement):
    zroofElmakans =[]
    for token in statement:
        if token in zroofElmakan:
            zroofElmakans.append(token)
    return zroofElmakans

def getElmawsool(statement):
    mawsools =[]
    for token in statement:
        if token in elmusool:
            mawsools.append(token)
    return mawsools

def getVerbs(statement):
    verbs =[]
    for index ,token in enumerate(statement):
        if token.startswith('س') or token.endswith('تْ'):
            verbs.append(token)      
        if statement[index-1] == 'قد' or statement[index-1] == 'سوف' :
            verbs.append(statement[index])
        string = 'أنيت'
        orginal = token
        if token[0] in string :
            token = token[1:]
            for wazn in awazanElmodare:
                 if len(token) == len(wazn):
                    for char in wazn:
                        if char != 'ف' and char != 'ع' and char != 'ل' :
                            if wazn.index(char) == token.index(char):
                                token = token[:token.index(char)] + token[token.index(char)+1:]
                                wazn = wazn[:wazn.index(char)] + wazn[wazn.index(char)+1:]
                    if len(token) == 3:
                        verbs.append(orginal)
    return verbs


# paragraph = "الطالب الذي يذاكر فوق المكتب يحصل علي أعلي الدرجات"
# # statements = statementTokenize(paragraph)
# statement = tokenizeArabic(paragraph)
# nouns = getNouns(statement)
# Elgrs = getElgr(statement)
# Elatfs = getElAtf(statement)
# Elnedaa = getElnedaa(statement)
# Elnasb = getNasb(statement)
# Elgazm = getGazm(statement)
# Elzamman = getElzaman(statement)
# Elmakkan = getElmakkan(statement)
# Elmawsool = getElmawsool(statement)
# verbs = getVerbs(statement)
# for word in statement:
#     if word in nouns:
#         print(word , "N")
#     if word in Elgrs:
#         print(word , "Gr")
#     if word in Elatfs:
#         print(word , "Atf")
#     if word in Elnedaa:
#         print(word , "Nedaa")
#     if word in Elnasb:
#         print(word , "Nasb")
#     if word in Elgazm:
#         print(word , "Gazm")
#     if word in Elzamman:
#         print(word , "Zamman")
#     if word in Elmakkan:
#         print(word , "Makkan")
#     if word in Elmawsool:
#         print(word , "Mawsool")
#     if word in verbs:
#         print(word , "V")

def show_outputs():
    output = []
    paragraph = e1.get()
    # statements = statementTokenize(paragraph)
    statement = tokenizeArabic(paragraph)
    nouns = getNouns(statement)
    Elgrs = getElgr(statement)
    Elatfs = getElAtf(statement)
    Elnedaa = getElnedaa(statement)
    Elnasb = getNasb(statement)
    Elgazm = getGazm(statement)
    Elzamman = getElzaman(statement)
    Elmakkan = getElmakkan(statement)
    Elmawsool = getElmawsool(statement)
    verbs = getVerbs(statement)
    for word in statement:
        if word in nouns:
            output.append(word + " N")
        if word in Elgrs:
            output.append(word + " Gr")
        if word in Elatfs:
            output.append(word + " Atf")
        if word in Elnedaa:
            output.append(word + " Nedaa")
        if word in Elnasb:
            output.append(word + " Nasb")
        if word in Elgazm:
            output.append(word + " Gazm")
        if word in Elzamman:
            output.append(word + " Zamman")
        if word in Elmakkan:
            output.append(word + " Makkan")
        if word in Elmawsool:
            output.append(word + " Mawsool")
        if word in verbs:
            output.append(word + " V")
    lbl["text"] = str(output)

if __name__ == "__main__":    
    master = Tk()
    # master.geometry("500x600")
    master.title('PosTagger')
    Label(master, text="Enter your text : ",font=("Helvetica", 16)).grid(row=0)
    Label(master, text="PosTagger output :",font=("Helvetica", 16)).grid(row=1)

    e1 = Entry(master)

    lbl = Label(master, text = '')
    # lbl.config(height=15, width=30)

    e1.grid(row=0, column=1,pady=10)
    lbl.grid(row=1, column=1,pady=10)

    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Tag', command=show_outputs).grid(row=3, column=1, sticky=W, pady=4)

    mainloop()