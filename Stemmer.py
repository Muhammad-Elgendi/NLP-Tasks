
# -*- coding: utf-8 -*-
#اللغة العربية 
# فعل: ماضي مضارع أمر
# إسم: مفرد مثني جمع مذكر سالم جمع مؤنث سالم جمع تكسير
# حرف: حروف الجر والعطف والنصب والجزم ,والإستفهام مثلاً
import re
from tkinter import *
unchangeable = ["من","إلي","عن","علي","في","حتي","ثم","هل","لم","لما","إن",
"إنما","ما","مهما","متي","أينما","حيثما","أن","لن","كي","إثنان","إثنتان","ثنتان"]
postfixs = ['ان','ين','ون','ات','ة','و','وا']
prefixs = ['لا','م','ي','ن','ت','س','ب','ك','ل','ال','و']
# infixs =[('ا',1),('ا',2),('ت',1)]
elAwazan = ['مفاعلة','إفتعل','فعال','فاعل','أفعل']

# return list of stemmed tokens
def stemArabic(listOftokens):
    stemmedTokens = []
    for token in listOftokens:
        if token in unchangeable:
            stemmedTokens.append(token)
        else:
            newToken = treatPrefix(token)
            newToken = treatPostfix(newToken)            
            newToken = treatInfix(newToken)
            stemmedTokens.append(newToken)
    return stemmedTokens

# remove prefix from token or return the token
def treatPrefix(token):
    for prefix in prefixs:
        if token.startswith(prefix) and len(token[len(prefix)-1:]) > 2:
            return token[len(prefix):]
    return token

# remove postfix from token or return the token
def treatPostfix(token):
    for postfix in postfixs:
        if token.endswith(postfix) and len(token[:len(postfix)*-1]) > 2:
            return token[:len(postfix)*-1]
    return token

# remove infix from token or return the token
def treatInfix(token):
    # for infix in infixs:
    #     try:
    #         if token[infix[1]] == infix[0]  and len(token[:infix[1]] + token[infix[1]+1:]) > 2:
    #             return token[:infix[1]] + token[infix[1]+1:]
    #     except IndexError:
    #         pass
    # return token
    for wazn in elAwazan:
        if len(token) == len(wazn):
            for char in wazn:
                if char != 'ف' and char != 'ع' and char != 'ل' :                  
                    if char in token and wazn.index(char) == token.index(char):
                        token = token[:token.index(char)] + token[token.index(char)+1:]
                        wazn = wazn[:wazn.index(char)] + wazn[wazn.index(char)+1:]
                   
    return token
    
def tokenizeArabic(text):
    return re.split(r'[-,،!\s\_]+',text)

def show_outputs():
    tokens = tokenizeArabic(e1.get())
    lbl["text"] = str(stemArabic(tokens))
    
if __name__ == "__main__":    
    master = Tk()
    # master.geometry("500x600")
    master.title('Stemmer')
    Label(master, text="Enter your text : ",font=("Helvetica", 16)).grid(row=0)
    Label(master, text="Stemmer output :",font=("Helvetica", 16)).grid(row=1)

    e1 = Entry(master)

    lbl = Label(master, text = '')
    # lbl.config(height=15, width=30)

    e1.grid(row=0, column=1,pady=10)
    lbl.grid(row=1, column=1,pady=10)

    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Stem', command=show_outputs).grid(row=3, column=1, sticky=W, pady=4)

    mainloop()

# # return list of stemmed tokens
# def stemArabic(listOftokens):
#     stemmedTokens = []
#     for token in listOftokens:
#         if token in unchangeable:
#             stemmedTokens.append(token)
#         else:
#             newToken = treatPrefix(token)
#             newToken = treatPostfix(newToken)            
#             newToken = treatInfix(newToken)
#             stemmedTokens.append(newToken)
#     return stemmedTokens

# # remove prefix from token or return the token
# def treatPrefix(token):
#     for prefix in prefixs:
#         if token.startswith(prefix) and len(token[len(prefix)-1:]) > 2:
#             return token[len(prefix):]
#     return token

# # remove postfix from token or return the token
# def treatPostfix(token):
#     for postfix in postfixs:
#         if token.endswith(postfix) and len(token[:len(postfix)*-1]) > 2:
#             return token[:len(postfix)*-1]
#     return token

# # remove infix from token or return the token
# def treatInfix(token):
#     for infix in infixs:
#         try:
#             if token[infix[1]] == infix[0]  and len(token[:infix[1]] + token[infix[1]+1:]) > 2:
#                 return token[:infix[1]] + token[infix[1]+1:]
#         except IndexError:
#             pass
#     return token

# def tokenizeArabic(text):
#     return re.split(r'[-,،!\s\_]+',text)

# tokens = tokenizeArabic("الله يثيب من العاملين من إجتهد وسعي وغالب هواه")
# print('tokens :',tokens)
# print ('stems :',stemArabic(tokens))