-- A57 rollback of fix8039_es (not run): restore the row from backup/fix8039_es_before.json
-- (python3 restore_fix8039.py es prints the update)
begin;
commit;
