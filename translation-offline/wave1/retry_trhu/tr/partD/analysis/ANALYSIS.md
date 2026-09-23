# Wave 1 Part D - Turkish, fresh production set: analysis

Frozen stack (L3 SOURCE-ONLY + content check, TIP rejected, no F4/AG); set opened once; truth = 4 opus judge sessions.

| block | coverage (accepted / judge-correct) CP95 | >= 90 % point / interval | FA (accepted / judge-wrong) CP95 | < 5 % point / interval |
|---|---|---|---|---|
| pooled | 467/504 = 92.66 % [90.02, 94.78] | MET / MET | 18/396 = 4.55 % [2.72, 7.09] | MET / missed |
| A1 | 102/128 = 79.69 % [71.67, 86.28] | missed / missed | 1/97 = 1.03 % [0.03, 5.61] | MET / missed |
| A2 | 117/123 = 95.12 % [89.68, 98.19] | MET / missed | 6/102 = 5.88 % [2.19, 12.36] | missed / missed |
| B1 | 120/124 = 96.77 % [91.95, 99.11] | MET / MET | 7/101 = 6.93 % [2.83, 13.76] | missed / missed |
| B2 | 128/129 = 99.22 % [95.76, 99.98] | MET / MET | 4/96 = 4.17 % [1.15, 10.33] | MET / missed |

Both targets met on the point (pooled): True

Diagnostic, L3 only (before the content check): | L3 only | 473/504 = 93.85 % [91.38, 95.78] | MET / MET | 42/396 = 10.61 % [7.75, 14.07] | missed / missed |

Gemini: 1415 counted calls (HTTP 200; {'l3': 900, 'cc': 515}), 0 failed-but-counted, spend $0.203629; language ledger {'D_CC': 515, 'D_L3': 900}.

Judge noise (80 hidden duplicates, different sessions): 0/80 disagree = 0.0 % [0.0, 4.51].

## False rejections (37) by cause

by layer {'L3': 17, 'CC:MISSING': 6, 'L3:TIPrej': 14}; by writer {'correct/None': 32, 'wrong/S': 1, 'wrong/M': 4}; by level {'B1': 4, 'A2': 6, 'A1': 26, 'B2': 1}

