-- A57 rollback of wl_8039 (not run)
begin;
update public.word_localizations set translation = 'Durchgang', display_form = 'der Durchgang' where id = 54301 and concept_id = 6040 and language_code = 'de';
update public.word_localizations set translation = 'paso', display_form = 'el paso' where id = 54303 and concept_id = 6040 and language_code = 'es';
commit;
