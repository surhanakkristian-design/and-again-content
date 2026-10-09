# Owner decisions after Phase 2L (22 Sept 2026)

Recorded at the start of the SK/CZ upload session, as given in the upload brief.

1. **Czech accepted on the point estimate** (coverage 95.17 %, FA 3.23 %). The FA interval (upper bound 5.45 %) is waived. No re-measurement.
2. **Content-check line** "tense, articles and word order are not part of this question" (2L defect 1): **KEPT**.
3. **Judge line replaced by "- Added content is wrong."** (2L defect 3): **CONFIRMED** as intended.
4. **Upload of the SK and CZ files: APPROVED.** The only write allowed is an UPDATE of existing `exercise_localizations` rows for the exercises and languages in the two files. No INSERT, DELETE, schema change, migration, deploy or push.
5. **Frozen checker configuration for both languages:** SOURCE-ONLY + content check, TIP rejected (2L Part C freeze 0042aaa, Czech freeze f9f794c).

## Decisions after the SK/CZ upload stop (22 Sept 2026, Phase 3A brief)

6. **The 54 disputed English references:** KEEP the live English. No write.
7. **structure_json:** WAITS until app integration. No column is created now.
8. **The SK/CZ upload is a no-op** (`src` already live on 8,128/8,128 rows). **Closed.**
9. **Next step:** integrate the SK + CZ checker into the app (Phase 3A).

## Decisions after the Phase 3A Part A stop (22 Sept 2026, Phase 3A continued brief)

10. **AG is DROPPED from the app checker** (option C). App stack = F4v2 -> F4v3 -> L3 -> content check. The 14 AG-decided items are re-measured first (Part A2).
11. **Scope option C:** for learners whose native language is `sk` or `cz`, the translate format shows ONLY the 4,064 selected exercises (the exercise_ids of upload_sk_final.xlsx / upload_cz_final.xlsx, same ids in both), all checked by the new checker. Every other native language keeps today's behaviour and today's check.
12. **ONE additive database change approved:** a new small table listing the 4,064 selected exercise_ids (Part A3). No change to existing tables.

## Decisions before the Phase 3B deploy (22 Sept 2026, Phase 3B brief)

13. **Production Gemini spend for the sk/cz check approved** (projected about $0.14 per 1,000 checks).
14. **Cache stays OFF on the sk/cz path.** No database change for it.
15. **The exact-reference match stays for sk/cz.**
16. **No feedback text for sk/cz:** a wrong answer shows only the correct English sentence, then advances. The MISSING word is not shown.
17. **sk/cz learners of German, Spanish or French keep today's check** (the new checker judges English only).
18. **The 23 concepts without a selected exercise stay as they are.** No change.
19. **No backward compatibility for old app versions is needed** (almost no active users). Deploy as built.
20. **Deploy approved** as in the Phase 3B brief.

## Decision after the Phase 3B deploy (22 Sept 2026, Phase 3C-prep brief)

21. **Warm-up for check-translation:** add a warm-up ping so the learner does not wait for a cold start (built and tested in Phase 3C-prep, deployed separately).

## Decisions for the new languages (22 Sept 2026, Wave 1 brief)

22. **Genderless sources:** when the source does not mark gender (e.g. Turkish/Hungarian 3rd person, Spanish "su", French "son/sa/ses"), BOTH he/she and his/her are correct. This rule is added only to the new languages' prompts.
23. **Explicit-subject rewrite** (arm B, as for sk/cz) for es, ua, tr, hu, on the 4,064 selected exercises only.
24. **Gemini budget for all six new languages:** up to $3.00 in total.
25. **Two waves:** wave 1 = de, ua, es (Wave 1 brief); wave 2 = fr, tr, hu (later).

## Decisions for the data pass (22 Sept 2026, Data pass brief)

26. **Headless CLI sessions are NOT used.** All Claude work runs as Opus subagents in the main session (the headless OAuth token belongs to an old account).
27. **Rewritten/translated native sentences go DIRECTLY into exercise_localizations.** The owner confirmed that the gap-fill fields and chunks of non-English languages are not used by the app.
28. **Translate ALL 10,283 exercises into de/ua/es/fr/tr/hu:** the 2,015 selected first, then the rest.
29. **Check the 4,064 selected SK and CZ sentences for grammar errors and FIX them at once**, with backup.
30. **Fix the punctuation defects found in Wave 1 Part A.**

## Decisions for the Spanish re-measurement (22 Sept 2026, Wave 1 es brief)

31. **Spanish is re-measured with the packet-level fix:** 8 shuffled judge packets instead of 4 (still ONE judge prompt, shuffled across levels, 80 hidden duplicates in different sessions); after each session the returned jid set is checked and a deterministic follow-up session judges the MISSING jids only, with the same prompt, merged; cap 2 follow-ups per packet. Every packet is an Opus subagent (decision 26).
32. **Grammatical gender decides:** a grammatically masculine source noun (e.g. "спортсмен", "el atleta") is "he"; "she" is wrong. Decision 22 covers only sources that mark no gender at all.
33. **An ADDED interjection (e.g. "Wow", "Bro") is NOT an error**, mirroring the rule that a dropped interjection is not an error. Added content of any other kind stays an error. This changes the JUDGE prompt only; the checker prompts stay byte-identical (the checker already accepts these, so no re-measurement is needed).

## Decisions for the overnight deploy (22 Sept 2026, overnight deploy brief)

34. **The fast-start, reference-data cache, icon line weight, exercise-mix and typed-input fixes are deployed to the web.**
35. **Exercise mix:** a chosen exercise type may be mixed with other types so the 3-in-a-row rule and the build/typed opening can hold. Approved as built.
36. **Storage caching:** Words and Thumbnails get `max-age=31536000, immutable`; user-media gets `max-age=86400`.
37. **The scope restriction to the 4,064 selected exercises also applies to native de, ua and es learners of English.**
38. **Decision 32 (grammatical gender) stays in the JUDGE prompt only.** The checker prompts stay byte-identical and nothing is re-measured.
39. **The last 2 untranslated cells (40497 tr, 39286 hu) are fixed.**

## Decisions for the CDN / ua check / translate mix brief (23 Sept 2026)

40. **Purge the Cloudflare CDN copies of the Words and Thumbnails buckets** so the new Cache-Control takes effect now.
41. **The Ukrainian checker is sanity-checked offline** after the two live false rejections on exercise 1067.
42. **The translate format must appear more often for the routed natives** (sk, cz, de, ua, es learning English), while the "at most 3 of the same exercise in a row" rule keeps holding.
43. **Signed-URL caching for user-media is deliberately left unsolved for now.**

## Decisions for the cadence deploy / mismatch scan brief (23 Sept 2026)

44. **The CDN purge was run by the owner on 23 Sept 2026; verified on 10 files.**
45. **The translate cadence (at least 1 translate card in 6, rule "max 3 of the same kind in a row" intact) is deployed.**
46. **The selected 4,064 exercises are scanned in all six non-English natives for source/reference mismatches.** Report only, no fix in this run.

## Decisions for the mismatch fix brief (23 Sept 2026)

47. **All 303 confirmed mismatches are fixed:** the 174 Spanish pronouns, the 123 other native rows, and the 6 rows where the English is wrong.
48. **Spanish keeps the explicit subject;** only the wrong pronoun is corrected (not a restore from the Part 4 backup).
49. **Where the native sentence says something entirely different** (most of the Hungarian A1 series), it is re-translated from the English, not patched.
50. **The 440 native rows with an empty gap word stay as they are for now.**

## Decisions for the pronoun sweep / wave 2 brief (23 Sept 2026)

51. **A deterministic pronoun/person sweep runs over all 4,064 selected exercises in de, ua, es, fr, tr and hu;** what it finds is fixed with the same two-pass rule (one judge, an independent verifier, only rows both call wrong are fixed).
52. **Wave 2 (fr, tr, hu) is measured with the same method and the same targets as wave 1.**

## Decisions for the fr deploy / punctuation / tr-hu retry brief (23 Sept 2026)

53. **French is routed and deployed;** fr learners of English get the translate format only on the 4,064 selected exercises.
54. **Missing sentence-final punctuation is repaired in ALL nine languages, across the whole table,** not only the selection.
55. **Turkish and Hungarian are fixed and re-measured on NEW sets:** vocatives droppable, the genderless rule made effective, punctuation repaired.
56. **Rows where a native distractor equals the correct answer are NOT an issue:** the options are shown to the learner in English. No action, and this is not to be raised again.

## Decisions for the tr/hu deploy / 5 source fixes brief (23 Sept 2026)

57. **Turkish and Hungarian are routed and deployed.** All eight non-English natives (sk, cz, de, ua, es, fr, tr, hu) now use the SOURCE-ONLY checker, each restricted to the 4,064 selected exercises.
58. **Type-69 definition rows keep NO sentence-final mark, in every language, as the English rows do.** apply_type69.py is not run and the convention in validate_part.stem_sentence stays.
59. **Five broken source sentences are fixed:** tr 27060, tr 31993, tr 13301, hu 31482, hu 36905.

## Decisions for the new-exercises data groundwork brief (23 Sept 2026)

60. **Three new exercise types are being built:** Tinder (images, all learning languages), Listening and Speaking (videos only, English as the learning language only).
61. **Video voiceover transcripts go into the database;** they drive Speaking (which sentences are acceptable, subtitles) and Listening (eligibility and answer checking).
62. **Listening questions and their correct answers are pre-generated and stored,** so the runtime check is a fast comparison by Gemini.
63. **Speech recognition for Speaking uses Gemini** (the key already exists); pronunciation is judged leniently; audio is never stored.
64. **Tinder: no pair table.** At runtime one correct sentence for the image, or one sentence taken from a DIFFERENT word of the SAME level. Correct/incorrect ratio 50:50. Images: all styles. 30 s to start, +5 s per correct answer, no penalty for a wrong one, no upper limit, counts towards the streak.
65. **Background music for Tinder: royalty-free tracks from Pixabay,** several, played at random.

## Decisions for the widen-eligibility / more listening questions / music brief (23 Sept 2026)

66. **Eligibility is widened: a spoken line qualifies if it contains a FINITE VERB.** An explicit subject is no longer required, so imperatives and set phrases count ("Take me to the tower.", "Hold them like this, slowly."). A line with no verb at all ("Awesome!", "Two coffees.", sound markers) still does not qualify.
67. **Listening may have MORE THAN ONE question per video** where the transcript carries them (up to 3).
68. **Music: tracks 01 (upbeat electro), 02 (disco funk) and 05 (dance pop) are kept.** Tracks 03 and 04 are dropped.

## Decisions for the finish-the-three-new-exercises brief (23 Sept 2026)

69. **Tinder keeps +5 s per correct answer, with no upper limit and no XP cap.** Accepted as built.
70. **Listening and Speaking filter their videos by the learner's level (A/B),** the way Tinder does.
71. **The free listening check forgives ONE wrong letter in a word of 5+ letters (the speaking rule),** and the stored correct spelling is shown in green above the learner's answer whenever the two differ.
72. **Tinder, Listening and Speaking go live on the web.**

## Decisions for the UI fixes (bubbles) + cadence brief (23 Sept 2026)

73. **The new exercises appear much more often:** Tinder about once every 6 cards, Listening/Speaking about once every 4 cards, and the first of them inside the opening 5 cards.
74. **Bubble rule for the whole app:** text in the learner's NATIVE language sits in a WHITE bubble, text in the LEARNING language sits in a BLACK glass bubble, per the Figma designs. — *For translations: superseded by 148 (the translation shows inside the same black bubble; no white cell).*
75. **The translate input follows Figma 1623-1722:** a compact field, not the oversized bubble that was live.

## Decisions for the overnight brief: comment questions, exercise rebuild, translations (23 Sept 2026)

76. **The exercise set is rebuilt.** Choice, build, typed and translate stop being shown; their DATA STAYS untouched and the code paths stay behind one switch. Multiplayer is out of scope for now.
77. **Remaining exercises:** Tinder (images AND videos, all learning languages), Speaking-repeat, Comment (all learning languages, typed or spoken), Listening (English only, because the audio is English).
78. **Comment questions:** one OPEN question per media per level (A and B), from the asset description, max 70 characters, written in English and translated into the other 8 languages.
79. **Tinder has NO timer, NO rounds and NO music:** one sentence per card. The music files and the audio bucket stay, unused.
80. **Tinder may appear in runs of up to 8 cards;** the max-3 rule no longer applies to it. Other kinds keep it.
81. **Comment answers are stored from the start** (not shown to anyone yet) and are checked for grammar AND for whether they fit the media. Limit 60 words.

## Decisions for the recommender brief (24 Sept 2026)

82. **The feed and the Training wall are driven by what the learner shows interest in.** Similarity = the SAME category, style AND word topic; among equals, the media that does best with other learners comes first.
83. **A rejection is a FAST SKIP** (under 2 s on the card). Closing the session with the X, a wrong Tinder answer and the 1-hour skip are NOT rejections.
84. **A rejection is read in context:** after a run of similar cards it means "enough of this topic for now", so the feed switches TOPIC rather than downgrading it. It switches again on the next rejection, and again, until the learner stays; if nothing sticks, it falls back to their long-term favourite topics.
85. **A media the learner rejected once or twice is never shown to them again.** A topic is only downgraded after repeated rejections in DIFFERENT situations.
86. **The Training wall is re-ranked after every finished session and on every app start.** For now only the ORDER changes; nothing is hidden (hiding comes later, with more content).
87. **Cold start:** a learner we know nothing about gets mostly media uploaded on or after 10 Sept 2026 (1,489 of 3,667). As soon as their own signals exist, those decide; new media still fill the gaps whenever the picture is thin.

## Decisions for the fix brief: comment check, microphone, translations on every card (24 Sept 2026)

88. **BLOCK_AFTER_REJECTIONS = 2:** a media is blocked only after the SECOND rejection, so one accidental flick does not remove it for good.
89. **EVERY sentence and question the learner sees must be translatable on demand into their native language, on every card kind.**
90. **The comment check function is deployed** so the comment exercise works locally and live.

## Decisions for the Tinder drag, UI corrections, listening/speaking translations, meaning check and deploy brief (24 Sept 2026)

91. **The translation toggle works on EVERY card kind,** listening and speaking included.
92. **No XP badge in the top bar.**
93. **All top-bar and rail buttons keep the glass style of the Figma mockups;** the skip pill uses the mockup's font weight (not bold); every icon stroke is ICON_LINE_WIDTH (1.6 pt), the X included.
94. **Tinder uses a real drag-and-throw card,** identical on mobile and desktop, with the verdict mark DRAWN as the drag progresses.
95. **Listening questions and the spoken lines used as subtitles are translated into the 8 languages by CLAUDE agents** (no Gemini), stored in a new table.
96. **The comment check judges MEANING as well as grammar:** an answer that is nonsense, or does not answer the question, is wrong even when the grammar is perfect.
97. **This run ends with a web deploy.**

## Decisions for the swipe-up skip, transcript fix and gender-neutral feedback brief (24 Sept 2026)

98. **A fast upward flick on a Tinder card is an explicit SKIP:** it moves to the next card and counts as a rejection for the recommender, exactly as a fast skip does on the other card kinds.
99. **The 12 garbled English subtitle lines are re-transcribed from the video audio** and their translations are added.
100. **Every piece of feedback the learner reads must be gender-neutral in every language.**

## Decisions for the translation swap, blank cards and Tinder corners brief (25 Sept 2026)

101. **The translation REPLACES the text in place:** there is always exactly ONE bubble, always the black glass one. Tapping ⇄ swaps the learning-language text for the native one, tapping again swaps it back. The learner can answer with either language showing. White bubbles are no longer used for translations anywhere.
102. **The translation state does NOT carry over:** every new card starts in the LEARNING language, even if the learner left the previous card translated. — *Superseded by 149.*
103. **A card must never show without its media.** If the media cannot be shown, the card is replaced.
104. **The Tinder card keeps the mockup's rounded corners at all times,** including while dragging and flying.

## Decisions for the sound-from-the-start and hold brief (25 Sept 2026)

105. **Comment, listening and speaking cards play WITH SOUND from the first frame.** The muted fallback is a last resort only, when the browser truly refuses, never the normal path.
106. **The Tinder card has SQUARE corners at rest.** The corners round only while the learner is holding the card (pointer down), and go square again when it is released or flies away. (Supersedes 104.)
107. **While the card is held, every other control disappears** (the rail, the top bar, the check and X buttons), so only the card and its verdict mark are on screen. They come back when the card is released.

## Decisions for the card-under corners, tap, verdict mark and audio pool brief (25 Sept 2026)

108. **The card UNDERNEATH has the same rounded corners as the held card,** so the two read as one stack.
109. **A single tap on a card's video does nothing:** it must not pause, play or toggle anything. The card moves only while it is held.
110. **The verdict mark is drawn on the OPPOSITE side to the drag:** dragging RIGHT (yes) draws the green check on the LEFT of the card, dragging LEFT (no) draws the red X on the RIGHT. The mark is attached to the card, so it moves and tilts with it.
111. **AUDIO_UNLOCK_POOL_SIZE goes from 12 to 24.**
112. **The desktop left sidebar (AppShell) stays visible while a card is held.** Only the feed's own chrome fades.

## Decisions for the live speech text, result states and instructions brief (25 Sept 2026)

