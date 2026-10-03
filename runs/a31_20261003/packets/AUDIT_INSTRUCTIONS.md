# A31 second look (audit of the wrong words that survived)

The app shows a short video and ONE word. The learner swipes right if the word fits the video, left if not.
Each item of a packet `packets/audit/<name>.json` is a video (`desc` = what it shows, `said` = what is spoken, `key_word` = its correct word) and `wrong`: words a first reviewer approved as WRONG words for this video.
You are the strict second reviewer. For every wrong word decide:
- "ok": plainly not in the video and not about it; nobody could argue it fits;
- "fits": the thing / action / quality / feeling it names is visible, done, heard, said or clearly implied, or it is a synonym, broader or narrower word of the key word, or it describes the scene as a whole. Judge the bare word as a learner reads it (every everyday sense of the word counts, not only the given definition);
- "doubt": arguable either way.
Write `packets/audit_out/<name>.json`: {"<media id>": {"<concept id>": "ok" | "fits" | "doubt", ...}, ...} covering every video and every wrong word, plus for each "fits"/"doubt" a line in {"notes": {"<media id>:<concept id>": "<why>"}} at top level. Read and judge; no string-matching scripts. Re-open the output and check it is valid JSON and complete.
Reply: packet name, number of judgments, number of fits, number of doubt.
