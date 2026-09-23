# Wave 1 Part D - Turkish, fresh production set: analysis

Frozen stack (L3 SOURCE-ONLY + content check, TIP rejected, no F4/AG); set opened once; truth = 4 opus judge sessions.

| block | coverage (accepted / judge-correct) CP95 | >= 90 % point / interval | FA (accepted / judge-wrong) CP95 | < 5 % point / interval |
|---|---|---|---|---|
| pooled | 440/502 = 87.65 % [84.45, 90.40] | missed / missed | 26/398 = 6.53 % [4.31, 9.43] | missed / missed |
| A1 | 104/128 = 81.25 % [73.40, 87.60] | missed / missed | 2/97 = 2.06 % [0.25, 7.25] | MET / missed |
| A2 | 114/122 = 93.44 % [87.49, 97.13] | MET / missed | 7/103 = 6.80 % [2.78, 13.50] | missed / missed |
| B1 | 113/125 = 90.40 % [83.83, 94.94] | MET / missed | 10/100 = 10.00 % [4.90, 17.62] | missed / missed |
| B2 | 109/127 = 85.83 % [78.53, 91.38] | missed / missed | 7/98 = 7.14 % [2.92, 14.16] | missed / missed |

Both targets met on the point (pooled): False

Diagnostic, L3 only (before the content check): | L3 only | 468/502 = 93.23 % [90.66, 95.26] | MET / MET | 44/398 = 11.06 % [8.15, 14.56] | missed / missed |

Gemini: 1412 counted calls (HTTP 200; {'l3': 900, 'cc': 512}), 0 failed-but-counted, spend $0.140035; language ledger {'D_CC': 512, 'D_L3': 900}.

Judge noise (80 hidden duplicates, different sessions): 3/80 disagree = 3.75 % [0.78, 10.57].

## False rejections (62) by cause

by layer {'L3': 20, 'CC:MISSING': 28, 'L3:TIPrej': 14}; by writer {'wrong/W': 2, 'correct/None': 56, 'wrong/M': 2, 'wrong/S': 2}; by level {'B1': 12, 'B2': 18, 'A2': 8, 'A1': 24}

