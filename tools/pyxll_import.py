from pyxll import xl_macro, rebind
import argparse

@xl_macro
def import_new_functions(args):
    """Import a new module and then call 'rebind' to tell PyXLL to update"""
    module = __import__(args.name)
    # Now the module has been imported and declared new UDFs using @xl_func
    # tell PyXLL to update it's Excel bindings.
    rebind()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'setup pyxll notebook')
    parser.add_argument('name', help='Enter new python module name to rebind to pyxll')
    args = parser.parse_args()

    main(args.name)