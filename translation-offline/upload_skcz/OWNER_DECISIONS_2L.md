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
116. **On a wrong answer only, a SHORT, gender-neutral encouragement is shown in about 3 of 10 cases,** chosen at random ("Blízko.", "Skoro tam.", "Ešte raz."). Never on a correct answer.
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

## Comment questions sample 3 brief (28 Sept 2026) — DRAFT rules for all future comment questions, pending the owner's approval of sample 3

202. **(draft) The word-limit rule (197) is withdrawn, and so is the shortened level-A form in 200. Rules 203-210 below replace 196-201 as the draft rules for all future comment questions, applied in this order of priority; a lower rule never excuses breaking a higher one.**
203. **(draft) Rule 1 — Grammar 100 %, en and sk (and every language): every question is a complete, standard model question a teacher would write on the board: a subject and a finite verb, the auxiliary in yes/no and wh-questions ("Do you want …?", "Would you take …?", "What would you …?"), no ellipsis, no fragments, no imperatives with a question mark; correct articles, tenses, word order and punctuation; Slovak with correct case, agreement, aspect and word order.**
204. **(draft) Rule 2 — Clarity: the learner understands at once what is asked and can answer from the picture or from their own opinion; no riddles, no "it"/"that" without a clear antecedent in the question or the picture.**
205. **(draft) Rule 3 — One question per media, by the word's level: a level-A word (type-74 level exercise) gets only a level-A question; a level-B word (type 75) gets only a level-B question.**
206. **(draft) Rule 4 — Level: A uses simple structures and everyday words (present simple/continuous, can, would like, would you …), as short as a complete question allows (a guide, not a limit: usually 5-9 words); B may use richer structures and opinion/"why" questions.**
207. **(draft) Rule 5 — The key word, exactly that word, in every question: never a phrasal verb, idiom or related word in its place ("to order" is not "to order around"); in a normal question it may be inflected or conjugated; in a definition question it stands in its dictionary form (display_form, as on the tiles).**
208. **(draft) Rule 6 — About one question in five is a definition question, exactly: How would you define "<key word in dictionary form>"? / sk: Ako by si definoval „<sk dictionary form>“?, spread over levels and parts of speech.**
209. **(draft) Rule 7 — The sk question (and every other language) is a faithful translation of the en question: same content, same people and things, key word translated, grammatically perfect and natural.**
210. **(draft) Rule 8 — Humour: the other questions are playful with a small twist, like the Tinder sentences, never mean, but only when rules 1-7 are fully met (model: "Would you trade your lunch for a Czech beer?"). Process: writer; a content verifier (rules 2-8) and a separate grammar verifier (rule 1 only, word by word, naming the exact error); a question passes only if both pass it; on failure the writer rewrites; after two failed rewrite rounds it is shown as failed with the reason.**

## Comment questions sample 4 brief (28 Sept 2026) — DRAFT, pending the owner's approval of sample 4

211. **(draft) Question types: about 40 % "picture" questions (about what happens in the picture or video: the person, animal or thing shown, what they do, why, what happens next, e.g. "Why is the woman dancing in front of the ruined castle?", "What is the robot ordering the others to do?"), about 40 % "you" questions (the learner's opinion or experience, e.g. "Would you trade your lunch for a Czech beer?") and about 20 % definition questions (decision 208); picture and you questions are mixed over levels A and B and over parts of speech. Nothing is invented that the media does not show.**
212. **(draft) Level-A soft length target (refines 206): an English level-A question is usually at most 10 words. Grammar comes first: the target is never a reason for an incomplete or unnatural question; if a complete, clear question needs more words, it gets them. Level B has no target.**
213. **(draft) In a definition question the Slovak key word (and every other language's) is the dictionary form of the word for THIS sense (the definition taught), not a word of another sense of the English word (e.g. "waiting" = ready to be used at any moment → not „pripravený“).**
214. **(draft) Words about the body or looks (e.g. "slim") may be treated playfully but never mock anyone's body (e.g. card 48: "How would you draw a slim person with only five lines?").**
215. **(draft) New split (revises 211): about 20 % definition questions, about 20 % statements, about 30 % "picture" questions and about 30 % "you" questions, mixed over levels A and B and parts of speech.**
216. **(draft) A statement is not a question: a short, slightly controversial claim about what the picture or video shows that makes the learner agree or disagree in the comment (model: "That customer would trade even his girlfriend for a Czech beer." / sk "Ten zákazník by vymenil aj svoju frajerku za české pivo."). The learner is not in it (no "you", "your", "would you"; sk no "ty", "tvoj", "by si"). It contains the key word (inflected is fine, never a phrasal verb, idiom or related word in its place), is grammatically perfect, clear, level-appropriate (level A soft target usually at most 10 English words, as 212) and funny, and ends with a full stop. Playfully provocative, never hurtful: no politics, religion, sex, violence, mocking bodies, or offensive stereotypes about nations, genders or origins. Every other language is a faithful translation (201/209). Both verifiers check statements like questions.**
217. **(draft) Definition questions rotate three forms, roughly evenly (refines 208); the key word stays in its dictionary form in quotation marks: How would you define "<key word>"? / sk Ako by si definoval „<sk>“?; What does "<key word>" mean? / sk Čo znamená „<sk>“?; What is "<key word>"? / sk Čo je „<sk>“? — the last only for nouns; verbs, adjectives, adverbs and phrases use one of the first two ("What does "to care" mean?", "How would you define "hazardous"?").**
218. **(draft) "What is …?" for a noun naming a person: English keeps "What is "a coach"?" (it asks for the meaning; "Who is the coach?" would ask for one person's identity). The native version uses the language's natural question word for a person, as a native speaker asks for the meaning of such a word: sk "Kto je „tréner“?", cz "Kdo je „trenér“?", and the equivalent in de ("Wer ist …?" only if natural for a definition, otherwise "Was ist ein …?"), es, fr, ua, hu and tr. The grammar verifier checks this.**