| aid | lvl | layer | cc word | writer | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:2039:c3 | B1 | L3 |  | correct/ | Gözyaşları daha kurumadan en yakın arkadaşı tarafından avutuldu. | Her best friend comforted her before her tears had even dried. | Active voice keeps the agent; meaning matches. |
| A:10861:c5 | B1 | L3 |  | correct/ | Ülkeye girebileceğini söyledi. | He said he could come into the country. | Same meaning |
| A:12092:c3 | A2 | CC:MISSING | al | correct/ | Bir nefes daha al, dibe ulaşacaksın! | One more breath, you'll get to the bottom! | Same meaning. |
| A:13841:c1 | A1 | L3 |  | correct/ | Sunucu doğru cevabını karta yazıyor. | The presenter writes his correct answer on the card. | Faithful meaning. |
| A:13841:c2 | A1 | L3 |  | correct/ | Sunucu doğru cevabını karta yazıyor. | The host is writing her correct answer on the card. | Genderless possessive; her acceptable. |
| A:13841:c4 | A1 | L3 |  | correct/ | Sunucu doğru cevabını karta yazıyor. | The presenter is writing his right answer onto the card. | Accurate meaning. |
| A:13841:c5 | A1 | L3 |  | correct/ | Sunucu doğru cevabını karta yazıyor. | The TV host writes her correct answer on the card. | Same meaning; genderless source |
| A:20213:c4 | A1 | L3:TIPrej |  | correct/ | Bu telefon yine çalıyor! | This phone rings again! | Present time frame kept; tense free |
| A:23033:c4 | A1 | L3:TIPrej |  | correct/ | Parktaki taş basamaklardan aşağı iniyor. | He comes down the stone stairs in the park. | Meaning matches; gender free. |
| A:24198:c1 | A1 | CC:MISSING | kadar | correct/ | Bu yabancı onu kırmızı otobüse kadar götürüyor. | This stranger takes her to the red bus. | Faithful meaning. |
| A:27060:c1 | A1 | L3 |  | correct/ | Macera gün batımı bitiyor. | The adventure sunset is ending. | Same meaning |
| A:27060:c2 | A1 | L3 |  | correct/ | Macera gün batımı bitiyor. | The adventure sunset ends. | Literal, matches source. |
| A:27060:c3 | A1 | L3 |  | correct/ | Macera gün batımı bitiyor. | The adventure sunset is coming to an end. | Accurate meaning. |
| A:27060:c4 | A1 | L3 |  | correct/ | Macera gün batımı bitiyor. | The sunset adventure is ending. | Faithful. |
| A:27060:c5 | A1 | L3 |  | correct/ | Macera gün batımı bitiyor. | The sunset adventure is coming to an end. | Same meaning |
| A:30792:c5 | A2 | CC:MISSING | haykırışın | correct/ | Kızım, ben üçüncü haykırışın yavaşça geri geldiğini duydum. | Daughter, I heard the third yell echo back slowly. | Faithful meaning. |
| A:30792:s | A2 | L3:TIPrej |  | wrong/S | Kızım, ben üçüncü haykırışın yavaşça geri geldiğini duydum. | My daughter, I heard the third shout come back slow. | Same meaning; informal flat adverb acceptable |
| A:31993:c1 | A1 | L3:TIPrej |  | correct/ | Kürek toprağı çeviriyor ve iki yapraklar ortaya çıkıyor. | The shovel turns the soil and two leaves appear. | Accurate |
| A:31993:c2 | A1 | L3:TIPrej |  | correct/ | Kürek toprağı çeviriyor ve iki yapraklar ortaya çıkıyor. | The spade turns over the earth and two leaves come out. | Accurate |
| A:31993:c3 | A1 | L3:TIPrej |  | correct/ | Kürek toprağı çeviriyor ve iki yapraklar ortaya çıkıyor. | The shovel is turning the soil, and two leaves are appearing. | Faithful; plural corrected naturally. |
| A:31993:c4 | A1 | L3:TIPrej |  | correct/ | Kürek toprağı çeviriyor ve iki yapraklar ortaya çıkıyor. | The shovel turns over the dirt and two leaves emerge. | Accurate meaning. |
| A:31993:c5 | A1 | L3 |  | correct/ | Kürek toprağı çeviriyor ve iki yapraklar ortaya çıkıyor. | The spade is turning the soil and two leaves show up. | Same meaning |
| A:32116:c2 | A2 | L3 |  | correct/ | Canım, yaşlı hanımın arkasında çok komşunun yürüdüğünü söyledi. | Honey, she said a lot of neighbors are walking behind the old woman. | Accurate |
| A:32116:c4 | A2 | L3 |  | correct/ | Canım, yaşlı hanımın arkasında çok komşunun yürüdüğünü söyledi. | Dear, she said that many neighbours are walking behind the old lady. | Accurate |
| A:33261:m | A1 | CC:MISSING | tava | wrong/M | Çanta neden bu kadar ağır? Üstünde tencere tava asılı. | Why is the bag so heavy? Pots are hanging on it. | Same meaning. |
| A:33274:c3 | A2 | L3 |  | correct/ | Hey, tam masanın üstünde yardım için mendil var, kanka. | Hey dude, there's a handkerchief right on the table to help. | Accurate |
| A:34687:c2 | A1 | CC:MISSING | giyiyor | correct/ | Bir kadın onun zümrüt kolyesiyle kırmızı giyiyor. | A woman wears red with her emerald necklace. | Accurate |
| A:34687:c5 | A1 | L3 |  | correct/ | Bir kadın onun zümrüt kolyesiyle kırmızı giyiyor. | One woman wears red with her emerald necklace. | Accurate meaning. |
| A:34701:c4 | A1 | L3:TIPrej |  | correct/ | Onlar nerede dinleniyor? Bir tuz gölünün suyunda. | Where are they relaxing? In salt lake water. | Acceptable mass-noun phrasing; same meaning. |
| A:35311:c4 | A1 | L3:TIPrej |  | correct/ | Açıkçası etkileyici: sen ona kadar sayıyorsun ve on numaralı kar tanesi konuyor. | Frankly, it's impressive: you count up to ten and snowflake number ten settles. | Meaning matches. |
| A:35621:m | A1 | L3:TIPrej |  | wrong/M | Hey, o onun kollarını havaya kaldırıyor çünkü başarı çok büyük. | Hey, she raises her arms because the success is huge. | Same meaning; she acceptable |
| A:35823:c2 | A1 | L3:TIPrej |  | correct/ | İki genç kanepede oyun oynuyor. | Two teenagers play games on the couch. | Accurate meaning. |
| A:35823:c4 | A1 | L3:TIPrej |  | correct/ | İki genç kanepede oyun oynuyor. | Two young people play a game on the sofa. | Faithful meaning. |
| A:35823:m | A1 | CC:MISSING | oyun | wrong/M | İki genç kanepede oyun oynuyor. | Two young people are playing on the sofa. | "playing" covers "oyun oynuyor" |
| A:36865:m | B2 | L3:TIPrej |  | wrong/M | Dinle, o bana yarına kadar o kütüklerin küle dönmüş olacağını söyledi. | Listen, he told me those logs will have turned to ash. | Only time adverbial dropped, acceptable |
| A:43555:c5 | B1 | L3 |  | correct/ | Dün taksi yoğun saatte tek elle sürüldü; belli ki şehrin en güvenli yolculuğu. | Somebody drove the taxi with one hand in rush hour yesterday; obviously the safest ride in the city. | Active with somebody, same meaning |
| A:43602:c5 | B1 | L3:TIPrej |  | correct/ | Elleri yapış yapış bir felaket! Ve kolları da. | His hands are one sticky disaster! His arms are too. | Meaning matches. |

