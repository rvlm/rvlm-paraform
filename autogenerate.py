import os
import itertools
import textwrap

# The following inspection is suppressed because library user isn't required to
# have Jinja installed for the library to operate, as this script is only
# supposed to be run on a developer's system.
# ---
# noinspection PyPackageRequirements
import jinja2


def all_possible_arguments():
    """
    Enumerates all possible permutations of ('x', 'y', 'z') tuple, starting
    with ('x') up to ('z', 'y', 'z'). These are argument names which function
    being expanded can take and return.
    """
    arguments = ('x', 'y', 'z')
    yield from itertools.permutations(arguments, 1)
    yield from itertools.permutations(arguments, 2)
    yield from itertools.permutations(arguments, 3)


def generate_expand_function_code():
    """
    Generates program text for :func:`rvlm.utils.expand_function`. This, in
    fact, is the main function of this script. Don't forget to re-run code
    generation if you've changed the template below.
    """
    template_string = textwrap.dedent("""\
        def expand_function_autogen(f, argspec):
            # This function code is GENERATED AUTOMATICALLY, please, do not
            # edit it by hand as your improvements are more than likely to be
            # lost on regeneration.

            {% for input in inputs %}
            {% for output in outputs %}
            if argspec == "{{''.join(output)}}_{{''.join(input)}}":
                # noinspection PyUnusedLocal
                def result(x, y, z):
                    {{', '.join(output)}} = f({{', '.join(input)}})
                    return x, y, z

                return result

            {% endfor %}
            {% endfor %}
            raise ValueError("Unsupported 'argspec' value")
        """)

    env = jinja2.Environment(lstrip_blocks=True, trim_blocks=True)
    template = env.from_string(template_string)
    return template.render(inputs=list(all_possible_arguments()),
                           outputs=list(all_possible_arguments()))


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    autogen_file = os.path.join(current_dir, "src/rvlm/paraform/autogen.py")
    with open(autogen_file, mode="w") as f:
        f.write(generate_expand_function_code())
