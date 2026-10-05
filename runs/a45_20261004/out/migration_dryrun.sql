-- A45 (4 Oct 2026): the three main exercises of a video ("Tap who does it.", "Place the nouns.",
-- the question with its model answer), one row per media. Additive; read-only for everyone
-- (like comment_questions); written only by the content pipeline (service role / owner scripts).
begin;

create table if not exists public.media_exercise_sets (
  media_id          bigint primary key references public.media(id) on delete cascade,
  level             text   not null check (level in ('A', 'B')),
  status            text   not null default 'live' check (status in ('live', 'draft', 'failed')),
  default_voice     text   not null check (default_voice in ('female', 'male')),
  -- "Tap who does it.": [{ phrase, target, voice: 'female'|'male', audio_url,
  --   keys: [{ t, x, y, w, h } | { t, off: true }] }]  (x, y = top-left, shares of the picture, one key per 0.5 s)
  taps              jsonb  not null,
  -- "Place the nouns.": [{ word, x, y, voice, audio_url }]  (x, y = the slot's centre on the still picture)
  nouns             jsonb  not null,
  still_s           real   not null default 0,   -- the moment of the still picture of the nouns step
  answer_s          real,                        -- the moment of the small picture beside the question (NULL = still_s)
  question          text   not null,
  answer_chips      jsonb  not null,             -- the model answer as word chips in order
  answer_text       text   not null,             -- the model answer as one sentence
  answer_voice      text   not null check (answer_voice in ('female', 'male')),
  answer_audio_url  text,
  -- native texts: { de|fr|es|sk|cz|ua|tr|hu: { phrases: [..], nouns: [..], question, answer } } (English is the content itself)
  tr                jsonb  not null default '{}'::jsonb,
  voice_names       jsonb  not null default '{}'::jsonb,  -- { female: 'Samantha', male: 'Daniel' } = the voices of the audio files
  content_version   integer not null default 1,
  created_at        timestamptz not null default now(),
  updated_at        timestamptz not null default now()
);

create index if not exists media_exercise_sets_level_idx on public.media_exercise_sets (level) where status = 'live';

alter table public.media_exercise_sets enable row level security;

drop policy if exists "Enable read access for all users" on public.media_exercise_sets;
create policy "Enable read access for all users" on public.media_exercise_sets
  for select using (true);

revoke all on public.media_exercise_sets from anon, authenticated;
grant select on public.media_exercise_sets to anon, authenticated;

comment on table public.media_exercise_sets is 'A45: the three main exercises of a video (tap phrases with regions, nouns with slots, question + model answer), native texts, voices and audio.';

-- The recorded words, phrases and model answers are AAC (.m4a) files in the public bucket `audio`
-- under sets/<media id>/. The bucket allowed only audio/mpeg (the Tinder music); audio/mp4 is added.
update storage.buckets
   set allowed_mime_types = array['audio/mpeg', 'audio/mp4']
 where id = 'audio' and allowed_mime_types = array['audio/mpeg'];

select count(*) as rows_in_new_table from public.media_exercise_sets; rollback;
