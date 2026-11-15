# fixlock playground

A live demo of the [fixlock GitHub App](https://abinandhmj.github.io/fixlock/github-app) by Algotricz.

`payments.py` has one locked bug fix, `FIX-001`: a charge of zero or less must raise an error. It's owned by a demo teammate, Ravi, so only he can approve a PR that changes it.

Open the pull requests to see the **fixlock** check in action:
- a PR that removes the fix fails, and the comment explains why and who must approve;
- a PR that only reformats the locked lines passes.

Learn more: https://abinandhmj.github.io/fixlock/