113. **Speech is written into the input WHILE the learner speaks,** word by word, not as one sentence at the end. This applies to Speaking-repeat and to the Comment/answer input.
114. **A CORRECT answer shows no text at all:** the answer pill simply turns green. The correct version is not repeated and nothing is praised.
115. **A WRONG answer shows the corrected version,** as the Figma "wrong" frames show. In Speaking-repeat the corrected version is THE SENTENCE FROM THE VIDEO, not a repair of what the learner said.
116. **On a wrong answer only, a SHORT, gender-neutral encouragement is shown in about 3 of 10 cases,** chosen at random ("Blízko.", "Skoro tam.", "Ešte raz."). Never on a correct answer. *(superseded by 256)*
117. **The instructions of an exercise are shown only the FIRST time that learner opens that exercise kind** (stored per device / account). Afterwards they appear only when the learner taps the exercise icon in the top left. This applies to listening, speaking, comment AND Tinder. — *For Tinder: superseded by 150 (the hint on the first Tinder card of each session).*
118. **After SKIP the card moves on by itself after 2 s.** After a correct or a wrong answer it does NOT move on: the learner decides when to continue.
119. **No tip for now.**

## Decisions for the Tinder texts brief (25 Sept 2026)

120. **Tinder stops using grammar-exercise sentences.** Every media gets FOUR purpose-written English texts, stored in a new table (`tinder_sentences`) and translated into the 8 other languages later.
121. **Per media: a TRUE sentence and a FALSE sentence (max 60 characters), plus a TRUE short phrase and a FALSE short phrase** (max 30 characters, 2-5 words, not sentences).
122. **Grammar first, humour second.** 70 % of the sentences must be short (max 30 characters), counted separately for A-level and for B-level media.

## Decisions for the vocabulary sessions brief (25 Sept 2026)

123. **Vocabulary tiles disappear from the Training home grid.** They live only in the profile's vocabulary section. The media grid in Training keeps only ordinary media tiles.
124. **A vocabulary tile shows its NAME in a white pill in the top left,** as the owner's screenshot marks.
125. **Opening a vocabulary still shows its word tiles (unchanged). TAPPING A WORD now starts an exercise session for that vocabulary:** it begins with the word the learner tapped, then the other words follow in random order and the list repeats endlessly, so a learner can go through it ten times.
126. **A vocabulary session uses all three exercises: Tinder, Speaking-repeat and Answer (the comment/answer card).** On a later pass through the same word, a DIFFERENT exercise is chosen when one is available.
127. **Two automatic vocabularies are kept per learner and filled automatically from their answers: "Not yet" (words answered wrong) and "You got this" (words answered right).** A word moves from "Not yet" to "You got this" as soon as it is answered correctly, and back on a wrong answer, so both lists always show the current state.
128. **The two automatic vocabularies cannot be deleted.** Their settings sheet offers only SHARE and RESET (Figma 1796-651).

## Decisions for the Tinder finish brief (25 Sept 2026)

129. **Tinder switches from grammar-exercise sentences to `tinder_sentences`.** The old source stays in the code behind a fallback for media that have no row yet. — *The fallback part is superseded by 151.*
130. **The four texts are mixed independently of level:** every Tinder card picks at random whether it shows the PHRASE pair or the SENTENCE pair, about 50:50, the same on A-level and B-level media. There is no difference between the levels.
131. **The English rows are translated into de, ua, es, fr, tr, hu, sk, cz,** in this order of usefulness: sk, cz, de, ua, es, fr, tr, hu.

## Decisions for the Tinder translations brief es, fr, tr, hu (26 Sept 2026)

132. **The Tinder texts are translated into es, fr, tr and hu with the same method as sk, cz, de and ua.**

## Decisions for the 17.9.2026 image batch import brief (26 Sept 2026)

133. **The 17.9.2026 image batch is imported WITHOUT the ~70 grammar exercises per level.** Only what the app needs to show the media in Tinder, Comment, the feed, the Training wall and vocabularies is created.
134. **The extra word "chosen" (not in the workbook) is added:** adjective, "selected as the best or most suitable; the chosen one", CEFR B1.
135. **A target whose word AND meaning already exist in the database is attached to the EXISTING concept** (a new picture for a known word). Only genuinely new meanings get a new concept.
136. **Targets without an image in the folder (the 29 rows not marked done, or any other missing file) are skipped.**

## Decisions for the 17.9 follow-up and 26.9.2026 image batch brief (26 Sept 2026)

137. **Media 6578 ("short", a sand timer) gets the Tinder texts written by the owner's planning chat.** They go through check.py and an independent verifier who looks at the image; every language that passes is inserted.
138. **Of the 6 images dropped from batch 17.9, permit_6599, outrageous_8596 and lose-contact_9803 are imported after all,** using the owner's reading: permit = the raised flat hand tells the dog to wait, it needs permission before it may go ahead; outrageous = someone walked through the wet concrete on purpose, which is outrageous; lose contact = the woman has lost contact with other people, a loner alone with old letters.
139. **right_242, pointless_7314 and unfollow-someone_9908 are to be regenerated:** marked not done in the image-targets workbook, and their orphan storage objects are deleted.
140. **Batch 26.9.2026 is imported like batch 17.9:** media, words, Tinder texts, comment questions and one minimal level exercise per media; no grammar exercises (same as decision 133).

## Owner addendum to the 17.9 follow-up brief (26 Sept 2026)

141. **bloody (media 5662), affordable (5534) and discrimination (5862) stay, with new Tinder texts and comment questions** that follow the owner's reading: bloody = the man is not really bleeding, he is covered in tomato sauce ("bloody" in quotation marks as an exaggeration, in every language); affordable = the flowers are affordable FOR HER, she can pay for them; discrimination = the bouncer lets the man in and stops her because she is a woman.
142. **respectable (6514, target 9391) and sentence (6567, target 9399) are removed from the app and regenerated later.** Their concepts (4616, 4664) and word_localizations stay so the new images can attach to them.
143. **The rest of the 17.9 review page (the other weak images and the 9 meanings without their own picture) is accepted as it is.**

## Owner addendum 2 to the 17.9 follow-up brief (26 Sept 2026)

144. **Media 6975 "company" (concept 5056, "a guest or guests visiting someone") uses the owner's replacement image** (generic file name hf_20260926_121746_344e7e40-b316-4960-8962-ada303237f21.png), uploaded under the new object name company_6975b.webp. The file is the replacement for target 3636, never a media of its own. Its description, Tinder texts, comment questions and 74/75 exercise are rewritten from the new image; the meaning taught is "having company": unexpected visitors arriving.

## Decisions for the card fixes brief (26 Sept 2026)

145. **The comment card no longer shows the character counter ("0/60"); the 60-character limit stays.** (The counter was the 0/60 word counter of the pre-25 Sept build; the limit in the code is 60 words and stays as it is.)
146. **Every exercise card shows its exercise-type icon in the top-left corner.**
147. **After a CORRECT comment answer the card shows only the learner's answer in its green cell:** no model answer, no verdict line. After a wrong answer the model answer and the explanation stay.
148. **The ⇄ translation shows the translated text inside the same black text bubble, replacing the original text.** The earlier rule that the translation appears only in a white cell (74) is withdrawn.
149. **The ⇄ translation stays on across cards until the learner turns it off.**
150. **The Tinder hint "swipe left or right" appears only on the first Tinder card of a session** (the normal feed and a vocabulary session each count as a session).
151. **Tinder cards use only the tinder_sentences texts.** A media without a complete row (learning language, else English) is not dealt as a Tinder card; the old exercise-sentence path is removed from Tinder.

## Owner addendum to the card fixes brief (26 Sept 2026)

152. **The answer controls of the Answer/Comment card and of the Speaking-repeat card follow Figma 4evr-2.0 frames 1741:183 and 1786:365.**

## Decisions for the comment notice brief (27 Sept 2026)

153. **The answer controls stay as in Figma 1741:183 / 1786:365: one long pill (speak part + write part) and ONE round chevron under it that sends and checks at once.** There is no separate "check answer" button.
154. **The comment limit stays 60 WORDS (COMMENT_MAX_WORDS = 60), not 60 characters.** This settles the open question of 145 (whose wording said "60-character limit"): no character cap is added.

## Decisions for the Training wall brief: fresh tiles, labels, meaning count (27 Sept 2026)

