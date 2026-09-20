# Phase 2E (Czech) STOP: throughput_guard

measured throughput 0.0 tok/s stayed under 60 tok/s for 20 consecutive minutes (trailing 300 s window).

2C ran five hours at 25 tok/s because nothing checked; this run stops spawning instead. In-flight sessions finish or hit the circuit breaker, everything complete is committed, resume with the same command.

Written 2026-09-21 00:13:25.
Spent so far: 285312 headless tokens, 1260.3 s wall, par 2.
