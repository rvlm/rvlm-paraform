Additional notes for developers
===============================

Before-you-commit checklist
---------------------------

 #. If you have changed any template for automatically generated function,
    make sure you have also regenerated the target file.

 #. Make sure your code passes unit tests, including the ones which compares
    with saved rendering results.

 #. Make sure your code passes doctests.

 #. Make sure your code is as PEP-8 compliant as possible without making code
    look ugly. Run (or let your IDE run) pep8.py tool, with the following
    exceptions:

    - E221: multiple spaces before operator
    - E222: multiple spaces after operator
    - E272: multiple spaces before keyword
    - E271: multiple spaces after keyword
    - E127: over-indented for visual indent
    - E225: missing whitespace around operator
    - E226: missing whitespace around arithmetic operator

    (Ideally,) you shouldn't commit if your code doesn't pass style check. As
    the very last resort, you may add a new entry error into the list above,
    after negotiation with the whole team.

 #. Make sure PyCharm code inspections passes.


How to prepare illustrations for documentation
----------------------------------------------

Proper illustrations are crucial for good documentation, but it's highly
desirable to have a common look for them. Current style is the following:

 #. Render your scene as point cloud
 #. Import points into Paraview
 #. Apply Glyph transform

    - Glyph mode: all points
    - Representation: Surface with Edges
    - background color: white
    - solid color: RGB 205, 230, 255
    - edge color:  blue 128
    - center axes visibility: on
    - orientation axes visibility: off
    - screenshot: 600x600 or something x600

TODO:
-----

 #. Find file format common to numpy and Paraview
 #. Find fast way to produce point list over numpy's meshgrid