155. **Returning to the Training wall without having tapped a tile shows tiles not seen before; tiles already seen go to the end** (least recently seen first). A tile counts as seen when it entered the wall's rendered window (as the impression events); kept per learner and per guest device.
156. **Newer media rank higher for everyone (the owner's content keeps getting better); learners with history get their liked topics, unseen and newer first.** Newer = the newest upload batch of media.uploaded_at first, found from the upload times themselves (no fixed date). Supersedes the "recent = on/after 10 Sept 2026" part of 86 for the wall.
157. **The search field shows the live number of meanings, rounded to thousands: "+" only when the rounded number is not above the real count** (5,400 -> 5,000+; 5,800 -> 6,000).
158. **Every wall tile shows the meaning it represents, in the learning language (Figma 1105:584).**
159. **The settings icon in the wall header uses the same stroke as the heart icon.**

## Decisions for the Training wall brief: layout, video slots, thumbnails, results in Profil (27 Sept 2026)

160. **Wall and bottom bar follow Figma 1105:584: lower tiles (more per screen), smaller search bar and header icons, a lower bottom bar used on every screen of the app.** (Not built yet on 27 Sept: the Figma Dev Mode MCP Server did not answer; see WALL_LAYOUT_VIDEO_THUMBS_REPORT.md.)
161. **Video tiles sit at fixed positions and play: phone (3 columns) positions 3, 4, 9, 10, 15, 16 … (6k+3 and 6k+4, 1-based), i.e. one video per row on the edge, alternating right and left; never two video tiles side by side. Desktop (4 columns): the same principle, one video per row on the edge column, alternating right and left** (positions 4, 5, 12, 13 … = 8k+4 and 8k+5).
162. **Image tiles on the wall load the thumbnail on every device; the full image only when the media is opened.**
163. **A thumbnail is always smaller (lower resolution and fewer bytes) than its full image.**

## Owner addendum: results screen moves to Profil (27 Sept 2026)

164. **Pressing X in a training session no longer shows the results screen; points are saved as before and summed until the learner opens Profil, where the results screen (with the bottom bar visible) is the first screen; "Keep going, Tiger" then shows the profile.**

## Decisions for the noun display form brief (27 Sept 2026)

165. **Every noun gets a dictionary display form in en, de, es, fr, stored next to the translation (`word_localizations.display_form`) and used for tile labels: en with a/an (none for uncountable, plural-only and proper nouns, following the meaning); de, es, fr with the definite article (der/die/das, el/la/los/las, le/la/les), and in French, where the article elides to l', the indefinite un/une so the gender stays visible. sk, cz, ua, hu, tr stay without articles.**

## Decisions for the wall Figma layout + tile previews brief (27 Sept 2026)

166. **Video tiles play a small preview file (400 px wide, the first 5 s, or the whole clip if it is at most 6.5 s, no audio); the full video plays when the media is opened.** (`media.preview_url`, bucket `Previews`.)
167. **The 242 full videos with the moov atom at the end are remuxed with faststart (no re-encode, no quality change) and served from new objects** (`Words/<title>_fs.mp4`; the old objects stay).
168. **At the end of the wall, when the images run out (about row 450 on phone, 300 on desktop), the remaining videos stay on the wall even if side by side; nothing is left out.** (Settles open point 3 of WALL_LAYOUT_VIDEO_THUMBS_REPORT.md; decision 161 applies while images last.)

## Decisions for the translation fix + display form brief (27 Sept 2026)

169. **The 98 translations flagged in the noun display-form run are corrected, and the corrected nouns get a display form with the same rules (decision 165).**
170. **My Vocabulary, the vocabulary group detail and the player word pill show display_form for nouns in en/de/es/fr; sorting, A-Z grouping, search, matching and saved vocabulary text keep the bare word.**
171. **English display forms follow British pronunciation ("a herb").** (Settles open point 3 of NOUN_DISPLAY_FORM_REPORT.md.)
172. **The vocabulary group detail uses the same grid and tile labels as the Training wall: on desktop the same column count, tile size and grid width as the wall; on every device the meaning label bottom-left in the wall's style (no white pill top-left); its image tiles use the thumbnail (this replaces the earlier "vocabulary detail keeps the full image"). Video tiles in the vocabulary group detail follow the wall's video-slot rule (decision 161): videos on the edge slots, never two side by side, playing only while on screen.**

## Speed rules + instant open brief (27 Sept 2026)

Standing speed rules (also in the app repo's CLAUDE.md, section "Speed rules (owner, 27 Sept 2026)"):

173. **Model:** Opus for the main session, for writing and verifying content (translations, texts, exercises) and for code; Sonnet for mechanical subagents (running scripts, encoding, uploads, file checks, test runs, screenshots, measurements).
174. **Speed measurements only when the brief is about speed;** then 3 runs, the median, and say when a difference is inside the spread.
175. **Screenshots only for visual changes, main screens only.**
176. **Report:** first line, what changed, open points; tables, logs and per-run data go into asset files, not into the report text.
177. **Quality gates never drop:** tests, type checks, style/colour checks, deploy verification, backups before writes, writer + verifier for content.
178. **Opening a media shows the already-loaded smaller file at once and swaps to the full-quality file when it is ready, for everyone (not only on slow connections):** images show `thumbnail_url` and cross-fade to the decoded `media_url`; videos show the thumbnail as poster and play the muted `preview_url`, then switch to the full video at the preview's position and cross-fade. Sound, audio exercises and all normal card behaviour start with the full file. This applies to tiles on the wall, in the vocabulary detail and every other grid, and to every card in a session.

## Phrase display form brief (27 Sept 2026)

179. **English phrase concepts that work as a verb (phrasal verbs and verb phrases such as "break apart", "hold up", "book a table") get the display form "to …"; other phrases (adjectives like "worn out", pronouns like "nobody", fixed expressions) stay as they are.**

## One card at a time brief (27 Sept 2026)

180. **A tap on a tile always opens that tile's media as the first card, whatever the pools' rules (level, cooldown, seen, rejected).**
181. **A session loads one card at a time: first only the card on screen (its media and its exercise data); only when that card is fully loaded (full-quality media and exercise data), the next card is chosen and prepared in the background. Always exactly one card ahead. No loading of whole pools (texts, questions, media) up front.**

## Intro text in the search slot brief (27 Sept 2026)

182. **The typing intro on the Training wall (shown after a page load, e.g. "Zapamätaj si slovíčka a…") is written in 12 pt inside the search bar's slot, at the level of the search placeholder; the wall grid never moves during or after it.**

## Next card on preview brief (27 Sept 2026)

183. **The next card is prepared as soon as the card on screen shows its thumbnail or preview and has its data (replaces "fully loaded" in decision 181). Still exactly one card ahead. The next card fetches its data and its thumbnail/preview at once; its full-quality file starts only after the card on screen has its full-quality file (or after the learner moves on).**
184. **Touch-down prefetch no longer fetches a byte range of the full video; images keep their touch-down prefetch.**

## Three videos and missing Tinder brief (27 Sept 2026)

185. **Media 12 (to hug), 43 (to spin) and 275 (argue) get a description, Tinder texts in 9 languages and comment questions (A + B, 9 languages) like every other media; the 13 missing Tinder translations of batch 26.9 are filled.**

## Intro text 24 pt brief (28 Sept 2026)

186. **The typing intro is 24 pt as in Figma 1876:434 (replaces the 12 pt of decision 182). A text that does not fit on one line at 24 pt gets a smaller size for that text only, just enough to fit, never below 14 pt (the placeholder's size). The grid never moves (decision 182 stays).**

## Small clean-up brief (28 Sept 2026)

187. **The slower full image of card 1 on Slow 4G (about +0.6 s, NEXT_CARD_ON_PREVIEW open point 1) is accepted; the next card keeps loading its data, thumbnail and preview at once.**
188. **Media 12, 43 and 275 get their transcripts and become listen/speak eligible like other videos if they meet the same rules.**

## Answers and unclear translations brief (28 Sept 2026)

189. **The exercise answers that still equal a corrected translation are updated to the corrected word; the 3 unclear translations are resolved by writer + verifier.**

## Search, stack and tap brief (28 Sept 2026)

190. **Every card in the swipe stack has the same rounded corners as the card being dragged, at every moment of a drag.**
191. **A short tap on a card pauses/plays it; a card is grabbed only after the finger/pointer moves beyond a small threshold.**
192. **The ⇄ translation button uses the same stroke width as the other icons in the card's right-hand rail.**
193. **The heart and settings icons are visible and tappable from the first frame, also during the intro (replaces the hidden-icons part of decision 186); the intro text uses the room left of them, with the existing per-text shrink rule (24 pt, down to 14 pt).**

## Gerund nouns brief (28 Sept 2026)

194. **bringing (3838), entering (4041), following (4113), modeling (5418) and solo (4703) stay nouns (part_of_speech and definition unchanged). Every translation becomes a noun naming the activity (e.g. sk "prinášanie", de "das Bringen"); the English display form has no article (uncountable activity, like "swimming").**

## Tinder phrase rule brief (28 Sept 2026)

195. **A Tinder phrase is not a sentence. Both phrases (true and false) contain the concept's key word exactly in its dictionary form, as on the tiles and in the vocabulary: verbs in the infinitive (en "to care", never "caring"; other languages their infinitive), nouns with the article the language needs (en/de/es/fr display_form; none for uncountable, plural-only, proper nouns; sk/cz/ua/hu/tr bare), adjectives in their base form, except that in sk, cz, ua, de, es and fr an adjective agrees with its noun (e.g. "nebezpečná cesta"). Lowercase first letter, except proper nouns and German nouns. Sentences may inflect and conjugate as before.**

## Comment questions sample 2 brief (28 Sept 2026) — DRAFT, pending the owner's approval of sample 2

196. **(draft) One comment question per media, by the word's level: a level-A word (type-74 level exercise, A1/A2) gets only a level-A question; a level-B word (type 75, B1/B2) gets only a level-B question.**
197. ~~**(draft) Length: en level A at most 7 words, level B at most 10 (a contraction counts as one word); sk A at most 8, B at most 12.**~~ WITHDRAWN 28 Sept 2026 (sample-3 brief, decision 202): the hard limits forced elliptical, ungrammatical questions.
198. **(draft) The key word is in every question, exactly that word: never a phrasal verb, idiom or related word in its place ("to order" is not "to order around"); in a normal question it may be inflected or conjugated; in a definition question it stands in its dictionary form, as on the tiles (display_form: "a coach", "to care", "self-confidence").**
199. **(draft) About one question in five is a definition question, exactly: How would you define "<key word in its dictionary form>"?, spread over levels and parts of speech.**
200. **(draft) The other questions are about the picture or the learner's opinion and are funny: playful, cheeky, a small twist, like the Tinder sentences, never mean (model: "Would you trade your lunch for a Czech beer?", level A shortened "Trade your lunch for a Czech beer?" — the shortened form is WITHDRAWN with 197, see 202-210). Plain inventory questions are phased out.**
201. **(draft) The sk question (and every other language) is a faithful translation of the en question: same content, same people and things, the key word translated, neutral natural language, never a different question; in a definition question the key word is in that language's dictionary form ("Ako by si definoval „tréner“?").**

## Comment questions sample 3 brief (28 Sept 2026) — rules for all future comment questions, APPROVED by the owner 28 Sept 2026

202. **(approved by the owner 28 Sept 2026) The word-limit rule (197) is withdrawn, and so is the shortened level-A form in 200. Rules 203-210 below replace 196-201 as the draft rules for all future comment questions, applied in this order of priority; a lower rule never excuses breaking a higher one.**
203. **(approved by the owner 28 Sept 2026) Rule 1 — Grammar 100 %, en and sk (and every language): every question is a complete, standard model question a teacher would write on the board: a subject and a finite verb, the auxiliary in yes/no and wh-questions ("Do you want …?", "Would you take …?", "What would you …?"), no ellipsis, no fragments, no imperatives with a question mark; correct articles, tenses, word order and punctuation; Slovak with correct case, agreement, aspect and word order.**
204. **(approved by the owner 28 Sept 2026) Rule 2 — Clarity: the learner understands at once what is asked and can answer from the picture or from their own opinion; no riddles, no "it"/"that" without a clear antecedent in the question or the picture.**
205. **(approved by the owner 28 Sept 2026) Rule 3 — One question per media, by the word's level: a level-A word (type-74 level exercise) gets only a level-A question; a level-B word (type 75) gets only a level-B question.**
206. **(approved by the owner 28 Sept 2026) Rule 4 — Level: A uses simple structures and everyday words (present simple/continuous, can, would like, would you …), as short as a complete question allows (a guide, not a limit: usually 5-9 words); B may use richer structures and opinion/"why" questions.**
207. **(approved by the owner 28 Sept 2026) Rule 5 — The key word, exactly that word, in every question: never a phrasal verb, idiom or related word in its place ("to order" is not "to order around"); in a normal question it may be inflected or conjugated; in a definition question it stands in its dictionary form (display_form, as on the tiles).**
208. **(approved by the owner 28 Sept 2026) Rule 6 — About one question in five is a definition question, exactly: How would you define "<key word in dictionary form>"? / sk: Ako by si definoval „<sk dictionary form>“?, spread over levels and parts of speech.**
209. **(approved by the owner 28 Sept 2026) Rule 7 — The sk question (and every other language) is a faithful translation of the en question: same content, same people and things, key word translated, grammatically perfect and natural.**
210. **(approved by the owner 28 Sept 2026) Rule 8 — Humour: the other questions are playful with a small twist, like the Tinder sentences, never mean, but only when rules 1-7 are fully met (model: "Would you trade your lunch for a Czech beer?"). Process: writer; a content verifier (rules 2-8) and a separate grammar verifier (rule 1 only, word by word, naming the exact error); a question passes only if both pass it; on failure the writer rewrites; after two failed rewrite rounds it is shown as failed with the reason.**

## Comment questions sample 4 brief (28 Sept 2026) — APPROVED by the owner 28 Sept 2026

211. **(approved by the owner 28 Sept 2026) Question types: about 40 % "picture" questions (about what happens in the picture or video: the person, animal or thing shown, what they do, why, what happens next, e.g. "Why is the woman dancing in front of the ruined castle?", "What is the robot ordering the others to do?"), about 40 % "you" questions (the learner's opinion or experience, e.g. "Would you trade your lunch for a Czech beer?") and about 20 % definition questions (decision 208); picture and you questions are mixed over levels A and B and over parts of speech. Nothing is invented that the media does not show.**
212. **(approved by the owner 28 Sept 2026) Level-A soft length target (refines 206): an English level-A question is usually at most 10 words. Grammar comes first: the target is never a reason for an incomplete or unnatural question; if a complete, clear question needs more words, it gets them. Level B has no target.**
213. **(approved by the owner 28 Sept 2026) In a definition question the Slovak key word (and every other language's) is the dictionary form of the word for THIS sense (the definition taught), not a word of another sense of the English word (e.g. "waiting" = ready to be used at any moment → not „pripravený“).**
214. **(approved by the owner 28 Sept 2026) Words about the body or looks (e.g. "slim") may be treated playfully but never mock anyone's body (e.g. card 48: "How would you draw a slim person with only five lines?").**
215. **(approved by the owner 28 Sept 2026) New split (revises 211): about 20 % definition questions, about 20 % statements, about 30 % "picture" questions and about 30 % "you" questions, mixed over levels A and B and parts of speech.**
216. **(approved by the owner 28 Sept 2026) A statement is not a question: a short, slightly controversial claim about what the picture or video shows that makes the learner agree or disagree in the comment (model: "That customer would trade even his girlfriend for a Czech beer." / sk "Ten zákazník by vymenil aj svoju frajerku za české pivo."). The learner is not in it (no "you", "your", "would you"; sk no "ty", "tvoj", "by si"). It contains the key word (inflected is fine, never a phrasal verb, idiom or related word in its place), is grammatically perfect, clear, level-appropriate (level A soft target usually at most 10 English words, as 212) and funny, and ends with a full stop. Playfully provocative, never hurtful: no politics, religion, sex, violence, mocking bodies, or offensive stereotypes about nations, genders or origins. Every other language is a faithful translation (201/209). Both verifiers check statements like questions.**
217. **(approved by the owner 28 Sept 2026) Definition questions rotate three forms, roughly evenly (refines 208); the key word stays in its dictionary form in quotation marks: How would you define "<key word>"? / sk Ako by si definoval „<sk>“?; What does "<key word>" mean? / sk Čo znamená „<sk>“?; What is "<key word>"? / sk Čo je „<sk>“? — the last only for nouns; verbs, adjectives, adverbs and phrases use one of the first two ("What does "to care" mean?", "How would you define "hazardous"?").**
218. **(approved by the owner 28 Sept 2026) "What is …?" for a noun naming a person: English keeps "What is "a coach"?" (it asks for the meaning; "Who is the coach?" would ask for one person's identity). The native version uses the language's natural question word for a person, as a native speaker asks for the meaning of such a word: sk "Kto je „tréner“?", cz "Kdo je „trenér“?", and the equivalent in de ("Wer ist …?" only if natural for a definition, otherwise "Was ist ein …?"), es, fr, ua, hu and tr. The grammar verifier checks this.**

## Bus 4881 brief (28 Sept 2026)

219. **Media 4881 ("bus") uses a thumbnail and a tile preview taken from the moment the bus is visible (the hard cut to the bus at 1.625 s; the clip opens on a car): Thumbnails/bus_4881_b.webp and Previews/bus_4881_b.mp4 (5 s from 1.625 s). media_url, the full video, is unchanged. A preview that does not start at 0 s records its start in media.preview_start_s so the card continues the full video at the right place (branch preview-start-offset, with its migration, in the next deploy).**

## Comment statements brief (28 Sept 2026)

220. **Comment cards have two kinds, question and statement (comment_questions.kind, default 'question'). For a statement the learner agrees or disagrees and gives a view in a sentence (a reason is welcome, not required; a bare "Yes." / "I agree." is not a sentence). The check-comment function and the card texts (instruction pill, wrong-meaning note, neutral fallback, in all 9 app languages) handle both.**

## Tinder phrase follow-up brief (28 Sept 2026)

221. **Person nouns in sk, cz, ua, de, es and fr take the gender of the person shown in the media in Tinder phrases and sentences (e.g. sk „študentka", de „die Studentin", es „la modelo"); the dictionary form elsewhere is unchanged; en unchanged.**
222. **French uncountable (mass) nouns take the definite article (le/la/l') in display forms and phrases, never un/une ("l'oxygène", "l'argent", "l'huile d'olive"); decision 165's un/une-for-elision applies to countable nouns only.**
223. **Hungarian verb key words stay in the Hungarian dictionary form (3rd person singular, e.g. "hámoz"), which is how Hungarian dictionaries list verbs.**
224. **A phrase must read naturally; when the dictionary form of the key word makes a caption stiff, the rest of the phrase is rephrased (the key word stays in its dictionary form).**

## Sound / lowercase brief (28 Sept 2026)

225. **Tinder video cards play with sound from the start, the same way Repeat and Answer cards do (no extra tap, no sound button). The silent preview may bridge the load; the full video takes over with sound.**
226. **Short phrases (Tinder true/false phrases and similar short answers) are displayed exactly as stored, with no automatic capital letter; full sentences keep their stored capital.**

## Comment rewrite (all media) brief (28 Sept 2026)

227. **Slovak comma before „alebo“ (Czech „nebo“): a comma when the two clauses exclude each other (choose one: „Urobil by si fotku, alebo by si si len užil výhľad?“); no comma when they join freely (either or both). Grammar verifiers of sk and cz apply this rule everywhere.**

## Image batch 27.9 brief (29 Sept 2026)

228. **Image batch 27.9.2026 is imported like batch 26.9 (no grammar exercises; one type-74/75 level exercise per media), from workbook `And_Again_image_targets_v6_new_only.xlsx` (the only workbook whose target ids and keywords match the files: 313/313; v2 and v3 match 0), with the display-form (165, 179, 222), Tinder-phrase (195, 221-224) and comment (202-218, 227) rules; the 74/75 answers mirror the Tinder phrases. Images whose picture does not show the word (two independent looks) are not imported.**

## Comment rewrite follow-up brief (29 Sept 2026)

229. **The 70-character limit on comment items (comment_questions) stays; approved texts that are longer (the sample-4 texts) are shortened to at most 70 characters, keeping the approved meaning, type and tone.**
230. **The sk key words of concepts 4029 „elementárny“, 4862 „navštevovanie“ and 4866 „čakajúci“ stay as written by the comment rewrite (owner's decision; the verifier's objection is noted and closed).**

## Key flags apply brief (29 Sept 2026)

231. **Split rule (standing): when the media of one concept show different senses that some language translates with different words, the concept is split instead of replacing the key. The existing concept keeps one sense; a new concept (same English word and part of speech, its own definition) takes the other, with all 9 word_localizations and display forms, and each media moves to the concept of the sense it shows. Example: concept 1563 "messy" stays "dirty and not in any order" (sk „neporiadny", media 4991); a new "messy" = untidy hair, not combed (sk „strapatý", de „zerzaust", media 2477).**
232. **The 282 real-error and the 33 unclear key-flag cards (KEY_FLAGS_REVIEW) are approved through the split rule (231): every card first passes a two-verifier split check; where the media show another sense (for unclear cards: another sense than the definition), the concept is split, otherwise the proposed key is applied. Card #291 (cz thick, concept 2822): "thick" = wide stays; a new "thick" = growing close together, dense (sk/cz „hustý", de „dicht") takes media 4383.**
233. **Cards #119 (es solo), #127 (es wearing), #153 (fr pouring), #161 (fr spilling): the concepts stay nouns (decision 194); the key is a noun that names the activity in that language, with a display form, not a verb or phrase.**

## Key flags follow-up brief (29 Sept 2026)

234. **Concepts left without media after a split (the 14 "—" rows of KEY_FLAGS_APPLIED: to dive 871, anybody 997, club 2312, same 2705, thick 2822, bounce 2971, burst 2982, platform 3375, rod 3439, sickness 3490, transfer 3606, introduction 4280, come up 5052, tie 5708) stay in the database; the app hides them because they have no media, and they go on the image-target list for new pictures (`And_Again_image_targets_split_senses.xlsx`).**
235. **A key on a tile is always a full word, never a prefix (e.g. de „Haupt-“ is not a key).**

## Grammar 100 % brief: listening questions and line translations (29 Sept 2026)

236. **Every learner-facing text we write is grammatically perfect in every language: complete model sentences and questions (listening questions and their answers, translations of video lines and questions, and every other written text). Transcripts of what people SAY in a video (media.transcript) are never corrected; they must match the audio.**

## Pill and stack brief (29 Sept 2026)

237. **The answer pill (AnswerPill on comment, listening, speaking-repeat cards) is wide enough for its placeholder and text in every app language and screen size; it never shows scroll arrows or a resize handle.**
238. **The card behind the dragged card never changes: it already has exactly the size, position and corner radius it will have as the front card; nothing is scaled, re-rounded or animated on it during a drag, fly-out or snap-back.**

## Eleven words fix brief (29 Sept 2026)

239. **window 2154 (media 1548, building windows; definition vehicle window): split rule (231). A new concept "window" = an opening with glass in the wall of a building takes media 1548; the other 2 media of 2154 were checked (5498 building windows moves too, 4231 truck window stays).**
240. **minaret 592 (media 2614, minaret not clearly visible, religious topic): the concept stays; its comment item becomes a neutral definition question (What is "a minaret"?) in 9 languages.**
241. **closing 3895 (media 5748, hands pushing a door shut) stays a noun (decision 194); its definition becomes the activity "the act of shutting something, e.g. a door", sk „zatváranie“ and the other 8 keys name that activity.**
242. **coming 3905 (media 5761): the concept stays; its comment item becomes a definition question (What does "coming" mean?).**
243. **cross 3951 (adjective "lying sideways", media 5811, a tree lying across a road): the media move to "across" (from one side to the other).**
244. **upside 4844 "the top surface" (media 6755, a man wiping a car roof): the media move to "a roof".**
245. **loading 5356 "the weight a vehicle has to carry" (media 7300, a truck with a huge load of hay): the media move to "a load".**
246. **modeling 5418 (media 7366, a sculptor's studio): the definition becomes the activity "shaping figures from clay by hand"; the keys stay activity nouns (decision 194).**
247. **pussy 5525 (media 7478, a cat): the media move to "a kitty" (sk „mačička“).**
248. **trump 5726 "a brass instrument" (media 7689, a man playing a trumpet): the media move to "a trumpet".**
249. **upper 5734 "the higher of two stacked beds" (media 7698, a cat on a top bunk): the media move to "a bunk bed".**
250. **Tinder sentences (tinder_sentences.true_sentence / false_sentence, all 9 languages) are complete sentences: subject (or the language's dropped subject) + finite verb; imperatives fine; a short interjection next to a complete sentence ("Wow!", "¡Uf!") is fine; a text made only of verbless fragments ("Cheap tent, big storm.", "Such a brave dog!") is rewritten. Grammar 100 %, true stays true, false stays clearly false on the same fact in every language. Brief of 29 Sept 2026, report GRAMMAR_TINDER_SENTENCES_REPORT.md.**

## G4 brief (30 Sept 2026)

251. **The gerund keys of decision 194 go live without the stale parts: 3838 bringing de „das Bringen“, sk „prinášanie“, cz „přinášení“; 4041 entering sk „vchádzanie“, cz „vcházení“, ua „входження“; 4703 en display „solo“. Their Tinder phrases, sentences (verb forms bringt / prináša / přináší / vchádza / vchází) and mirrored 74/75 answers follow the new keys. 5418 modeling needs nothing more (live through the eleven-words fix). Report G4_REPORT.md.**

## G6 brief (30 Sept 2026)

252. **Exclamative sentences are complete sentences and are allowed in Tinder sentences: "What a view!", "Such a brave dog!", "How cute!" and their natural equivalents in each language. Verbless captions that are not exclamatives ("Cheap tent, big storm.") stay rewritten. Refines decision 250. Report G6_REPORT.md.**
253. **The true Tinder sentence always contains the key word of the media's own concept in that language (inflected or conjugated forms count). Report G6_REPORT.md.**

## G8 brief (30 Sept 2026)

254. **The 183 KEYDOUBT rows of G6 are resolved by concept, not by sentence: a stored key that is wrong for its concept is fixed for every media of that concept (72 key changes); a media that shows another sense is split off by the split rule (decision 231; 24 new concepts 6075–6098); a key that fits keeps its place and the true sentence is written with it. Tinder phrases, 74/75 answers and comment items that quoted an old key follow the new key. Where the new key cannot carry the English false joke, the false phrase may swap a different, clearly false item. Report G8_REPORT.md.**

## G7 brief (30 Sept 2026)

255. **The old exercises (the 66 types other than 74/75) are no longer used anywhere: the two-player mode is removed, shared links open the new card of the same media (old `?sharedVideoId=<exercise id>` links resolve through `legacy_exercise_media`, new links are `?sharedMediaId=<media id>`), and share and report use media ids. The old exercise rows that nothing references are deleted (40,081 exercises, 360,729 localizations, backed up); the 4,824 still referenced by the translation pipeline, caches and repetitions are kept. Report G7_REPORT.md.**
256. **No encouraging texts anywhere in the app ("Blízko.", "Skoro tam.", "Close.", "Almost there." and every similar praise or encouragement line, in every language). Results are shown by colour and state only: green / red, the learner's answer and the corrected answer where one is shown. Supersedes 116. Report G7_REPORT.md.**

257. **The Training wall paints progressively: the first rows load first, each tile appears as soon as its own image is ready, and nothing else may delay the first tiles. Report G9_REPORT.md.**
258. **Images first: on the first screen every tile starts as an image (video tiles show their thumbnail); video previews start only after the whole first screen is painted. Report G9_REPORT.md.**
259. **Language choice for a new learner is two cards (Figma 1892:503 and 1892:605) instead of one; the wall's first images are prefetched while the learner chooses. Report G9_REPORT.md.**

## G10 brief (30 Sept 2026)

260. **The remaining 4,824 old exercises and their references (translation_selected_exercises, sentence_chunk_rejects, translation_check_cache, user_exercise_repetitions) are deleted, with backup; nothing but 74/75 remains. Supersedes the "kept" part of 255. Report G10_REPORT.md.**
261. **The automatic vocabulary lists get neutral names: "Learned" / "To practise" (sk „Naučené" / „Na precvičenie"), in all 9 app languages. Report G10_REPORT.md.**
262. **Training Settings has no "I focus on… (Vocabulary / Grammar)" option any more (an old stored value is ignored); the vocabulary library level filter shows A (A1+A2) and B (B1+B2) only. Report G10_REPORT.md.**
263. **Person nouns take the gender of the person shown also in Tinder SENTENCES (extends 221 for phrases): e.g. sk „poetka", „pokladníčka", cz „pokladní"; the feminine form counts as the key. Report G10_REPORT.md.**

## G11 brief (1 Oct 2026)

264. **The wall's data for a device without a copy comes from one database function, `wall_tiles(lang)` (read-only, security invoker, all levels; migration 20261001100000), with the parallel REST wave as a silent fallback (error, 2.5 s timeout or a missing function). Report G11_REPORT.md.**
265. **Dead legacy code is removed: the old exercise feed and everything only it used (choice / build / typed / translate cards, the timed Tinder round, translation_selected_exercises and user_exercise_repetitions clients). Database tables and edge functions stay. Report G11_REPORT.md.**
266. **No language choice before playing. A new learner (guest device, or a signed-in profile without languages) starts with learning language English, all levels ("?"), native language = the browser language; when the browser language is English or not one of the app's 9 languages: native English, learning Spanish. An existing choice is never overwritten. The G9 start cards are gone (supersedes 259). Report G11_REPORT.md.**
267. **Settings are ONE card (Figma 1892:503): learning language, level (A1 A2 B1 B2 and "?" = all levels: A and B words together on the wall and in sessions), native language, number of players (1-4), Save. Training Settings is removed. Report G11_REPORT.md.**
268. **The homepage shows the round flag of the learning language next to the heart (Figma 1105:584), in place of the settings icon; tapping it opens the settings card. Report G11_REPORT.md.**
269. **Several players (Figma 1903:1002): 2-4 people play on one device at the same time, each with their own pair of black answer buttons on the same card; only Tinder cards; no swipe, no rail, no left sidebar; nothing counts (no XP, leaderboard, profile progress, results summary, repetitions, recommender learning or account events). Setting players back to 1 or closing the session returns to normal play. Answer window (Figma 1920:1284): a video card until its video ends (it plays once, no loop, no replay), an image card 5 s; each player answers once and nothing is revealed during the window; at its end, silently, both buttons of every player who answered turn green (right) or red (wrong), a player who did not answer keeps the black buttons; the colours stay ~1.5 s, then the next card. Normal one-player play is unchanged. Report G11_REPORT.md.**

## G12 brief (1 Oct 2026)

270. **Starter wall: a learner with no history (no interest signal yet) sees the same curated wall of 60 tiles in every learning language (only the labels differ): photos, cartoons, anime / 3D and videos; animals, vehicles, objects, fantasy (the dragon 3772 is tile 1), people in suits, nature, sport, food, funny everyday moments; level A and B mixed; the "curious" cat in the box (media 209) is the first video, on the first screen on phone and desktop. Seen starter tiles go to the end on a return, the next unseen ones come first; with history the wall is ranked as before. The order is `scripts/wall-files/starter_order.json`. Report G12_REPORT.md.**
271. **The wall's data for a device without a copy comes from precomputed static files on the storage CDN (one starter file with the order and every tile row, one label file per learning language, a manifest with a 60 s cache; versioned names with a one-year cache), rebuilt by `node scripts/wall-files/build.mjs` after every content import; the REST wave is the fallback (error or 2.5 s). `wall_tiles(lang)` is dropped. Supersedes 264. Report G12_REPORT.md.**
272. **The G11 tap fix is live: with several players the card is live as soon as it is the active one (a tap in the snap moment counts). Report G12_REPORT.md.**
273. **The unused database objects of the removed formats are dropped with backup (7 tables, 5 functions, media_categories.level) and the edge function check-translation is undeployed (source in git history). Kept because still used: exercise_localizations intro_text / distractor_1 / distractor_2 / full_sentence (written by the content import) and the sentence-chunk objects (used by the deployed chunk-sentences function). Report G12_REPORT.md.**

## G13 brief (1 Oct 2026)

274. **Tiles the learner has already seen keep their place; tiles not seen yet are re-ranked continuously by the learner's latest behaviour (after every signal of the recommender: session close, likes, rejections, tile taps, answers). Only tiles never on screen AND more than about one screen below the viewport move; a tile never changes while it is about to appear or its image is being fetched. Supersedes the visit rules of 155 where they differ. Report G13_REPORT.md.**
275. **Back from a card or a session (X, browser back, gesture, closing the several-players mode): exactly the same screen and scroll position, the tapped tile in place. Report G13_REPORT.md.**
276. **Another browser tab or app and back: the same wall; after more than 6 hours away (measured from the last time the wall was visible): a new wall. Report G13_REPORT.md.**
277. **Settings: the same wall whether or not something changed; a learning-language change switches the labels; a level change moves only the not-yet-seen tiles. Heart and search: the same wall. Report G13_REPORT.md.**
278. **A new wall when the learner goes to another section (Profil, Rebríček, Pridať) and back, reloads, opens the app on another device, signs in or out, comes back after more than 6 hours, or opens a shared link. Rotation / resize: same tiles and order, reflowed, anchored on the top tile. New media appear only with a new wall. Report G13_REPORT.md.**
279. **Settings save automatically: no Save button; every choice is saved the moment it is tapped (device, and the profile when signed in; the last tap wins, a failed save retries quietly). Supersedes the Save button of 267. Report G13_REPORT.md.**
280. **Videos first: every wall (starter and ranked) aims at about 70 % video tiles while there are enough videos. Only videos on the edge slots (161) play automatically; videos on other positions show their thumbnail and play only when opened. The starter wall (270) is 42 videos + 18 images; the cat 209 is tile 1. Report G13_REPORT.md.**

## G14 brief (1 Oct 2026)

281. **Media 209 ("curious", the cat in the box) is at tile 4 of the starter wall, which is a playing edge slot on both layouts (phone 3 columns: slots 3, 4, 9, 10 …; desktop 4 columns: slots 4, 5, 12, 13 …), so it plays at once on phone and desktop. Report G14_REPORT.md.**
282. **The header row (search, heart, learning-language icon) hides while the learner scrolls down and shows again when the learner scrolls up, over the wall, without moving the grid. Report G14_REPORT.md.**

## G16 brief (1 Oct 2026)

283. **Touch scrolling starts anywhere on the wall, including on tiles; overscroll protection applies to the page as a whole, not to every element. Report G16_REPORT.md.**

## G17 brief (1 Oct 2026)

284. **The search field on the Training wall is solid white #FFFFFF (no transparency, no blend with the background). Report G17_REPORT.md.**
285. **Icons are never clipped: every icon shows its full shape on all sides. Report G17_REPORT.md.**

## G18 brief (1 Oct 2026)

286. **The Tinder card's two answer buttons swap sides as in Figma 1620:1305 and 1920:1284 (X left, check right; one player and every player's pair); nothing else changes. Report G18_REPORT.md.**

## G19 brief (1 Oct 2026)

287. **Browser tests make no sound: every browser a session starts is muted (`--mute-audio`) and is closed when its script ends, also on errors; in the owner's Chrome a tab used for checks is muted before it plays anything and closed afterwards; no video or audio keeps playing after a check; at the end of a session no test browser or tab is left open. Standing rule in and-again CLAUDE.md "Browser tests: no sound", guarded by `npm run check:browser-mute`. Report G19_REPORT.md.**

## G20 brief (2 Oct 2026)

288. **Videos made from an existing image replace that image in the same media row (same media id, concept, exercises and texts); the image files are deleted from storage after the video is verified; uploaded_at is set to the import date. Report G20_REPORT.md.**

## G21 brief (2 Oct 2026)

289. **When a video exists in a shortened or hand-edited version (also under a generic name such as 1002.mp4), that version is always used. Report G21_REPORT.md.**
290. **Videos without an image to replace are imported as new video media if two independent looks confirm they show the word. Report G21_REPORT.md.**

## G22 brief (3 Oct 2026)

291. **Videos only: the app shows only video media everywhere (wall, starter wall, search, every card kind, sessions, vocabulary lists and details, several-players mode, shared links). Image media stay in the database and come back by one switch (and-again `lib/mediaKinds.ts` `MEDIA_KINDS`). Words without a video are hidden until they get one. Only the edge-slot videos play automatically on the wall (decision 161, G13); the others show their thumbnail. Report G22_REPORT.md.**

## G23 brief (3 Oct 2026)

292. **A video the owner made for a word is never rejected by the verifiers: they may flag issues (AI artefacts, unclear meaning), but the video is imported. Where the meaning is not obvious from the picture, the texts (description, Tinder sentences, comment item) make the word's meaning clear. This replaces the "two confirming looks" condition of decision 290. Report G23_REPORT.md.**

## G24 brief (3 Oct 2026)

293. **There are three starter walls: level A, level B and all levels; a learner without history gets the one for the chosen level (and-again `scripts/wall-files/starter_order.json`: `A`, `B`, `media`). Media 209 is tile 4 in the A and the all-levels order. Report G24_REPORT.md.**
294. **"an idiot" may stay on the starter wall (owner).**
295. **The learner's own uploads (Add flow) are not affected by the videos-only switch; their photos keep showing.**

## G25 brief (3 Oct 2026)

296. **Behind and around an open card the app's grey background shows, never black (phone and desktop): the card screen, the safe areas at the top and bottom, the browser bars (theme-color) and the overscroll take the wall's background (and-again `MOBILE_GRID_BACKGROUND`). Media inside the card keep their own fit. Report G25_REPORT.md.**
297. **While the keyboard is open on a card, only that card is visible: the page and the feed do not scroll to the next card, the card keeps its size, and the answer pill sits just above the keyboard (and-again `lib/keyboardCardLock.ts`). Closing the keyboard restores the layout exactly.**

## G27 brief (3 Oct 2026)

298. **The text bubbles at the top of every card follow Figma 1620:1305 (padding, width, radius, font, line height, background, position): the bubble hugs its text, 20 / 10 padding with the 1 pt hairline inside, radius 45, 16 / 19 text, black 60 % with the Glass blur 4, top 76, centred; it may grow to the card minus 21 pt on each side, and a wrapped text keeps the 20 pt side padding (and-again `lib/topBubble.ts`, `components/feedChrome.ts`, `components/CardLineBubble.tsx`). Report G27_REPORT.md.**

## G28 brief (3 Oct 2026)

299. **Standing rule: desktop and phone never differ in settings like which card kinds or which texts a session shows; only the design differs.** (An earlier G28 draft, phones only Tinder, was stopped and discarded before anything was committed.)
300. **Sessions deal only Tinder cards, everywhere: the feed, vocabulary sessions, several players, tile taps (the tapped media opens as its Tinder card) and shared links. One switch brings the other kinds back: and-again `lib/cardKinds.ts` `CARD_KINDS = ['tinder']` (all kinds: `['tinder', 'comment', 'listening', 'speaking']`). Comment questions, listening questions and spoken lines stay in the database.**
301. **Tinder cards show only the short phrases (`true_phrase` / `false_phrase`), at most 30 characters in every language; the full sentences are not shown (they stay in the database). Switch: and-again `lib/tinderTexts.ts` `TINDER_TEXT = 'phrase'` (`'both'` = phrase or sentence as before). The 30-character limit replaces "other languages max ~40" of decision 195; where a key word is too long for a natural phrase of 30 characters, its shortest natural form stands in.**
302. **Every video has Tinder texts: a complete `tinder_sentences` row in all 9 languages. Report G28_REPORT.md.**

## G30 brief (3 Oct 2026)

303. **The answer sound plays on every answer.** Both sounds are loaded once when the app starts, the audio is unlocked on the first user gesture and kept unlocked, the sound starts in the same gesture as the answer (button press, end of the swipe) and the card change never cuts it. Only the learner's own mute (the M key) silences it (and-again `lib/answerSound.ts`, `lib/answerFeedback.ts`).
304. **After a button answer the result shows for about 600 ms (the pressed button green or red, the ✓ / ✗ mark, the sentence in the result colour), then the card scrolls up and the next one slides in from below, the same motion as a manual scroll.** A swipe answer keeps its own motion (the thrown card).
305. **Videos loop without a hitch; videos made from images start and loop at 0.2 s** in tiles, previews and cards (`media.start_s`; every later video from the same pipeline gets `start_s = 0.2`; and-again `lib/seamlessLoop.ts`, `lib/mediaStart.ts`).
306. **The Tinder game is left only with the X.** The swipe exit is removed, and the browser's own back navigation (the iOS edge swipe, the trackpad swipe, the back button) does not leave an open session (and-again `lib/sessionExit.ts`).
307. **Answered cards stay reachable by scrolling back: they show their result, their media plays, and they cannot be answered again; scrolling down returns to the current card.** The last 20 cards keep their media; older ones show their thumbnail and their result. Cards ahead are still loaded one at a time (decisions 181, 183).
308. **The move from one card to the next takes about 250 ms and is smooth: one slide with a scroll-snap-like easing, animated only with transform on the compositor, with the heavy work after it, and the next card's picture already painted before it starts. The same slide for a manual scroll, a button answer (decision 304) and the way back to answered cards (and-again `lib/feedSlide.ts`, `lib/feedSlideWeb.ts`).** A vertical drag on a Tinder card moves the feed (up = the next card, still a skip when the card was not answered; down = back); this replaces the fly-up of decision 98.
309. **Every instruction hint on a card (the swipe hint and every other instruction pill of a card kind) shows only the first time ever for that learner, then never again.** It is remembered on the device and, for a signed-in learner, in the profile (`profiles.hints_seen`), so another device does not show it again; a guest who signs in keeps the "already shown" state. The exercise icon still opens the hint. This replaces the once-per-session rule of the card fixes brief (PART 5) (and-again `lib/exerciseInstructions.ts`). Report G30_REPORT.md.

## A31 brief (3 Oct 2026)

310. **App briefs and reports use the prefix A (A31, A32, …); G is the prefix of the video-generation project.** App briefs up to G30 keep their names. Also in and-again `CLAUDE.md`.
311. **Videos are organised in 35 groups, each with at least 10 videos at level A and at level B; every video has one main group** (and-again `media_groups`, `media.group_id`). The groups come from the 40 categories; merged: Travel & Countries (Travel + Countries), Sport (Team Sports + Sport Gear), Family & People (Family + People), Health (Health Care + Feeling Sick), Beauty & Care (Hair & Care + Makeup & Skin). Each group has a name in the 9 languages and a representative video for a learner without history at level A, level B and all levels (media 209 represents Animals); each video has the list of key words of its group and level that may be shown as the wrong word on a one-word Tinder card (`tinder_word_distractors`). Report A31_REPORT.md.

## A33 brief (3 Oct 2026)

312. **The full file of a video keeps the quality of its original: the original's own H.264 stream is stored (copied, with faststart), and only an original in another codec is encoded (libx264 CRF 16).** The CRF 28 files of G20 / G21 / G23 had a quarter of the original's bitrate. The 985 videos made from images were replaced under new names (`Words/<title>_a33.mp4`); previews and thumbnails stay. Also in and-again `CLAUDE.md`.
313. **The answer sound never depends on an audio context that is not running:** such an answer plays through a pool of preloaded `<audio>` elements unlocked by a gesture, the context is resumed for the next answer, and a context that stays stuck or is closed is replaced inside a gesture. `?sounddebug=1` shows on the device what the sound did (and-again `lib/answerSound.ts`, `lib/answerFeedback.ts`).
314. **The 600 ms result of a button answer (decision 304) starts when the mark is on the screen, not at the tap; the mark is its own layer above the video.** A card paused by a tap shows the full file, not the 400 px preview; the play sign of a refused autoplay goes when the video plays, and any tap starts it. Report A33_REPORT.md.

## A34 brief (3 Oct 2026)

315. **For a hand-edited video, if the edit is only a cut (one or several parts of the original in time, joined with hard cuts), the same parts are taken from the true original at full quality; if the edit changed the picture (or has transitions, or frames that match no part of the original), the edited copy stays.** All 59 hand-edited videos were cuts (21 of them in two parts) and were rebuilt from their hf_ originals (`Words/<title>_a34.mp4`, H.264 High CRF 16, the original's size and 24 fps, audio from the same parts); previews, thumbnails and the 0.2 s start stay. Report A34_REPORT.md.

## A32 brief (3 Oct 2026)

316. **The Training wall shows one tile per group (its representative video) with the group's name in the learning language, where the key word used to be.** Representative: the curated one (A31) for a learner without history, else the best-ranked video of the group. The search still finds words and opens their video. Switch `GROUP_WALL` (and-again `lib/groupWall.ts`); the wall files carry the groups.
317. **Tapping a group tile starts a session with only that group's videos at the learner's level; the first card is exactly the video shown on the tile.** When every video of the group was shown, the next pass through the group starts.
318. **Tinder cards show only a word: the video's key word (correct) or another key word from the same group and level (wrong), from the A31 lists. Right = the word fits. Phrases are not used for now.** Switch `TINDER_TEXT` = 'keyword' | 'phrase' | 'both' (and-again `lib/tinderTexts.ts`); the same in vocabulary sessions and with several players.
319. **Thin lists: a video with fewer than 5 wrong words takes extra wrong words from the same group's other level** (`tinder_word_distractors.fallback_concept_ids`); a video without any wrong word gets only correct cards.
320. **Body parts: no body-part word is ever a wrong word on a video that shows a person (or an animal with that part), on every video. Videos of the Body Parts group take their wrong words from other groups** (words that clearly do not fit the clip). The list of body-part concepts and the rules: and-again-content `runs/a32_20261003/out/`.
321. **Tinder card look as Figma 1620:1305: a larger font for the word (48), always on one line (a long word shrinks just enough, never below 18, never wraps); no exercise-type icon in the top-left corner; the streak (flame and number) sits in the top-left corner and shows only from the 6th correct answer in a row on.** Report A32_REPORT.md.

## A35 brief (3 Oct 2026)

322. **When a group session has shown every video of its group at the learner's level, it continues with videos of the next groups, in the order of the wall (by the learner's interest); the wrong word of a card always comes from that card's own group list.** The session never restarts the first group while unseen videos exist elsewhere. This replaces the second sentence of decision 317. and-again `lib/groupWall.ts` (`groupStages`, `byGroupStage`). Report A35_REPORT.md.
323. **The owner will redesign the wrong-word lists later; no change to them now.**

## A36 brief (3 Oct 2026)

324. **The ⇄ translation starts OFF on every new card.** This replaces decision 149 ("the ⇄ translation stays on across cards", CARD_FIXES PART 4). and-again `lib/translationToggle.ts`.
325. **Group names are one word in every language; the wall repeats the groups after the last one, each repeat with a different representative video** (the group's next best-ranked video not yet on the wall; no video twice; a tap on a repeated tile starts that group with that tile's video). and-again `lib/groupWall.ts` (`groupRounds`); the names: `supabase/scripts/a36_names_4754_20261003/names_table.md`.
326. **The sound icon over a paused video switches the sound of the whole app off / on (card videos and answer sounds), remembered on the device.** and-again `lib/appSound.ts`.
327. **Media 4754 gets a key word its clip clearly shows: "a referee" (it was "protest"); it moves to Sport.** "protest" stays without media.
328. **An answered card shown again has no ✓ / ✗ mark, only the word in its result colour and the highlighted button.** This changes decision 307's "with its result" for the mark only.
329. **Nothing but the next card is ever visible behind a card while it moves.** On iOS a session has no history entry of its own, so Safari's back swipe has no picture of the wall to show (and-again `lib/sessionExit.ts`).
330. **Edge videos on the wall play reliably on iOS; if iOS refuses autoplay, they start on the next touch.** and-again `lib/wallAutoplay.ts`.
331. **Text inputs never make iOS zoom the page.** The font sizes stay; on iOS the viewport gets `maximum-scale=1` (and-again `lib/webViewport.ts`).
332. **On phones the card's video fills the screen down to the bottom edge (under the browser's bottom bar); the answer buttons, the right-hand rail and the X stay where they are, inside the safe area, above the browser's bars.** and-again `lib/fullHeightMedia.ts`. Report A36_REPORT.md.

## A37 brief (3 Oct 2026)

333. **About 100 groups instead of 35 (112), each with at least 6 videos at level A and at level B; one-word names in every language; every video has one main group.** The 35 groups of A31 stay as parents (`media_groups.parent_id`) and hold no video. and-again `supabase/scripts/a37_groups_20261003/` (names: `group_names.md`, counts and representatives: `group_list.md`); run folder `runs/a37_20261003`.
334. **Until the owner redesigns the wrong words: a card's wrong word comes from its own (new) group; if that gives fewer than 5 options, from the group it was split from (the A31 list), then from the other level (the A32 rule); the body-part rule stays.** `tinder_word_distractors.distractor_concept_ids` = the own group's words, `fallback_concept_ids` = the parent's rest (plus the other level's words only where both are below 5). This narrows decision 323.
335. **The search field has a clear button (×) at its end while it holds text: it clears the text, closes the keyboard and returns to the wall at the same place.** and-again `screens/GameSelectionScreen.tsx` (`search-clear`). Report A37_REPORT.md.

## A38 brief (4 Oct 2026)

336. **New Tinder card layout for every card (videos and images), Figma 1620:1305 as of 4 Oct 2026: the key word above the media, large, dark text on the grey app background; the media smaller, with slightly rounded corners (radius 35), not full height; no right-hand rail (no avatar, heart, share, flag); the ✗ / ⇄ / ✓ buttons below the media, ⇄ between ✗ and ✓, grey as in the frame; the close X inside the media at its top right; no streak shown.** and-again `lib/cardLayout.ts`, `components/TinderCard.tsx`, `components/RoundButton.tsx`.
337. **This replaces: full-height video on phones (decision 332, A36), the streak badge on the card (A32), the rail and its share button on the card. Sharing goes through the card's own URL (A37 PART 3). The streak logic and XP stay as they are, only not shown.**
338. **After an answer, the word above the media turns green (right) or red (wrong) and the pressed button is highlighted; then the card moves on as today (G30).** Several players: players 1 and 2 have their pairs below the media beside ⇄, players 3 and 4 on the media's lower edge (`multiPlaces`). Report A38_REPORT.md.

## A39 brief (4 Oct 2026)

339. **Lottie animations are imported as ordinary videos: each HTML file of `UGC Videos/HTML` is rendered to an MP4 (720x1280-class, 30 fps) and gets the full video pipeline; its key word is its file name.** The ten files of 4 Oct 2026 are SVG + CSS animations (no Lottie player inside); they are stepped frame by frame with the Web Animations API, one full loop (the common loop of all periods up to 30 s; cat 19.8 s and toad 13.0 s have no common loop and take the length with the smallest seam), H.264 High CRF 18, no audio track, `start_s` NULL, the word under the picture left out. `media.source = 'lottie'` (additive column). Run folder and-again-content `runs/a39_20261004`. Report A39_REPORT.md.
340. **The Lottie videos come first on the wall, for everyone (new and returning learners, every level): each group that contains one comes first with it as its tile; a group with several appears again right after with its next one (the A36 repeat rule); only when every Lottie video has had a tile do the other groups follow in their normal order (starter order or the learner's ranking). A tap starts that group with the Lottie video as card 1.** A level's wall shows the Lottie videos of that level (A: 7, B: 3, all levels: 10). One switch: and-again `lib/featured.ts` `FEATURED_SOURCE = 'lottie'` (`null` = off); `lib/groupWall.ts` `groupRounds`. Report A39_REPORT.md.

## A40 brief (4 Oct 2026)

341. **A hidden test page 4evr.app/lab tries a new three-step exercise on 10 videos (verbs while the video plays, nouns on the still picture, a sentence answering a question about it); it is not linked from the app and changes nothing else.** It opens with a wall of the 10 videos (one tile each, its key word in its display form, the Training wall's grid and video slots); a tap starts that video, then the others not done yet; the X returns to the lab wall; after the 10th an end screen with "again". The content is a JSON file in the app (and-again `lib/labExercises.json`, no database): 6 verb chips and 7 noun chips per video, the still frame time, and the video's own live comment question, which check-comment judges (kind question, the video's description as context). and-again `screens/LabScreen.tsx`, `components/LabMedia.tsx`, `lib/labExercise.ts`. Run folder and-again-content `runs/a40_20261004`. Report A40_REPORT.md.

## A41 brief (4 Oct 2026)

342. **In the lab's nouns step the learner places each correct noun onto its slot on the still picture (drag, or tap the word then the slot); only the correct nouns are offered.** The picture shows one translucent slot pill per noun, on or right next to its object; a noun on its own slot becomes a white pill with the word, on another slot or elsewhere it returns to its place with the wrong state shown briefly and does not count; when every noun sits in its slot the sentence step comes. 3-4 nouns per video, each with its slot (`x`, `y` as a share of the whole picture) in and-again `lib/labExercises.json`; rules `lib/labSlots.ts`, sizes `lib/labLayout.ts`. Also on the lab page: the app's sound switch stands on the playing media, the media reaches both side edges on phones, the chips and the arrow button are about 18 % larger. Report A41_REPORT.md.

## A42 brief (4 Oct 2026)

343. **The lab's nouns step keeps the title "Place the nouns." (owner).**
344. **On the lab page quick taps in a row are never lost on touch devices; the Tinder cards are not changed (the owner expects them to be replaced).** No double-tap wait anywhere on the page (`touch-action: manipulation` on the page), and a tap on a lab control (chips, slots, buttons, the sound switch, the lab wall's tiles) presses at the end of the touch instead of waiting for the browser's click, which iOS Safari drops for a second tap that comes right after the first. The dragged noun chips keep their own touch handling; the A36 no-zoom-at-focus rule stays. and-again `lib/labTap.ts`, `screens/LabScreen.tsx`, `components/LabMedia.tsx`. Report A42_REPORT.md.

## A43 brief (4 Oct 2026)

345. **A second hidden test page, 4evr.app/lab/catch, tests a catch game: cut-outs from a video's still frame fall from the top; a board at the bottom shows a label (who / what, where, when); the learner moves the board to catch the cut-out that fits; only correct catches count.** Time is shown by a clue taken from the picture itself (lit lamps = in the evening). 3 videos; per video three labels in English (display forms with article / preposition), each with its cut-out: who / what = the person or object without background (transparent picture, made with a free local tool), where = a rounded crop of the background without people, when = a crop of the time clue; nothing in a cut-out is invented. A label's decoys are the cut-outs of the same kind from the other two videos, never one that also fits. The page starts with a wall of the 3 videos; the video plays a few seconds, then its game: the correct picture and its decoys fall one after another with a slight tilt, at most 3 at once, a fall takes about 3-4 s; a caught decoy shakes red with the wrong sound and does not count; a missed correct picture falls again later; after the three labels the next video; end screen with the count of correct catches and "again"; X back to the wall. Content: and-again `lib/catchGame.json` (no database), pictures in storage under `Thumbnails/lab/catch/`; rules `lib/catchGame.ts`, sizes `lib/catchLayout.ts`, page `screens/CatchScreen.tsx`. Report A43_REPORT.md.
346. **The catch game's board is a tray (owner's addendum, replaces the board of the first mockup):** a wide white pill, 48 high, fully rounded, solid white, no stroke, no shadow, the label centred in the lab chips' font; under it a small grip bar (64 x 8, fully rounded, dark grey) that the learner drags (the tray may be dragged too), so the finger covers neither the label nor the falling picture; a catch zone right above the tray lights softly (a light tint of an existing colour, no glow) while a falling picture would land on the tray and goes dark when the picture is caught or misses; the background stays the app's light grey (#F5F5F5). The addendum's width, "about 85 % of the screen", is open: at that width the tray cannot step aside from a picture, so it was built at 50 % (one number, `CATCH_TRAY.widthShare`); the owner decides.
347. **The catch page (4evr.app/lab/catch, decisions 345-346) is removed.** Route, screen, game code, content file and tests are gone; the path shows the lab wall. Its 18 pictures in storage (`Thumbnails/lab/catch/*_a43.png|webp`) are read by nothing; the owner deletes them with `docs/features/reports/assets/a44/DELETE_catch_objects.sh` (a session does not delete stored files). Report A44_REPORT.md.
348. **The lab (4evr.app/lab, its 10 videos) has three exercises per video:** "Tap who does it." (a phrase - verb + object or detail, e.g. "to hold a rope" - stands under the playing video; the learner taps the person, animal or thing it is about in the video; each phrase has a tap region that follows its target: boxes as shares of the picture at keyframes every 0.5 s, interpolated; a tap inside the region at that moment is correct, elsewhere wrong and does not count; 3 phrases), "Place the nouns." (as decision 342) and "Answer the question." (a question about what the clip shows; the model answer's words are chips: a tap moves a chip into the answer box in order, a tap in the box sends it back, all chips in the model order = correct; or the learner writes or says an own sentence, which check-comment judges against this question; chips and typing are one text). check-comment takes an optional question (and kind) from the caller and then judges against it instead of the stored comment question; the app's cards send none and are unchanged.
349. **The lab's exercise sets are a vertical feed:** scrolling down goes to the first exercise of the next video, scrolling up returns to the previous video's set exactly where it was left (step, placed nouns, taps done, chips in the box, typed text); a swipe to the left (or the X) returns to the lab wall at its scroll position; the wall opens the tapped video's set first, then the others in the wall's order. The media carry the rail buttons: heart (the video's key word into the vocabulary, as in the app), translate (the native text of the current phrase / nouns / question, in the 9 app languages), share (the lab link of this video, /lab/v/<media id>), flag (the app's report for this media).
350. **All lab texts are grammatically perfect model English; a lab question is answerable from the clip** (no invented details such as durations), its tense matches what the clip shows (ongoing = present continuous), and its model answer uses words of the video's phrases or nouns. Phrases, regions, questions and answers: writer + verifier (the verifier looks at every frame with the boxes drawn); native texts: writer + grammar verifier.
351. **Layout of the lab exercises (owner's addendum, his mockups of 4 Oct 2026):** the exercise title is small (16 px, medium) and left-aligned above the media ("Tap who does it.", "Place the nouns."); the media takes the room freed by the smaller title (edge to edge on phones, taller); the third exercise has no title: the small picture with the question beside it, "For example:", the chips, the answer box ("Tell your own sentence." with the mic) and the arrow button; the phrase chip and the noun chips stay centred under the media, the rail buttons on the media's right edge.

## A46 brief (4 Oct 2026)

352. **The three exercises are the main game: tapping a group tile on the Training wall opens the exercise feed of that group's videos (the tapped video first); the Tinder cards are switched off (the switch is kept).** The feed is the lab's (decisions 348-349, 351): tap who does it, place the nouns, the question; scroll down = the next video, scroll up = back, swipe left or the X = the wall; the rail buttons. After the group's videos the other groups follow in the wall's order (A35). Vocabulary sessions (the videos of the vocabulary's words first) and shared links (their video first) open the same feed. One result per finished set (the verdict of its third exercise), scored and stored like a card's answer. One switch: and-again `lib/mainGame.ts` `MAIN_GAME` (`'exercises'` / `'cards'`); `CARD_KINDS` and `TINDER_TEXT` stay. The cards still play for several players and for a learning language other than English. Report A46_REPORT.md.
353. **Only videos with exercise content appear in the feed (the content fills up over time).** Content = the table `media_exercise_sets` (A45), live rows; while the table cannot be read or is empty, the lab's 10 sets (and-again `lib/labExercises.json`). A tile whose video has no content opens the group's videos that have it, a group without any the next groups.
354. **The device's volume buttons control the app's sound (videos and feedback sounds).** Every sound is media: the page's audio session is `playback` from the app's start, videos and recorded voices are media elements, the answer sounds Web Audio on the same session; the app sets no volume of its own, the in-app switch only mutes. and-again `lib/mediaChannel.ts`.
355. **A finished exercise set starts again from the beginning when the learner scrolls back to it; an unfinished one is restored where it was left.** Finished = its third exercise was judged.
356. **Every correctly tapped phrase, correctly placed noun and correctly built answer plays its recorded voice.** One voice at a time (a new one stops the previous), none while the app's sound is off, the recordings of the set on screen and of the next one are loaded ahead. and-again `lib/voice.ts`.
357. **The three lab exercises ("Tap who does it.", "Place the nouns.", the question with its model answer) are the main exercises of every video.** Content per media in the table `media_exercise_sets` (A45): 3 phrases with targets and a tap region every 0.5 s, 3-4 nouns with slots on a still picture, one question with its model answer as chips, the native texts in the 8 other app languages. Videos with one or two targets are allowed; phrases may share a target. Run folder and-again-content `runs/a45_20261004`.
358. **Exercise texts follow the video's level.** A level-B video uses B-level words in every exercise (phrases, nouns, question, model answer); a level-A video uses simple A-level words.
359. **Every phrase, noun and model answer has a recorded voice.** Female for female persons and "She" sentences, male for male persons and "He" sentences; everything else takes the video's default voice (the main person's gender, else female for an even media id, male for an odd one). macOS voices, AAC .m4a 64 kbit/s mono, bucket `audio` under `sets/<media id>/`; Samantha and Daniel until Premium / Enhanced voices are installed.

## A48 brief (5 Oct 2026)

360. **Each lab video has five exercises:** (1) "Tap who does it.", (2) "Place the nouns.", (3) "Choose matching caption." (a two-way carousel of image variants), (4) the question with its model answer (no title), (5) "Fill in what you remember." (recall). Exercises 1-4 come in a random order per video (a new order at every visit); exercise 5 is always last. A video whose carousel has no pictures yet skips exercise 3 (and its carousel rows in exercise 5). and-again `lib/labExercise.ts` `labStepOrder`
361. **Typography of the lab exercises:** exercise titles and descriptions 12 px; text in bubbles, chips and buttons 20 px; image positions as in the owner's frames of 5 Oct 2026 (Figma 2029:1014, 2030:1237, 2034:1280, 2025:576/860, 2044:1622). and-again `lib/labLayout.ts` `LAB48_*`
362. **Carousel captions:** vertical = noun collocations for a noun key word ("blind date", "double date"), or three verb forms in different tenses for a verb key word; horizontal = verb collocations ("to plan a date"). Captions are the shortest possible phrases: infinitive phrases for collocations; for tenses a finite verb phrase without subject ("ran from a dragon", "is leading a horse", "was led by a knight").
363. **Tenses (vertical, verb key words), exactly 3 forms per verb, varied between words:** level A from present simple (with -s for one person: "always runs"), present continuous, past simple, future (will); level B mostly harder forms: present perfect ("has just run"), past continuous only for an action in progress at a moment (never with a total duration), passive, past perfect continuous, future continuous. Past preferred over future; future rarely and only when clearly drawable.
364. **Time travel in tense pictures:** past = the same person, same pose, same camera, centuries ago; future = the same, about 1000 years ahead; only clothes, surroundings and people around change, always from the key word's own world (horse -> knight and castle / robot horse on Mars). Clarity of the word and the tense always wins over keeping the pose.
365. **Every carousel variant is made by EDITING the video's still frame** (keep faces, pose, composition, camera angle), never a new image from scratch.
366. **Children and babies MAY appear in carousel images** (owner's correction to A48, 5 Oct 2026; replaces the brief's "no children or teenagers" for this work): only in normal, safe, everyday situations (no danger, no distress beyond an ordinary crying baby, nothing suggestive). "to calm" may use a baby ("is calming a baby", "was calmed by a nanny", "to calm a baby").

## A49 brief (5 Oct 2026)

367. **Video 7071 teaches "king", not "duke"** (he wears a closed crown and ermine; he reads as a king). Its concept link is concept 2542 "king"; concept 5144 "duke" and every other row stay (only unlinked). Its exercise set, Tinder sentences, comment questions, exercise texts, carousel captions and recordings say "king"; its title is `king_7071` (the storage file names keep "duke"). Run and-again-content `runs/a49_20261005`.
368. **Lab exercise titles follow the Figma frames:** 14 px; the recall title 32 px, centred. The recall title text stays "Fill in what you remember." (the frame's "Fill all you remember." is not grammatical). and-again `lib/labLayout.ts` `LAB48_TITLE`, `LAB48_RECALL_TITLE`.
369. **Carousel pictures are made efficiently, with no more credits than A48's 100:** every A48 failure reason is a rule written into every edit prompt up front (remove every logo, badge, emblem and sticker of the source; no faces resembling real people; keep framing and camera; explicit eyelines; correct hands; no text), a free verifier checks each prompt with the still before any credit is spent, at most 2 paid attempts per picture (else the variant is dropped; 3 pictures per word is fine), a word starts only when the credits left cover all its edits once plus one spare.
370. **Carousel picture QC (replaces the strict A48 QC and the QC part of decision 369):** ALLOWED and never a reason to regenerate: a face resembling a real person, logos / emblems / stickers carried over from the source video, framing differences, imperfect eyelines (edit prompts still ask for clear eyelines). Only avoid deliberately depicting a recognisable celebrity or deliberately adding a large famous brand logo. HARD fails only (regenerate, at most 2 paid attempts per picture): text / letters / digits in the image, the word or tense not readable at first glance, broken anatomy or physics, violence or gross details. The blind verifier runs 3 times per picture; a picture passes when the right caption wins at least 2 of 3; a single miss never causes a remake - the picture is marked UNSURE for the owner. Reuse before paying: every earlier paid generation (also rejected ones) is checked first. Every word gets a contact sheet of the kept pictures with captions and UNSURE marks for the owner's approval. Rules stored in and-again `CLAUDE.md` ("Carousel pictures").

## A45 resumed (5 Oct 2026)

371. **`media_exercise_sets` stores every video's picture shape in two columns, `width` and `height` (the video's pixel size; aspect = width / height; NULL = unknown, assume 9:16).** Migration 20261005100000 (applied and recorded 5 Oct 2026); filled for every row (the lab 10 from ffprobe, the rest from the frame extraction). The app (A46 open point 11) maps tap regions and noun slots with this aspect instead of 9:16. and-again `supabase/migrations/20261005100000_a45_exercise_set_shape.sql`
372. **The A45 owner script retries network errors before it gives up a batch:** missing audio files are uploaded again (up to 5 rounds, pauses of 30, 60, 90 ... s), SQL files are sent again up to 3 times, every database read 3 times; a batch is still written only when every one of its audio objects reads back. `runs/a45_20261004/apply_a45.sh`

## A51 brief (5 Oct 2026)

373. **A lab carousel has exactly 3 pictures = 3 answers (replaces the cross of decisions 360 and 362).** The video's original still is NOT shown; every picture is still an EDIT of the still (same person, scene, camera; decision 365). The three pictures stand in one row, walked by swiping sideways; under the media the three captions are the chips. and-again `lib/labCarousel.ts`.
374. **Tenses in a carousel: per word at most ONE future, ONE present and ONE past form (replaces "exactly 3 forms" of decision 363).** The forms must stay distinct in German, Spanish and French. Far-future and centuries-ago variants stay allowed (decision 364). Infinitive collocations ("to lead a horse") are not tense forms.
375. **Carousel collocations are common phrases only, no idioms yet; each caption's key word translates to the same word as the video's key word** (captions are later simply translated: the native caption must contain the native word the video teaches, e.g. German "Weg" for "way", so "way out" = "Ausgang" is out).
376. **Lead (432) keeps "will be leading robots on Mars" as it is** (braid outside the helmet accepted).
377. **Higgsfield budget for A51: 22 credits (krasty1333; the owner adds 20 to the 2 left).** The real balance is read before every job and is never exceeded.
378. **A51 is lab only; the main game is not changed.**
379. **Celebrities and brand logos (owner's addition to A51, confirms decision 370):** never deliberately depict a recognisable celebrity or add a large famous brand logo; accidental resemblance and logos carried over from the video stay allowed.
380. **The contact sheet per word shows every kept picture with its caption, its tense / collocation type and any UNSURE mark**, so the owner approves a word in one look.


## A50 brief (5 Oct 2026)

381. **Tinder is removed completely: code, the switch, components, routes, styles, edge functions only it uses, and its data in the database.** Done as the whole old card game (Tinder, listening, speaking and comment cards; `screens/GameplayScreen`, `MAIN_GAME`), the edge function `check-listen-speak`, the music files `audio/tinder/*` and the tables `tinder_sentences`, `tinder_word_distractors`, `media_line_translations`, `listening_questions` (migration 20261005210000, applied and recorded). Kept because features that stay use them: `comment_questions` / `comment_answers` (check-comment, used by the feed), `user_word_answers` (the "Not yet" / "Got this" vocabularies). Backup + tested restore: `backups/a50_tinder/`. and-again `docs/features/reports/A50_REPORT.md`.
382. **Every path that showed Tinder opens the exercise feed (A46).** A mode that cannot use the feed is not redesigned: its entry point is disabled and reported as an open point - several players are off (`lib/settingsCard.ts` `SEVERAL_PLAYERS_ON = false`, the settings card hides the row).
383. **Videos without a `media_exercise_sets` row are hidden everywhere (wall, groups, vocabulary lists, feed), dynamically:** a row written later shows at the next app start with no extra step; a group with no visible video at the learner's level has no tile. and-again `lib/mainGame.ts` `withExercises`, `lib/mediaKindStore.ts`.
384. **English is the only learning language for now** (German / Spanish / French exercises come in a later brief); native-language translations stay. The other learning languages are hidden in the settings card and Profile Settings, an account or device learning one of them uses English, and one switch brings a language back: and-again `lib/learnLanguages.ts` `LEARN_LANGUAGES_ON = ['en']`.

## A53 brief (5 Oct 2026)

These apply to every exercise type (tap, place the nouns, carousel, question + model answer, recall) in the main game feed AND /lab, on phones and desktop alike (only the look differs, never the behaviour). and-again `lib/labLayout.ts` `exerciseLayout`, `lib/exerciseScreen.ts`, `components/ExerciseFeed.tsx`; report `docs/features/reports/A53_REPORT.md`.

385. **The picture/video window is taller: it uses the free height so the clip is less cropped (closer to its 9:16 frame), and the answers/chips sit BELOW it.** It is never higher than the clip needs at that width (phones) and never wider than the clip at that height (desktop / tablet column, centred).
386. **Nothing overlaps anything:** answers never cover the picture, never sit under the browser's toolbars (Safari's bottom bar, Chrome's bars, the iOS home indicator), never under the rail buttons (heart / ⇄ / share / flag) or the close button.
387. **A safe zone of at least 20 px between any two elements** (title, picture, rail buttons, chips, slots, fields, the arrow, the browser's UI = the visible top and bottom edge plus the safe-area insets); chips in a row are 20 px apart too. The full-width picture may touch the side edges; a recall sentence (its words and its gap) is one element.
388. **Noun slots and other markers on the picture never overlap:** each slot stays at its noun's place but is nudged apart, at least 20 px between slots and 20 px from the rail (`lib/labSlots.ts` `nudgeSlots`); the carousel's dots stand 20 px inside the picture's edge.
389. **Exercise titles are 20 px (as the chip text; replaces the 14 px of decision 368). The recall title stays 32 px, centred.**
390. **The layout fills the real visible screen:** the visual viewport (dynamic viewport) and the safe-area insets; with a phone's keyboard open (recall, own sentence) the step stands in the visible part above the keyboard - the field being typed in stays visible and nothing overlaps (the question's hint chips and the recall title wait until the keyboard closes).

## A56 brief (5 Oct 2026)

391. **A carousel caption's key word is the database word the app teaches (the concept's `word_localizations.translation`)**, e.g. 8039 = the passage sense (Durchgang / paso / passage), 8055 = the hot-air balloon (Heißluftballon / montgolfière). A51's choices stay (confirms A51 open point 2 and decision 375). and-again `CLAUDE.md` ("Carousel pictures"), run folder `runs/a51_20261005/pics/RULES.md`.
392. **When the natural translation of a caption does not contain the translated key word, the natural translation wins** (e.g. Turkish "to lead a horse" = "bir atı yularından çekmek", "weight bench"): the natural caption is kept and marked in the report; the English caption is not replaced. Exception to decision 375 for these cases only.
393. **Higgsfield budget for A56: at most 40 credits spent (krasty1333, balance about 9,002, nothing topped up).** The run tracks its own spending from the balance at its start, never waits for the balance to change and stops before exceeding 40. A56 is lab only; the main game is not changed.

## A55 brief (5-6 Oct 2026)

394. **German, Spanish from Spain (es-ES) and French from France (fr-FR) are made at once.** Lab pilot first (the 10 lab videos), then a stop for the owner's review; the other 3,034 videos only after approval. and-again `docs/features/reports/A55_REPORT.md`, run folder `runs/a55_20261005`.
395. **The exercises are written natively per language, not word for word:** model grammar, natural for a native speaker, everything answerable from the clip, tense matching the clip, nothing invented; level A videos with A-level words of that language, level B with B-level words. Writer -> independent native verifier who sees the frames with the boxes and pills drawn -> fix -> help translations with a grammar verifier per native language -> audio -> validation -> guarded write.
396. **Per exercise:** tap phrases written natively, tap regions reused unchanged; nouns with their definite article (der/die/das, el/la/los/las, le/la/l'/les), still nouns, plural where the clip shows several, at the English slots; question + model answer written natively, chips = the answer's words shuffled; recall rows built like the English ones (same sources and order, one gap, one-letter typos accepted); carousel captions translated naturally with the same tense type as English (at most one future, one present, one past), common phrases, key word = the database word, the natural translation wins and is listed in the report.
397. **Every video gets its key word per language** (`word_localizations` of its concept; nouns with the article). One-to-two or two-to-one mappings between English and a language are not restructured: listed as open points with a proposal.
398. **Help translations (tr) of each learning language into the app's native languages** sk, cz, en, de, es, fr, hu, tr, ua minus the learning language itself.
399. **Voices (each item keeps the English female / male choice):** German Anna (Premium, de_DE) / Yannick (Enhanced, de_DE); Spanish Mónica (Enhanced, es_ES) / Jorge (Enhanced, es_ES); French Aude (Enhanced, fr_BE; texts stay France French) / Thomas (Enhanced, fr_FR). Recorded by voice identifier (`com.apple.voice.premium.de-DE.Anna` ...), so the compact voice of the same name is never used.
400. **Storage: one row per (media, learning language) in the new table `media_exercise_sets_l10n`** (migration 20261006100000); the English table `media_exercise_sets` is not touched and English works exactly as before. Regions, slots, still moment, shape and carousel pictures are copied unchanged from the English set into the row.
401. **Learning languages stay switched off in the main app** (`lib/learnLanguages.ts`, decision 384) until the owner approves a language after the full run; only `/lab` gets a learning-language switch (EN / DE / ES / FR, `?learn=de` in a link).

## A58 brief (6 Oct 2026)

407. **Scope of the new five-exercise design: `/lab` only, the 7 noun videos** (8055 balloon, 236 dolphin, 7071 king, 8056 bench, 461 mannequin, 62 bag, 8039 way), English only; the verb videos 624, 4265, 432 are hidden in the lab (data kept). The main game stays as it is, except the drag-layer fix (decision 412). No new pictures (no Higgsfield credits). Design source: Figma 4evr-2.0, dark 2098-9, 2057-1816, 2055-1745, 2088-104, 2055-1653, white 2109-168, 2109-185, 2109-142, 2109-213, 2109-277; where they differ from A53's layout rules the frames win (in the dark theme the Tap phrase pill and the nouns' bank sit ON the picture); 20 px between interactive elements and the browser UI.
408. **Fixed order of five exercises:** 1 "Tap who does it." (one phrase at a time in a pill, the learner taps who / what does it; only with at least 2 actors AND no scene cut, detected automatically and confirmed by a verifier; an actor may be a thing when it makes sense; B may use the passive), 2 "Place the nouns." (exactly the nouns of the three phrases, slots on those things), 3 "Choose the caption." (the existing carousel pictures and captions, swiped; only the tapped correct button lights green), 4 "Fill the empty spaces." (mind map: key word in the centre, the carousel collocations with the key word's partner empty; the three phrases with gaps - verb part or noun; the bank holds only the correct pieces; tap only), 5 "Make a story." (three short funny sentences using the phrases and collocations, shuffled as a) b) c), tapped into the right order, or the learner's own story judged by check-comment). The question + model answer exercise is removed from the lab.
409. **Content per noun video** rewritten at the video's level, grammar 100 %, everything visible in the clip: three phrases tied to the key word's situation, each with one placeable noun; "laugh at jokes" (never "about"); objects where the verb needs one ("impress her with his self-confidence"); idioms only at level B; humour and puns welcome. Help translations into the 8 app languages with a native grammar verifier each; voices Ava / Zoe (Premium) and Evan / Nathan (Enhanced), each video keeping its female / male choice; an independent verifier with the frames (boxes and pills drawn) before anything is written. Stored as lab-only data (`lib/lab58.json`); `media_exercise_sets` and the main game untouched.
410. **The theme is decided by the picture's edges:** content reaching the edges (photos, videos) = dark theme; plain white / light edges with the content in the centre (SVG-style illustrations) = white theme. The lab wall shows each video's theme.
411. **Navigation inside a video's exercises:** swipe left = the next exercise (skipping allowed), swipe right = one step back; on the carousel picture a horizontal swipe flips the pictures, outside it it navigates. Vertical scroll = the next / previous video. The wall only via the X.
412. **Drag-layer fix everywhere (main game and lab):** a chip being dragged is always on the top layer, above slots and pictures; after the drop it sits on its slot.

## A57 brief (6 Oct 2026)

402. **The full run is approved: all remaining 3,034 videos × German, Spanish (Spain), French (France) go into `media_exercise_sets_l10n`** with exactly the A55 pipeline, voices and rules (decisions 394-401). Batches of 100 videos per language, resumable, guarded writes with backups; a video that still fails after one rewrite and a second verification is skipped and listed. Run folder `runs/a57_20261006`, report and-again `docs/features/reports/A57_REPORT.md`.
403. **8039 "way": the concept's German word becomes "der Weg" and its Spanish word "el camino"** (`word_localizations` of concept 6040; French stays "le passage"). The 8039 German and Spanish rows (captions included) are rewritten so the key word is used consistently, and their voices re-recorded. Applied 6 Oct 2026 (`runs/a57_20261006/out/wl_8039.sql`, backup `backup/wl_6040_before.json`, rollback `out/wl_8039_rollback.sql`).
404. **A German compound counts as containing the key word** (die Sporttasche, die Hantelbank, die Strandtasche).
405. **4265's carousel pictures stay as they are** (the parrot does the calming).
406. **German, Spanish and French stay switched off in the main app** (`lib/learnLanguages.ts`) until the owner approves turning each on.

## A59 brief (6 Oct 2026)

413. **Key-word phrase first, always (lab):** the first phrase of exercise 1 always contains the key word as its placeable noun ("to have a date", "to sit on a bench") and has a clear doer visible in the clip; when two people do it together, tapping either is correct (a second region, `alsoKeys`). The same phrase then comes back in exercise 2 (its noun = noun 1), exercise 4 (row 1) and the story. This holds also when exercise 1 is not shown (one actor or a scene cut).
414. **Step numbers run 1, 2, 3 … over the exercises a video actually shows** (as A58 does): kept.
415. **Verbs (rule for later, not built yet):** exercise 4 uses a TIMELINE instead of the mind map: past → present → future, the three carousel captions with the verb form left empty (the bank holds the forms); below it the three exercise-1 phrases as rows, as for nouns; the bank holds only correct pieces.
416. **Verb carousel (rule for later):** exactly three tenses - one past (centuries ago), one present, one future (about 1,000 years ahead); every picture is an edit of the still (same people, same camera).
417. **8039 help captions:** the German and Spanish help captions of `lib/labExtras.json` switch to Weg / camino (decision 403), checked by a native verifier each.
418. **"to select" (owner correction, 6 Oct 2026): not done on purpose** - no lab item, no picture search, no carousel pictures, 0 Higgsfield credits. Decisions 415-416 stay written for a later verb pilot.

## A61 brief (7 Oct 2026)

419. **Any video with a cut (a hard scene change inside the clip) is excluded from ALL exercises everywhere** (main game: wall, groups, feed, vocabulary lists, search, shared links; a group with no visible video at the learner's level is hidden until it has one). Nothing is deleted, only hidden (`media.has_cut` + `media.cut_times`); the owner remakes these videos later (list `A61_CUT_VIDEOS.csv`). Translations into `media_exercise_sets_l10n` (a resumed A57) skip them too.

## A60 brief (7 Oct 2026)

420. **Exercise 3 captions are FULL SENTENCES for every part of speech; exercise 4 uses only the short part** (noun: the partner word, e.g. "blind"; adjective: the noun; verb: the verb form on the timeline exactly as in its sentence, e.g. "are selecting").
421. **Carousel pictures (all parts of speech): each is an edit of the still that changes only a bit** - keep something of the original (the room, or the people, or the object) and stay in the same world (doughnut -> cake -> pastry, never cars). The setting may change just for fun (a future city ~1000 years ahead, the Middle Ages, animals instead of people, suddenly drawn / animated) - whatever grabs attention. Lively, funny, young people; the picture rules of CLAUDE.md stay.
422. **Verbs (also phrasal verbs and verb phrases such as "get dressed", "break apart"):** the carousel = one past, one present, one future sentence; the subjects vary (He / you / I); the past picture shows the moment one step AFTER (already done), the present picture the action itself, the future picture the moment BEFORE. Exercise 4 = the timeline (past left, "now" mark, future right, present under "now").
423. **Adjectives:** level A and gradable = comparison (brave -> braver -> the bravest), exercise 4 = a weak-to-strong scale. Otherwise (level B, or not gradable) = the adjective in front of a DIFFERENT noun visible in each picture (classical piano / classical architecture / classical music), exercise 4 = the mind map with the adjective in the centre and the nouns empty.
424. **Adverbs:** like adjectives but combined with VERBS: level A and gradable = comparison (fast -> faster -> the fastest); otherwise the adverb with a different verb each time. Adverbial phrases (in advance, next door, in no time) follow the adverb model. Rule only - no adverb pilot.
425. **Story (exercise 5, rule 6):** always exactly 3 sentences (ordering 2 is too easy); level A about 20 words, level B 20-25; short sentences; connectors between sentences (so, but, then, meanwhile, luckily ...); a funny point at the end; not every phrase must appear.
426. **Credits: at most 24 Higgsfield credits in A60** (krasty1333, Nano Banana Pro edit of the still); QC exactly as CLAUDE.md "Carousel pictures"; stop and report when the cap is reached.
427. **A video with a cut is excluded from ALL exercises, not only from exercise 1** (with decision 419). In the lab 461 mannequin (cut at 4.3 s) is removed completely: the lab has 6 nouns + the two pilots; its data files are kept, it is only hidden.
428. **The story order must be unambiguous (rule 6):** sentence 1 introduces the character by name; sentence 2 starts with a linking word that needs something before it (So, Meanwhile, But ...); sentence 3 clearly ends it (In the end, Finally ...) or refers back ("his friend"). A verifier tests all 6 orders; if more than one makes sense the story is rewritten; only if that truly fails does the app accept every valid order (`storyOrders`). The "to select" story: "Max was trying to select the perfect doughnut." / "So the girl held the tongs and waited." / "In the end, his friend reached over the glass!". The check applies to "classical" and the lab nouns too.
429. **Model split for every brief (7 Oct 2026, during A60):** Sonnet 5.5 subagents for the simpler work - help translations into the 8 app languages and their grammar checks, recordings, uploads and read-back checks, automatic scene-cut detection passes, screenshots, Figma comparisons, play-through tests, file moves and count checks. Opus stays for writing and independently verifying the English learning content (phrases, captions, stories), learning-language content (DE / ES / FR when A57 resumes), carousel picture prompts and picture QC, app code and design, and confirming doubtful cuts. Applies from A60 on.

## A62 brief (7 Oct 2026)

430. **Exercise 4 is "Use the words from the box." (Figma 4evr-2.0 2133:1393), tapping AND dragging:** order top to bottom = mind map / timeline, divider, the label "Words in the box:" and the box in the middle, divider, the phrase rows. Tap: the learner always taps a chip of the box first; it is held (same size, blue Roboto Medium text, no grey); a tap on an empty space then moves it there - right = it stays, shown as a normal white chip; wrong = it goes back to the box; the held chip tapped again = cancel; another chip = the hold moves; an empty space tapped with nothing held = nothing. Drag: a chip dragged from the box onto a space follows the same rule, always on the top layer.
431. **Exercise 5's story chips work the same way:** tap a chip (held look), then its place in the answer field (a tap on a chip in the field puts the held chip in front of it, a tap elsewhere in the field puts it at the end); dragging into the field, reordering inside it by dragging, and taking a placed chip back (tap, or drag out) all work. A full field in a wrong order flashes red and the chips stay for reordering.
432. **Exercise 1 audio:** the top phrase's voice plays 1 s after the picture (or the video's first frame) is there and the set is on screen; after a correct tap the next phrase's voice plays at once - after the voice that sounds, never over it (one waiting place: a phrase already solved before its voice could start is skipped). Nothing plays while the app's sound is off (the phrase text stays the fallback).
433. **Exercise 3 captions: SHORT wherever possible** (nouns and adjectives: "blind date", "classical piano", "weight bench"); a full sentence ONLY for verbs, where the caption shows a tense ("He selected more doughnuts."). Replaces decision 420 for nouns / adjectives. "classical" = classical piano · classical architecture · classical music (same pictures, voices re-recorded); the 6 lab nouns keep their short captions.
434. **Exercise 3:** a caption chosen right for its picture stays green and disabled for the rest of the exercise.
435. **Stories - connectors vary:** no fixed opener / closer, no repeated connector pair across neighbouring videos. Level A pool: so, but, then, suddenly, luckily, finally, after that; level B also meanwhile, unfortunately, as a result, however, eventually, surprisingly, in the end. A check flags a connector used in more than 30 % of the stories (`lab58Problems` / `connectorProblems`). The order must stay unambiguous (the order verifier stays).
436. **Level B stories:** one of the three sentences may be a longer sentence split into TWO chips (the second gives a reason or an explanation: because..., so..., which..., although...); the first chip starts with a capital letter, the second ends with the full stop; total 20-25 words. "to select": "Max couldn't select the perfect doughnut" · "because they all looked amazing." · "So the girl waited with the tongs." · "Then his friend reached over the glass!"
437. **Group starters:** every curated group representative and starter-wall video with a cut is re-picked among the group's videos without a cut (best fit for group and level, same quality bar); groups are not otherwise hidden or changed.

## A64 brief (7 Oct 2026)

438. **Exercise 2 "Place the nouns" - protected zones:** no drop target (slot) and no bubble may stand in the bottom chip tray (its full height), the right rail column (heart, ⇄, share, flag) or the title bar, each grown by 16 px. The layout moves a slot out of every zone to the free place nearest its object (`lib/labSlots` `nounZones`, `clearZones`); a data check (`zoneProblems`, at 390 x 844 and 375 x 667) flags an object that itself lies inside a zone - then the point moves to a visible part of the same object outside the zones, or a different noun of the picture is chosen.
439. **Exercise 4 "Use the words from the box" - the mind map holds every phrase with the key word** (nouns and adjectives; verbs keep the timeline unchanged): the carousel's collocations ("blind" date) AND the picture's key-word phrases, including verb collocations ("to have" -> date, "to sit on" -> bench; a verb chip keeps its "to"). The "to ..." rows below the box hold ONLY phrases WITHOUT the key word, from the picture. 3-4 bubbles; fewer key-word collocations = fewer bubbles and more rows. The mind-map slots are order-free (any mind-map chip in any mind-map slot).
440. **Exercise 4 ambiguity check before publishing:** no box chip may fit both a mind-map slot and a row, and no chip may fit two different rows; an ambiguous chip is replaced (e.g. "share": "to share a bench" is also a key-word phrase). An independent verifier tests every chip.
441. **Exercise 5 "Make a story" - stories rewritten:** first one good, meaningful story about the picture close to the word maximum (level A at most 20 words, level B at most 25); the number of sentences is free; the story is split into exactly 3 parts that clearly follow each other (a part = a sentence, several sentences or part of one; each part keeps its capitals and punctuation from its place in the story). No forced connectors ("But", "Then", "Finally" only where they really connect the content). The 6-order verifier stays: exactly one order of the 3 parts makes sense. Changed parts are re-recorded with the item's voice. Replaces decisions 425, 428 (sentence and connector parts), 435 and 436.
442. **Exercise 4 left alignment:** the label "Words in the box:", the TEXT of the first chip in every box row and the "to" of the rows start on one vertical line; the light-blue box background (its padding) extends to the left of that line. Same on every lab item and screen size.
443. **Model use for every run (7 Oct 2026, during A64), always the 5.5 generation:** the main session stays on Opus 5.5 for content, design, code, verification and DB writes. Sonnet 5.5 subagents for audio re-recording, translations, screenshots and lab play-through tests; Haiku 5.5 for purely mechanical steps with a clear expected output (moving / renaming / uploading files, running existing scripts and reading back their output, counting, file / hash comparisons, code search, report formatting). Haiku 5.5 never judges content quality, never writes exercise content and never writes to the DB; a failed or odd Haiku step is redone with Sonnet 5.5 or Opus 5.5. Never older model versions. Replaces decision 429 and every earlier model rule.

## A65 brief (8 Oct 2026)

444. **Lab exercise 3 "Choose and write the caption.":** the carousel keeps 3 pictures; pictures 1 and 2 keep their tap captions, picture 3 has NO caption - the learner writes (or speaks) a caption. Every picture stores a short scene description and 2-3 model captions; the checker uses them as text (no image per check). Accepted: describes the picture, uses the key word correctly (verbs: the tense the picture implies), grammatical.
445. **Lab exercise 4 "Write in the empty spaces.":** the word box is gone; the learner types (or speaks) every empty space of the mind map and the "to ..." rows. Level A only: a hint button reveals more letters of the word in place with each tap, never the whole word; level B has no hint. Accepted: every expected answer and any other natural collocation that fits the picture (AI checker); the mind-map slots stay order-free.
446. **Lab exercise 5 "Make a story.":** a) and c) are shown in place; the learner writes (or speaks) b) so the story makes sense; the ordering task is dropped. b) at most 10 words (level A) / 15 (level B); any grammatical b) that logically connects a) and c) is accepted; 2 model answers for b) are stored; stories rewritten where a) and c) did not leave a clear gap.
447. **Speaking:** every writing field has a microphone using the browser's built-in speech recognition (en-US; webkitSpeechRecognition on iOS Safari); the recognised text lands in the field, can be edited and is checked like typed text. No speech recognition in the browser = no microphone.
448. **AI checking with the app's Gemini integration (key server-side):** one check per submitted answer (input: exercise type, key word, level, scene / story parts, model answers, the answer; output JSON verdict correct | correct_with_typo | wrong, corrected text, one-sentence reason). Typos forgiven (corrected spelling shown), strict on the key word's meaning and grammar, any natural answer accepted. Wrong: the corrected version and the reason in the help language (lab default Slovak); one retry, then the model answer. At most 200 checks per user per day; on a Gemini failure or timeout the answer is compared with the model answers locally (exact / near match accepted). Every call is logged with tokens in / out.
449. **Lab "Match the words." round:** after every 3 new words, one round of 4 words <-> 4 pictures (the representative still of each item), all from words already seen; tap a word, then a picture, or drag; no distractors; swipe and X as in the other exercises.
450. **Naturalness check for all lab content, now and in every future content run:** after writing, a separate Opus 5.5 subagent that did not write it checks every phrase and sentence ("Would a native speaker say exactly this?"); unnatural items are rewritten and checked again ("got her a drink", not "went to bring her a drink"). No literal picture jokes for fixed expressions (no blind people for "blind date"). Abstract nouns in exercise 2 only when they belong to one clear visible place of the picture. All existing lab content (8 items, 5 exercises) re-checked and fixed in A65.


## A66 brief (8 Oct 2026)

451. **Lab exercise 5 "Make a story." on two pages** (replaces decision 446): ‹ › buttons and two dots under the content; both pages freely reachable, no locking. **Page 1 = order the story** (the A64 ordering of the story's 3 parts as a/b/c chips into the white field, tap and drag; the 6-order verifier stays: exactly one order makes sense). **Page 2 = write your own story:** the item's picture (rounded) top left, a list of 4 phrases from the item's exercises top right with a white circle each (options of one phrase grouped with "or"), a grey 5th row of connector suggestions (never ticked); below one large writing field with the placeholder "Firstly,…" and a large microphone in its centre (browser speech recognition, typing works too, the mic hides when unsupported). A used phrase gets a green tick while the learner writes or speaks; the match is forgiving (inflected forms, any option of a grouped phrase). **Length (owner change during A66): no minimum; at most 60 words at both levels;** a small word counter; the arrow works from 1 to 60 words. The arrow sends the story to the Gemini checker (check-lab-answer, mode "story"): grammar and naturalness only, using the phrases is NOT required; it returns the corrected story with the changed words marked and at most 2 short reasons in the help language; the learner may edit and resend once, then continues. Phrase lists by an Opus writer + a separate Opus naturalness reviewer.
452. **Lab speed:** measure first (Chrome mobile emulation, Fast 4G + 4x CPU, cold and warm), fix the biggest causes, measure again. Every tap shows a visible reaction under 100 ms (a pressed state at once, the work after). Ideas: preload the next exercise's pictures and audio, the poster at once, fitting image sizes, code splitting, cache headers, preconnect to storage, no whole-feed re-render on a tap, heavy work off the tap handler.
453. **Lab audio: every phrase plays to its end** unless the learner leaves the exercise; audio decoded / preloaded before it is needed; a test plays every lab recording and compares the played length with the file length (all must play fully).
454. **Small fixes:** 7071 says "quad bike" everywhere instead of "ATV" (texts, recordings, translations); typo feedback names both the wrong and the right spelling ("bga → bag").

## A67 brief (8 Oct 2026)

455. **Lab wall tiles:** only the word ("a balloon"), no "· dark / · white"; the label is readable on every tile - black text with a soft white shadow on light pictures (the set's edge theme "white"), white text with a soft dark shadow on dark ones.
456. **Lab exercise 3 "Choose and write the caption." (replaces 444's fixed third picture):** no green frame anywhere, ever - a correct caption shows only the green circle with the tick on its picture. Swiping between the pictures is smooth (no flash: the pressed state never darkens the swiped picture). A smaller picture with more room below (Figma 2127:1274). 3 pictures: 2 prepared captions + 1 "write" chip; the picture without a prepared caption is fixed per item but mixed across items (first / second / third). The write chip shows the first 5 letters of that picture's model caption + "...". A tap on it hides the other chips and the rail and shows the field with grey ↺ (clear), grey ? (the model caption of the picture on screen) and blue → (send); a long text makes the field grow and the buttons move below it, centred. The caption belongs to the picture on screen; a full sentence or a short phrase in the learner's own words that fits that picture is accepted (the key word is not required), typos forgiven. Right = a green chip with ✕ (cut with "..."); wrong = a white "Feedback:" card over the picture (1-2 short sentences in the help language), the text stays for editing, retries unlimited. ✕ deletes the own caption so it can be rewritten; the exercise is complete only when every picture has exactly one caption.
457. **Lab exercise 4 "Fill white boxes.":** key word bubble blue, colours and the lighter grey buttons per Figma (2168:224 ...). A "Tips" toggle top right with "Tips" under it, off by default, the last choice remembered (device; account when logged in) and used next time; it slides, the word box slides in / out without the rest jumping. Tips on: a box of chips including distractors and near alternatives; tap a chip (held = blue), then a white box; a placed chip leaves the box; tapping a placed chip sends it back. Tips off: the learner types into the white boxes (keyboard dictation, no extra mic). A new row = the model caption of the picture the learner captioned in exercise 3 with one blank (key word or another part, mixed across items). Bottom: grey ↺ (clear everything) and blue → = check ALL boxes at once (exact answers locally, the rest in one checker call); the same result with Tips on and off: right = green box; right with a typo = green box with the typed text, the right spelling above it; wrong = white box, the typed text struck through in grey, the right answer in green next to it. After the check → continues.
458. **Lab exercise 5 "Make a story.":** both pages in the Figma design (page 1 ordering, page 2 own story) with the small microphone at the left of the field and the placeholder "Firstly, she wanted...". The connector row (the last row of the phrase list) changes per item (e.g. "however, although, unfortunately...", "first, then, finally..."); repeats across items are fine, but varied; a suggestion only, never required.
459. **"quad bike" in the main game (7071):** backup of the live media_exercise_sets row, one guarded UPDATE "ATV" -> "quad bike" in the English texts (article "a quad bike") with the A66 recordings, media_exercise_sets_l10n de / es / fr checked and fixed; Turkish keeps "ATV". Read-back: 0 "ATV" in en / de / es / fr.
460. **Lighter pictures for 900001 / 900002:** webp q72 at 1080 px width, uploaded as NEW files (nothing overwritten), the lab file points at them.
461. **Checker tense rule:** when the learner mixes tenses, the correction keeps the tense used by most of the learner's verbs (test: "Sam pack ... lay ... can not" -> a past-tense correction).

## A68 brief (8 Oct 2026)

462. **One branch line:** the lab branches a66 + a67 are merged into master and pushed (and-again-content A64-A67 commits pushed too); every brief from now on works on master (or a branch merged back into master at its end), and every live bundle is built from master.
463. **The lab is set in Roboto** (the font of the Figma file 4evr-2.0: Regular + Medium, Bold for the few bold labels), loaded as a web font and preloaded so text does not jump while loading; nothing may overflow after the switch. Example: "The bear drives a car." fits on one row beside its buttons in exercise 3, as in Figma.
464. **Exercise 3 carousel dots:** white on dark / normal pictures, black on pictures with a white borderless background (the existing white theme).
465. **Exercise 5 page dots (between ‹ and ›):** the Figma colours stay (white on the light grey page); the empty (inactive) dot gets a thicker inner stroke so it is clearly visible (Figma 2150:30).
466. **Exercise 5 swipe by where the finger starts** (replaces the brief's first part 3): the UPPER zone (page 1: the a) b) c) slots; page 2: the picture + phrase list) - a horizontal swipe switches between the two pages with a smooth slide and never changes the exercise. The LOWER zone (the ‹ dots › row, the white field / chip box, the blue arrow) - a horizontal swipe changes the exercise as everywhere in the lab (left = next exercise, right = exercise 4). A drag that starts on a story chip always moves the chip, in either zone; typing / scrolling in the writing field never switches anything; ‹ › keep switching the pages.

## A69 brief (8 Oct 2026; owner's iPhone test)

467. **Lab sounds never overlap:** the answer sound (right / wrong) and the voices are one queue - the answer sound plays to its end, then a short pause (~250 ms), then the next voice; an answer sound waits only for the voice that sounds now and goes before the voices that wait.
468. **Lab sounds levelled:** voices and answer sounds at one loudness measured in LUFS, the answer sounds slightly quieter than the voices (voices -19 LUFS, answer sounds -22 LUFS while they sound; the main game keeps its own sounds).
469. **Lab wall:** a black label (white-theme tile) has no grey background / halo behind the word; white labels on dark pictures keep their shadow.
470. **Exercise 3 captions with the article English needs** ("a beach bag", "a gym bag", "the way out"; genre / uncountable uses like "classical music" stay without one), re-checked on all 8 items by the naturalness reviewer; the write chip's starter counts 5 letters including the article, spaces not counted ("a gym b...").
471. **Exercise 4, Tips on:** chips move both ways - drag a chip from the box to a white box, or tap a chip then a white box; a placed chip can be dragged to another white box or back into the box. Gestures by where the finger starts: inside the word box a gesture only moves chips (no scroll, no exercise change); in the mind-map area above and the rows + buttons area below the lab's feed gestures work (vertical = video, horizontal = exercise); a drag that starts on a placed chip always moves that chip.
472. **Exercise 4, Tips on: no distractors** (replaces 457's distractors / A67's 3): the box holds exactly as many chips as there are white boxes.
473. **No duplicate answers in one exercise 4:** the own row from exercise 3 never repeats a phrase already in the mind map or a row (map "gym" + row "gym [bag]" is not allowed) - another blank or another part of the caption is chosen; checked by lab58Problems.
474. **Exercise 4 check with Tips on is local (no AI):** right chips turn green, wrong chips are struck through in grey, no right answer is revealed; the learner moves chips and presses → again. Tips off keeps 457's check (one AI call, the right answer in green).
475. **The Tips control = the owner's Figma toggle** (2168:267 on / 2168:332 off; owner's correction during A69, replaces the brief's round icon button): a white pill with a round knob - on = knob left, pale blue (the Tips box blue) with the lit lightbulb; off = knob right, grey with the lightbulb with an X; no text; the Figma SVGs used unchanged; the knob slides and the icon cross-fades; accessible label "Tips on" / "Tips off"; remembered as before, default off. Its place and size as in Figma 2168:332 (left of the X, in the title row); the exercise number and the title 8 px apart in every exercise (Figma 2168:332).
476. **iPhone keyboard:** opening / closing the keyboard never moves the bottom buttons over the content; when it opens, the active white box / field is moved into view; when it closes, the screen returns exactly to its normal layout (visualViewport handling; tested with an emulated iOS keyboard in exercises 3, 4 and 5).

## A69b brief (8 Oct 2026; follow-up to A69)

477. **The Tips toggle follows the owner's updated Figma** (2168:267 on / 2168:158 off; replaces 475's icons): on = knob left, pale blue (the Tips box blue) with the lightbulb in BLACK, re-exported from Figma and used unchanged; off = knob right, grey, white text "no tips" on two lines (Roboto 12, line height 0.9), no icon. Sizes, font and colours from Figma; the knob slides, the content cross-fades; label "Tips on" / "Tips off"; remembered as before; default off.
478. **The main game's answer sounds are the lab's levelled files** (right / wrong at -22 LUFS while they sound; were -8.8 / -25.2). The lab's sound queue is not used there: the main game's voices are one-at-a-time `<audio>` elements that cut each other (lib/voicePlayer) and the answer sounds play on Web Audio, so the queue does not apply cleanly. Its voices already measure -19 LUFS (sample of 40: median -19.0, range -20.2 ... -18.8); no re-encode.
479. **Lab exercise 1: the phrase voice plays only when the learner taps the black phrase bubble** (replaces A62 decision 3: no voice 1 s after the picture, none after a right tap); a tap while that voice sounds starts nothing; the answer sounds stay. The main game's exercise 1 and the other lab exercises are unchanged.

## A71 brief (9 Oct 2026; lab)

480. **Lab exercise 1: the right / wrong colour appears on finger DOWN** (target < 100 ms, Chrome mobile emulation 4x CPU; measured 122-125 ms before -> 25 ms after); the colour never waits for audio. The answer counts (sound, next phrase) when the touch ends as a tap; a touch that turns into a swipe or a long hold drops the colour and answers nothing.
481. **Shorter, softer answer sounds:** the lab's right / wrong sounds are new 0.30 s generated tones (own work, CC0), levelled to -22 LUFS while they sound; the pause after an answer sound before the next voice is 150 ms (was 250). The main game plays the same levelled files.
482. **Content must match the video - every item, permanently:** no text may claim anything the video / picture does not clearly show (example: 8039 "to give a thumbs-up through the window" - the man never gives a thumbs-up). Every content run ends with a separate Opus 5.5 verifier (not the writer) that checks every exercise text against the whole video frame by frame (dense sampling): exercise 1 phrases + doers, 2 nouns + points, 3 captions + scene descriptions, 4 map / rows / own row, 5 story + phrase list; every mismatch is fixed (text, voice, translations, model answers) and verified again.
483. **Strict A / B levels from the owner's Excel (And_Again_coverage_v3.xlsx), permanently:** item level = the Excel level of the item's sense (Register linked level_ab, else the Target cefr: A1-A2 = A, B1-B2 = B). Level A: every word of every exercise at most A2 (key word excepted), short simple sentences, present simple / continuous, past simple, going to, can. Level B: the practised vocabulary (ex 1 phrases, ex 2 nouns, ex 3 captions, ex 4 chips, ex 5 phrase list) B1 or higher, at most ONE A2 word per item, never an A1 word. An automatic check in lab58Problems reads the Excel's CEFR (word + sense where possible) and must report 0 violations. 7071 "king" (Target 382, A1) moved from level B to A.
484. **One caption per picture (exercises 3 + 4):** every carousel picture has exactly one caption and is used once; exercise 4's own row is exactly the model caption of the picture the learner wrote about in exercise 3 (e.g. "He selected [a lot of] doughnuts."), never a second description; nothing appears there that was not said in the exercises; the blank never repeats another box's answer. Where a verb's timeline / an adjective's map already holds all three captions, that node is the own row (no second row).
485. **Noun key word -> mind map (Figma 2168:389):** the map holds only words that stand in front of the key word (adjectives / nouns: "blind", "double", "dream" date) - never verbs, never mixed word classes; verb collocations with the key word go into the rows ("to [have] a date", the verb is the blank). The key word is NEVER a blank anywhere.
486. **Carousel pictures (future generation):** in POV-style pictures (a person showing something to the viewer, like the man holding the bags) the person may look into the camera.

## A72 brief (9 Oct 2026; follow-up to A71, owner approved A71 open points 1-4)

487. **8039 exercise 2 "a way":** an earlier still (0.4 s instead of 2.3 s) where the cleared path floor is clearly visible outside the protected zones; the point sits on the path floor between her legs; the other points (the shovel, the cottage) re-placed on that still; confirmed by the separate video verifier, checked at 390 x 844 and 375 x 667.
488. **A noun mind map may hold ONE bubble** when only one natural, visible word of the item's level fits in front of the key word (8039: "narrow" only, "cleared" dropped); the freed room goes to the rows only with a natural, visible phrase of the right level (8039: "to [dig] a way past the cottage"); lab58Problems allows 1-4 bubbles for a noun; the one bubble stands left of the key word on its line.
489. **The verb timeline layout of A71 is approved as it is:** the key word's forms on the line (blue, never a box), the three captions with their boxes as the first rows, then the phrase rows.
490. **The 8 missing lab words are rows of the owner's Excel** (Target, source "register extra", cefr = the A71 estimate, level_ab derived, ab_focus yes, status open): doughnut A2, display case B1, quad bike A2, tongs B2, pastry B1, moose B2, shovel B2, duet B2; backup And_Again_coverage_v3_backup_a72.xlsx next to the file; lib/labCefr.json rebuilt, lib/labCefrExtra.json empty, level check 0 violations.

## A73 brief (9 Oct 2026; lab)

491. **Exercise 3 checker accepts every caption that correctly describes something clearly visible in the picture, also a partial one** ("A king's wife" for the king-and-queen picture without the quad bike); wrong only = wrong / unrelated / ungrammatical. The fallback "Odpoveď sa teraz nedá overiť..." is answered by retries: one more model attempt when a call fails, is slow (5 s, story 7 s) or unreadable; one more client request when the first gets no answer; every check logs attempts, the client's retry and the device's local fallbacks.
492. **The ? button in exercise 3:** closes the keyboard and the field and returns to the carousel on the picture shown before; the model caption appears as a normal caption chip among the others, assigned to no picture; the learner assigns it like the other chips.
493. **Carousel pictures:** each of the three is derived from the item's ORIGINAL picture / video still and has its OWN different change; never the same added element in all three. All 8 items checked; 8055 (a basket added to all three) regenerated with Nano Banana Pro: a red balloon / to travel over the sea by balloon / a balloon at night (8 credits).
494. **No repeats between exercises 1 and 3:** apart from the key word, no verb, noun or phrase of exercise 1 appears again in exercise 3 (checked by lab58Problems; other exercises may repeat).
495. **Exercise 4 uses only words and phrases from exercises 1-3** of that item (mind map, rows, chips; checked by lab58Problems).
496. **Exercise 5 layout (Figma 2152:111 page 1, 2150:30 page 2):** the pages differ only in the upper part; the ‹ dots › row, the white box (same size and place; page 1 "Drag the parts here in order.", page 2 mic + story) and the blue arrow stay identical and do not move; only the upper part slides. Page 2's picture never touches the ‹ › buttons. In the upper part a vertical swipe never changes the video, only a horizontal swipe switches the pages; the lower part keeps the lab's gestures.
497. **Happier right sound:** a short bright celebratory chime (0.45 s, own work CC0) at -19 LUFS like the voices; the wrong sound stays soft and short (0.30 s, -22 LUFS); the main game uses the same files; the queue gap stays 150 ms.

## A74 brief (9 Oct 2026; lab)

498. **Exercise 4 (Figma 2168:224):** the arrow is grey and cannot be tapped until every white box is filled, then blue. The Tips chip box stands directly under the title row, above the exercise content, for EVERY word type and layout (noun mind map, verb timeline, adjective map; owner's addition during A74); a thin divider between the map and the rows.
499. **Right / wrong feedback (exercise 3 and exercise 5's ordering):** after a check every wrongly placed chip / part is red for 1 s, then white again; right ones turn green and stay green; nothing moves or advances by itself; after a wrong check the arrow is grey until the learner changes something.
500. **↺ in every exercise (1-5; Figma 2218:896):** a grey ↺ puts the exercise (in exercise 5 the page shown) back to its start - placed chips back, typed text cleared, colours reset. Exercises 3, 4 and 5: the 101 x 50 grey button left of the arrow; exercises 1 and 2 (no arrow there): a round grey ↺ on the picture.
501. **Exercise 5 page order:** page 1 = the own story, page 2 = ordering the parts (lower part identical, only the upper part slides). Exercise 5 opens on the page that completed more of the last 5 completed rounds; a tie or no history = the story page; stored like the Tips setting (device + account). After a completed page the next tap on the arrow goes to the next video; the other page is not required.
502. **Exercise 5 story page (Figma 2150:30):** a bigger picture that starts higher and is always taller than the phrase list; the list 26 px right of it, centred on its height; only the item's 3 exercise-1 phrases plus one grey connector line; the arrow grey while the box is empty, blue with text; the story is checked only on that tap; ‹ › never touch the picture.
503. **Exercise 5 ordering page (Figma 2123:981, 2218:896):** no automatic check; the arrow grey while the box is empty, blue with one part; all in order = only the bubbles turn green and the next tap goes to the next video; a wrong order follows 499.
504. **Sound candidates:** 5 right (C1-C5) and 5 wrong (W1-W5) sounds, own work CC0, on 4evr.app/lab/sounds and in Drive AndAgain_reports/A74_sounds/; the live sounds stay until the owner picks one of each.
505. **8056:** exercise 1 "to sit near the man" (the dog sits at the bench's far end, never next to the man), story part 2 "His dog sits near him.", exercise 4's own row "a dog [on] a park bench" (no chip gives a plausible but untrue sentence); new recordings and translations. 900001 "They're going to select a spectacular one." stays.


## A75 brief (9 Oct 2026; lab, owner's choice from A74)

506. **Answer sounds = C1 / W1 (replaces 497's files, chosen from 504):** right = C1 bell arpeggio (0.60 s, -19 LUFS), wrong = W1 soft falling minor third (0.34 s, -22 LUFS); the live files assets/sounds/lab-correct.mp3 / lab-wrong.mp3 are byte copies of the A74 candidates; the main game plays the same files; the queue stays sound -> 150 ms -> voice. 4evr.app/lab/sounds stays as it is.
507. **Exercise 5 opens on the page the learner completed LAST (replaces 501's majority rule):** the story page or the ordering page, whichever completed the last round; no history = the story page; same storage (device + account, account wins). When one visit completes both pages, the later one counts.
508. **No ↺ in exercises 1 and 2 (replaces 500 for them):** the round ↺ buttons are removed; exercises 3, 4 and 5 keep theirs.
