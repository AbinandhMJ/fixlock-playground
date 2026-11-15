# CLAUDE

<!-- fixlock:start -->
## Locked fixes & features — managed by fixlock (do not edit this section)

Project: fixlock-playground. Team: Abi (developer, @AbinandhMJ), Ravi (demo teammate) (lead).

Rules for AI assistants working in this repo:
0. **Never rewrite, delete or replace code that already works without telling the developer first.** Before changing existing lines, say which lines, why, and what behaviour could change, then wait for a yes. Prefer adding new code next to existing code over rewriting it.
1. Before changing an existing line, check it: if you have the fixlock MCP tools, call `fixlock_check_edit` with the file and the exact text you will replace (or `fixlock_why` for a whole file); otherwise run `npx -y @abinandhmj/fixlock@0.7 why <file>:<line>`. Follow the verdict: block = don't change it, ask = ask the developer first, warn = mention it.
2. Locked lines fix real bugs or hold finished features. Do not delete, rewrite or "simplify" them, and never overwrite them with code from another codebase. Build around them.
3. If the task cannot be done without changing a locked line, STOP and tell the developer which lock is affected and who owns it. The PR will need that person's approval.
4. Keep diffs minimal: no unrelated refactors, renames or formatting changes.
5. Write commit messages as Conventional Commits (`fix: …`, `feat: …`, `perf: …`). CHANGELOG.md is generated from them.
6. Before finishing, run `npx -y @abinandhmj/fixlock@0.7 check --staged` (or the `fixlock_check_staged` MCP tool) and report anything it flags.

A fixlock hook in .claude/settings.json also checks every Edit/Write before it happens.

### Current locks
- **FIX-001** A charge of zero or less crashed the ledger on refunds (bug, owner Ravi (demo teammate), on edit: ask) — `payments.py`
  - Must keep: `if amount <= 0:` / `raise ValueError("amount must be positive")`
<!-- fixlock:end -->
