-- A45 addition (5 Oct 2026): the picture shape of every video in media_exercise_sets (A46 open point 11: tap regions and
-- noun slots are shares of the picture; on videos that are not exactly 9:16 the app was off by about 2 % without it).
-- width / height = the video's stored pixel size (ffprobe of media_url); aspect = width / height. Additive.
begin;

alter table public.media_exercise_sets
  add column if not exists width  integer check (width is null or width > 0),
  add column if not exists height integer check (height is null or height > 0);

comment on column public.media_exercise_sets.width is 'A45: pixel width of the video (aspect = width / height); NULL = unknown, assume 9:16.';
comment on column public.media_exercise_sets.height is 'A45: pixel height of the video.';

commit;
