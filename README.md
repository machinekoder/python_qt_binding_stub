# Stub for python_qt_binding module

It's quite annoying that most ides can't fully resolve the `python_qt_binding` module. 
This repo contains a workaround for this.

## Generate some stubs

To regenerate the stubs run the `create_stubs.py` script.

## VSCode

Add this in your `settings.json`:

```json
    "python.analysis.extraPaths": [
        "<path>/python_qt_binding_stub",
    ],
```
