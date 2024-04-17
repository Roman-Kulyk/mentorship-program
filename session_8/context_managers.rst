
A context manager is an object defines the runtime context to be established
when executing a with statement. The context manager handles the entry into, and
the exit from, the desired runtime context for the execution of the block of
code. Context managers are normally invoked  using the with statement, but can
also be used by directly invoking their methods.
Typical uses of context managers include saving and restoring various kinds of
glogal state, locking and unlocking resources, closing opened files, etc.

object.__enter__(self)
Enter the runtime context related to this object. The with statement will bind
this method's return value ot the target(s) specified in the as clause of the
statement, if any.

object.__exit__(self)
Exit the runtime context related to this object. The parameters describe the
exception that cause the context to be exited. If the context was exited without
an exception, all three arguments will be None.
