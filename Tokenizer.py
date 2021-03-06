# -*- coding: UTF-8 -*-
import re
from tkinter import *

def tokenizeArabic(text):
    return re.split(r'[-,،!\s\_]+',text)

def show_outputs():
    lbl["text"] = str(tokenizeArabic(e1.get()))

master = Tk()
master.title('Tokenizer')
# master.geometry("500x600")
Label(master, text="Enter your text : ",font=("Helvetica", 16)).grid(row=0)
Label(master, text="Tokenizer output :",font=("Helvetica", 16)).grid(row=1)

e1 = Entry(master)

lbl = Label(master, text = '')
# lbl.config(height=15, width=30)

e1.grid(row=0, column=1,pady=10)
lbl.grid(row=1, column=1,pady=10)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Tokenize', command=show_outputs).grid(row=3, column=1, sticky=W, pady=4)

mainloop()


moalkitAmrIbnKolthom= '''أَلاَ هُبِّي بِصَحْنِكِ فَاصْبَحِينَا 		وَلاَ تُبْقِي خُمُورَ الأَنْدَرِينَا 	
مُشَعْشَعَةً كَأَنَّ الْحُصَّ فِيهَا 		إِذَا مَا الْمَاءُ خَالَطَهَا سَخِينَا 	
تَجُورُ بِذِي اللُّبَانَةِ عَنْ هَوَاهُ 		إِذَا مَا ذَاقَهَا حَتَّى يَلِينَا 	
تَرَى اللَّحِزَ الشَّحِيحَ إِذَا أُمِرَّتْ 		عَلَيْهِ لِمَالِهِ فِيهَا مُهِينَا 	
صَبَنْتِ الكَأْسَ عَنَّا أُمَّ عَمْرٍو 		وَكَانَ الكَأْسُ مَجْرَاهَا الْيَمِينَا 	
وَمَا شَرُّ الثَّلاَثَةِ أُمَّ عَمْرٍو 		بِصَاحِبِكِ الَّذِي لاَ تَصْبَحِينَا 	
وَكَأْسٍ قَدْ شَرِبْتُ بِبَعْلَبَكٍّ 		وَأُخْرَى فِي دِمَشْقَ وَقَاصِرِينَا 	
وَأَنَّا سَوْفَ تُدْرِكُنَا الْمَنَايَا 		مُقَدَّرَةً لَنَا وَمُقَدَّرِينَا 	
قِفِي قَبْلَ التَّفَرُّقِ يَا ظَعِينَا 		نُخَبِّرْكِ الْيَقِينَ وَتُخْبِرِينَا 	
قِفِي نَسْأَلْكِ هَلْ أَحْدَثْتِ صُرْماً 		لِوَشْكِ البَيْنِ أَمْ خُنْتِ الأَمِينَا 	
بِيَوْمِ كَرِيهَةِ ضَرْبَاً وَطَعْنَاً 		أَقَرَّ بِهِ مَوَالِيكِ العُيُونَا 	
وَإِنَّ غَدَاً وَإِنَّ اليَوْمَ رَهْنٌ 		وَبَعْدَ غَدٍ بِمَا لاَ تَعْلَمِينَا 	
تُرِيكَ إِذَا دَخَلَتْ عَلَى خَلاَءٍ 		وَقَدْ أَمِنْتَ عُيُونَ الكَاشِحِينَا 	
ذِرَاعَي عَيْطَلٍ أَدْمَاءَ بِكْرٍ 		هِجَانِ اللَّوْنِ لَمْ تَقْرَأْ جَنِينَا 	
وَثَدْيَاً مِثْلَ حُقِّ العَاجِ رَخْصَاً 		حَصَانَاً مِنْ أَكُفِّ اللاَمِسِينَا 	
وَمَتَنَيْ لَدْنَةٍ سَمَقَتْ وَطَالَتْ 		رَوَادِفُهَا تَنُوءُ بِمَا وَلِينَا 	
وَمأْكَمَةً يَضِيقُ البَابُ عَنْهَا 		وَكَشْحَاً قَدْ جُنِنْتُ بِهِ جُنُونَا 	
وَسَارِيَتَيْ بِلَنْطٍ أَوْ رُخَامٍ 		يَرِنُّ خَشَاشُ حَلْيِهِمَا رَنِينَا 	
فَمَا وَجَدَتْ كَوَجْدِي أُمُّ سَقْبٍ 		أَضَلَّتْهُ فَرَجَّعَتِ الْحَنِينَا 	
وَلاَ شَمْطَاءُ لَمْ يَتْرُكْ شَقَاهَا 		لَهَا مِنْ تِسْعَةٍ إلاَّ جَنِينَا 	
تَذَكَّرْتُ الصِّبَا وَاشْتَقْتُ لَمَّا 		رَأَيْتُ حُمُولَهَا أُصُلاً حُدِينَا 	
فَأَعْرَضَتِ اليَمَامَةُ وَاشْمَخَرَّتْ 		كَأَسْيَافٍ بِأَيْدِي مُصْلِتِينَا 	
أَبَا هِنْدٍ فَلاَ تَعْجَلْ عَلَيْنَا 		وَأَنْظِرْنَا نُخَبِّرْكَ اليَقِينَا 	
بِأَنَّا نُوْرِدُ الرَّايَاتِ بِيضَاً 		وَنُصْدِرُهُنَّ حُمْرَاً قَدْ رَوِينَا 	
وَأَيَّامٍ لَنَا غُرٍّ طِوَالٍ 		عَصَيْنَا المَلْكَ فِيهَا أَنْ نَدِينَا 	
وَسَيِّدِ مَعْشَرٍ قَدْ تَوَّجُوهُ 		بِتَاجِ المُلْكِ يَحْمِي المُحْجَرِينَا 	
تَرَكْنَا الْخَيْلَ عَاكِفَةً عَلَيْهِ 		مُقَلَّدَةً أَعِنَّتُهَا صُفُونَا 	
وَأَنْزَلْنَا البُيُوتَ بِذِي طُلُوحٍ 		إِلَى الشَامَاتِ تَنْفِي الموعِدِينَا 	
وَقَدْ هَرَّتْ كِلاَبُ الحَيِّ مِنَّا 		وَشَذَّبْنَا قَتَادَةَ مَنْ يَلِينَا 	
مَتَى نَنْقُلْ إِلَى قَوْمٍ رَحَانَا 		يَكُونُوا فِي اللِّقَاءِ لَهَا طَحِينَا 	
يَكُونُ ثِفَالُهَا شَرْقِيَّ نَجْدٍ 		وَلُهْوَتُهَا قُضَاعَةَ أَجْمَعِينَا 	
نَزَلْتُمْ مَنْزِلَ الأَضْيَافِ مِنَّا 		فَأَعْجَلْنَا الْقِرَى أَنْ تَشْتِمُونَا 	
قَرَيْنَاكُمْ فَعَجَّلْنَا قِرَاكُمْ 		قُبَيْلَ الصُّبْحِ مِرْدَاةً طَحُونَا 	
نَعُمُّ أَنَاسَنَا وَنَعِفُّ عَنْهُمْ 		وَنَحْمِلُ عَنْهُمُ مَا حَمَّلُونَا 	
نُطَاعِنُ مَا تَرَاخَى النَّاسُ عَنَّا 		وَنَضْرِبُ بِالسِّيُوفِ إِذَا غُشِينَا 	
بِسُمْرٍ مِنْ قَنَا الخَطِّيِّ لُدْنٍ 		ذَوَابِلَ أَوْ بِبِيضٍ يَعْتَلِينَا 	
كَأَنَّ جَمَاجِمَ الأَبْطَالِ فِيهَا 		وُسُوقٌ بِالأَمَاعِزِ يَرْتَمِينَا 	
نَشُقُّ بِهَا رُؤُوسَ القَوْمِ شَقًّاً 		وَنَخْتَلِبُ الرِّقَابَ فَتَخْتَلِينَا 	
وَإِنَّ الضِّغْنَ بَعْدَ الضِّغْنِ يَبْدُو 		عَلَيْكَ وَيُخْرِجُ الدَّاءَ الدَّفِينَا 	
وَرِثْنَا المَجْدَ قَدْ عَلِمَتْ مَعَدٌّ 		نُطَاعِنُ دُونَهُ حَتَّى يَبِينَا 	
وَنَحْنُ إِذَا عِمَادُ الحَيِّ خَرَّتْ 		عَنِ الأَحْفَاضِ نَمْنَعُ مَنْ يَلِينَا 	
نَجُذُّ رُؤُوسَهُمْ فِي غَيْرِ بِرٍّ 		فَمَا يَدْرُونَ مَاذَا يَتَّقُونَا 	
كَأَنَّ سُيُوفَنَا مِنَّا وَمِنْهُمْ 		مَخَارِيقٌ بِأَيْدِي لاَعِبِينَا 	
كَأَنَّ ثِيَابَنَا مِنَّا وَمِنْهُمْ 		خُضِبْنَ بِأُرْجُوَانٍ أَوْ طُلِينَا 	
إِذَا مَا عَيَّ بِالإِسْنَافِ حَيٌّ 		مِنَ الهَوْلِ المُشَبَّهِ أَنْ يَكُونَا 	
نَصَبْنَا مِثْلَ رَهْوَةَ ذَاتَ حَدٍّ 		مُحَافَظَةً وَكُنَّا السَّابِقِينَا 	
بِشُبَّانٍ يَرَوْنَ القَتْلَ مَجْدَاً 		وَشِيبٍ فِي الحُرُوبِ مُجَرَّبِينَا 	
حُدَيَّا النَّاسِ كُلِّهِمُ جَمِيعَاً 		مُقَارَعَةً بَنِيهِمْ عَنْ بَنِينَا 	
فَأَمَّا يَوْمَ خَشْيَتِنَا عَلَيْهِمْ 		فَتُصْبِحُ خَيْلُنَا عُصَبَاً ثُبِينَا 	
وَأَمَّا يَوْمَ لاَ نَخْشَى عَلَيْهِمْ 		فَنُمْعِنُ غَارَةً مُتَلَبِّبِينَا 	
بِرَأْسٍ مِنْ بَنِي جُشَمِ بن بَكْرٍ 		نَدُقُّ بِهِ السُّهُولَةَ وَالحُزُونَا 	
أَلا لا يَعْلَمُ الأَقْوَامُ أَنَّا 		تَضَعْضَعْنَا وَأَنَّا قَدْ وَنِينَا 	
أَلاَ لاَ يَجْهَلَن أَحَدٌ عَلَيْنَا 		فَنَجْهَلَ فَوْقَ جَهْلِ الجَاهِلِينَا 	
بِأَيِّ مَشِيئَةٍ عَمْرَو بْنَ هِنْدٍ 		نَكُونُ لِقَيْلِكُمْ فِيهَا قَطِينَا؟ 	
بِأَيِّ مَشِيئَةٍ عَمْرَو بْنَ هِنْدٍ 		تُطِيْعُ بِنَا الوُشَاةَ وَتَزْدَرِينَا؟ 	
تَهَدَّدْنَا وَأَوْعِدْنَا رُوَيْدَاً 		مَتَى كُنَّا لأُمِّكَ مَقْتَوِينَا؟ 	
فَإِنَّ قَنَاتَنَا يَا عَمْرُو أَعْيَتْ 		عَلَى الأَعْدَاءِ قَبَلَكَ أَنْ تَلِينَا 	
إِذَا عَضَّ الثِّقَافُ بِهَا اشْمَأَزَّتْ 		وَوَلَّتْهُم عَشَوْزَنَةً زَبُونَا 	
عَشَوْزَنَةً إِذَا انْقَلَبَتْ أَرَنَّتْ 		تَشُجُّ قَفَا المُثَقَّفِ وَالجَبِينَا 	
فَهَلْ حُدِّثْتَ فِي جُشَمِ بْنِ بَكْرٍ 		بِنَقْصٍ فِي خُطُوبِ الأَوَّلِينَا؟ 	
وَرِثْنَا مَجْدَ عَلْقَمَةَ بْنِ سَيْفٍ 		أَبَاحَ لَنَا حُصُونَ المَجْدِ دِينَا 	
وَرِثْتُ مُهَلْهِلاً وَالخَيْرَ مِنْهُ 		زُهَيْرَاً نِعْمَ ذُخْرُ الذَّاخِرِينَا 	
وَعَتَّابَاً وَكُلْثُومَاً جَمِيعَاً 		بِهِمْ نِلْنَا تُرَاثَ الأَكْرَمِينَا 	
وَذَا البُرَةِ الذِي حُدِّثْتَ عَنْهُ 		بِهِ نُحْمَى وَنَحْمِي المُحْجَرِينَا 	
وَمِنَّا قَبْلَهُ السَّاعِي كُلَيْبٌ 		فَأَيُّ المَجْدِ إِلاَّ قَدْ وَلِينَا؟ 	
مَتَى نَعْقِدْ قَرِينَتَنَا بِحَبْلٍ 		تَجُذُّ الحَبْلَ أَوْ تَقَصِ القَرِينَا 	
وَنُوجَدُ نَحْنُ أَمْنَعَهُمْ ذِمَارَاً 		وَأَوْفَاهُمْ إِذَا عَقَدُوا يَمِينَا 	
وَنَحْنُ غَدَاةَ أُوقِدَ فِي خَزَازَى 		رَفَدْنَا فَوْقَ رَفْدِ الرَّافِدِينَا 	
وَنَحْنُ الحَابِسُونَ بِذِي أُرَاطَى 		تَسَفُّ الجِلَّةُ الخُورُ الدَّرِينَا 	
وَنَحْنُ الحَاكِمُونَ إِذَا أُطِعْنَا 		وَنَحْنُ العَازِمُونَ إِذَا عُصِينَا 	
وَنَحْنُ التَّارِكُونَ لِمَا سَخِطْنَا 		وَنَحْنُ الآخِذُونَ لِمَا رَضِينَا 	
وَكُنَّا الأَيْمَنِينَ إِذَا التَقَيْنَا 		وَكَانَ الأَيْسَرِينَ بَنُو أَبِينَا 	
فَصَالُوا صَوْلَةً فِيْمَنْ يَلِيهِمْ 		وَصُلْنَا صَوْلَةً فِيْمَنْ يَلِينَا 	
فَآبُوا بِالنِّهَابِ وَبِالسَّبَايَا 		وَأُبْنَا بِالمُلُوكِ مُصَفَّدِينَا 	
إِلَيْكُمْ يَا بَنِي بَكْرٍ إِلَيْكُمْ 		أَلَمَّا تَعْرِفُوا مِنَّا اليَقِينَا 	
أَلَمَّا تَعْلَمُوا مِنَّا وَمِنْكُمْ 		كَتَائِبَ يَطَّعِنَّ وَيَرْتَمِينَا 	
عَلَيْنَا البَيْضُ وَاليَلَبُ اليَمَانِي 		وَأسْيَافٌ يَقُمْنَ وَيَنْحَنِينَا 	
عَلَيْنَا كُلُّ سَابِغَةٍ دِلاَصٍ 		تَرَى فَوْقَ النِّجَادِ لَهَا غُضُوناً 	
إِذَا وُضِعَتْ عَنِ الأَبْطَالِ يَوْمَاً 		رَأَيْتَ لَهَا جُلُودَ القَوْمِ جُونَا 	
كَأَنَّ غُضُونَهُنَّ مُتُونُ غُدْرٍ 		تُصَفِّقُهَا الرِّيَاحُ إِذَا جَرَيْنَا 	
وَتَحْمِلُنَا غَدَاةَ الرَّوْعِ جُرْدٌ 		عُرِفْنَ لَنَا نَقَائِذَ وَافْتُلِينَا 	
وَرَدْنَ دَوَارِعاً وَخَرَجْنَ شُعْثَاً 		كَأَمْثَالِ الرَّصَائِعِ قَدْ بَلِينَا 	
وَرِثْنَاهُنَّ عَنْ آبَاءِ صِدْقٍ 		وَنُورِثُهَا إِذَا مُتْنَا بَنِينَا 	
عَلَى آثَارِنَا بِيضٌ حِسَانٌ 		نُحَاذِرُ أَنْ تُقَسَّمَ أَوْ تَهُونَا 	
أَخَذْنَ عَلَى بُعُولَتِهِنَّ عَهْدَاً 		إِذَا لاَقَوْا فَوارِسَ مُعْلِمِينَا 	
لَيَسْتَلِبُنَّ أَفْرَاسَاً وَبَيضَاً 		وَأَسْرَى فِي الحَدِيدِ مُقَرَّنِينَا 	
تَرَانَا بَارِزِينَ وَكُلُّ حَيٍّ 		قَدِ اتَّخَذُوا مَخَافَتَنَا قَرِينَا 	
إِذَا مَا رُحْنَ يَمْشِينَ الهُوَيْنَى 		كَمَا اضْطَرَبَتْ مُتُونُ الشَّارِبِينَا 	
يَقُتْنَ جِيَادَنَا وَيَقُلْنَ لَسْتُمْ 		بُعُولَتَنَا إِذَا لَمْ تَمْنَعُونَا 	
ظَعَائِنَ مِنْ بَنِي جُشَمِ بْنِ بَكْرٍ 		خَلَطْنَ بِمِيسَمٍ حَسَبَاً وَدِينَا 	
وَمَا مَنَعَ الظَّعَائِنَ مِثْلُ ضَرْبٍ 		تَرَى مِنْهُ السَّوَاعِدَ كَالقُلِينَا 	
كَأَنَّا وَالسُّيُوفُ مُسَلَّلاَتٌ 		وَلَدْنَا النَّاسَ طُرَّاً أَجْمَعِينَا 	
يُدَهْدُونَ الرُّؤُوسَ كَمَا تُدَهْدَي 		حَزَاوِرَةٌ بِأَبْطَحِهَا الكُرِينَا 	
وَقَدْ عَلِمَ القَبَائِلُ مِنْ مَعَدٍّ 		إِذَا قُبَبٌ بِأَبْطَحِهَا بُنِينَا 	
بِأَنَّا المُطْعِمُونَ إِذَا قَدَرْنَا 		وَأَنَّا المُهْلِكُونَ إِذَا ابْتُلِينَا 	
وَأَنَّا المَانِعُونَ لِمَا أَرَدْنَا 		وَأَنَّا النَّازِلُونَ بِحَيْثُ شِينَا 	
وَأَنَّا التَارِكُونَ إِذَا سَخِطْنَا 		وَأَنَّا الآخِذُونَ إِذَا رَضِينَا 	
وَأَنَّا العَاصِمُونَ إِذَا أُطِعْنَا 		وَأَنَّا العَازِمُونَ إِذَا عُصِينَا 	
وَنَشْرَبُ إِنْ وَرَدْنَا المَاءَ صَفْواً 		وَيَشْرَبُ غَيْرُنَا كَدَراً وَطِينَا 	
أَلاَ أَبْلِغْ بَنِي الطَّمَّاحِ عَنَّا 		وَدُعْمِيَّاً فَكَيْفَ وَجَدْتُمُونَا 	
إِذَا مَا المَلْكُ سَامَ النَّاسَ خَسْفَاً 		أَبَيْنَا أَنْ نُقِرَّ الذُّلَّ فِينَا 	
مَلأْنَا البَرَّ حَتَّى ضَاقَ عَنَّا 		وَمَاءَ البَحْرِ نَمْلَؤُهُ سَفِينَا 	
إِذَا بَلَغَ الفِطَامَ لَنَا صَبِيٌّ 		تَخِرُّ لَهُ الجَبَابِرُ سَاجِدِينَا
'''

# def tokenizeArabic(text):
#     return re.split(r'[-,،!\s\_]+',text)

# print(tokenizeArabic(moalkitAmrIbnKolthom))