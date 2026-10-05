-- A55 (5 Oct 2026): the exercises of a video for learners of German, Spanish (Spain) and French (France), one row per
-- (media, learning language). Additive: media_exercise_sets (English) is not touched and stays what the app reads. Written
-- natively per language (not word for word); the tap regions, the noun slots, the still moment and the carousel pictures
-- are the English set's, copied unchanged into the row so a row is complete on its own. Read-only for everyone (like
-- media_exercise_sets); written only by the content pipeline (owner scripts). Read by the lab page (/lab) only; the main
-- app's learning languages stay switched off (lib/learnLanguages.ts, A50) until the owner approves a language.
begin;

create table if not exists public.media_exercise_sets_l10n (
  media_id          bigint not null references public.media(id) on delete cascade,
  learning_language text   not null check (learning_language in ('de', 'es', 'fr')),
  level             text   not null check (level in ('A', 'B')),
  status            text   not null default 'live' check (status in ('live', 'draft', 'failed')),
  -- the word the video teaches in this language (word_localizations of the video's concept; nouns with their article)
  key_word          text   not null,
  default_voice     text   not null check (default_voice in ('female', 'male')),
  -- "Tap who does it.": [{ phrase, target, voice, audio_url, keys }]  (keys = the English set's, unchanged)
  taps              jsonb  not null,
  -- "Place the nouns.": [{ word, voice, audio_url, x, y }]  (word with its definite article; x, y = the English slot)
  nouns             jsonb  not null,
  still_s           real   not null default 0,
  answer_s          real,
  question          text   not null,
  answer_chips      jsonb  not null,
  answer_text       text   not null,
  answer_voice      text   not null check (answer_voice in ('female', 'male')),
  answer_audio_url  text,
  -- "Choose matching caption.": [{ en, caption, url, audio_url, type, has_key_word }] in the pictures' order (NULL = none)
  carousel          jsonb,
  -- "Fill in what you remember.": [{ from, parts: [{ text, gap?, accept? }] }]
  recall            jsonb  not null default '[]'::jsonb,
  -- help texts per native language (sk, cz, en, de, es, fr, hu, tr, ua minus the learning language):
  --   { <native>: { phrases: [..], nouns: [..], question, answer, captions: { <caption>: text }, recall: [..] } }
  tr                jsonb  not null default '{}'::jsonb,
  voice_names       jsonb  not null default '{}'::jsonb,  -- { female: 'Anna (Premium)', male: 'Yannick (Enhanced)' }
  width             integer check (width is null or width > 0),
  height            integer check (height is null or height > 0),
  content_version   integer not null default 1,
  created_at        timestamptz not null default now(),
  updated_at        timestamptz not null default now(),
  primary key (media_id, learning_language)
);

create index if not exists media_exercise_sets_l10n_lang_idx on public.media_exercise_sets_l10n (learning_language, level) where status = 'live';

alter table public.media_exercise_sets_l10n enable row level security;

drop policy if exists "Enable read access for all users" on public.media_exercise_sets_l10n;
create policy "Enable read access for all users" on public.media_exercise_sets_l10n
  for select using (true);

revoke all on public.media_exercise_sets_l10n from anon, authenticated;
grant select on public.media_exercise_sets_l10n to anon, authenticated;

comment on table public.media_exercise_sets_l10n is 'A55: the exercises of a video for learners of de / es / fr (written natively), one row per media and learning language; English stays in media_exercise_sets.';

commit;