| aid | lvl | layer | cc word | writer | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:565:w | B1 | L3 |  | wrong/W | Slime parmaklarına yapışmıyor, içindeki boncuklar de yapışmıyor. | The slime doesn't stick to your toes, and neither do the beads inside it. | Parmak covers toes; same meaning. |
| A:5728:c1 | B2 | CC:MISSING | imzalayınca | correct/ | Belediye başkanı imzalayınca köprüyü açık ilan edeceğine söz verdi. | The mayor promised that he would declare the bridge open once he signed. | Same meaning. |
| A:5728:c2 | B2 | L3 |  | correct/ | Belediye başkanı imzalayınca köprüyü açık ilan edeceğine söz verdi. | The mayor promised to declare the bridge open when she signed. | Same meaning. |
| A:6806:c3 | B2 | CC:MISSING | kolun | correct/ | Bu akşama kadar kolun iyileştiğini herkese söylemiş olacak | By this evening, she'll have told everyone your arm got better | Same meaning. |
| A:6806:c5 | B2 | CC:MISSING | kolun | correct/ | Bu akşama kadar kolun iyileştiğini herkese söylemiş olacak | By this evening she will have told everybody your arm had healed | Same meaning. |
| A:7607:c1 | B2 | CC:MISSING | sırayı | correct/ | Merceği netlerken sırayı sallamamamızı bizden rica etti | He asked us not to shake the desk while he was focusing the lens | Accurate translation. |
| A:7607:c2 | B2 | CC:MISSING | sırayı | correct/ | Merceği netlerken sırayı sallamamamızı bizden rica etti | She asked us not to shake the desk while focusing the lens | Same meaning. |
| A:7607:c3 | B2 | CC:MISSING | sırayı | correct/ | Merceği netlerken sırayı sallamamamızı bizden rica etti | While focusing the lens, he asked us not to rock the desk | Same meaning. |
| A:7607:c4 | B2 | CC:MISSING | sırayı | correct/ | Merceği netlerken sırayı sallamamamızı bizden rica etti | She requested that we not shake the desk while she focused the lens | Same meaning. |
| A:11941:c4 | A2 | L3:TIPrej |  | correct/ | Dün battaniyeyi bacaklarının üstüne çekti | He pulled a blanket onto his legs yesterday. | Accurate translation. |
| A:12002:c2 | A1 | L3:TIPrej |  | correct/ | Kedi sıcak battaniyenin altında uyuyor. | The cat sleeps under the warm blanket. | Same meaning. |
| A:12864:c2 | A1 | L3:TIPrej |  | correct/ | Eski ahşap köprüden geçiyorlar. | They cross the old wooden bridge. | Same meaning. |
| A:18873:c5 | A1 | CC:MISSING | Kedi | correct/ | Kedi ne içiyor? Taze beyaz süt. | What is that cat drinking? Fresh white milk. | Same meaning. |
| A:21424:c3 | A1 | CC:MISSING | Rauttan | correct/ | Rauttan önce o kendi mavi eldivenlerini bağlıyor. | Before the round, he is tying his blue gloves. | Same meaning. |
| A:25362:c2 | A1 | CC:MISSING | zeminde | correct/ | O, zeminde gittikçe daha yükseğe zıplar | She jumps higher and higher on the ground. | Zemin can be ground; same meaning. |
| A:25552:c1 | A1 | L3 |  | correct/ | Takımın sonunda bir altın kupası var | The team finally has a gold cup. | Same meaning |
| A:25552:c2 | A1 | L3 |  | correct/ | Takımın sonunda bir altın kupası var | The team has finally got a gold cup. | Same meaning. |
| A:25552:c3 | A1 | L3 |  | correct/ | Takımın sonunda bir altın kupası var | At last the team has a golden cup. | Accurate translation. |
| A:25552:c4 | A1 | L3 |  | correct/ | Takımın sonunda bir altın kupası var | The team has a gold cup. | Dropped finally is acceptable time adverb. |
| A:25552:c5 | A1 | L3 |  | correct/ | Takımın sonunda bir altın kupası var | Finally, the team's got a gold trophy. | Same meaning |
| A:25755:m | A1 | L3:TIPrej |  | wrong/M | Beşinci haftada bütün öğrenciler nerede | Where are all the students? | Only time phrase dropped; acceptable. |
| A:27490:c5 | A1 | CC:MISSING | kaldırıyor | correct/ | Genç kadın onun elini kaldırıyor ve bir soru soruyor. | The young woman puts her hand up and asks a question. | Accurate translation. |
| A:28820:c2 | A1 | L3:TIPrej |  | correct/ | Onlar pazar sabahı köprüyü geçiyorlar. | They cross the bridge on Sunday morning. | Present frame kept; tense free. |
| A:28820:c4 | A1 | L3:TIPrej |  | correct/ | Onlar pazar sabahı köprüyü geçiyorlar. | They go across the bridge on Sunday morning. | Same meaning; tense free. |
| A:32038:c1 | A2 | L3 |  | correct/ | Kolay olsun olmasın, havayolu büyük valizi vermek zorunda diyor. | Easy or not, the airline says he has to hand over the big suitcase. | Same meaning; genderless subject |
| A:32038:c3 | A2 | L3 |  | correct/ | Kolay olsun olmasın, havayolu büyük valizi vermek zorunda diyor. | Easy or not, the airline says he has to give up the big suitcase. | Accurate translation. |
| A:32038:c4 | A2 | L3 |  | correct/ | Kolay olsun olmasın, havayolu büyük valizi vermek zorunda diyor. | The airline says that, easy or not, she has to hand in the big suitcase. | Same meaning; genderless subject. |
| A:32602:c4 | A2 | L3 |  | correct/ | O lalelerini kaybediyor ve diyor ki: Söz veriyorum, daha dikkatli olacağım. | He loses his tulips and says that he promises: I will be more careful. | Awkward but meaning preserved. |
| A:32824:s | A2 | L3:TIPrej |  | wrong/S | Kaplumbağa özgür, bu yüzden o mutlulukla yüzüp uzaklaşıyor çünkü mutlu. | The turtle is free, so it swims away happy because it is happy. | Same meaning |
| A:33668:c5 | A2 | CC:MISSING | saat | correct/ | O hep geç uyanıyor, bu yüzden daha sesli bir çalar saat almalı. | He always wakes up late, therefore he should buy a louder alarm. | Same meaning. |
| A:33803:c1 | A1 | CC:MISSING | ayıya | correct/ | Kanka, iki ayıya bir bakış, ben de çığlığı basacağım. | Bro, one look at two bears and I'm going to scream. | Faithful translation. |
| A:33803:c2 | A1 | CC:MISSING | basacağım | correct/ | Kanka, iki ayıya bir bakış, ben de çığlığı basacağım. | Dude, one glance at two bears and I'll scream. | Same meaning |
| A:33803:c3 | A1 | CC:MISSING | ayıya | correct/ | Kanka, iki ayıya bir bakış, ben de çığlığı basacağım. | Bro, one look at two bears and I will start screaming. | Same meaning |
| A:33803:c4 | A1 | CC:MISSING | basacağım | correct/ | Kanka, iki ayıya bir bakış, ben de çığlığı basacağım. | Mate, one look at two bears and I'm going to shriek. | Same meaning. |
| A:33803:c5 | A1 | CC:MISSING | iki | correct/ | Kanka, iki ayıya bir bakış, ben de çığlığı basacağım. | Bro, one look at the two bears and I'll let out a scream. | Same meaning. |
| A:33915:c2 | A1 | L3 |  | correct/ | O onun kartını okutuyor çünkü kartlı bir üye. | She scans his card because he's a cardholder member. | Same meaning |
| A:33915:c3 | A1 | L3 |  | correct/ | O onun kartını okutuyor çünkü kartlı bir üye. | He is scanning her card because she is a member with a card. | Same meaning; genderless source. |
| A:33995:c4 | A1 | L3 |  | correct/ | Kanka, o koca bir arabayı hareket ettirir, saygı duymak lazım. | Bro, she shifts a huge car, you must respect that. | Same meaning, interjection kept |
| A:33995:c5 | A1 | L3:TIPrej |  | correct/ | Kanka, o koca bir arabayı hareket ettirir, saygı duymak lazım. | Bro, he moves an enormous car, respect. | Same meaning. |
| A:33995:w | A1 | L3:TIPrej |  | wrong/W | Kanka, o koca bir arabayı hareket ettirir, saygı duymak lazım. | Bro, he moves a huge truck, you have to respect that. | Araba as vehicle; meaning preserved. |
| A:35605:c2 | A2 | L3 |  | correct/ | Onlar yapı için o kadar çok ahşaba ihtiyaç duyuyor. | They need that much wood for the structure. | Accurate translation. |
| A:36781:c3 | B1 | CC:MISSING | 10'luk | correct/ | Kanka, onay daha gelmeden kalabalık 10'luk kartlarını hazır etmişti, cidden. | Mate, before the approval had even come, the crowd had their 10 cards ready, seriously. | Same meaning. |
| A:36781:c5 | B1 | CC:MISSING | 10'luk | correct/ | Kanka, onay daha gelmeden kalabalık 10'luk kartlarını hazır etmişti, cidden. | Dude, the crowd had got their 10 cards ready even before the approval came, for real. | Same meaning; added interjection style fine. |
| A:37638:c4 | B2 | CC:MISSING | mükemmel | correct/ | Kızım, duyduğuma göre o, o mükemmel atıştan önce saatlerce çalışmıştı. | Girl, I've heard he had worked on it for hours before that flawless shot. | Same meaning; genderless pronoun. |
| A:37638:s | B2 | L3:TIPrej |  | wrong/S | Kızım, duyduğuma göre o, o mükemmel atıştan önce saatlerce çalışmıştı. | Girl, I heard she had practice for hours before that perfect shot. | Acceptable English, same meaning and past frame. |
| A:37722:c1 | B1 | CC:MISSING | parçalanırdı | correct/ | Boğa arabaya bir daha saldırsa, cam tamamen parçalanırdı! | If the bull attacked the car again, the glass would shatter completely! | Same meaning |
| A:37722:c3 | B1 | L3:TIPrej |  | correct/ | Boğa arabaya bir daha saldırsa, cam tamamen parçalanırdı! | If the bull attacked the car again, the glass would break into pieces! | Same meaning; degree adverb dropped is acceptable. |
| A:38188:c4 | B2 | CC:MISSING | belgeleri | correct/ | Gelecek aya kadar o, belgeleri için iki yıldır bu mahkeme salonuna geliyor olacak. | For two years by next month, she will have been coming to this courtroom for her documents. | Awkward order but meaning preserved. |
| A:38287:c2 | B2 | CC:MISSING | karşıya geçişi | correct/ | Yayalar burada karşıya geçişi tipik olarak yalnızca ışık yeşilken yapar. | Here, pedestrians usually cross only when the light is green. | Same meaning. |
| A:38773:c4 | B1 | L3:TIPrej |  | correct/ | O güvercinler bütün sabah sepetlerde oturuyor! Uçmak için can atıyorlar! | Those pigeons have been sat in the baskets all morning! They are desperate to fly! | Colloquial have been sat acceptable; meaning kept. |
| A:41023:c4 | B2 | L3 |  | correct/ | O onu durdurduğunda, o çoktan o timsahı köpeğiyle karıştırmıştı, tam bir kâbus! | When she stopped her, she had already mixed up that crocodile with her dog, what a nightmare! | Same meaning. |
| A:42166:m | B1 | L3:TIPrej |  | wrong/M | Dinle, o bana bir gün önce bütün geri dönüşümünü ayırmış olduğunu söyledi. | Listen, she told me she had sorted all her recycling. | Only time adverbial dropped. |
| A:42290:c2 | B2 | L3 |  | correct/ | Kızım, o herkesin önünde bir kazdan geri çekildiğini itiraf etti. | Girl, he admitted he'd retreated from a goose in front of everybody. | Accurate translation. |
| A:42290:c3 | B2 | CC:MISSING | Kızım | correct/ | Kızım, o herkesin önünde bir kazdan geri çekildiğini itiraf etti. | Girl, she confessed that she had backed off from a goose in front of everyone. | Accurate translation. |
| A:42290:c4 | B2 | L3:TIPrej |  | correct/ | Kızım, o herkesin önünde bir kazdan geri çekildiğini itiraf etti. | Girl, he admitted backing away from a goose in front of everyone. | Same meaning; genderless source |
| A:43339:c1 | B2 | CC:MISSING | dalgadan | correct/ | O dalgadan geri çekildiğinde bütün kıyı mavi ışıkla parıldıyordu. | When he pulled back from the wave, the whole shore was glowing with blue light. | Accurate translation. |
| A:43339:c2 | B2 | CC:MISSING | geri çekildiğinde | correct/ | O dalgadan geri çekildiğinde bütün kıyı mavi ışıkla parıldıyordu. | When she retreated from the wave, the entire shore was shimmering with blue light. | Same meaning |
| A:44032:c1 | B1 | L3 |  | correct/ | Belli ki çok rahat: palyaço belirince o dehşet içinde adamın kolunu yakaladı. | Clearly very relaxed: when the clown appeared, she grabbed the man's arm in terror. | Same meaning. |
| A:44032:c2 | B1 | L3 |  | correct/ | Belli ki çok rahat: palyaço belirince o dehşet içinde adamın kolunu yakaladı. | Obviously very calm: when the clown showed up, he seized the man's arm in horror. | Same meaning. |
| A:44032:c3 | B1 | L3 |  | correct/ | Belli ki çok rahat: palyaço belirince o dehşet içinde adamın kolunu yakaladı. | Clearly totally relaxed: as the clown appeared, she grabbed the man's arm in terror. | Totally is degree variant; meaning kept. |
| A:44032:c4 | B1 | CC:MISSING | Belli ki çok rahat | correct/ | Belli ki çok rahat: palyaço belirince o dehşet içinde adamın kolunu yakaladı. | Very relaxed, obviously: when the clown turned up, he clutched the man's arm in terror. | Same meaning. |
| A:44032:c5 | B1 | CC:MISSING | çok | correct/ | Belli ki çok rahat: palyaço belirince o dehşet içinde adamın kolunu yakaladı. | Evidently very relaxed: when the clown appeared, she grabbed the guy's arm in fright. | Same meaning. |

