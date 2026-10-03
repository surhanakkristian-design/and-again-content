begin;
-- A31 (3 Oct 2026): videos are organised in 35 groups. Additive only.
--   media_groups              one row per group: names in the 9 languages, the categories it is
--                             made of, and its representative video for a learner without history
--                             (level A, level B, all levels)
--   media.group_id            the one main group of a media
--   tinder_word_distractors   per video (its key word): the other key words of the same group
--                             and level that may be shown as the WRONG word on a one-word Tinder card
--                             (same part of speech first)
-- The rows are written by the guarded data script of the run (and-again-content
-- runs/a31_20261003); this file only creates the objects.

create table if not exists public.media_groups (
  id bigint primary key,
  name jsonb not null,
  source_category_ids bigint[] not null,
  rep_media_a bigint references public.media(id) on delete set null,
  rep_media_b bigint references public.media(id) on delete set null,
  rep_media_all bigint references public.media(id) on delete set null
);

alter table public.media_groups enable row level security;
drop policy if exists "Media groups are viewable by everyone" on public.media_groups;
create policy "Media groups are viewable by everyone" on public.media_groups for select using (true);
revoke all on public.media_groups from anon, authenticated;
grant select on public.media_groups to anon, authenticated;

alter table public.media add column if not exists group_id bigint references public.media_groups(id) on delete set null;
create index if not exists media_group_id_idx on public.media(group_id);

create table if not exists public.tinder_word_distractors (
  media_id bigint primary key references public.media(id) on delete cascade,
  concept_id bigint not null references public.word_concepts(id) on delete cascade,
  group_id bigint not null references public.media_groups(id) on delete cascade,
  level text not null check (level in ('A', 'B')),
  distractor_concept_ids bigint[] not null,
  -- only for a video with fewer than 5 options: key words of the same group at the OTHER level
  fallback_concept_ids bigint[] not null default '{}'
);
create index if not exists tinder_word_distractors_concept_idx on public.tinder_word_distractors(concept_id);

alter table public.tinder_word_distractors enable row level security;
drop policy if exists "Tinder word distractors are viewable by everyone" on public.tinder_word_distractors;
create policy "Tinder word distractors are viewable by everyone" on public.tinder_word_distractors for select using (true);
revoke all on public.tinder_word_distractors from anon, authenticated;
grant select on public.tinder_word_distractors to anon, authenticated;
commit;
