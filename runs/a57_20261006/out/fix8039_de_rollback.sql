-- A57 rollback of fix8039_de (not run): restore the row from backup/fix8039_de_before.json
-- (python3 restore_fix8039.py de prints the update)
begin;
commit;
