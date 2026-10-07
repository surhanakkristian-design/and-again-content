-- A61 rollback of the data write: no video counts as cut (the columns stay; to drop them see the migration's header).
begin;
update public.media set has_cut = false, cut_times = null where has_cut;
commit;