## False acceptances (26) by cause

by layer {'L3+CC:NONE': 26}; by writer type {'M': 10, 'T': 8, 'None': 4, 'S': 2, 'W': 2}; by level {'B1': 10, 'B2': 7, 'A2': 7, 'A1': 2}

| aid | lvl | layer | cc | writer type | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:565:m | B1 | L3+CC:NONE | none | M | Slime parmaklarına yapışmıyor, içindeki boncuklar de yapışmıyor. | The slime doesn't stick to your fingers, and neither do the ones inside it. | Drops noun 'beads'. |
| A:871:m | B1 | L3+CC:NONE | none | M | O kanatlar neredeyse bir metre, yani bu sıradan küçük bir ev yarasası olamaz. | Those wings are almost a metre, so this can't be an ordinary house bat. | Adjective little dropped. |
| A:871:t | B1 | L3+CC:NONE | none | T | O kanatlar neredeyse bir metre, yani bu sıradan küçük bir ev yarasası olamaz. | Those wings were almost a metre, so this couldn't have been an ordinary small house bat. | Past frame; Turkish is present. |
| A:3781:m | B2 | L3+CC:NONE | none | M | Merdivenlerin tepesine varır varmaz arkadaşını arayacak. | As soon as he reaches the top, he will call his friend. | Drops noun stairs |
| A:7686:m | B2 | L3+CC:NONE | none | M | Kamerada bu kadar iyi görünen bir kahvaltıyı daha önce hiç görmemişlerdi | They had never seen a breakfast that looked so good before | Dropped 'on camera' |
| A:7686:t | B2 | L3+CC:NONE | none | T | Kamerada bu kadar iyi görünen bir kahvaltıyı daha önce hiç görmemişlerdi | They have never seen a breakfast that looks so good on camera before | Present perfect; Turkish is past perfect frame. |
| A:9697:t | B1 | L3+CC:NONE | none | T | Turkuaz devlet özgür, turuncu olan da öyle | The turquoise state was free, and so was the orange one. | Past time frame; Turkish is present. |
| A:23409:m | A2 | L3+CC:NONE | none | M | Laleleri çok seviyor, ama onu hapşırtıyorlar. | She loves them very much, but they make her sneeze. | Dropped noun 'tulips' |
| A:23751:t | A1 | L3+CC:NONE | none | T | Bu sıçrama günün en büyüğü. | This jump was the biggest of the day. | Past time frame; Turkish is present |
| A:25381:t | A2 | L3+CC:NONE | none | T | Bu zıplama ilkinden daha yüksek | This jump was higher than the first one. | Past instead of present |
| A:25755:t | A1 | L3+CC:NONE | none | T | Beşinci haftada bütün öğrenciler nerede | Where were all the students in the fifth week? | Past frame; Turkish is present. |
| A:29949:t | A2 | L3+CC:NONE | none | T | Yatakta kıyafet kuleleri: uyumadan önce hepsini taşımak zorunda. | Towers of clothes on the bed: she had to move all of them before sleeping. | Past frame; Turkish is present. |
| A:30980:c4 | A2 | L3+CC:NONE | none | None | Dans eden kalabalıkta beyaz gözlüklü bir ahtapot var. | An octopus with white sunglasses is in the dancing crowd. | gözlük is glasses, not sunglasses |
| A:34414:m | A2 | L3+CC:NONE | none | M | Denetim: onun pembe saçı 2 makine çamaşırdan daha parlak. | Inspection: her hair is brighter than 2 machine loads of laundry. | Dropped adjective pink. |
| A:34601:c4 | A2 | L3+CC:NONE | none | None | Bil bakalım, o dedi ki kaleci şu an hızlı bir plonjon yapıyor. | Guess what, he told me the keeper is diving quickly right now. | Adds 'me'; Turkish only says he said. |
| A:35156:c5 | A2 | L3+CC:NONE | none | None | Bavul asla kapanmayacak! Sen daha az tişört koymalısın! | The suitcase will never close! You should put less T-shirts in it! | Grammar error: less T-shirts |
| A:37241:m | B1 | L3+CC:NONE | none | M | Krem şeritleri makyöz tarafından cilde yedirildi ve eşit bir ton gözlemlendi. | The cream streaks were blended into the skin, and an even tone was observed. | Passive drops named agent (makeup artist). |
| A:37722:t | B1 | L3+CC:NONE | none | T | Boğa arabaya bir daha saldırsa, cam tamamen parçalanırdı! | If the bull had attacked the car again, the glass would have shattered completely! | Past counterfactual; Turkish is present hypothetical |
| A:37751:m | B2 | L3+CC:NONE | none | M | Yavru kedi, yakalamadan önce topu tam beş dakika kovalamıştı, tam bir profesyonel. | The kitten had chased the ball for exactly five minutes, a real pro. | Dropped clause 'before catching it'. |
| A:37751:s | B2 | L3+CC:NONE | none | S | Yavru kedi, yakalamadan önce topu tam beş dakika kovalamıştı, tam bir profesyonel. | Kitten had chased the ball for exactly five minutes before catching it, a real pro. | Missing article before 'Kitten'. |
| A:39070:c2 | B1 | L3+CC:NONE | none | None | Başının üstünden bir ara papağanı uçtuğunda kâşif lianları kesiyordu. | At one point, when a parrot flew over her head, the explorer was cutting vines. | Drops possessive: her parrot, not a parrot. |
| A:39131:w | B1 | L3+CC:NONE | none | W | Bir şey kıpırdadığında o dürbünle uzak kıyıyı tarıyordu. | She was scanning the far shore with a telescope when something moved. | Telescope instead of binoculars. |
| A:41884:s | B1 | L3+CC:NONE | none | S | O kitabının üstünde uyuyor, yani pek verimli değil, öyle mi? | She's sleeping on her book, so she's not very productive, isn't she? | Wrong question tag: not ... isn't she. |
| A:42875:m | B2 | L3+CC:NONE | none | M | Çift barınağın çıkışına vardığında görevli formları çoktan damgalamıştı. | When the couple reached the exit, the attendant had already stamped the forms. | Drops noun shelter |
| A:42875:w | B2 | L3+CC:NONE | none | W | Çift barınağın çıkışına vardığında görevli formları çoktan damgalamıştı. | When the couple reached the shelter's entrance, the attendant had already stamped the forms. | 'entrance' instead of 'exit'. |
| A:44565:m | B1 | L3+CC:NONE | none | M | Onlar bir saattir bu kuyrukta bekliyor, oy vermek için. Hızlı bir süreç, belli ki. | They've been waiting in this queue for an hour. A quick process, obviously. | 'to vote' dropped. |

## Judge duplicate disagreements

- A:25755:m (A1, wrong/M) s1 correct vs s2 wrong: "Where are all the students?"
- A:6806:c5 (B2, correct/None) s2 correct vs s1 wrong: "By this evening she will have told everybody your arm had healed"
- A:565:w (B1, wrong/W) s7 correct vs s4 wrong: "The slime doesn't stick to your toes, and neither do the beads inside it."
