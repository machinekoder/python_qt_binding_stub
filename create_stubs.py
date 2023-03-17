import os
import PyQt5


def create_submodule_files(module_path, output_path):
    module_name = os.path.basename(module_path)
    extension = '.pyi'
    for filename in os.listdir(module_path):
        if filename.endswith(extension) and filename != '__init__.py':
            print(filename)
            submodule_name = filename[:-len(extension)]
            output_file = os.path.join(output_path, f'{submodule_name}.py')
            with open(output_file, 'w') as f:
                f.write(f'from {module_name}.{submodule_name} import * # noqa: F401')


if __name__ == '__main__':
    module_path = os.path.dirname(PyQt5.__file__)
    output_path = os.path.join(os.path.dirname(__file__), 'python_qt_binding')
    create_submodule_files(module_path, output_path)
