#!/usr/bin/env python3
"""True detach on macOS (no setsid(1) here): double fork + os.setsid, stdio to a log, then exec.
Usage: daemonize.py <logfile> <cwd> <cmd> [args...]"""
import os, sys
logp, cwd, cmd = sys.argv[1], sys.argv[2], sys.argv[3:]
if os.fork() > 0: os._exit(0)
os.setsid()
if os.fork() > 0: os._exit(0)
os.chdir(cwd)
fd = os.open(logp, os.O_WRONLY | os.O_CREAT | os.O_APPEND)
os.dup2(fd, 1); os.dup2(fd, 2)
os.dup2(os.open(os.devnull, os.O_RDONLY), 0)
open(os.path.join(os.path.dirname(logp), "CHAIN_PID"), "w").write(str(os.getpid()) + "\n")
os.execvp(cmd[0], cmd)
