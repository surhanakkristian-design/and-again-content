-- A57 owner decision 2: concept 6040 (media 8039 "way"): German "der Weg", Spanish "el camino"; French stays "le passage".
-- Guarded: writes only when both rows still hold the old words.
begin;
do $g$ begin
  if (select count(*) from public.word_localizations where id in (54301, 54303) and concept_id = 6040
      and ((language_code = 'de' and translation = 'Durchgang' and display_form = 'der Durchgang')
        or (language_code = 'es' and translation = 'paso' and display_form = 'el paso'))) <> 2 then
    raise exception 'A57 wl_8039: rows are not in the expected before-state - nothing written';
  end if;
end $g$;
update public.word_localizations set translation = 'Weg', display_form = 'der Weg' where id = 54301 and concept_id = 6040 and language_code = 'de';
update public.word_localizations set translation = 'camino', display_form = 'el camino' where id = 54303 and concept_id = 6040 and language_code = 'es';
commit;
