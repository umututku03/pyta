"""
Use the 'inspect' module to extract local variables from
 multiple stack frames. Useful for dynamic debugging.
"""
import inspect


def get_filtered_global_variables(frame) -> dict:
    """
    Helper function for retriving global variables
    (i.e. top level variables in "__main__" frame's scope)
    excluding, certain types (types of data that is
    irrelevant in an intro level to Python programming language).
    """
    global_vars = frame.f_globals
    true_global_vars = {
        var: global_vars[var]
        for var in global_vars
        if not var.startswith("__")
        and not inspect.ismodule(global_vars[var])
        and not inspect.isfunction(global_vars[var])
        and not inspect.isclass(global_vars[var])
    }
    return {"__main__": true_global_vars}


def snapshot():
    """Capture a snapshot of local variables from the current and outer stack frames
    where the 'snapshot' function is called. Returns a list of dictionaries,
    each mapping function names to their respective local variables.
    Excludes the global module context.
    """
    local_vars = []
    frame = inspect.currentframe().f_back

    while frame:
        # whether the current stack frame corresponds to the global module context or not
        if frame.f_code.co_name != "<module>":  # skips the global module context
            local_vars.append({frame.f_code.co_name: frame.f_locals})
        else:
            global_vars = get_filtered_global_variables(frame)
            local_vars.append(global_vars)

        frame = frame.f_back

    return local_vars