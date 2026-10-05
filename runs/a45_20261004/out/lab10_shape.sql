begin;
-- A45 batch lab10: picture shape (pixel width / height) of its 10 videos; only rows without a shape are touched.
update public.media_exercise_sets s set width = v.w, height = v.h, updated_at = now()
  from (values
(8055, 720, 1280),
(236, 496, 864),
(624, 496, 864),
(7071, 496, 864),
(8056, 720, 1280),
(4265, 480, 854),
(461, 496, 864),
(62, 496, 864),
(8039, 496, 864),
(432, 496, 864)
  ) as v(id, w, h)
 where s.media_id = v.id and s.width is null;
do $g$ begin
  if (select count(*) from public.media_exercise_sets where media_id in (8055,236,624,7071,8056,4265,461,62,8039,432) and width > 0 and height > 0) <> (select count(*) from public.media_exercise_sets where media_id in (8055,236,624,7071,8056,4265,461,62,8039,432)) then raise exception 'A45 lab10 shape: a row has no shape after the update, rolled back'; end if;
end $g$;
commit;