## False acceptances (18) by cause

by layer {'L3+CC:NONE': 18}; by writer type {'T': 1, 'None': 5, 'M': 10, 'W': 2}; by level {'B1': 7, 'A2': 6, 'A1': 1, 'B2': 4}

| aid | lvl | layer | cc | writer type | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:2236:t | B1 | L3+CC:NONE | none | T | Halatta elleri titriyor, yani yukarıda ödü kopuyor olmalı. | His hands were shaking on the rope, so he must have been terrified up there. | Past time frame; Turkish is present. |
| A:8787:c4 | B1 | L3+CC:NONE | none | None | Bu rauntan önce iki raunt yaptığı için kolları yanıyordu. | Her arms burned because she had already done two rounds before this one. | Added 'already' not in source. |
| A:11580:m | A2 | L3+CC:NONE | none | M | Açık ağzına bak! Muzu yemek üzere. | Look at his mouth! He's about to eat the banana. | Dropped adjective 'open' |
| A:14306:c5 | A2 | L3+CC:NONE | none | None | Ortadaki buz, iskelenin yanındakinden daha ince. | Ice in the middle is thinner than that next to the pier. | Missing obligatory article before "Ice" |
| A:20891:w | A1 | L3+CC:NONE | none | W | Dar sokakta büyük bir su birikintisine atlıyor. | He jumps into a big puddle in the wide street. | "wide" instead of narrow |
| A:26708:m | A2 | L3+CC:NONE | none | M | Onlar her akşam buraya çıkarlar ama şimdi el ele tutuşuyorlar. | They come up every evening, but now they're holding hands. | Dropped place word "here" |
| A:27364:m | A2 | L3+CC:NONE | none | M | Doktordan çoktan randevu aldı. O ayak bileğini sonsuza dek dinlendirecek! | She has already made an appointment. She is going to rest her ankle forever! | Dropped 'from the doctor' |
| A:32116:c5 | A2 | L3+CC:NONE | none | None | Canım, yaşlı hanımın arkasında çok komşunun yürüdüğünü söyledi. | Sweetie, he told me many neighbors were walking behind the old woman. | Adds 'me'; Turkish only says 'said'. |
| A:36188:c5 | A2 | L3+CC:NONE | none | None | Yeleğin kolu yok, bu yüzden ceketten daha az malzeme gerekir. | The vest has no arms, so it takes less material than the jacket. | 'arms' wrong for sleeves. |
| A:36687:m | B1 | L3+CC:NONE | none | M | Bol kolları görünce terzi anında karar veriyor: onları da düzeltecek. | When he sees the sleeves, the tailor decides instantly: he will fix them too. | Dropped adjective "baggy" |
| A:36687:w | B1 | L3+CC:NONE | none | W | Bol kolları görünce terzi anında karar veriyor: onları da düzeltecek. | When he sees the baggy trousers, the tailor decides instantly: he will fix them too. | trousers instead of sleeves |
| A:39538:m | B2 | L3+CC:NONE | none | M | Şu anda alnı terden parlıyor; kusursuz planlama, belli ki. | Right now his forehead is shining; perfect planning, clearly. | Dropped 'with sweat'. |
| A:40373:m | B1 | L3+CC:NONE | none | M | Kanka, o yabancı yaşlı adama gerçek bir iyilik gösterdiğinde bardaktan boşanırcasına yağmur yağıyordu, yalan yok. | Bro, it was pouring with rain when he showed that stranger a real kindness, no lie. | Dropped 'old man'. |
| A:40618:m | B1 | L3+CC:NONE | none | M | Sen her bir bavulu o minibüse kaldırdın, değil mi? Sırtın tamamen mahvoldu! | You lifted every single suitcase, didn't you? Your back is completely ruined! | Dropped direction phrase 'into that minibus'. |
| A:43555:m | B1 | L3+CC:NONE | none | M | Dün taksi yoğun saatte tek elle sürüldü; belli ki şehrin en güvenli yolculuğu. | Yesterday the taxi was driven during rush hour; clearly the safest ride in the city. | Dropped 'one-handed' |
| A:43956:c3 | B2 | L3+CC:NONE | none | None | O çorbayı tattığında, adam çiçekleri çoktan arkasına saklamıştı. | When she tasted the soup, the man had already put the flowers behind his back. | "put" loses the meaning "hid" |
| A:43956:m | B2 | L3+CC:NONE | none | M | O çorbayı tattığında, adam çiçekleri çoktan arkasına saklamıştı. | When she tasted the soup, the man had already hidden the flowers. | Dropped place phrase 'behind his back' |
| A:44014:m | B2 | L3+CC:NONE | none | M | Bahçede şişme şatonun yanındaki çadır hâlâ ayakta duran tek şey. | The tent next to the bouncy castle is the only thing still standing. | Drops "in the garden". |

## Judge duplicate disagreements

