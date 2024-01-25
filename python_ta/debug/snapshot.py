"""
Use the 'inspect' module to extract local variables from
 multiple stack frames. Useful for dynamic debugging.
"""
import inspect


def snapshot():
    """Capture a snapshot of local variables from the current and outer stack frames
    where the 'snapshot' function is called. Returns a list of dictionaries,
    each mapping function names to their respective local variables.
    Excludes the global module context.
    """
    local_vars = []
    frame = inspect.currentframe().f_back

    local_vars.append(get_filtered_global_variables(frame=frame))

    while frame:
        if frame.f_code.co_name != "<module>":
            local_vars.append({frame.f_code.co_name: frame.f_locals})
        frame = frame.f_back

    return local_vars


def get_filtered_global_variables(frame) -> dict:
    """
    Helper function for retriving top level global variables,
    i.e. variables in __main__ frame's scope.
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
